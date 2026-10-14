"""Inspect hash-bound initialization clocks and explicit normalization policies."""
from copy import deepcopy
import hashlib
import json
import math
import re


def validate(declaration, index, archive_sha256, members):
    """Validate source coordinates without asserting equilibrium or qualification."""
    if declaration is None:
        return None
    def keys(value, fields):
        if not isinstance(value, dict) or set(value) != set(fields.split()):
            raise ValueError('Protocol initialization has missing or unknown fields')
    def text(value):
        return isinstance(value, str) and bool(value.strip()) and len(value) <= 1024 and not any(ord(c) < 32 for c in value)
    def digest(value):
        return isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value)
    def quantity(value):
        keys(value, 'value unit')
        if type(value['value']) not in (int, float) or not math.isfinite(value['value']) or not text(value['unit']):
            raise ValueError('Invalid protocol clock quantity')
    keys(declaration, 'file_sha256 manifest')
    record = declaration['manifest']
    keys(record, 'schema model_id model_version archive_sha256 native_model_sha256 scenarios normalizations scope')
    native_path = index['native_execution'].get('model')
    if not native_path or native_path not in members:
        raise ValueError('Protocol initialization requires an executable native model')
    native = json.loads(members[native_path])
    if (record['schema'] != 'qspquest.protocol-initialization/v1'
            or record['model_id'] != index['model_id'] or record['model_version'] != index['model_version']
            or record['archive_sha256'] != archive_sha256
            or record['native_model_sha256'] != hashlib.sha256(members[native_path]).hexdigest()
            or not digest(declaration['file_sha256']) or not text(record['scope'])):
        raise ValueError('Protocol initialization archive/version/native identity mismatch')
    if not isinstance(record['scenarios'], dict) or set(record['scenarios']) != set(index['native_execution']['scenarios']):
        raise ValueError('Protocol initialization must cover the exact archived scenario set')
    for scenario_id, declared in record['scenarios'].items():
        keys(declared, 'native_request_sha256 integration_start intervention_time explicit_initial_override_count interpretation')
        path = index['native_execution']['scenarios'][scenario_id]
        request = json.loads(members[path])
        quantity(declared['integration_start'])
        if declared['intervention_time'] is not None:
            quantity(declared['intervention_time'])
        start = request['regimen'].get('start') or {'value': 0, 'unit': native['time_unit']}
        if (declared['native_request_sha256'] != hashlib.sha256(members[path]).hexdigest()
                or declared['integration_start'] != start
                or type(declared['explicit_initial_override_count']) is not int
                or declared['explicit_initial_override_count'] != len(request.get('initial_states', {}))
                or not text(declared['interpretation'])):
            raise ValueError('Protocol initialization differs from archived scenario: ' + scenario_id)
    states = {s['name'] for s in native.get('states', [])}
    outputs = {o['name']: o for o in native['outputs']}
    parameters = {p['name'] for p in native['parameters']}
    derived = {p['name'] for p in native.get('individual', [])}
    if not isinstance(record['normalizations'], list) or len(record['normalizations']) > 128:
        raise ValueError('Protocol normalization inventory exceeds 128 readouts')
    seen = set()
    for normalized in record['normalizations']:
        keys(normalized, 'canonical_output numerator_state denominator_input multiplier basis interpretation')
        name, state, denominator = (normalized[k] for k in ('canonical_output', 'numerator_state', 'denominator_input'))
        if (any(not text(normalized[k]) for k in ('canonical_output', 'numerator_state', 'denominator_input', 'interpretation'))
                or name in seen or name not in outputs or state not in states
                or type(normalized['multiplier']) not in (int, float)
                or not math.isfinite(normalized['multiplier']) or normalized['multiplier'] <= 0):
            raise ValueError('Invalid or duplicate normalization coordinates')
        seen.add(name)
        if ((normalized['basis'] == 'declared_reference_input' and denominator not in parameters)
                or (normalized['basis'] == 'condition_specific_binding' and denominator not in derived)
                or normalized['basis'] not in ('declared_reference_input', 'condition_specific_binding')):
            raise ValueError('Normalization basis differs from native input kind')
        expression = {'kind': 'binary', 'operator': 'divide', 'arguments': [
            {'kind': 'binary', 'operator': 'multiply', 'arguments': [
                {'kind': 'literal', 'value': normalized['multiplier']}, {'kind': 'symbol', 'name': state}]},
            {'kind': 'symbol', 'name': denominator}]}
        if outputs[name]['expression'] != expression:
            raise ValueError('Normalization differs from native readout expression: ' + name)
    return deepcopy(declaration)
