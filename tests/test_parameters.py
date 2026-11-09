"""Parameter roles, provenance and readable names in parameters.json."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

from qspquest_models import Library
from qspquest_models import parameters as meta

ROOT = Path(__file__).resolve().parents[1]
RITUXIMAB = 'qspquest_serkland_2025_rituximab_ms_pkpd'
sys.path.insert(0, str(ROOT / 'scripts'))


def native_model(library, model_id):
    model = library.load(model_id)
    return json.loads(model.members[model.index['native_execution']['model']])


class ParameterMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = Library(ROOT)
        cls.record = cls.library.parameter_metadata(RITUXIMAB)

    def test_stored_records_match_the_generator(self):
        import build_parameter_metadata
        count, stale = build_parameter_metadata.build(check_only=True)
        self.assertEqual(count, 62)
        self.assertEqual(stale, [])

    def test_rituximab_roles_follow_the_source_fit(self):
        rows = {r['source_name']: r for r in self.record['parameters']}
        self.assertEqual(self.record['model_version'], '0.5.0')
        self.assertEqual({n for n, r in rows.items() if r['role'] == 'structural'},
                         {'V_l', 'kel_day', 'kdeg1_mm3_cell_day', 'kdeg2_l_mg_day', 'L0_cells_mm3', 'kout_day'})
        self.assertEqual(rows['omega_L0']['variability'],
                         {'distribution': 'additive', 'target': 'l0_cells_mm3', 'scale': 'sd'})
        self.assertEqual(rows['omega_cl']['variability'],
                         {'distribution': 'log_normal', 'target': 'kel_day', 'scale': 'sd'})
        self.assertEqual({rows[n]['role'] for n in ('residual_a1', 'residual_b2')}, {'residual_error'})
        self.assertEqual({rows[n]['role'] for n in ('ofv', 'aic', 'bic', 'bic_c')}, {'information_criterion'})
        self.assertEqual(rows['subject1_kel_day']['role'], 'subject_replay')
        self.assertEqual(rows['kdeg1_mm3_cell_day']['provenance']['unit_basis'], 'ode_inferred')
        self.assertEqual(rows['kel_day']['provenance'], {
            'source': '10.5281/zenodo.14712277', 'locator': 'RTX_PKPD_model3/populationParameters.txt: cl_pop',
            'status': 'estimated', 'unit_basis': 'declared'})

    def test_uncurated_records_never_claim_a_status(self):
        for row in self.library.list_models():
            record = self.library.parameter_metadata(row['id'])
            if record is None:
                continue
            for parameter in record['parameters']:
                if parameter['classification'] != 'curated':
                    self.assertEqual(parameter['provenance']['status'], 'not_curated')

    def test_readable_names_are_legal_and_unique(self):
        names = meta.name_map(self.record)
        self.assertEqual(names['symbols']['source_symbol_0'], 'c')
        self.assertTrue(all(meta.legal(n) for n in names['symbols'].values()))
        self.assertEqual(len(set(names['symbols'].values())), len(names['symbols']))
        for name in ('time', 'true', 'input_c', 'V', '1x', 'a-b', 'x' * 129):
            self.assertFalse(meta.legal(name), name)
        for name in ('time', 'V_l', '1x', 'input_c', 'a--b'):
            self.assertTrue(meta.legal(meta.readable(name)), name)

    def test_check_rejects_a_record_that_misdescribes_the_archive(self):
        model = native_model(self.library, RITUXIMAB)
        identity = {k: self.record[k] for k in ('model_id', 'model_version', 'archive_sha256')}
        meta.check(deepcopy(self.record), model, **identity)
        cases = {
            'structural role': lambda r: r['parameters'][1].update(role='source_check'),
            'illegal readable': lambda r: r['states'][0].update(readable_name='C'),
            'duplicate readable': lambda r: r['states'][1].update(readable_name='c'),
            'unit': lambda r: r['parameters'][1].update(unit='mL'),
            'missing symbol': lambda r: r['parameters'].pop(),
            'claimed status': lambda r: r['parameters'][0].update(classification='name_rule', provenance={**r['parameters'][0]['provenance'], 'status':'estimated'}),
            'archive': lambda r: r.update(archive_sha256='0' * 64),
        }
        for name, change in cases.items():
            record = deepcopy(self.record)
            change(record)
            with self.assertRaises(ValueError, msg=name):
                meta.check(record, model, **identity)

    def test_explicit_source_map_rejects_missing_and_wrong_aliases(self):
        import build_parameter_metadata as builder
        archive = self.library.load(RITUXIMAB)
        model = native_model(self.library, RITUXIMAB)
        for failure in ('missing', 'unknown', 'wrong_default'):
            index = deepcopy(archive.index)
            names = index['native_execution']['source_symbols']
            parameter = next(p for p in self.record['parameters'] if p['source_name'] in names.values())
            key = parameter['native_name']
            if failure == 'missing': names.pop(key)
            elif failure == 'unknown': names[key] = 'unknown_source_parameter'
            else:
                alternate = next(p for p in self.record['parameters'] if p['source_name'] in names.values() and p['native_name'] != key)
                other = alternate['native_name']
                names[key], names[other] = names[other], names[key]
            with self.subTest(failure=failure), self.assertRaises(ValueError):
                builder.source_names(archive.members, index, model, 'qspquest-serkland-2025-rituximab-ms-pkpd')

    @unittest.skipUnless(importlib.util.find_spec('qspquest'), 'needs the QSPQuest Python binding')
    def test_readable_rituximab_model_runs_like_the_native_model(self):
        import check_readable_names
        row = next(r for r in self.library.list_models() if r['id'] == RITUXIMAB)
        self.assertEqual(check_readable_names.check(self.library, row, self.record, 'all'), 3)


if __name__ == '__main__':
    unittest.main()
