import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from qspquest_models import InputBindingError, Library, ModelArchive


def fixture():
    model = {'model_id': 'synthetic_bindings', 'time_unit': 'h',
             'parameters': [
                 {'name': 'cl', 'default': {'value': 0.3, 'unit': 'L/h'},
                  'bounds': [{'value': 0, 'unit': 'L/h'}, {'value': 1, 'unit': 'L/h'}]},
                 {'name': 'v', 'default': {'value': 3, 'unit': 'L'}, 'fixed': True}],
             'states': [
                 {'name': 'central', 'unit': 'mg', 'initial': {'kind': 'quantity', 'quantity': {'value': 6, 'unit': 'mg'}}},
                 {'name': 'satellite', 'unit': 'mg', 'initial': {'kind': 'symbol', 'name': 'central'}}],
             'outputs': [
                 {'name': 'central_readout', 'unit': 'mg', 'expression': {'kind': 'symbol', 'name': 'central'}},
                 {'name': 'central', 'unit': 'mg', 'expression': {'kind': 'literal', 'value': 16}},
                 {'name': 'computed', 'unit': 'mg', 'expression': {'kind': 'literal', 'value': 16}}]}
    request = {'parameters': {}, 'initial_states': {'central': {'value': 6, 'unit': 'mg'}, 'satellite': {'value': 12, 'unit': 'mg'}},
               'regimen': {'observations': [{'time': {'value': 0, 'unit': 'h'}, 'side': 'post'}, {'time': {'value': 1, 'unit': 'h'}, 'side': 'post'}], 'administrations': [{'amount': {'value': 6, 'unit': 'mg'}}]}}
    index = {'model_id': model['model_id'], 'model_version': '1.0.0',
             'native_execution': {'model': 'native/model.json', 'scenarios': {'baseline': 'native/scenarios/baseline.json'},
                 'parameters': {'clearance': {'native_name': 'cl', 'source_unit': 'mL/h', 'request_unit': 'L/h'}},
                 'states': {'central_amount': {'native_name': 'central_readout', 'unit': 'ug'},
                            'computed_amount': {'native_name': 'computed', 'unit': 'mg'},
                            'ambiguous_readout': {'native_name': 'central', 'unit': 'mg'}}}}
    members = {'native/model.json': json.dumps(model).encode(),
               'native/scenarios/baseline.json': json.dumps(request).encode()}
    return ModelArchive(members, index, 'a' * 64, guide={'availability': 'dynamic'})


class InputBindingTests(unittest.TestCase):
    def test_native_units_defaults_and_readout_aliases_are_distinct(self):
        model = fixture()
        bindings = model.input_bindings
        scalar = bindings['parameters']['clearance']
        self.assertEqual((scalar['native_name'], scalar['unit']), ('cl', 'L/h'))
        self.assertEqual(scalar['default'], {'value': 0.3, 'unit': 'L/h'})
        self.assertEqual(scalar['declared_source_unit'], 'mL/h')
        state = model.resolve_input_alias('initial_states', 'central_amount')
        self.assertEqual((state['native_name'], state['unit'], state['declared_source_unit']), ('central', 'mg', 'ug'))
        self.assertNotIn('computed_amount', bindings['initial_states'])
        self.assertNotIn('ambiguous_readout', bindings['initial_states'])
        self.assertEqual(bindings['initial_states']['satellite']['initial_expression'], {'kind': 'symbol', 'name': 'central'})
        bindings['parameters']['cl']['default']['value'] = 123
        self.assertEqual(model.input_bindings['parameters']['cl']['default']['value'], 0.3)

    def test_alias_edits_use_native_units_preserve_coupled_inputs_and_save_context(self):
        model = fixture()
        digest = model.input_bindings['context']['input_binding_hash']
        copy = model.research_copy('baseline', expected_input_binding_hash=digest)
        copy.set_parameter('clearance', 0.4, expected_input_binding_hash=digest)
        copy.set_initial_state('central_amount', 3)
        self.assertEqual(copy.request['parameters']['cl'], {'value': 0.4, 'unit': 'L/h'})
        self.assertEqual(copy.request['initial_states']['central'], {'value': 3, 'unit': 'mg'})
        self.assertEqual(copy.request['initial_states']['satellite'], {'value': 12, 'unit': 'mg'})
        copy.set_initial_state('central', 4)
        self.assertEqual(copy.initial_states['central_amount']['value'], 4)
        self.assertEqual(model.research_copy('baseline').initial_states['central_amount']['value'], 6)
        for value in (True, float('nan'), float('inf'), 1.1):
            with self.assertRaises(ValueError):
                copy.set_parameter('clearance', value)
        with self.assertRaisesRegex(ValueError, 'fixed parameter'):
            copy.set_parameter('v', 4)
        with tempfile.TemporaryDirectory() as tmp:
            folder = copy.save(Path(tmp) / 'copy')
            self.assertEqual(json.loads((folder / 'input-bindings.json').read_text())['context']['input_binding_hash'], digest)
            self.assertEqual(json.loads((folder / 'provenance.json').read_text())['input_binding_hash'], digest)

    def test_changed_model_alias_and_scenario_refuse_edits_execution_and_save(self):
        for changed in ('default', 'alias', 'scenario'):
            model = fixture()
            copy = model.research_copy('baseline')
            old = copy.input_binding_hash
            if changed == 'default':
                native = json.loads(model.members['native/model.json'])
                native['parameters'][0]['default']['value'] = 0.6
                model.members['native/model.json'] = json.dumps(native).encode()
            elif changed == 'alias':
                model.index['native_execution']['parameters']['clearance']['native_name'] = 'v'
            else:
                native = json.loads(model.members['native/scenarios/baseline.json'])
                native['initial_states']['central']['value'] = 8
                model.members['native/scenarios/baseline.json'] = json.dumps(native).encode()
            with patch.object(model, '_run_request') as run:
                with self.assertRaises(InputBindingError) as caught:
                    copy.run()
                run.assert_not_called()
            error = caught.exception.diagnostic
            self.assertEqual(error['code'], 'input_bindings_changed')
            self.assertEqual(error['expected_input_binding_hash'], old)
            self.assertNotEqual(error['current_input_binding_hash'], old)
            self.assertEqual(error['migration'], 'inspect_current_bindings')
            with self.assertRaises(InputBindingError):
                copy.set_parameter('clearance', 0.4)
            with self.assertRaises(InputBindingError):
                copy.set_initial_state('central', 4)
            with self.assertRaises(InputBindingError):
                copy.set_dose(0, 3)
            with tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / 'refused'
                with self.assertRaises(InputBindingError):
                    copy.save(target)
                self.assertFalse(target.exists())
            with self.assertRaises(InputBindingError):
                model.research_copy('baseline', expected_input_binding_hash=old)

    def test_unknown_names_and_malformed_hashes_have_actionable_diagnostics(self):
        model = fixture()
        for value in ('invalid', 42, True, {}, 'sha256:' + 'A' * 64):
            with self.assertRaises(InputBindingError) as caught:
                model.resolve_input_alias('parameters', 'cl', expected_input_binding_hash=value)
            self.assertEqual(caught.exception.diagnostic['code'], 'input_binding_hash')
        with self.assertRaises(InputBindingError) as caught:
            model.resolve_input_alias('parameters', 'old_clearance')
        error = caught.exception.diagnostic
        self.assertEqual((error['code'], error['model_version'], error['migration']),
                         ('input_alias_unknown', '1.0.0', 'inspect_current_bindings'))
        with self.assertRaises(ValueError):
            model.resolve_input_alias('outputs', 'cl')

    def test_input_alias_metadata_cannot_shadow_a_different_native_input(self):
        model = fixture()
        model.index['native_execution']['parameters']['cl'] = {'native_name': 'v'}
        with self.assertRaisesRegex(ValueError, 'Invalid archive input alias'):
            _ = model.input_bindings
        model = fixture()
        model.index['native_execution']['input_states'] = {'central_amount': {'native_name': 'satellite', 'source_unit': 'mg', 'request_unit': 'mg'}}
        self.assertEqual(model.resolve_input_alias('initial_states', 'central_amount')['native_name'], 'satellite')

    def test_explicit_version_never_loads_a_replacement_and_archive_version_matches(self):
        library = Library.__new__(Library)
        library.root = Path('.')
        library.executable = None
        library.availability_records = {}
        library.catalog = {'models': [{'id': 'synthetic_bindings', 'version': '1.0.0',
            'archive': 'models/synthetic/model.omex', 'omex_sha256': 'a' * 64,
            'scenario_ids': ['baseline']}]}
        with patch('qspquest_models.load_archive', return_value=fixture()) as load:
            with self.assertRaises(InputBindingError) as caught:
                library.load('synthetic_bindings', version='0.9.0')
            load.assert_not_called()
            error = caught.exception.diagnostic
            self.assertEqual((error['code'], error['available_versions'], error['migration']),
                             ('model_version_unavailable', ['1.0.0'], 'inspect_current_bindings'))
            self.assertEqual(library.load('synthetic_bindings', version='1.0.0').index['model_version'], '1.0.0')
        wrong = fixture()
        wrong.index['model_version'] = '2.0.0'
        with patch('qspquest_models.load_archive', return_value=wrong):
            with self.assertRaisesRegex(ValueError, 'catalog/archive mismatch'):
                library.load('synthetic_bindings', version='1.0.0')

    def test_returned_values_keep_native_units_and_separate_source_labels(self):
        model = fixture()
        model.guide = None
        native = model.index['native_execution']
        native['coordinates'] = 'unchanged_source_numeric_values'
        native['outputs'] = {'central_display': {'native_name': 'central_readout', 'unit': 'ug'}}
        output = {'schema': 'qspquest.result/v0.1', 'model_id': model.model_id,
                  'time_unit': 'h', 'times': [0, 1], 'sides': ['post', 'post'],
                  'outputs': [{'name': name, 'unit': 'mg', 'values': [6, 5]}
                              for name in ('central_readout', 'central', 'computed')]}
        model.executable = 'synthetic-mocked-executor'
        with patch.object(model, '_cli', return_value=output):
            result = model.run('baseline')
        for column in result['outputs'] + result['states']:
            self.assertEqual(column['unit'], 'mg')
            self.assertEqual(column['values'], [6, 5])
        self.assertEqual(result['outputs'][0]['declared_source_unit'], 'ug')
        self.assertEqual(result['states'][0]['declared_source_unit'], 'ug')


if __name__ == '__main__':
    unittest.main()
