"""Version-bound native input names and units for verified model archives."""
from copy import deepcopy
import hashlib
import json

SCHEMA = 'qspquest.models.input-bindings/v1'


class InputBindingError(ValueError):
    """Input lookup or migration failure with a machine-readable diagnostic."""

    def __init__(self, diagnostic):
        self.diagnostic = diagnostic
        super().__init__(diagnostic['message'])


def _digest(value):
    body = json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode('utf-8')
    return hashlib.sha256(body).hexdigest()


def _states(model):
    rows = list(model.get('states', []))
    pk = model.get('linear_pk')
    if pk:
        for row in ([pk['depot']] if pk.get('depot') else []) + pk['compartments']:
            rows.append({'name': row['state'], 'unit': pk['amount_unit'],
                         'initial': row['initial']})
    return {row['name']: row for row in rows}


def build(members, index, archive_sha256):
    """Describe canonical and declared aliases; never infer physical conversions."""
    native = index['native_execution']
    path = native.get('model')
    if not path:
        raise ValueError('Native input bindings require an executable model archive')
    raw = members[path]
    model = json.loads(raw)
    parameters = {row['name']: row for row in model.get('parameters', [])}
    states = _states(model)
    readouts = {row['name']: row['expression'] for row in model.get('outputs', [])}
    tables = {'parameters': {}, 'initial_states': {}}

    def add(group, alias, target, declared=None):
        rows = parameters if group == 'parameters' else states
        if target not in rows or alias in rows and alias != target:
            raise ValueError('Invalid archive input alias: ' + group + '.' + alias)
        row = rows[target]
        entry = {'native_name': target, 'canonical': alias == target,
                 'description': row.get('description'),
                 'unit': row['default']['unit'] if group == 'parameters' else row['unit'],
                 'declared_source_unit': None if declared is None else declared.get('source_unit', declared.get('unit')),
                 'archive_request_unit': None if declared is None else declared.get('request_unit')}
        if group == 'parameters':
            entry.update(default=deepcopy(row['default']), fixed=row.get('fixed', False),
                         bounds=deepcopy(row.get('bounds')))
        else:
            entry['initial_expression'] = deepcopy(row['initial'])
        tables[group][alias] = entry

    for name in parameters:
        add('parameters', name, name)
    for name in states:
        add('initial_states', name, name)
    for alias, row in native.get('parameters', {}).items():
        add('parameters', alias, row['native_name'], row)
    explicit = native.get('input_states')
    if isinstance(explicit, dict):
        for alias, row in explicit.items():
            add('initial_states', alias, row['native_name'], row)
    else:
        for alias, row in native.get('states', {}).items():
            target = row['native_name']
            expression = readouts.get(target)
            if expression:
                if expression.get('kind') != 'symbol':
                    continue
                target = expression['name']
            if target in states:
                add('initial_states', alias, target, row)
    context = {'model_id': index['model_id'], 'model_version': index['model_version'],
               'archive_sha256': archive_sha256,
               'native_model_sha256': hashlib.sha256(raw).hexdigest(),
               'index_sha256': _digest(index),
               'scenario_sha256': {name: hashlib.sha256(members[path]).hexdigest()
                                   for name, path in native.get('scenarios', {}).items()}}
    result = {'schema': SCHEMA, 'context': context, **tables,
              'value_unit': 'Numeric edits use the actual native unit in each binding. Source labels and archive request coordinates are informational; no physical conversion is inferred.',
              'initial_values': 'Initial expressions remain native declarations; this registry does not evaluate coupled or derived starting values.'}
    context['input_binding_hash'] = 'sha256:' + _digest(result)
    return result


def check(bindings, expected):
    if expected is None:
        return
    context = bindings['context']
    if (not isinstance(expected, str) or len(expected) != 71
            or not expected.startswith('sha256:')
            or any(c not in '0123456789abcdef' for c in expected[7:])):
        raise InputBindingError({'code': 'input_binding_hash',
            'message': 'Use the exact input_binding_hash string from model.input_bindings.context.',
            'model_id': context['model_id'], 'model_version': context['model_version']})
    if expected != context['input_binding_hash']:
        raise InputBindingError({'code': 'input_bindings_changed',
            'message': 'Model, archive inputs or aliases changed. Inspect model.input_bindings and explicitly migrate names, units and starting values before creating a new research copy.',
            'model_id': context['model_id'], 'model_version': context['model_version'],
            'expected_input_binding_hash': expected,
            'current_input_binding_hash': context['input_binding_hash'],
            'migration': 'inspect_current_bindings'})


def resolve(bindings, group, name, expected=None):
    check(bindings, expected)
    if group not in ('parameters', 'initial_states'):
        raise ValueError('Input binding group must be parameters or initial_states')
    if not isinstance(name, str) or name not in bindings[group]:
        context = bindings['context']
        raise InputBindingError({'code': 'input_alias_unknown',
            'message': 'Unknown ' + group + ' alias for this model version; inspect model.input_bindings and explicitly select its current native input name.',
            'model_id': context['model_id'], 'model_version': context['model_version'],
            'group': group, 'name': str(name)[:128],
            'current_input_binding_hash': context['input_binding_hash'],
            'migration': 'inspect_current_bindings'})
    return deepcopy(bindings[group][name])
