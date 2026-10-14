"""Structural fitting guards; mocked receipts are not numerical qualification."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from qspquest_models import Library, load_archive
from qspquest_models.fitting import validate, select


def fixture():
    model = {'model_id': 'synthetic-contract-fixture',
             'parameters': [{'name': 'k', 'default': {'value': .5, 'unit': '1'}, 'transform': 'identity', 'fixed': False}],
             'outputs': [{'name': 'cp', 'unit': '1'}]}
    observations = [{'row': 0, 'output': 'cp', 'value': {'value': 1.0, 'unit': '1'},
                     'error': {'additive_sd': {'value': .1, 'unit': '1'}, 'proportional_sd': 0}}]
    members, index = {}, {'model_id': model['model_id'], 'model_version': 'test', 'members': {}, 'native_execution': {'model': 'native/model.json'}}
    def add(path, value):
        raw = json.dumps(value, allow_nan=False).encode()
        members[path] = raw
        digest = hashlib.sha256(raw).hexdigest()
        index['members'][path] = digest
        return {'path': path, 'sha256': digest}
    source = add('native/model.json', model)
    data = add('fitting/observations.json', observations)
    request = {'schema': 'qspquest.scalar-fit/v0.1', 'run': {'schema': 'qspquest.run/v0.1', 'solver': 'diffsol_bdf', 'budgets': {}, 'regimen': {}},
               'parameter': 'k', 'lower': {'value': .1, 'unit': '1'}, 'upper': {'value': 1, 'unit': '1'}, 'observations': observations,
               'max_iterations': 200, 'absolute_tolerance': 1e-8}
    workflow = {'id': 'synthetic', 'operation': 'fit_scalar', 'native_request': request, 'synthetic_observations': data,
                'parameters': [{'native_name': 'k', 'unit': '1', 'lower': .1, 'upper': 1, 'starter': .5, 'synthetic_truth': .7, 'recovery_absolute_tolerance': 1e-5}],
                'qualification': {'status': 'not_assessed', 'independent_method': 'structural mock only', 'expected_status': 'converged', 'interpretation': 'No numerical/scientific qualification'},
                'limitations': ['Structural mock only']}
    declaration = {'schema': 'qspquest.library-fitting/v1', 'model_id': model['model_id'], 'model_version': 'test',
                   'native_model_sha256': source['sha256'], 'fit_ready': False, 'fitting_supported': False,
                   'scope': 'synthetic_parameter_recovery_fixture', 'source_population_reproduction': False, 'workflows': [workflow]}
    return declaration, index, members, add


class FittingGuardTests(unittest.TestCase):
    def test_pinned_simulation_only_archive_cannot_execute_and_returns_copies(self):
        model = load_archive(Path(__file__).resolve().parents[1]/'models/qspquest_diffdose_2026_idr_benchmark/0.1.0/model.omex', expected_sha256='fd703aa06e91c456512164a5972645a563656397d01ce049b519d72ddb23c778')
        self.assertEqual(model.fitting_contract, {})
        self.assertEqual(model.fitting_workflows, [])
        model.fitting_contract['fit_ready'] = True
        self.assertEqual(model.fitting_contract, {})
        with self.assertRaisesRegex(ValueError, 'not fit ready'):
            model.fit_workflow('synthetic')

    def test_fit_ready_archive_inspection_and_simulation_do_not_import_fitting_sdk(self):
        root = Path(__file__).resolve().parents[1]
        with patch.dict('sys.modules', {'qspquest': None}):
            for ident in ('qspquest_serkland_2025_rituximab_ms_pkpd', 'qspquest_diffdose_2026_idr_benchmark'):
                with self.subTest(model=ident):
                    model = Library(root, executable='/test/cli').load(ident)
                    self.assertTrue(model.scenario_ids)
                    self.assertTrue(model.availability['fit_ready'])
                    self.assertEqual(model.availability['current_engine_qualification'], 'not_assessed')
                    # Reaching the simulation dispatcher proves no fitting SDK is imported.
                    with patch.object(model, '_cli', side_effect=RuntimeError('simulation dispatch')) as dispatch:
                        with self.assertRaisesRegex(RuntimeError, 'simulation dispatch'):
                            model.run(model.starter_scenario)
                        dispatch.assert_called_once()
                    for operation in (lambda: model.fitting_contract,
                                      lambda: model.fitting_workflows,
                                      lambda: model.fit_workflow('diffsol_bdf-start-1')):
                        with self.assertRaisesRegex(RuntimeError, 'Fitting requires the matching'):
                            operation()

    def test_draft_cannot_grant_readiness_or_population_scope(self):
        declaration, index, members, _ = fixture()
        validated = validate(declaration, index, members)
        validated['workflows'][0]['parameters'][0]['lower'] = -1
        self.assertEqual(declaration['workflows'][0]['parameters'][0]['lower'], .1)
        with self.assertRaisesRegex(ValueError, 'not fit ready'):
            select(declaration, 'synthetic')
        for key in ('fit_ready', 'fitting_supported', 'source_population_reproduction'):
            changed = deepcopy(declaration)
            changed[key] = True
            with self.assertRaises(ValueError):
                validate(changed, index, members)

    def test_data_source_roles_units_starters_and_unknown_fields_are_bound(self):
        declaration, index, members, _ = fixture()
        changes = [lambda d: d.update(native_model_sha256='0'*64),
                   lambda d: d.update(unrecognized=True),
                   lambda d: d['workflows'][0]['parameters'][0].update(unit='mg'),
                   lambda d: d['workflows'][0]['parameters'][0].update(starter=.6),
                   lambda d: d['workflows'][0]['native_request']['observations'][0]['value'].update(value=2),
                   lambda d: d['workflows'][0]['native_request']['observations'][0]['error'].update(model='lognormal'),
                   lambda d: d['workflows'][0]['native_request']['observations'][0].update(row=True),
                   lambda d: d['workflows'][0]['synthetic_observations'].update(path='../observations.json')]
        for change in changes:
            changed = deepcopy(declaration)
            change(changed)
            with self.assertRaises(ValueError):
                validate(changed, index, members)
        corrupt = dict(members)
        corrupt['fitting/observations.json'] += b' '
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            validate(declaration, index, corrupt)

    def test_individual_roles_priors_and_problem_kind_are_explicit(self):
        declaration, index, members, _ = fixture()
        workflow = declaration['workflows'][0]
        scalar = workflow['native_request']
        workflow['operation'] = 'fit_individual'
        workflow['native_request'] = {'schema': 'qspquest.fit/v0.1', 'problem': {'kind': 'individual', 'request': {
            'objective': {'simulation': {'schema': 'qspquest.sensitivity/v0.1', 'run': scalar['run'],
                                        'with_respect_to': ['k'], 'derivative_absolute_tolerances': {}},
                          'observations': scalar['observations'], 'priors': []},
            'bounds': [{'parameter': 'k', 'lower': scalar['lower'], 'upper': scalar['upper']}],
            'max_evaluations': 2000, 'max_iterations': 200, 'gradient_tolerance': 1e-7}}}
        validate(declaration, index, members)
        changes = [lambda d: d['workflows'][0]['native_request']['problem'].update(kind='population'),
                   lambda d: d['workflows'][0]['native_request']['problem']['request']['objective'].update(priors=[{}]),
                   lambda d: d['workflows'][0]['native_request']['problem']['request']['objective']['simulation'].update(with_respect_to=['k', 'extra']),
                   lambda d: d['workflows'][0]['native_request']['problem']['request']['bounds'].append({'parameter': 'extra'})]
        for change in changes:
            changed = deepcopy(declaration)
            change(changed)
            with self.assertRaises(ValueError):
                validate(changed, index, members)

    def test_mocked_passed_receipt_requires_exact_result_and_native_identities(self):
        declaration, index, members, add = fixture()
        declaration['fit_ready'] = declaration['fitting_supported'] = True
        workflow = declaration['workflows'][0]
        identity = {'model_content_hash': 'sha256:'+'a'*64, 'native_request_sha256': 'b'*64, 'native_request': workflow['native_request']}
        engine = {'model_content_hash': identity['model_content_hash'], 'compiler_source_sha256': 'sha256:'+'c'*64, 'target': 'structural-mock'}
        result = {'schema': 'qspquest.scalar-fit-result/v0.1', 'status': 'converged', 'parameters': {'k': {'value': .7, 'unit': '1'}},
                  'objective': {'identity': engine, 'observations': 1, 'objective': 0, 'negative_log_likelihood': 0}, 'evaluations': 1, 'iterations': 0, 'fit_request_hash': 'sha256:'+'d'*64}
        result_ref = add('fitting/result.json', result)
        evidence = {'schema': 'qspquest.fitting-qualification/v1', 'status': 'passed', 'model_id': declaration['model_id'], 'model_version': 'test',
                    'native_model_sha256': declaration['native_model_sha256'], 'native_request_sha256': identity['native_request_sha256'],
                    'synthetic_observations_sha256': workflow['synthetic_observations']['sha256'], 'workflow_id': 'synthetic', 'operation': 'fit_scalar',
                    'source_population_reproduction': False, 'engine_identity': engine, 'native_result': result_ref, 'fit_request_hash': result['fit_request_hash']}
        workflow['qualification'].update(status='passed', evidence=add('fitting/evidence.json', evidence))
        with patch('qspquest_models.fitting._native_identity', side_effect=AssertionError('unexpected SDK access')):
            archived = validate(declaration, index, members, native_identity=False)
            self.assertTrue(archived['fit_ready'])  # Historical declaration, not native verification.
            for changed_result in (
                {**result, 'status': 'max_iterations'},
                {**result, 'parameters': {'k': {'value': .9, 'unit': '1'}}},
                {**result, 'objective': {**result['objective'], 'observations': 2}},
                {**result, 'objective': {**result['objective'], 'identity': {**engine, 'target': 'different'}}},
                {**result, 'fit_request_hash': 'sha256:'+'e'*64},
            ):
                evidence['native_result'] = add('fitting/result.json', changed_result)
                workflow['qualification']['evidence'] = add('fitting/evidence.json', evidence)
                with self.assertRaises(ValueError):
                    validate(declaration, index, members, native_identity=False)
            evidence['native_result'] = add('fitting/result.json', result)
            workflow['qualification']['evidence'] = add('fitting/evidence.json', evidence)
            corrupt = dict(members)
            corrupt['fitting/result.json'] += b' '
            with self.assertRaisesRegex(ValueError, 'SHA-256'):
                validate(declaration, index, corrupt, native_identity=False)
            with self.assertRaisesRegex(AssertionError, 'unexpected SDK access'):
                validate(declaration, index, members)  # Full validation remains the default.
        with patch('qspquest_models.fitting._native_identity', return_value={**identity, 'native_result': result}):
            validate(declaration, index, members)
            self.assertEqual(select(declaration, 'synthetic')['id'], 'synthetic')
            evidence['native_request_sha256'] = 'e'*64
            workflow['qualification']['evidence'] = add('fitting/evidence.json', evidence)
            with self.assertRaisesRegex(ValueError, 'workflow identity'):
                validate(declaration, index, members)


class FitResultContractTests(unittest.TestCase):
    def test_fit_diagnostics_reject_false_success_before_recovery_scoring(self):
        from copy import deepcopy
        from qspquest_models.fitting import _check_result_numbers
        roles = [{'native_name': 'k', 'unit': '1'}]
        digest = 'sha256:' + 'a'*64
        good = {'parameters': {'k': {'value': .7, 'unit': '1'}}, 'iterations': 2, 'evaluations': 3,
                'fit_request_hash': digest, 'objective': {'observations': 2, 'objective': 0., 'negative_log_likelihood': 0.}}
        _check_result_numbers(good, roles, 2, 'fit_scalar', digest)
        for field, value in [('fit_request_hash', 'sha256:'+'b'*64), ('evaluations', 0), ('iterations', True), ('parameters', {})]:
            bad = deepcopy(good); bad[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                _check_result_numbers(bad, roles, 2, 'fit_scalar', digest)
        for field, value in [('observations', 0), ('observations', True), ('objective', float('nan')), ('negative_log_likelihood', float('inf'))]:
            bad = deepcopy(good); bad['objective'][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                _check_result_numbers(bad, roles, 2, 'fit_scalar', digest)


if __name__ == '__main__':
    unittest.main()
