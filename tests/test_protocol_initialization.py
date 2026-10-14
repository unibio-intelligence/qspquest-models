"""Require sealed source clocks and denominators; never manufacture equilibrium."""
from pathlib import Path
import copy
import json
from xml.etree import ElementTree as ET
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, load_archive
from qspquest_models.protocol_initialization import validate


class ProtocolInitializationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = Library(ROOT).load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp', version='2.1.2')

    def check(self, declaration):
        return validate(declaration, self.model.index, self.model.archive_sha256, self.model.members)

    def test_actual_protocol_clocks_and_readout_coordinates_are_explicit(self):
        declaration = self.model.protocol_initialization
        source = declaration['manifest']
        self.assertEqual(len(source['scenarios']), 13)
        self.assertEqual(source['scenarios']['icm_1e12_aav9']['integration_start'], {'value': -1000, 'unit': 'h'})
        self.assertEqual(source['scenarios']['figure3b_targetx_steady_state']['integration_start'], {'value': -504, 'unit': 'h'})
        self.assertIsNone(source['scenarios']['figure3b_targetx_steady_state']['intervention_time'])
        self.assertEqual({n['canonical_output'] for n in source['normalizations']}, {'source_output_20', 'source_output_22', 'source_output_24', 'source_output_26'})
        self.assertEqual({n['basis'] for n in source['normalizations']}, {'declared_reference_input'})
        declaration['manifest']['scope'] = 'caller changes a returned copy'
        self.assertNotEqual(self.model.protocol_initialization['manifest']['scope'], declaration['manifest']['scope'])

    def test_tolerance_patch_preserves_science_and_historical_evidence(self):
        previous = load_archive(ROOT / 'models' / self.model.model_id / '2.1.1/model.omex',
                                expected_sha256='fdd64ce17b2e6c3e69e2c0c0ca50e6c166a36e39857ac5acbba6aa13e11be5c5')
        self.assertEqual(previous.archive_sha256, 'fdd64ce17b2e6c3e69e2c0c0ca50e6c166a36e39857ac5acbba6aa13e11be5c5')
        self.assertEqual(self.model.index['model_version'], '2.1.2')
        self.assertEqual(previous.members['native/model.json'], self.model.members['native/model.json'])
        self.assertEqual(previous.scenario_ids, self.model.scenario_ids)
        for name, raw in previous.members.items():
            if name.endswith('model.xml') or name.startswith(('LICENSE', 'NOTICE')):
                self.assertEqual(raw, self.model.members[name])
        for scenario in self.model.index['scenarios']:
            with self.subTest(scenario=scenario['scenario_id']):
                native_path = self.model.index['native_execution']['scenarios'][scenario['scenario_id']]
                old = json.loads(previous.members[native_path])
                current = json.loads(self.model.members[native_path])
                self.assertIsNone(current['regimen']['atol'])
                self.assertEqual(current['regimen']['rtol'], old['regimen']['rtol'] * 0.1)
                normalized = copy.deepcopy(current)
                normalized['regimen']['rtol'] = old['regimen']['rtol']
                self.assertEqual(set(current['regimen']['absolute_tolerances']), set(old['regimen']['absolute_tolerances']))
                for state, quantity in current['regimen']['absolute_tolerances'].items():
                    baseline = old['regimen']['absolute_tolerances'][state]
                    self.assertEqual(quantity['value'], baseline['value'] * 0.1)
                    self.assertEqual(quantity['unit'], baseline['unit'])
                    normalized['regimen']['absolute_tolerances'][state]['value'] = baseline['value']
                self.assertEqual(normalized, old, 'Only integration tolerances may differ')
                request = json.loads(self.model.members[scenario['request']])
                policy = self.model.index['solver_policy']
                self.assertEqual(request['solver_options']['reltol'], policy['relative_tolerance'])
                self.assertEqual(request['solver_options']['abstol'], policy['native_request_absolute_tolerance'])
                xml = ET.fromstring(self.model.members[scenario['sedml']])
                parameters = {e.attrib['kisaoID']: float(e.attrib['value']) for e in xml.iter()
                              if e.tag.endswith('algorithmParameter')}
                self.assertEqual(parameters['KISAO:0000209'], policy['relative_tolerance'])
                self.assertEqual(parameters['KISAO:0000211'], policy['native_request_absolute_tolerance'])
        folder = ROOT / 'models' / self.model.model_id / '2.1.2'
        evidence = json.loads((folder / 'evidence.json').read_text())
        self.assertEqual(evidence['cases'], [], 'Previous trajectories cannot qualify changed requests')
        self.assertFalse(evidence['numerical_qualification_accepted'])
        self.assertEqual(evidence['current_engine_qualification'], 'not_assessed')
        self.assertFalse((folder / 'results').exists())

    def test_changed_clock_source_and_normalization_are_refused(self):
        for case in ('native', 'archive', 'scenario_hash', 'start', 'initials', 'missing_scenario', 'denominator', 'basis', 'extra'):
            wrong = self.model.protocol_initialization
            manifest = wrong['manifest']
            if case == 'native': manifest['native_model_sha256'] = 'b' * 64
            if case == 'archive': manifest['archive_sha256'] = 'b' * 64
            if case == 'scenario_hash': manifest['scenarios']['icm_1e12_aav9']['native_request_sha256'] = 'b' * 64
            if case == 'start': manifest['scenarios']['icm_1e12_aav9']['integration_start']['value'] = 0
            if case == 'initials': manifest['scenarios']['icm_1e12_aav9']['explicit_initial_override_count'] -= 1
            if case == 'missing_scenario': manifest['scenarios'].pop('figure3b_targetx_steady_state')
            if case == 'denominator': manifest['normalizations'][0]['denominator_input'] = 'source_symbol_894'
            if case == 'basis': manifest['normalizations'][0]['basis'] = 'condition_specific_binding'
            if case == 'extra': manifest['unexpected'] = True
            with self.subTest(case=case), self.assertRaises(ValueError): self.check(wrong)

    def test_undeclared_policy_and_malformed_descriptor(self):
        self.assertIsNone(self.check(None))
        library = Library(ROOT)
        row = next(r for r in library.catalog['models'] if r['id'] == self.model.model_id)
        row['protocol_initialization']['sha256'] = 'b' * 64
        with self.assertRaisesRegex(ValueError, 'SHA-256'): library.load(self.model.model_id)
        row['protocol_initialization']['path'] = '../outside.json'
        with self.assertRaisesRegex(ValueError, 'Unsafe'): library.load(self.model.model_id)


if __name__ == '__main__':
    unittest.main()
