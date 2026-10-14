"""Prevent executable-but-uninformative starter regressions without an engine."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, ModelArchive, load_archive, result_columns


class ReadoutTests(unittest.TestCase):
    def test_source_output_identities_keep_actual_units_and_compartments(self):
        model = Library(ROOT).load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
        semantics = model.output_semantics
        declared = {name: row for name, row in semantics.items() if row['analyte'] is not None}
        self.assertEqual(len(declared), 24)
        self.assertEqual(declared['aav_brain_Vg_mL']['analyte'], 'aav_vector')
        self.assertEqual(declared['mab_isf_nM']['analyte'], 'anti_targetx_mab')
        self.assertEqual(declared['mab_isf_nM']['compartment'], 'brain_interstitial_fluid')
        self.assertEqual(declared['target_csf_pM']['compartment'], 'cisterna_magna_csf')
        self.assertEqual(declared['target_lv_pM']['compartment'], 'brain_lateral_ventricle_csf')
        self.assertTrue(all(row['returned_unit'] == '1' for row in semantics.values()))
        self.assertIsNone(semantics['state_count_anchor']['analyte'])
        semantics['mab_isf_nM']['analyte'] = 'changed'
        self.assertEqual(model.output_semantics['mab_isf_nM']['analyte'], 'anti_targetx_mab')

    def test_every_archive_has_pinned_explicit_editorial_choices(self):
        profiles = json.loads((ROOT / 'qspquest_models/user_guides.json').read_text())
        observed = set()
        dynamic = replays = candidates = 0
        for path in ROOT.glob('models/*/*/model.omex'):
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            model = load_archive(path, expected_sha256=digest)
            observed.add(model.model_id + '/' + model.index['model_version'])
            self.assertIsNotNone(model.guide)
            self.assertEqual(model.guide['archive_sha256'], digest)
            if not model.scenario_ids:
                self.assertEqual(model.guide['availability'], 'inspection_only')
                continue
            self.assertIn(model.starter_scenario, model.scenario_ids)
            evidence = json.loads(path.with_name('evidence.json').read_text())
            source_only = evidence.get('schema') == 'qspquest.models.source-preparation-evidence/v1'
            preview = None
            if source_only:
                self.assertEqual(evidence['cases'], [])
                self.assertFalse(evidence['numerical_qualification_accepted'])
                self.assertEqual(evidence['current_engine_qualification'], 'not_assessed')
                self.assertEqual(evidence['omex_sha256'], digest)
                self.assertFalse(path.with_name('starter-preview.json').exists())
                candidates += 1
            else:
                preview = json.loads(path.with_name('starter-preview.json').read_text())
                self.assertEqual(preview['archive_sha256'], digest)
                self.assertEqual(preview['scenario_id'], model.starter_scenario)
                self.assertTrue(preview['engine_identity'])
            selection = model.guide['readouts']
            self.assertGreater(len(selection), 0)
            self.assertLessEqual(len(selection), 6)
            names = []
            for readout in selection:
                self.assertTrue(readout['meaning'])
                kind, name = readout['kind'], readout['name']
                if kind in ('output', 'state'):
                    self.assertIn(name, model.index['native_execution'][kind + 's'])
                else:
                    self.assertEqual(kind, 'source_parameter')
                    self.assertIn(name, json.loads(model.members['scientific/model.json'])['parameters'])
                names.append({'output': '', 'state': 'state__', 'source_parameter': 'source__'}[kind] + name)
            if source_only:
                continue
            self.assertEqual([c['name'] for c in preview['columns']], names)
            native = model.index['native_execution']
            document = json.loads(model.members[native['model']])
            units = {o['name']: o['unit'] for o in document['outputs']}
            for spec, column in zip(selection, preview['columns']):
                if spec['kind'] in ('output', 'state'):
                    binding = native[spec['kind'] + 's'][spec['name']]
                    self.assertEqual(column['unit'], units[binding['native_name']])
            if model.guide['availability'] == 'dynamic':
                dynamic += 1
                self.assertGreater(preview['rows'], 2)
                self.assertTrue(any(c['maximum'] - c['minimum'] > 1e-8 for c in preview['columns']), model.model_id)
            else:
                replays += 1
                self.assertEqual(model.guide['availability'], 'source_replay')
        self.assertEqual(observed, set(profiles))
        self.assertEqual((dynamic, replays, candidates), (63, 5, 7))

    def test_primary_csv_includes_selected_states_and_excludes_provenance(self):
        result = {'times': [0, 1], 'sides': ['post', 'pre'],
                  'outputs': [{'name': 'citation_count', 'unit': '1', 'values': [50, 50]}],
                  'states': [{'name': 'IL6', 'unit': 'pg/mL', 'values': [5, 40]}],
                  'primary_readouts': [{'name': 'IL6', 'kind': 'state', 'meaning': 'IL-6 concentration'}]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'primary.csv'
            ModelArchive.write_csv(result, path)
            with path.open() as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(list(rows[0]), ['time', 'side', 'state__IL6'])
            self.assertEqual(float(rows[-1]['state__IL6']), 40)
            path = Path(tmp) / 'all.csv'
            ModelArchive.write_csv(result, path, all_readouts=True)
            with path.open() as f:
                self.assertEqual(next(csv.reader(f)), ['time', 'side', 'citation_count', 'state__IL6'])
        self.assertEqual(result_columns(result)[0]['meaning'], 'IL-6 concentration')

    def test_research_edits_are_isolated_reject_invalid_amounts_and_save_identity(self):
        model = Library(ROOT).load('qspquest_ubi_2026_target_gated_cargo_qsp')
        original = model.research_copy(model.starter_scenario)
        changed = model.research_copy(model.starter_scenario)
        changed.set_dose(0, 15)
        self.assertEqual(original.doses[0]['amount']['value'], 30)
        self.assertEqual(changed.doses[0]['amount']['value'], 15)
        for index, amount in [(-1, 5), (1, 5), (0, -1), (0, float('nan')), (0, float('inf'))]:
            with self.assertRaises(ValueError):
                changed.set_dose(index, amount)
        with tempfile.TemporaryDirectory() as tmp:
            folder = changed.save(Path(tmp) / 'research')
            saved = json.loads((folder / 'request.json').read_text())
            self.assertEqual(saved['regimen']['administrations'][0]['amount']['value'], 15)
            identity = json.loads((folder / 'provenance.json').read_text())
            self.assertTrue(identity['research_copy'])
            self.assertEqual(identity['archive_sha256'], model.archive_sha256)
            with self.assertRaises(FileExistsError):
                changed.save(folder)

    def test_initial_concentration_edit_uses_biological_state_name(self):
        model = Library(ROOT).load('qspquest_serkland_2025_rituximab_ms_pkpd')
        changed = model.research_copy(model.starter_scenario)
        initial = changed.initial_states['C']['value']
        changed.set_initial_state('C', initial / 2)
        self.assertEqual(changed.initial_states['C']['value'], initial / 2)
        self.assertEqual(model.research_copy(model.starter_scenario).initial_states['C']['value'], initial)
        with self.assertRaises(ValueError):
            changed.set_dose(0, 10)
        with self.assertRaises(ValueError):
            changed.set_initial_state('unknown', 10)

    def test_summary_replays_do_not_offer_unqualified_research_runs(self):
        model = Library(ROOT).load('qspquest_yarur_2025_ustekinumab_clearance_ibd_pk')
        with self.assertRaisesRegex(ValueError, 'dynamic simulation unavailable'):
            model.research_copy(model.starter_scenario)


class ComparisonContractTests(unittest.TestCase):
    def test_native_result_rejects_partial_duplicate_and_wrong_coordinate_results(self):
        from copy import deepcopy
        from qspquest_models import _validate_native_result
        model = {'model_id': 'synthetic', 'time_unit': 'h', 'outputs': [{'name': 'c', 'unit': 'mg'}]}
        request = {'regimen': {'observations': [{'time': {'value': t, 'unit': 'min'}} for t in [0, 60]]}}
        good = {'schema': 'qspquest.result/v0.1', 'model_id': 'synthetic', 'time_unit': 'h',
                'times': [0, 1], 'sides': ['post', 'post'], 'outputs': [{'name': 'c', 'unit': 'mg', 'values': [2, 1]}]}
        _validate_native_result(good, model, request)
        mutations = [lambda r: r.update(times=[100, 101]), lambda r: r.update(times=[False, 1]),
            lambda r: r.update(sides=['pre', 'post']), lambda r: r.update(time_unit='s'),
            lambda r: r.update(outputs=[]), lambda r: r['outputs'].append(deepcopy(r['outputs'][0])),
            lambda r: r['outputs'][0].update(unit='g')]
        for values in ([], [2], [2, 1, 0], [True, 1], [float('nan'), 1], [2, float('inf')]):
            mutations.append(lambda r, values=values: r['outputs'][0].update(values=values))
        for mutate in mutations:
            broken = deepcopy(good); mutate(broken)
            with self.subTest(result=broken), self.assertRaises(ValueError):
                _validate_native_result(broken, model, request)
        trajectory = {'regimen': {'start': {'value': 0, 'unit': 'h'}, 'end': {'value': 1, 'unit': 'h'}, 'samples': []}}
        event = deepcopy(good); event.update(times=[0, .5, .5, 1], sides=['post', 'pre', 'post', 'post'])
        event['outputs'][0]['values'] = [2, 1.5, 3, 2.5]
        _validate_native_result(event, model, trajectory)

    def test_starter_csv_compares_full_inventory_and_coordinates(self):
        from scripts.validate_starters import compare_csv
        result = {'times': [0, 1], 'sides': ['post', 'pre']}
        columns = [{'name': 'c', 'values': [2, 1]}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'result.csv'
            path.write_text('c,side,time\n2,post,0\n1,pre,1\n')
            compare_csv(path, result, columns)
            for text in ['time,side,c\n0,post,2\n', 'time,side,c\n100,post,2\n101,pre,1\n',
                         'time,side,c\n0,pre,2\n1,pre,1\n', 'time,side\n0,post\n1,pre\n',
                         'time,side,c,c\n0,post,2,2\n1,pre,1,1\n',
                         'time,side,c\n0,post,2,999\n1,pre,1,999\n',
                         'time,side,c\n0,post,nan\n1,pre,1\n']:
                path.write_text(text)
                with self.subTest(text=text), self.assertRaises(ValueError):
                    compare_csv(path, result, columns)

    def test_starter_preview_checks_counts_units_and_extrema_coordinates(self):
        from copy import deepcopy
        from scripts.validate_starters import compare_preview
        good = {'scenario_id': 'baseline', 'archive_sha256': 'a'*64, 'rows': 2, 'time_unit': 'h',
            'columns': [{'name': 'c', 'unit': 'mg', 'first': 2., 'last': 1., 'minimum': 1., 'maximum': 2.,
                         'minimum_time': 1., 'minimum_side': 'post', 'maximum_time': 0., 'maximum_side': 'post'}]}
        compare_preview(good, good)
        for field, value in [('rows', 0), ('time_unit', 's'), ('columns', [])]:
            bad = deepcopy(good); bad[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): compare_preview(bad, good)
        for field, value in [('unit', 'g'), ('minimum_time', 2), ('maximum_side', 'pre'), ('first', True), ('last', float('nan'))]:
            bad = deepcopy(good); bad['columns'][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): compare_preview(bad, good)


if __name__ == '__main__':
    unittest.main()
