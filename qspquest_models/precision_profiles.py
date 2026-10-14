"""Verify and select complete, archive-bound source precision conventions."""
from copy import deepcopy
import hashlib
import json
import math


def digest(value):
    """SHA-256 of sorted compact Python JSON; distinct from native run identity."""
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def validate(record, index, archive_sha256, members):
    if record is None:
        return None
    if not isinstance(record, dict):
        raise ValueError('Precision profile manifest must be an object')
    native_path = index['native_execution'].get('model')
    if not native_path or native_path not in members:
        raise ValueError('Precision profiles require an executable native model')
    native = json.loads(members[native_path])
    if (record.get('schema') != 'qspquest.precision-profiles/v1'
            or record.get('model_id') != index['model_id']
            or record.get('model_version') != index['model_version']
            or record.get('archive_sha256') != archive_sha256
            or record.get('native_model_sha256') != hashlib.sha256(members[native_path]).hexdigest()):
        raise ValueError('Precision profile archive/version/native identity mismatch; reload the verified library')
    parameters = {p['name']: p for p in native['parameters']}
    immutable = {n: p['default'] for n, p in parameters.items() if p.get('fixed', False)}
    mutable = set(parameters) - set(immutable)
    if (record.get('immutable_parameters') != immutable
            or record.get('parameter_count') != len(parameters)
            or record.get('mutable_parameter_count') != len(mutable)):
        raise ValueError('Precision profile parameter inventory mismatch')
    profiles = record.get('profiles')
    if not isinstance(profiles, list) or not profiles or len(profiles) > 64:
        raise ValueError('Precision profile inventory must contain 1-64 named profiles')
    ids = set()
    for profile in profiles:
        if not isinstance(profile, dict) or set(profile) != {'id', 'choices', 'scenarios'} or not isinstance(profile['choices'], dict) or not isinstance(profile['scenarios'], dict):
            raise ValueError('Invalid precision profile fields')
        identifier = profile.get('id')
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise ValueError('Precision profile identifiers must be unique nonempty strings')
        ids.add(identifier)
        if set(profile.get('scenarios', {})) != set(index['native_execution']['scenarios']):
            raise ValueError('Precision profile must cover every archived scenario')
        for sid, entry in profile['scenarios'].items():
            if not isinstance(entry, dict) or not isinstance(entry.get('parameters'), dict) or not isinstance(entry.get('transformations'), list) or any(not isinstance(t, str) for t in entry['transformations']):
                raise ValueError('Invalid precision profile scenario entry: ' + sid)
            values = entry.get('parameters', {})
            if set(values) != mutable or entry.get('parameters_sha256') != digest(values):
                raise ValueError('Precision profile requires the complete hashed mutable parameter map: ' + sid)
            for name, quantity in values.items():
                if not isinstance(quantity, dict):
                    raise ValueError('Invalid precision profile native quantity: ' + name)
                p = parameters[name]
                value = quantity.get('value')
                if (set(quantity) != {'value', 'unit'} or quantity['unit'] != p['default']['unit']
                        or isinstance(value, bool) or not isinstance(value, (int, float))
                        or not math.isfinite(value)):
                    raise ValueError('Invalid precision profile native quantity: ' + name)
                if p.get('bounds') and not p['bounds'][0]['value'] <= value <= p['bounds'][1]['value']:
                    raise ValueError('Precision profile value outside native bounds: ' + name)
            if identifier == record.get('default_profile_id'):
                archived = json.loads(members[index['native_execution']['scenarios'][sid]])
                baseline = {n: archived.get('parameters', {}).get(n, parameters[n]['default']) for n in mutable}
                if baseline != values:
                    raise ValueError('Precision profile default differs from archived scenario: ' + sid)
    if record.get('default_profile_id') not in ids:
        raise ValueError('Precision profile default is unavailable')
    return deepcopy(record)


def select(record, scenario_id, profile_id=None):
    if record is None:
        if profile_id is not None:
            raise ValueError('No precision profiles declared for this archive; inspect model.precision_profiles')
        return None
    identifier = record['default_profile_id'] if profile_id is None else profile_id
    profile = next((p for p in record['profiles'] if p['id'] == identifier), None)
    if profile is None:
        raise ValueError('Unknown precision profile: ' + str(identifier) + '; inspect model.precision_profiles')
    if scenario_id not in profile['scenarios']:
        raise ValueError('Precision profile scenario unavailable: ' + str(scenario_id))
    return deepcopy(profile)


def receipt(record, index, members, request, scenario_id, profile_id=None):
    profile = select(record, scenario_id, profile_id)
    if profile is None:
        return None
    native = json.loads(members[index['native_execution']['model']])
    expected = profile['scenarios'][scenario_id]
    effective = {p['name']: request.get('parameters', {}).get(p['name'], p['default'])
                 for p in native['parameters'] if not p.get('fixed', False)}
    changes = sorted(n for n in expected['parameters'] if effective[n] != expected['parameters'][n])
    timed = bool(request.get('parameter_changes'))
    return {'schema': 'qspquest.precision-profile-receipt/v1',
            'model_id': record['model_id'], 'model_version': record['model_version'],
            'archive_sha256': record['archive_sha256'], 'manifest_sha256': digest(record),
            'profile_id': profile['id'], 'scenario_id': scenario_id, 'choices': profile['choices'],
            'parameters_status': 'modified' if changes or timed else 'matches_profile',
            'changed_parameter_names': changes, 'timed_parameter_changes_present': timed,
            'profile_parameters_sha256': expected['parameters_sha256'],
            'effective_parameters_sha256': digest(effective), 'effective_parameters': deepcopy(effective),
            'immutable_parameters': deepcopy(record['immutable_parameters']),
            'transformations': expected['transformations'], 'source': deepcopy(record['source']),
            'hash_encoding': record['hash_encoding'],
            'scope': 'Scalar parameter convention only. Initial states, doses, covariates and solver settings are separate. A modified receipt does not claim the named whole profile. Differences between source conventions do not establish failed biology or scientific qualification.'}


def validate_receipt(value, model, inputs):
    """Check retained transport against the saved inputs, not source accuracy."""
    keys = {'schema', 'model_id', 'model_version', 'archive_sha256', 'manifest_sha256',
            'profile_id', 'scenario_id', 'choices', 'parameters_status',
            'changed_parameter_names', 'timed_parameter_changes_present',
            'profile_parameters_sha256', 'effective_parameters_sha256', 'effective_parameters',
            'immutable_parameters', 'transformations', 'source', 'hash_encoding', 'scope'}
    if not isinstance(value, dict) or set(value) != keys or value['schema'] != 'qspquest.precision-profile-receipt/v1':
        raise ValueError('Invalid precision profile receipt fields or schema')
    if (value['model_id'] != model['id'] or value['model_version'] != model['version']
            or value['archive_sha256'] != model['archive_sha256']
            or value['scenario_id'] != inputs['scenario_id']):
        raise ValueError('Precision profile receipt differs from table model/scenario')
    for key in ('archive_sha256', 'manifest_sha256', 'profile_parameters_sha256', 'effective_parameters_sha256'):
        h = value[key]
        if not isinstance(h, str) or len(h) != 64 or any(c not in '0123456789abcdef' for c in h):
            raise ValueError('Invalid precision profile receipt digest')
    effective = value['effective_parameters']
    if not isinstance(effective, dict) or not effective or digest(effective) != value['effective_parameters_sha256']:
        raise ValueError('Precision profile receipt effective parameter hash mismatch')
    for values in (effective, value['immutable_parameters']):
        if not isinstance(values, dict):
            raise ValueError('Precision profile receipt parameters must be maps')
        for name, q in values.items():
            if (not isinstance(name, str) or not isinstance(q, dict) or set(q) != {'value', 'unit'}
                    or type(q['value']) not in (int, float) or not math.isfinite(q['value'])
                    or not isinstance(q['unit'], str) or not q['unit']):
                raise ValueError('Invalid precision profile receipt quantity')
    request = inputs['effective_request']
    if not isinstance(request, dict):
        raise ValueError('Precision profile receipt requires effective request')
    for name, q in request.get('parameters', {}).items():
        if q != effective.get(name, value['immutable_parameters'].get(name)):
            raise ValueError('Precision profile receipt differs from effective request parameter: ' + name)
    timed = bool(request.get('parameter_changes'))
    if type(value['timed_parameter_changes_present']) is not bool or value['timed_parameter_changes_present'] != timed:
        raise ValueError('Precision profile receipt timed changes differ from request')
    if (not isinstance(value['changed_parameter_names'], list)
            or len(set(value['changed_parameter_names'])) != len(value['changed_parameter_names'])
            or any(n not in effective for n in value['changed_parameter_names'])):
        raise ValueError('Invalid changed precision profile parameter names')
    if value['parameters_status'] not in ('matches_profile', 'modified'):
        raise ValueError('Invalid precision profile parameter status')
    if value['parameters_status'] == 'matches_profile' and (timed or value['changed_parameter_names']
            or value['effective_parameters_sha256'] != value['profile_parameters_sha256']):
        raise ValueError('Unchanged precision profile receipt contradicts its hashes/changes')
