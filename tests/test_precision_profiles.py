import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from qspquest_models import Library, load_archive
from qspquest_models.precision_profiles import digest, validate

ROOT = Path(__file__).resolve().parents[1]
MODEL = 'qspquest_yuan_2026_cd3x5t4_in_vitro_qsp'
SCENARIO = 'mda_mb_468_duobody_6_86nm_et8'


class PrecisionProfileTests(unittest.TestCase):
    def setUp(self):
        self.model = Library(ROOT).load(MODEL, version='2.0.1')

    def test_complete_profiles_default_and_group_assignment(self):
        manifest = self.model.precision_profiles
        self.assertEqual(len(manifest['profiles']), 8)
        self.assertEqual(len(self.model.scenario_ids), 11)
        for profile in manifest['profiles']:
            for sid in self.model.scenario_ids:
                research = self.model.research_copy(sid, precision_profile_id=profile['id'])
                receipt = research.precision_profile
                self.assertEqual(len(receipt['effective_parameters']), 33)
                self.assertEqual(receipt['parameters_status'], 'matches_profile')
                self.assertEqual(receipt['effective_parameters_sha256'], receipt['profile_parameters_sha256'])
                self.assertEqual(len(receipt['immutable_parameters']), 2)
                base = self.model.research_copy(sid)
                for key in base.request.keys() - {'parameters'}:
                    self.assertEqual(research.request[key], base.request[key])
                if sid.startswith('eplc_272h_'):
                    self.assertEqual(profile['scenarios'][sid]['killing_cell_line_group'], 3)
        manifest['profiles'].clear()
        self.assertEqual(len(self.model.precision_profiles['profiles']), 8)

    def test_modified_parameters_timed_changes_and_saved_receipt(self):
        research = self.model.research_copy(SCENARIO)
        receipt = research.precision_profile
        name = 'source_symbol_46'
        research.set_parameter(name, research.parameters[name]['value'] * 2)
        changed = research.precision_profile
        self.assertEqual(changed['parameters_status'], 'modified')
        self.assertEqual(changed['changed_parameter_names'], [name])
        self.assertEqual(changed['profile_parameters_sha256'], receipt['profile_parameters_sha256'])
        self.assertNotEqual(changed['effective_parameters_sha256'], receipt['effective_parameters_sha256'])
        research.set_precision_profile(receipt['profile_id'])
        self.assertEqual(research.precision_profile['parameters_status'], 'matches_profile')
        research.request['parameter_changes'] = [{'parameter': name}]
        self.assertEqual(research.precision_profile['parameters_status'], 'modified')
        with tempfile.TemporaryDirectory() as tmp:
            saved = research.save(Path(tmp) / 'inputs')
            self.assertEqual(json.loads((saved / 'precision-profile.json').read_text()), research.precision_profile)
            self.assertEqual(json.loads((saved / 'provenance.json').read_text())['precision_profile'], research.precision_profile)

    def test_invalid_or_changed_context_refuses_before_execution(self):
        with self.assertRaisesRegex(ValueError, 'Unknown precision profile'):
            self.model.run(SCENARIO, precision_profile_id='invented')
        research = self.model.research_copy(SCENARIO)
        self.model._precision_profiles['scope'] += ' changed'
        with patch.object(self.model, '_run_request') as run:
            with self.assertRaisesRegex(ValueError, 'manifest changed'):
                research.run()
            run.assert_not_called()
        for change in ('archive', 'version', 'partial', 'unit', 'nan', 'fixed', 'duplicate', 'default'):
            record = Library(ROOT).load(MODEL).precision_profiles
            entry = record['profiles'][0]['scenarios'][SCENARIO]
            if change == 'archive': record['archive_sha256'] = '0' * 64
            elif change == 'version': record['model_version'] = '2.0.0'
            elif change == 'partial': entry['parameters'].pop('source_symbol_46')
            elif change == 'unit': entry['parameters']['source_symbol_46']['unit'] = 'nM'
            elif change == 'nan': entry['parameters']['source_symbol_46']['value'] = float('nan')
            elif change == 'fixed': record['immutable_parameters']['legacy_unit_basis_0']['value'] = 2
            elif change == 'duplicate': record['profiles'].append(copy.deepcopy(record['profiles'][0]))
            elif change == 'default':
                entry['parameters']['source_symbol_46']['value'] *= 2
                entry['parameters_sha256'] = digest(entry['parameters'])
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate(record, self.model.index, self.model.archive_sha256, self.model.members)

    def test_table_receipt_refuses_changed_values_and_false_profile_status(self):
        from qspquest_models.precision_profiles import validate_receipt
        research = self.model.research_copy(SCENARIO)
        receipt = research.precision_profile
        model = {'id': self.model.model_id, 'version': '2.0.1', 'archive_sha256': self.model.archive_sha256}
        inputs = {'scenario_id': SCENARIO, 'effective_request': research.request}
        validate_receipt(receipt, model, inputs)
        changed = copy.deepcopy(receipt)
        changed['effective_parameters']['source_symbol_46']['value'] *= 2
        changed['effective_parameters_sha256'] = digest(changed['effective_parameters'])
        with self.assertRaisesRegex(ValueError, 'differs from effective request'):
            validate_receipt(changed, model, inputs)
        changed = copy.deepcopy(receipt)
        changed['profile_parameters_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'contradicts'):
            validate_receipt(changed, model, inputs)

    def test_catalog_digest_path_and_archive_only_behavior(self):
        library = Library(ROOT)
        row = next(r for r in library.catalog['models'] if r['id'] == MODEL)
        row['precision_profiles']['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            library.load(MODEL)
        for unsafe in ('../outside.json', '/outside.json', 'C:outside.json', r'models\outside.json', './outside.json'):
            row['precision_profiles']['path'] = unsafe
            with self.subTest(path=unsafe), self.assertRaisesRegex(ValueError, 'Unsafe'):
                library.load(MODEL)
        archive = ROOT / row['archive']
        raw = archive.read_bytes()
        direct = load_archive(archive, expected_sha256=hashlib.sha256(raw).hexdigest())
        self.assertIsNone(direct.precision_profiles)
        with self.assertRaisesRegex(ValueError, 'No precision profiles'):
            direct.run(SCENARIO, precision_profile_id='unknown')


if __name__ == '__main__':
    unittest.main()
