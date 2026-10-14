"""Archive-bound scalar/individual synthetic fitting declarations."""
from copy import deepcopy
import hashlib
import json
import math
import re

SCHEMA = 'qspquest.library-fitting/v1'


def _object(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= set(value) or set(value) - set(required) - set(optional):
        raise ValueError('Fitting declaration has missing or unknown fields')
    return value


def _number(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('Fitting quantities require finite numbers, excluding booleans')
    return value


def _text(value):
    if not isinstance(value, str) or not value:
        raise ValueError('Fitting text must be nonempty')
    return value


def _digest(value, prefix=''):
    if not isinstance(value, str) or not re.fullmatch(re.escape(prefix) + '[0-9a-f]{64}', value):
        raise ValueError('Fitting identity requires SHA-256')
    return value


def _json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate fitting JSON key: ' + key)
            result[key] = value
        return result
    def reject(value):
        raise ValueError('Nonfinite fitting JSON: ' + value)
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=reject)


def _member(reference, index, members):
    _object(reference, ('path', 'sha256'))
    path, digest = _text(reference['path']), _digest(reference['sha256'])
    if '\\' in path or ':' in path or any(part in ('', '.', '..') for part in path.split('/')):
        raise ValueError('Unsafe fitting archive member path')
    raw = members.get(path)
    if index['members'].get(path) != digest or not isinstance(raw, bytes) or len(raw) > 1_000_000 or hashlib.sha256(raw).hexdigest() != digest:
        raise ValueError('Fitting member SHA-256 or byte limit differs')
    return _json(raw)


def _quantity(value, number, unit):
    _object(value, ('value', 'unit'))
    if _number(value['value']) != number or value['unit'] != unit:
        raise ValueError('Fitting quantity differs from its declared units/value')


def _pieces(workflow):
    request = workflow['native_request']
    if workflow['operation'] == 'fit_scalar':
        _object(request, ('schema', 'run', 'parameter', 'lower', 'upper', 'observations', 'max_iterations', 'absolute_tolerance'))
        if request['schema'] != 'qspquest.scalar-fit/v0.1':
            raise ValueError('Scalar fitting schema differs')
        return request['run'], request['observations'], None
    if workflow['operation'] != 'fit_individual':
        raise ValueError('Only scalar and individual workflows are supported')
    _object(request, ('schema', 'problem'))
    _object(request['problem'], ('kind', 'request'))
    if request['schema'] != 'qspquest.fit/v0.1' or request['problem']['kind'] != 'individual':
        raise ValueError('Individual fitting requires problem.kind individual')
    fit = _object(request['problem']['request'], ('objective', 'bounds', 'max_evaluations', 'max_iterations', 'gradient_tolerance'))
    objective = _object(fit['objective'], ('simulation', 'observations', 'priors'))
    simulation = _object(objective['simulation'], ('schema', 'run', 'with_respect_to', 'derivative_absolute_tolerances'))
    if simulation['schema'] != 'qspquest.sensitivity/v0.1' or objective['priors'] != []:
        raise ValueError('Individual synthetic workflows require sensitivities and no priors')
    return simulation['run'], objective['observations'], fit


def _native_identity(model, request, operation, result=None):
    try:
        from qspquest import fitting_identity
    except ImportError as error:
        raise RuntimeError('Fitting requires the matching QSPQuest Python binding; follow tutorials/library-fitting.md. Archive inspection and preset simulation work without it') from error
    return fitting_identity(model, request, operation, result=result)



def _check_result_numbers(result, roles, observation_count, operation, fit_request_hash):
    """Check complete fit diagnostics before evaluating parameter recovery."""
    names = [r['native_name'] for r in roles]
    objective = result.get('objective', {})
    if (not names or set(result.get('parameters', {})) != set(names)
            or type(objective.get('observations')) is not int
            or objective['observations'] != observation_count or observation_count <= 0
            or type(result.get('evaluations')) is not int or result['evaluations'] <= 0
            or type(result.get('iterations')) is not int or result['iterations'] < 0
            or result.get('fit_request_hash') != fit_request_hash):
        raise ValueError('Fitting result parameters, counts or archived request/algorithm identity differ')
    _digest(fit_request_hash, 'sha256:')
    for role in roles:
        estimate = result['parameters'][role['native_name']]
        _quantity(estimate, _number(estimate.get('value')), role['unit'])
    for key in ('objective', 'negative_log_likelihood'):
        _number(objective.get(key))
    if operation == 'fit_individual':
        _number(objective.get('negative_log_prior'))
        gradient = objective.get('gradient')
        if (not isinstance(gradient, list) or len(gradient) != len(names)
                or [g.get('parameter') for g in gradient] != names):
            raise ValueError('Fitting objective gradient inventory differs')
        for role, value in zip(roles, gradient):
            _number(value.get('value'))
            if value.get('unit') != '1/(' + role['unit'] + ')':
                raise ValueError('Fitting objective gradient unit differs')
        if _number(result.get('projected_gradient_norm')) < 0:
            raise ValueError('Fitting projected gradient must be nonnegative')


def validate(declaration, index, members, availability=None, *, native_identity=True):
    """Check archive records; require native identity verification by default.

    Archive loading uses native_identity=False to check member digests, declared
    inputs and recorded recovery without a native SDK. That mode does not verify
    serde/JCS identities or qualify fitting on an installed engine. Fitting APIs
    always use the default full check, which requires the matching Python binding.
    Archive evidence qualifies only its synthetic fixture and recorded engine.
    It never establishes qualification of the currently installed engine.
    """
    if not isinstance(declaration, dict):
        raise ValueError('Fitting declaration must be a JSON object')
    flags = tuple(declaration.get(key, False) for key in ('fit_ready', 'fitting_supported'))
    if any(type(flag) is not bool for flag in flags):
        raise ValueError('Fitting readiness flags must be boolean')
    if availability is not None and flags != tuple(availability[key] for key in ('fit_ready', 'fitting_supported')):
        raise ValueError('Fitting readiness differs from availability')
    if 'schema' not in declaration:
        if any(flags):
            raise ValueError('Ready fitting requires an explicit supported declaration')
        return deepcopy(declaration)
    _object(declaration, ('schema', 'model_id', 'model_version', 'native_model_sha256', 'fit_ready', 'fitting_supported', 'scope', 'source_population_reproduction', 'workflows'))
    if declaration['schema'] != SCHEMA or declaration['scope'] != 'synthetic_parameter_recovery_fixture' or declaration['source_population_reproduction'] is not False:
        raise ValueError('Unsupported fitting schema or scientific scope')
    native_path = index['native_execution'].get('model')
    if (declaration['model_id'], declaration['model_version']) != (index['model_id'], index['model_version']):
        raise ValueError('Fitting archive identity differs')
    model = _member({'path': native_path, 'sha256': declaration['native_model_sha256']}, index, members)
    if model['model_id'] != declaration['model_id']:
        raise ValueError('Fitting native model identity differs')
    if any(flags) and availability and availability['availability'] != 'dynamic':
        raise ValueError('Ready fitting requires dynamic availability')
    workflows = declaration['workflows']
    if not isinstance(workflows, list) or not 1 <= len(workflows) <= 8:
        raise ValueError('Fitting requires one to eight workflows')
    ids, requests, ready = set(), set(), False
    parameters = {p['name']: p for p in model['parameters']}
    outputs = {o['name']: o for o in model['outputs']}
    for workflow in workflows:
        _object(workflow, ('id', 'operation', 'parameters', 'native_request', 'synthetic_observations', 'qualification', 'limitations'))
        wid = _text(workflow['id'])
        if wid in ids:
            raise ValueError('Duplicate fitting workflow ID')
        ids.add(wid)
        limitations = workflow['limitations']
        if not isinstance(limitations, list) or not limitations:
            raise ValueError('Fitting limitations are required')
        for item in limitations:
            _text(item)
        qualification = _object(workflow['qualification'], ('status', 'independent_method', 'expected_status', 'interpretation'), ('evidence',))
        for key in ('independent_method', 'interpretation'):
            _text(qualification[key])
        if qualification['expected_status'] != 'converged' or qualification['status'] not in ('not_assessed', 'passed'):
            raise ValueError('Fitting qualification status differs')
        run, observations, fit = _pieces(workflow)
        _object(run, ('schema', 'solver', 'budgets', 'regimen'), ('request_id', 'seed', 'accuracy_control', 'parameters', 'initial_states'))
        if run['schema'] != 'qspquest.run/v0.1':
            raise ValueError('Fitting run schema differs')
        if not isinstance(observations, list) or not 1 <= len(observations) <= 4096 or observations != _member(workflow['synthetic_observations'], index, members):
            raise ValueError('Fitting observation rows differ from their complete archived data')
        for observation in observations:
            _object(observation, ('row', 'output', 'value', 'error'), ('censoring',))
            if type(observation['row']) is not int or observation['row'] < 0 or observation.get('censoring') is not None:
                raise ValueError('Fitting rows require nonnegative indices and uncensored data')
            endpoint = outputs.get(observation['output'])
            if endpoint is None:
                raise ValueError('Unknown fitting endpoint')
            error = _object(observation['error'], ('additive_sd', 'proportional_sd'), ('model',))
            if error.get('model', 'normal') != 'normal':
                raise ValueError('Synthetic fitting requires normal residual errors')
            additive, proportional = _number(error['additive_sd']['value']), _number(error['proportional_sd'])
            _quantity(observation['value'], _number(observation['value']['value']), endpoint['unit'])
            _quantity(error['additive_sd'], additive, endpoint['unit'])
            if min(additive, proportional) < 0 or max(additive, proportional) <= 0:
                raise ValueError('Fitting requires a positive residual-error component')
        roles = workflow['parameters']
        if not isinstance(roles, list) or not 1 <= len(roles) <= 32:
            raise ValueError('Fitting roles are required')
        names = []
        for role in roles:
            _object(role, ('native_name', 'unit', 'lower', 'upper', 'starter', 'synthetic_truth', 'recovery_absolute_tolerance'))
            name = role['native_name']
            parameter = parameters.get(name)
            if name in names or parameter is None or parameter.get('fixed', False) is True or role['unit'] != parameter['default']['unit']:
                raise ValueError('Fitting roles differ from native parameters')
            names.append(name)
            lower, upper, starter, truth, tolerance = (_number(role[k]) for k in ('lower', 'upper', 'starter', 'synthetic_truth', 'recovery_absolute_tolerance'))
            transform = parameter.get('transform', 'identity')
            if lower >= upper or not lower <= starter <= upper or not lower <= truth <= upper or tolerance <= 0 or transform == 'log' and lower <= 0 or transform in ('logit', 'probit') and (lower <= 0 or upper >= 1):
                raise ValueError('Fitting bounds, starter, truth or transform differ')
            _quantity(run.get('parameters', {}).get(name, parameter['default']), starter, role['unit'])
            if fit is None:
                request = workflow['native_request']
                if len(roles) != 1 or request['parameter'] != name:
                    raise ValueError('Scalar fitting requires its exact single parameter')
                bound = request
            else:
                matching = [b for b in fit['bounds'] if b.get('parameter') == name]
                if len(matching) != 1:
                    raise ValueError('Individual fitting bound differs')
                bound = _object(matching[0], ('parameter', 'lower', 'upper'))
            _quantity(bound['lower'], lower, role['unit'])
            _quantity(bound['upper'], upper, role['unit'])
        if fit is not None and (fit['objective']['simulation']['with_respect_to'] != names or len(fit['bounds']) != len(names)):
            raise ValueError('Individual fitting must use exactly the ordered declared roles')
        # Draft requests have no qualification; complete native type normalization
        # is required below before a recorded workflow can grant readiness.
        request_key = (workflow['operation'], json.dumps(workflow['native_request'], sort_keys=True, allow_nan=False))
        if request_key in requests:
            raise ValueError('Duplicate fitting workflow request')
        requests.add(request_key)
        if qualification['status'] == 'not_assessed':
            if qualification.get('evidence') is not None:
                raise ValueError('Unassessed fitting cannot carry passed evidence')
            continue
        evidence = _member(qualification.get('evidence'), index, members)
        expected = {'schema': 'qspquest.fitting-qualification/v1', 'status': 'passed', 'model_id': declaration['model_id'], 'model_version': declaration['model_version'], 'native_model_sha256': declaration['native_model_sha256'], 'synthetic_observations_sha256': workflow['synthetic_observations']['sha256'], 'workflow_id': wid, 'operation': workflow['operation'], 'source_population_reproduction': False}
        if any(type(evidence.get(k)) is not type(v) or evidence.get(k) != v for k, v in expected.items()):
            raise ValueError('Fitting evidence differs from its archived workflow identity')
        _digest(evidence.get('native_request_sha256'))
        engine = evidence.get('engine_identity', {})
        _digest(engine.get('compiler_source_sha256'), 'sha256:')
        _digest(engine.get('model_content_hash'), 'sha256:')
        _text(engine.get('target'))
        result = _member(evidence.get('native_result'), index, members)
        if native_identity:
            identity = _native_identity(model, workflow['native_request'], workflow['operation'])
            normalized_key = (workflow['operation'], json.dumps(identity['native_request'], sort_keys=True, allow_nan=False))
            if normalized_key != request_key and normalized_key in requests:
                raise ValueError('Duplicate normalized fitting workflow request')
            requests.add(normalized_key)
            if evidence['native_request_sha256'] != identity['native_request_sha256']:
                raise ValueError('Fitting evidence differs from its complete native workflow identity')
            if engine['model_content_hash'] != identity['model_content_hash']:
                raise ValueError('Fitting evidence canonical native model differs')
            result = _native_identity(model, workflow['native_request'], workflow['operation'], result)['native_result']
        if fit is None:
            if result.get('schema') != 'qspquest.scalar-fit-result/v0.1':
                raise ValueError('Recorded scalar fitting result schema differs')
        else:
            if result.get('schema') != 'qspquest.fit-result/v0.1' or result.get('population') is not None or not isinstance(result.get('fit'), dict):
                raise ValueError('Recorded individual fitting result schema differs')
            result = result['fit']
            gradient = _number(result.get('projected_gradient_norm'))
            tolerance = _number(fit['gradient_tolerance'])
            if gradient < 0 or tolerance <= 0 or gradient > tolerance:
                raise ValueError('Recorded fitting projected gradient exceeds tolerance')
        objective = result.get('objective', {})
        if result.get('status') != 'converged' or objective.get('identity') != engine or type(result.get('evaluations')) is not int or result['evaluations'] <= 0 or type(objective.get('observations')) is not int or objective['observations'] != len(observations) or result.get('fit_request_hash') != evidence.get('fit_request_hash'):
            raise ValueError('Recorded fitting status, observations or identity differs')
        _digest(result.get('fit_request_hash'), 'sha256:')
        _check_result_numbers(result, roles, len(observations), workflow['operation'], evidence['fit_request_hash'])
        for role in roles:
            estimate = result.get('parameters', {}).get(role['native_name'], {})
            if estimate.get('unit') != role['unit'] or abs(_number(estimate.get('value')) - role['synthetic_truth']) > role['recovery_absolute_tolerance']:
                raise ValueError('Recorded fitting recovery exceeds its original limit')
        ready = True
    if flags != (ready, ready):
        raise ValueError('Fitting readiness requires at least one passed hash-bound synthetic workflow')
    return deepcopy(declaration)


def select(declaration, workflow_id):
    """Select only one explicitly passed workflow; arbitrary edited data is refused."""
    if declaration.get('schema') != SCHEMA or declaration.get('fit_ready') is not True:
        raise ValueError('This archive is not fit ready; simulation support does not imply fitting support')
    workflows = [w for w in declaration['workflows'] if w['id'] == workflow_id and w['qualification']['status'] == 'passed']
    if len(workflows) != 1:
        raise ValueError('Choose an exact passed fitting workflow ID from fitting_workflows')
    return deepcopy(workflows[0])
