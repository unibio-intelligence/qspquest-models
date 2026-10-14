"""Plain CSV bundles with units, replay inputs and explicit evidence scope."""
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re

SCHEMA = 'qspquest.table-manifest/v1'
EVENT_RULE = 'nondecreasing_time;equal_time_requires_pre_then_post'
MAX_TABLE_BYTES = 256 * 1024 * 1024
MAX_MANIFEST_BYTES = 16 * 1024 * 1024
MAX_ROWS = 2_000_000


def _object(value, keys, label):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError(label + ' has missing or unknown fields')


def _unique(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError('Duplicate manifest key: ' + key)
        value[key] = item
    return value


def _reject_constant(value):
    raise ValueError('Nonfinite manifest number: ' + value)


def _finite(value):
    try:
        finite = not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value)
    except OverflowError:
        finite = False
    if not finite:
        raise ValueError('Table values must be finite numbers')
    return value


def _event_counts(rows):
    previous = None
    previous_side = None
    paired = False
    counts = {'pre': 0, 'post': 0, 'event_pairs': 0}
    for row in rows:
        try:
            time = Decimal(str(row[0]))
        except InvalidOperation as error:
            raise ValueError('Invalid table time') from error
        if not time.is_finite() or row[1] not in ('pre', 'post'):
            raise ValueError('Table time must be finite and side must be pre or post')
        if previous is not None:
            if time < previous:
                raise ValueError('Table times must be nondecreasing')
            if time == previous:
                if paired or (previous_side, row[1]) != ('pre', 'post'):
                    raise ValueError('Equal-time rows must be exactly pre then post')
                paired = True
                counts['event_pairs'] += 1
            else:
                paired = False
        counts[row[1]] += 1
        previous, previous_side = time, row[1]
    return counts


def _column(name, unit, kind, native_name=None, meaning=None):
    return {'name': name, 'unit': unit, 'kind': kind, 'native_name': native_name, 'meaning': meaning}


def manifest_for(result, filename, data, columns, *, producer='model_library', time_name='time'):
    """Describe raw table bytes without inheriting archived qualification."""
    descriptors = [_column(time_name, result.get('time_unit'), 'time'),
                   _column('side', None, 'event_side')]
    descriptors += [_column(c['name'], c.get('unit'), c.get('kind', 'output'),
                            c.get('native_name'), c.get('meaning')) for c in columns]
    modified = result.get('research_copy')
    value = {
        'schema': SCHEMA,
        'producer': producer,
        'table': {'filename': filename, 'sha256': hashlib.sha256(data).hexdigest(),
                  'bytes': len(data), 'rows': len(result['times']), 'columns': descriptors},
        'events': {'rule': EVENT_RULE, **_event_counts(zip(result['times'], result['sides']))},
        'model': {'id': result.get('model_id'), 'version': result.get('model_version'),
                  'archive_sha256': result.get('archive_sha256'),
                  'provenance': result.get('model_provenance')},
        'engine_identity': result.get('identity'),
        'inputs': {'effective_request': result.get('effective_request'),
                   'selected_outputs': result.get('effective_outputs'),
                   'effective_request_hash': result.get('effective_request_hash'),
                   'scenario_id': result.get('scenario_id'), 'modified': modified},
        'qualification': {'qualified': False, 'status': 'not_assessed',
                          'scope': 'current_engine_and_effective_request',
                          'unit_status': ('source_scale_unqualified' if result.get('coordinates') == 'unchanged_source_numeric_values'
                                          else 'unqualified'),
                          'coordinates': result.get('coordinates'),
                          'recorded_dimensional_qualification': result.get('dimensional_qualification'),
                          'recorded_availability': result.get('availability')},
    }
    validate_manifest(value, filename)
    return value


def _mcp_receipts(value):
    """Validate retained receipt transport and table consistency, not science."""
    columns = {c['name']: c for c in value['table']['columns']}
    def label(s):
        return isinstance(s, str) and bool(s.strip()) and len(s) <= 512 and not any(ord(c) < 32 for c in s)
    def quantity(q, nonnegative=False):
        _object(q, ['value', 'unit'], 'Dose quantity')
        if type(q['value']) not in (int, float) or not math.isfinite(q['value']) or not label(q['unit']) or (nonnegative and q['value'] < 0):
            raise ValueError('Invalid dose quantity')
    def expression(root):
        pending = [root]
        operators = {'unary': ('positive', 'negative', 'not'),
                     'binary': ('add', 'subtract', 'multiply', 'divide', 'power', 'modulo'),
                     'compare': ('lt', 'le', 'gt', 'ge', 'eq', 'ne'), 'boolean': ('and', 'or')}
        functions = ('exp','log','log10','sqrt','sin','cos','tan','tanh','abs','min','max','floor','ceil','hill','ifelse')
        while pending:
            node = pending.pop()
            if not isinstance(node, dict):
                raise ValueError('Invalid dose scale expression')
            kind = node.get('kind')
            if kind == 'literal':
                _object(node, ['kind','value'], 'Dose scale literal')
                if type(node['value']) not in (int,float,bool) or (type(node['value']) is not bool and not math.isfinite(node['value'])):
                    raise ValueError('Invalid dose scale literal')
                continue
            if kind == 'symbol':
                _object(node, ['kind','name'], 'Dose scale symbol')
                if not label(node['name']):
                    raise ValueError('Invalid dose scale symbol')
                continue
            if kind in operators:
                _object(node, ['kind','operator','arguments'], 'Dose scale operator')
                if node['operator'] not in operators[kind]:
                    raise ValueError('Unsupported dose scale operator')
            elif kind == 'call':
                _object(node, ['kind','name','arguments'], 'Dose scale call')
                if node['name'] not in functions:
                    raise ValueError('Unsupported dose scale function')
            elif kind == 'conditional':
                _object(node, ['kind','arguments'], 'Dose scale conditional')
            else:
                raise ValueError('Unsupported dose scale expression kind')
            args = node['arguments']
            arity = {'unary':1,'binary':2,'compare':2,'conditional':3}.get(kind)
            if not isinstance(args,list) or (arity is not None and len(args) != arity):
                raise ValueError('Invalid dose scale expression arity')
            pending.extend(args)
    for key in ('required_output_receipts','dose_event_receipts'):
        if key not in value:
            continue
        if value['producer'] != 'mcp' or not isinstance(value[key], list):
            raise ValueError('MCP receipts must be lists from the MCP producer')
    for receipt in value.get('required_output_receipts', []):
        _object(receipt, ['requirement','canonical_output','returned_column','returned_unit','declared_analyte','declared_compartment','status','sample_count'], 'Required-output receipt')
        _object(receipt['requirement'], ['output','analyte','compartment'], 'Output requirement')
        requirement=receipt['requirement']
        if not all(label(receipt[k]) for k in ('canonical_output','returned_column','returned_unit')) or not label(requirement['output']):
            raise ValueError('Invalid required-output labels')
        for requested,declared in [('analyte','declared_analyte'),('compartment','declared_compartment')]:
            if receipt[declared] is not None and not label(receipt[declared]):
                raise ValueError('Invalid declared output identity')
            if requirement[requested] is not None and (not label(requirement[requested]) or requirement[requested] != receipt[declared]):
                raise ValueError('Unfulfilled output identity in table receipt')
        column=columns.get(receipt['returned_column'])
        if column is None and receipt['returned_column'] == receipt['canonical_output']:
            matches=[c for c in columns.values() if c['native_name'] == receipt['canonical_output']]
            column=matches[0] if len(matches)==1 else None
        if receipt['status'] != 'computed' or type(receipt['sample_count']) is not int or receipt['sample_count'] != value['table']['rows'] or column is None or column['unit'] != receipt['returned_unit'] or column['native_name'] != receipt['canonical_output']:
            raise ValueError('Required-output receipt differs from exported table')
    seen=set()
    for receipt in value.get('dose_event_receipts', []):
        _object(receipt, ['stage','event_index','canonical_target','delivery','time','amount_before_model_scaling','duration','target_state_unit','declared_base_scale','archive_source_coordinate','notice'], 'Dose-event receipt')
        if receipt['stage'] != 'executed_schedule' or type(receipt['event_index']) is not int or receipt['event_index'] < 0 or receipt['event_index'] in seen or receipt['delivery'] not in ('bolus','infusion'):
            raise ValueError('Invalid executed dose-event receipt')
        seen.add(receipt['event_index'])
        if not all(label(receipt[k]) for k in ('canonical_target','target_state_unit','notice')):
            raise ValueError('Invalid dose-event labels')
        quantity(receipt['time']);quantity(receipt['amount_before_model_scaling'], True)
        if receipt['time']['unit'] != value['table']['columns'][0]['unit']:
            raise ValueError('Dose-event time unit differs from table clock')
        if receipt['delivery']=='infusion':
            quantity(receipt['duration'], True)
            if receipt['duration']['value'] <= 0 or receipt['duration']['unit'] != receipt['time']['unit']:
                raise ValueError('Invalid infusion duration')
        elif receipt['duration'] is not None:
            raise ValueError('Bolus receipt cannot carry an infusion duration')
        expression(receipt['declared_base_scale'])
        source=receipt['archive_source_coordinate']
        if source is not None:
            _object(source,['native_target','amount_unit','state_unit','source_dose_unit','source_coordinate','scaling'],'Archive dose coordinate')
            if not all(label(s) for s in source.values()) or source['native_target'] != receipt['canonical_target'] or source['state_unit'] != receipt['target_state_unit'] or source['amount_unit'] != receipt['amount_before_model_scaling']['unit']:
                raise ValueError('Archive dose coordinate differs from effective event')


def _initialization_receipt(manifest):
    """Check initialization transport, native phase consistency and identity."""
    receipt = manifest.get('initialization_receipt')
    if receipt is None:
        return
    def keys(value, names):
        _object(value, names.split(), 'Initialization receipt')
    def text(value):
        return isinstance(value, str) and bool(value.strip()) and len(value) <= 1024 and not any(ord(c) < 32 for c in value)
    def number(value):
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError('Initialization coordinates must be finite numbers')
        return value
    def unit(value):
        keys(value, 'dimensions scale_numerator scale_denominator declared')
        if not isinstance(value['dimensions'], list) or len(value['dimensions']) != 8 or any(type(n) is not int or not -32768 <= n <= 32767 for n in value['dimensions']):
            raise ValueError('Invalid native unit dimensions')
        if any(not isinstance(value[k], str) or not re.fullmatch('[1-9][0-9]*', value[k]) for k in ('scale_numerator', 'scale_denominator')) or (value['declared'] is not None and not text(value['declared'])):
            raise ValueError('Invalid exact native unit scale')
    def normalization(value):
        keys(value, 'canonical_output numerator_state denominator_input multiplier basis interpretation')
        if any(not text(value[k]) for k in ('canonical_output', 'numerator_state', 'denominator_input', 'interpretation')) or number(value['multiplier']) <= 0 or value['basis'] not in ('declared_reference_input', 'condition_specific_binding'):
            raise ValueError('Invalid normalization policy')
    keys(receipt, 'schema stage time_unit integration_start integration_end first_dose_time predose_integration initialized_states binding_phases source_declaration declared_scenario normalization_receipts planned_execution_identity notice')
    start, end = number(receipt['integration_start']), number(receipt['integration_end'])
    if manifest['producer'] != 'mcp' or receipt['schema'] != 'qspquest.initialization-receipt/v1' or receipt['stage'] != 'executed' or receipt['time_unit'] != manifest['table']['columns'][0]['unit'] or end < start or not text(receipt['notice']) or receipt['planned_execution_identity'] != manifest['engine_identity']:
        raise ValueError('Initialization receipt clock, producer or execution identity differs from table')
    first = receipt['first_dose_time']
    if first is not None:
        number(first)
        if not start <= first <= end:
            raise ValueError('First dose is outside initialization clock')
    expected_window = {'start': start, 'end': first} if first is not None and first > start else None
    if receipt['predose_integration'] != expected_window:
        raise ValueError('Pre-dose interval differs from native clock')
    if not isinstance(receipt['initialized_states'], list) or not isinstance(receipt['binding_phases'], list) or not receipt['binding_phases'] or not isinstance(receipt['normalization_receipts'], list):
        raise ValueError('Initialization requires states, input phases and normalization lists')
    states = set()
    for state in receipt['initialized_states']:
        keys(state, 'name unit value'); number(state['value'])
        if not text(state['name']) or not text(state['unit']) or state['name'] in states:
            raise ValueError('Invalid or duplicate initialized state')
        states.add(state['name'])
    phases = []
    previous = start
    for index, phase in enumerate(receipt['binding_phases']):
        keys(phase, 'time activation inputs'); time = number(phase['time'])
        if phase['activation'] != ('initial' if index == 0 else 'post_boundary') or not previous <= time <= end or (index == 0 and time != start) or not isinstance(phase['inputs'], list):
            raise ValueError('Invalid native binding phase order or activation')
        previous = time
        inputs = {}
        for item in phase['inputs']:
            keys(item, 'name kind value unit'); number(item['value']); unit(item['unit'])
            if not text(item['name']) or item['name'] in inputs or item['kind'] not in ('parameter', 'covariate', 'individual_parameter', 'derived_covariate'):
                raise ValueError('Invalid or duplicate native phase input')
            inputs[item['name']] = item
        phases.append((phase, inputs))
    source = receipt['source_declaration']
    declarations = {}
    if source is not None:
        keys(source, 'file_sha256 manifest')
        declared = source['manifest']
        keys(declared, 'schema model_id model_version archive_sha256 native_model_sha256 scenarios normalizations scope')
        for digest in (source['file_sha256'], declared['archive_sha256'], declared['native_model_sha256']):
            if not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
                raise ValueError('Invalid source initialization digest')
        if declared['schema'] != 'qspquest.protocol-initialization/v1' or declared['model_id'] != manifest['model']['id'] or declared['model_version'] != manifest['model']['version'] or declared['archive_sha256'] != manifest['model']['archive_sha256'] or not text(declared['scope']) or not isinstance(declared['scenarios'], dict) or not isinstance(declared['normalizations'], list):
            raise ValueError('Initialization declaration differs from exported model')
        for scenario in declared['scenarios'].values():
            keys(scenario, 'native_request_sha256 integration_start intervention_time explicit_initial_override_count interpretation')
            if not isinstance(scenario['native_request_sha256'], str) or not re.fullmatch('[0-9a-f]{64}', scenario['native_request_sha256']) or type(scenario['explicit_initial_override_count']) is not int or scenario['explicit_initial_override_count'] < 0 or not text(scenario['interpretation']):
                raise ValueError('Invalid declared scenario initialization')
            for field in ('integration_start', 'intervention_time'):
                quantity = scenario[field]
                if quantity is None and field == 'intervention_time':
                    continue
                keys(quantity, 'value unit'); number(quantity['value'])
                if not text(quantity['unit']):
                    raise ValueError('Invalid declared scenario clock unit')
        for declaration in declared['normalizations']:
            normalization(declaration)
            if declaration['canonical_output'] in declarations:
                raise ValueError('Duplicate source normalization policy')
            declarations[declaration['canonical_output']] = declaration
    if receipt['declared_scenario'] is not None and (source is None or receipt['declared_scenario'] not in source['manifest']['scenarios'] or receipt['declared_scenario'] != manifest['inputs']['scenario_id']):
        raise ValueError('Initialization scenario differs from effective inputs')
    outputs = {c['native_name'] or c['name'] for c in manifest['table']['columns'] if c['kind'] == 'output'}
    expected = {name for name in declarations if name in outputs}
    seen = set()
    for normalized in receipt['normalization_receipts']:
        keys(normalized, 'declaration denominator_bindings')
        declaration = normalized['declaration']; normalization(declaration)
        name = declaration['canonical_output']
        if name in seen or name not in expected or declaration != declarations[name] or declaration['numerator_state'] not in states or not isinstance(normalized['denominator_bindings'], list) or len(normalized['denominator_bindings']) != len(phases):
            raise ValueError('Normalization differs from source, selected outputs or native phases')
        seen.add(name)
        for binding, (phase, inputs) in zip(normalized['denominator_bindings'], phases):
            keys(binding, 'time activation value unit'); number(binding['value']); unit(binding['unit'])
            item = inputs.get(declaration['denominator_input'])
            kinds = ('parameter', 'covariate') if declaration['basis'] == 'declared_reference_input' else ('individual_parameter',)
            if item is None or item['kind'] not in kinds or binding != {'time': phase['time'], 'activation': phase['activation'], 'value': item['value'], 'unit': item['unit']} or binding['value'] <= 0:
                raise ValueError('Normalization denominator differs from its actual native input phase')
    if seen != expected:
        raise ValueError('Selected normalized output lacks an initialization receipt')




def _scheduled_boundary_receipt(manifest, rows=None):
    """Check schedule transport against initialization, identity and CSV observation sides."""
    receipt = manifest.get('scheduled_boundary_receipt')
    if receipt is None:
        return
    def keys(value, names):
        _object(value, names.split(), 'Scheduled boundary receipt')
    def _text(value):
        return value is None or (isinstance(value,str) and bool(value.strip()) and len(value)<=1024 and not any(ord(c)<32 for c in value))
    def number(value):
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError('Boundary coordinates must be finite numbers')
        return value
    def index(value, count):
        if type(value) is not int or not 0 <= value < count:
            raise ValueError('Invalid boundary or phase index')
        return value
    def expression(root):
        nodes = [root]
        for node in nodes:
            if not isinstance(node, dict) or len(nodes) > 10000:
                raise ValueError('Invalid boundary expression')
            kind = node.get('kind')
            if kind == 'literal':
                keys(node, 'kind value')
                if type(node['value']) is not bool: number(node['value'])
            elif kind == 'symbol':
                keys(node, 'kind name')
                if not _text(node['name']) or node['name'] is None: raise ValueError('Invalid boundary symbol')
            else:
                field = 'name' if kind == 'call' else 'operator'
                keys(node, 'kind arguments' + ('' if kind == 'conditional' else ' ' + field))
                options = {'unary':('positive','negative','not'), 'binary':('add','subtract','multiply','divide','power','modulo'),
                           'compare':('lt','le','gt','ge','eq','ne'), 'boolean':('and','or'),
                           'call':('exp','log','log10','sqrt','sin','cos','tan','tanh','abs','min','max','floor','ceil','hill','ifelse')}
                if kind != 'conditional' and node.get(field) not in options.get(kind,()): raise ValueError('Invalid boundary operator')
                args = node['arguments']; arity = {'unary':1,'binary':2,'compare':2,'conditional':3}.get(kind)
                if not isinstance(args,list) or (arity is not None and len(args)!=arity): raise ValueError('Invalid boundary expression arity')
                nodes.extend(args)
    keys(receipt, 'schema stage time_unit integration_start integration_end planned_execution_identity fixed_switches dose_relative_switches boundaries observations observation_driver_rows pointwise_input_overrides requested_solver requested_relative_tolerance requested_state_absolute_tolerances achieved_error_estimate observation_convention')
    initial = manifest.get('initialization_receipt')
    if not isinstance(initial,dict) or receipt['schema'] != 'qspquest.scheduled-boundaries/v1' or receipt['stage'] != 'executed':
        raise ValueError('Boundary receipt requires an executed initialization receipt')
    if receipt['planned_execution_identity'] != manifest['engine_identity'] or any(receipt[k]!=initial[k] for k in ('planned_execution_identity','time_unit','integration_start','integration_end')):
        raise ValueError('Boundary clock or identity differs from native initialization')
    if receipt['achieved_error_estimate'] is not None or not _text(receipt['observation_convention']) or receipt['observation_convention'] is None:
        raise ValueError('Boundary receipt cannot assert an achieved error estimate')
    if receipt['requested_solver'] not in ('diffsol_bdf','diffsol_tsit45','diffsol_esdirk34','diffsol_tr_bdf2','diffsol_rosenbrock23','diffsol_rodas5p','analytic_linear_pk') or number(receipt['requested_relative_tolerance'])<=0:
        raise ValueError('Invalid requested solver or tolerance')
    for field in ('fixed_switches','dose_relative_switches','boundaries','observations','observation_driver_rows','pointwise_input_overrides','requested_state_absolute_tolerances'):
        if not isinstance(receipt[field],list): raise ValueError('Boundary receipt inventories must be arrays')
    boundaries = receipt['boundaries']; phases = initial['binding_phases']; seen_phases = set(); names = set()
    native_inputs = {v['name']:v for v in phases[0]['inputs']}
    prior = None
    for boundary in boundaries:
        keys(boundary, 'time native_checkpoint requested_checkpoint post_binding_phase_indices fixed_switch_names events')
        t = number(boundary['time'])
        if not receipt['integration_start']<=t<=receipt['integration_end'] or (prior is not None and t<=prior): raise ValueError('Boundary times must be ordered inside the run')
        prior=t
        if any(type(boundary[k]) is not bool for k in ('native_checkpoint','requested_checkpoint')) or (boundary['requested_checkpoint'] and not boundary['native_checkpoint']): raise ValueError('Invalid checkpoint origin')
        for field in ('post_binding_phase_indices','fixed_switch_names','events'):
            if not isinstance(boundary[field],list): raise ValueError('Invalid boundary inventory')
        for i in boundary['post_binding_phase_indices']:
            index(i,len(phases))
            if i==0 or i in seen_phases or phases[i]['time']!=t or phases[i]['activation']!='post_boundary': raise ValueError('Boundary phase differs from initialization')
            seen_phases.add(i)
        if len(boundary['fixed_switch_names'])!=len(set(boundary['fixed_switch_names'])): raise ValueError('Duplicate boundary switch')
        for event in boundary['events']:
            keys(event, 'native_event_index role target')
            if type(event['native_event_index']) is not int or event['native_event_index']<0 or event['role'] not in ('reset','bolus','infusion_start','infusion_end') or not _text(event['target']) or event['target'] is None:
                raise ValueError('Invalid native event reference')
    if seen_phases!=set(range(1,len(phases))): raise ValueError('Boundary table omits a native post-boundary phase')
    for switch in receipt['fixed_switches']:
        keys(switch, 'name time_expression parameter_bindings threshold comparison pointwise_value_at_threshold initial_input_value boundary_index')
        name=switch['name']; threshold=number(switch['threshold']); comparison=switch['comparison']
        if name in names or name not in native_inputs or number(switch['initial_input_value'])!=native_inputs[name]['value'] or comparison not in (None,'lt','le','gt','ge'):
            raise ValueError('Invalid declared native fixed switch')
        names.add(name); expression(switch['time_expression'])
        expected = None if comparison is None else int(comparison in ('le','ge'))
        if switch['pointwise_value_at_threshold'] != expected: raise ValueError('Pointwise predicate value differs from comparison')
        if not isinstance(switch['parameter_bindings'],list): raise ValueError('Invalid threshold parameter bindings')
        binding_names=set()
        for binding in switch['parameter_bindings']:
            if not isinstance(binding,dict) or binding.get('name') in binding_names or binding!=native_inputs.get(binding.get('name')) or binding.get('kind')!='parameter': raise ValueError('Threshold binding differs from native initialization')
            binding_names.add(binding['name'])
        if switch['boundary_index'] is not None:
            b=boundaries[index(switch['boundary_index'],len(boundaries))]
            if b['time']!=threshold or name not in b['fixed_switch_names']: raise ValueError('Fixed switch boundary correspondence differs')
        if comparison is not None and receipt['integration_start']<=threshold<=receipt['integration_end'] and switch['boundary_index'] is None: raise ValueError('In-window predicate boundary is missing')
    if {n for b in boundaries for n in b['fixed_switch_names']}!=names.intersection({n for s in receipt['fixed_switches'] if s['boundary_index'] is not None for n in [s['name']]}): raise ValueError('Undeclared boundary switch')
    for switch in receipt['dose_relative_switches']:
        keys(switch, 'name target offset comparison simultaneous'); expression(switch['offset'])
        if not _text(switch['name']) or switch['name'] is None or not _text(switch['target']) or switch['target'] is None or switch['name'] in names or switch['comparison'] not in ('lt','le','gt','ge') or switch['simultaneous'] not in ('first','last'): raise ValueError('Invalid dose-relative declaration')
        names.add(switch['name'])
    observations=receipt['observations']
    if len(observations)!=manifest['table']['rows'] or len(receipt['observation_driver_rows'])!=len(observations): raise ValueError('Boundary observation inventory differs from CSV')
    for observation,i in zip(observations,receipt['observation_driver_rows']):
        keys(observation, 'time side');t=number(observation['time'])
        if not receipt['integration_start']<=t<=receipt['integration_end'] or observation['side'] not in ('pre','post') or type(i) is not int or i<0: raise ValueError('Invalid native observation')
    seen_overrides=set()
    for override in receipt['pointwise_input_overrides']:
        keys(override, 'observation covariates');i=index(override['observation'],len(observations))
        if i in seen_overrides or not isinstance(override['covariates'],dict) or not override['covariates']: raise ValueError('Invalid pointwise override inventory')
        seen_overrides.add(i)
        for name,value in override['covariates'].items():
            keys(value, 'value unit')
            if name not in names or value['value'] not in (0,1) or type(value['value']) is bool or value['unit']!='1': raise ValueError('Invalid pointwise predicate override')
            fixed=next((s for s in receipt['fixed_switches'] if s['name']==name),None)
            if fixed and (observations[i]['time']!=fixed['threshold'] or value['value']!=fixed['pointwise_value_at_threshold']): raise ValueError('Pointwise override differs from fixed predicate')
    tolerances={}
    for tolerance in receipt['requested_state_absolute_tolerances']:
        keys(tolerance, 'state value unit')
        if tolerance['state'] in tolerances or number(tolerance['value'])<=0: raise ValueError('Invalid native state tolerance')
        tolerances[tolerance['state']]=tolerance['unit']
    if tolerances!={s['name']:s['unit'] for s in initial['initialized_states']}: raise ValueError('Tolerance coordinates differ from native initialized states')
    if rows is not None:
        columns=manifest['table']['columns'];time_name=columns[0]['name'];side_name=columns[1]['name']
        if any(row[time_name]!=o['time'] or row[side_name]!=o['side'] for row,o in zip(rows,observations)): raise ValueError('CSV observations differ from scheduled boundary receipt')


def _scientific_assessment(manifest):
    """Check declared status provenance and scope; never certify scientific truth."""
    receipt = manifest.get('scientific_assessment')
    if receipt is None:
        return
    def keys(v, names):
        if not isinstance(v, dict) or set(v) != set(names.split()):
            raise ValueError('Scientific assessment has missing or unknown fields')
    def text(v):
        if not isinstance(v, str) or not v.strip() or len(v.encode()) > 1024 or any(ord(c)<32 or 127<=ord(c)<=159 for c in v):
            raise ValueError('Invalid scientific assessment text')
    def digest(v):
        if not isinstance(v, str) or re.fullmatch('[0-9a-f]{64}', v) is None:
            raise ValueError('Invalid scientific assessment SHA-256')
    keys(receipt, 'schema declaration effective_source_matches_archive request_matches_stored_preset current_engine_and_request notice')
    if receipt['schema'] != 'qspquest.mcp-scientific-assessment/v1' or receipt['current_engine_and_request'] != 'not_assessed':
        raise ValueError('Scientific declaration cannot qualify the current engine and request')
    text(receipt['notice'])
    for k in ['effective_source_matches_archive', 'request_matches_stored_preset']:
        if receipt[k] is not None and type(receipt[k]) is not bool:
            raise ValueError('Invalid scientific assessment applicability')
    declaration = receipt['declaration']
    if declaration is None:
        if receipt['effective_source_matches_archive'] is not None:
            raise ValueError('Undeclared archive cannot have scientific assessment applicability')
        return
    keys(declaration, 'file_sha256 manifest');digest(declaration['file_sha256'])
    m = declaration['manifest']
    keys(m, 'schema model_id model_version archive_sha256 native_model_sha256 assessments scope')
    if m['schema'] != 'qspquest.scientific-assessments/v1':
        raise ValueError('Unsupported scientific assessment declaration')
    digest(m['archive_sha256']);digest(m['native_model_sha256']);text(m['model_id']);text(m['model_version']);text(m['scope'])
    model = manifest['model']
    if (m['model_id'],m['model_version'],m['archive_sha256']) != (model['id'],model['version'],model['archive_sha256']):
        raise ValueError('Scientific declaration differs from table model identity')
    metadata = (model.get('provenance') or {}).get('metadata') or {}
    descriptor = metadata.get('scientific_assessments') or {}
    if declaration != metadata.get('scientific_assessment_contract') or declaration['file_sha256'] != descriptor.get('sha256'):
        raise ValueError('Scientific declaration differs from retained pinned model provenance')
    axes = ['numerical_parity','source_fidelity','conservation','author_code_parity','clinical_validation','physical_dimensions']
    if not isinstance(m['assessments'],list) or len(m['assessments']) != 6 or {a.get('axis') for a in m['assessments'] if isinstance(a,dict)} != set(axes):
        raise ValueError('Scientific assessment must retain every independent axis exactly once')
    for a in m['assessments']:
        keys(a, 'axis outcome scope evidence findings');text(a['scope'])
        if a['outcome'] not in ('not_assessed','passed','failed','discrepancy_observed') or not isinstance(a['findings'],list) or len(a['findings'])>8:
            raise ValueError('Invalid scientific assessment outcome or findings')
        if a['outcome']=='not_assessed':
            if a['evidence'] is not None or a['findings']:
                raise ValueError('Unassessed axes cannot carry assessment evidence')
        else:
            keys(a['evidence'], 'artifact_sha256 method scope');digest(a['evidence']['artifact_sha256']);text(a['evidence']['method']);text(a['evidence']['scope'])
        if a['outcome'] in ('failed','discrepancy_observed') and not a['findings']:
            raise ValueError('Failed or discrepant assessment lacks findings')
        ids=set()
        for f in a['findings']:
            keys(f, 'id description expression value declared_unit native_symbols')
            for k in ['id','description','expression','declared_unit']:text(f[k])
            if f['id'] in ids or type(f['value']) not in (int,float) or not math.isfinite(f['value']):
                raise ValueError('Invalid scientific finding value or duplicate id')
            ids.add(f['id']);names=f['native_symbols']
            if not isinstance(names,list) or not 1<=len(names)<=64 or any(not isinstance(n,str) for n in names) or len(set(names)) != len(names):
                raise ValueError('Invalid scientific finding native symbols')
            for n in names:text(n)
    inputs = manifest['inputs']
    if type(receipt['effective_source_matches_archive']) is not bool or (inputs.get('modified') is False and not receipt['effective_source_matches_archive']):
        raise ValueError('Scientific source applicability differs from unchanged table provenance')
    if inputs.get('scenario_id') is not None and receipt['request_matches_stored_preset'] != (inputs.get('modified') is False):
        raise ValueError('Scientific assessment preset scope differs from effective input provenance')

def validate_manifest(value, filename):
    """Validate this version's closed transport contract, not scientific truth."""
    optional = [k for k in ('required_output_receipts','dose_event_receipts','initialization_receipt','scheduled_boundary_receipt','scientific_assessment') if isinstance(value, dict) and k in value]
    _object(value, ['schema', 'producer', 'table', 'events', 'model', 'engine_identity', 'inputs', 'qualification'] + optional, 'Manifest')
    if value['schema'] != SCHEMA or value['producer'] not in ('model_library', 'mcp'):
        raise ValueError('Unsupported table manifest schema or producer')
    table = value['table']
    _object(table, ['filename', 'sha256', 'bytes', 'rows', 'columns'], 'Table descriptor')
    if table['filename'] != filename or Path(filename).name != filename:
        raise ValueError('Manifest table filename differs from the supplied CSV')
    if not isinstance(table['sha256'], str) or not re.fullmatch('[0-9a-f]{64}', table['sha256']):
        raise ValueError('Table digest must be a lowercase SHA-256')
    for key, limit in [('bytes', MAX_TABLE_BYTES), ('rows', MAX_ROWS)]:
        if type(table[key]) is not int or not 0 <= table[key] <= limit:
            raise ValueError('Table ' + key + ' exceeds supported limits or is invalid')
    columns = table['columns']
    if not isinstance(columns, list) or len(columns) < 2:
        raise ValueError('Table requires time and side columns')
    names = []
    for column in columns:
        _object(column, ['name', 'unit', 'kind', 'native_name', 'meaning'], 'Column')
        if not isinstance(column['name'], str) or not column['name'] or '\x00' in column['name']:
            raise ValueError('Table column names must be nonempty text without NUL')
        for field in ['unit', 'native_name', 'meaning']:
            if column[field] is not None and (not isinstance(column[field], str) or not column[field]):
                raise ValueError('Column ' + field + ' must be nonempty text or null')
        if column['kind'] not in ('time', 'event_side', 'output', 'state', 'source_parameter'):
            raise ValueError('Unsupported column kind')
        names.append(column['name'])
    if len(names) != len(set(names)) or columns[0]['kind'] != 'time' or columns[1]['kind'] != 'event_side' or names[1] != 'side':
        raise ValueError('Table columns must be unique, beginning with time and side')
    if any(c['kind'] in ('time', 'event_side') for c in columns[2:]):
        raise ValueError('Time and side occur only in the first two columns')
    events = value['events']
    _object(events, ['rule', 'pre', 'post', 'event_pairs'], 'Events')
    if events['rule'] != EVENT_RULE or any(type(events[k]) is not int or events[k] < 0 for k in ('pre', 'post', 'event_pairs')):
        raise ValueError('Invalid event-side semantics or counts')
    if events['pre'] + events['post'] != table['rows'] or events['event_pairs'] > min(events['pre'], events['post']):
        raise ValueError('Event counts contradict table rows')
    model = value['model']
    _object(model, ['id', 'version', 'archive_sha256', 'provenance'], 'Model provenance')
    for key in ('id', 'version', 'archive_sha256'):
        if model[key] is not None and (not isinstance(model[key], str) or not model[key]):
            raise ValueError('Model ' + key + ' must be nonempty text or null')
    if model['archive_sha256'] is not None and not re.fullmatch('[0-9a-f]{64}', model['archive_sha256']):
        raise ValueError('Archive digest must be a lowercase SHA-256')
    for obj in (model['provenance'], value['engine_identity']):
        if obj is not None and not isinstance(obj, dict):
            raise ValueError('Engine identity and model provenance must be objects or null')
    provenance = model['provenance'] or {}
    if provenance.get('source_interpretations') is not None:
        from . import _source_interpretations
        interpretation = _source_interpretations(provenance['source_interpretations'], model['id'], model['version'], model['archive_sha256'])
        if interpretation['native_model_sha256'] != provenance.get('native_model_sha256'):
            raise ValueError('Source interpretation differs from table native model provenance')
    inputs = value['inputs']
    _object(inputs, ['effective_request', 'selected_outputs', 'effective_request_hash', 'scenario_id', 'modified'], 'Inputs')
    if inputs['effective_request'] is not None and not isinstance(inputs['effective_request'], dict):
        raise ValueError('Effective request must be an object or null')
    if inputs['modified'] is not None and type(inputs['modified']) is not bool:
        raise ValueError('Modified-run status must be boolean or null')
    for key in ('effective_request_hash', 'scenario_id'):
        if inputs[key] is not None and (not isinstance(inputs[key], str) or not inputs[key]):
            raise ValueError('Input ' + key + ' must be nonempty text or null')
    if provenance.get('precision_profile') is not None:
        from .precision_profiles import validate_receipt
        validate_receipt(provenance['precision_profile'], model, inputs)
    selected = inputs['selected_outputs']
    if selected is not None and (not isinstance(selected, list) or any(not isinstance(s, str) or not s for s in selected) or len(selected) != len(set(selected))):
        raise ValueError('Selected outputs must be unique names or null')
    q = value['qualification']
    _object(q, ['qualified', 'status', 'scope', 'unit_status', 'coordinates', 'recorded_dimensional_qualification', 'recorded_availability'], 'Qualification')
    if q['qualified'] is not False or q['status'] != 'not_assessed' or q['scope'] != 'current_engine_and_effective_request':
        raise ValueError('Table manifests cannot assert current-engine qualification')
    if q['unit_status'] not in ('source_scale_unqualified', 'unqualified'):
        raise ValueError('Unsupported table unit status')
    if q['coordinates'] is not None and (not isinstance(q['coordinates'], str) or not q['coordinates']):
        raise ValueError('Coordinates must be nonempty text or null')
    if q['coordinates'] == 'unchanged_source_numeric_values' and q['unit_status'] != 'source_scale_unqualified':
        raise ValueError('Source coordinates require a source-scale warning')
    if q['recorded_dimensional_qualification'] is not None and type(q['recorded_dimensional_qualification']) is not bool:
        raise ValueError('Recorded dimensional qualification must be boolean or null')
    if q['recorded_availability'] is not None and not isinstance(q['recorded_availability'], dict):
        raise ValueError('Recorded availability must be an object or null')
    _mcp_receipts(value)
    _scientific_assessment(value)
    _initialization_receipt(value)
    _scheduled_boundary_receipt(value)
    # Reject nonfinite numbers anywhere in opaque recorded metadata, too.
    json.dumps(value, allow_nan=False)


def write_table(result, path, columns):
    """Create CSV and sidecar without replacing existing files; return the manifest."""
    path = Path(path)
    if path.suffix != '.csv':
        raise ValueError('Choose a new .csv filename; the sidecar appends .manifest.json')
    times, sides = result['times'], result['sides']
    if len(times) != len(sides) or len(times) > MAX_ROWS or any(len(c['values']) != len(times) for c in columns):
        raise ValueError('Table columns and event sides must match the time row count')
    _event_counts(zip(times, sides))
    rows = ([_finite(t), sides[i]] + [_finite(c['values'][i]) for c in columns] for i, t in enumerate(times))
    text = io.StringIO(newline='')
    writer = csv.writer(text, lineterminator='\n')
    writer.writerow(['time', 'side'] + [c['name'] for c in columns])
    writer.writerows(rows)
    data = text.getvalue().encode('utf-8')
    manifest = manifest_for(result, path.name, data, columns)
    metadata = (json.dumps(manifest, indent=2, allow_nan=False) + '\n').encode('utf-8')
    if len(metadata) > MAX_MANIFEST_BYTES:
        raise ValueError('Table manifest exceeds the 16 MiB limit')
    sidecar = Path(str(path) + '.manifest.json')
    created = []
    try:
        # Reserve both names exclusively before writing either payload.
        with path.open('xb') as table:
            created.append((path, os.fstat(table.fileno())))
            with sidecar.open('xb') as meta:
                created.append((sidecar, os.fstat(meta.fileno())))
                table.write(data)
                table.flush()
                os.fsync(table.fileno())
                meta.write(metadata)
                meta.flush()
                os.fsync(meta.fileno())
    except BaseException:
        for name, identity in reversed(created):
            try:
                current = name.stat(follow_symlinks=False)
                if (current.st_dev, current.st_ino) == (identity.st_dev, identity.st_ino):
                    name.unlink()
            except OSError:
                pass
        raise
    return manifest


def read_table(path):
    """Validate raw bytes, ordered columns and pre/post events before returning rows.

    The digest detects corruption. It does not authenticate the producer or qualify
    the run; inspect recorded identities and the explicit qualification scope.
    """
    path = Path(path)
    sidecar = Path(str(path) + '.manifest.json')
    for name, limit in [(path, MAX_TABLE_BYTES), (sidecar, MAX_MANIFEST_BYTES)]:
        if name.is_symlink() or not name.is_file() or name.stat().st_size > limit:
            raise ValueError('Bundle requires ordinary files within the documented size limits: ' + str(name))
    with sidecar.open('rb') as file:
        metadata = file.read(MAX_MANIFEST_BYTES + 1)
    if len(metadata) > MAX_MANIFEST_BYTES:
        raise ValueError('Manifest exceeds 16 MiB')
    manifest = json.loads(metadata, object_pairs_hook=_unique, parse_constant=_reject_constant)
    validate_manifest(manifest, path.name)
    with path.open('rb') as file:
        data = file.read(MAX_TABLE_BYTES + 1)
    descriptor = manifest['table']
    if len(data) != descriptor['bytes'] or hashlib.sha256(data).hexdigest() != descriptor['sha256']:
        raise ValueError('CSV byte count or SHA-256 differs from its manifest')
    reader = csv.reader(io.StringIO(data.decode('utf-8'), newline=''), strict=True)
    names = [c['name'] for c in descriptor['columns']]
    rows = []
    try:
        if next(reader, None) != names:
            raise ValueError('CSV header differs from the ordered manifest columns')
        for row in reader:
            if len(row) != len(names) or len(rows) >= MAX_ROWS:
                raise ValueError('CSV row width or supported row count is invalid')
            rows.append(row)
    except csv.Error as error:
        raise ValueError('Invalid CSV syntax: ' + str(error)) from error
    if len(rows) != descriptor['rows'] or _event_counts(rows) != {k: manifest['events'][k] for k in ('pre', 'post', 'event_pairs')}:
        raise ValueError('CSV row count or event-side counts differ from its manifest')
    for index, row in enumerate(rows):
        values = [_finite(float(value)) if i != 1 else value for i, value in enumerate(row)]
        rows[index] = dict(zip(names, values))
    _scheduled_boundary_receipt(manifest, rows)
    return {'manifest': manifest, 'rows': rows}
