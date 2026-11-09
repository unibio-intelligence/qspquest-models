"""Discovery fields: ontology-coded species, drugs, targets, indications, routes and readouts."""
import json
from pathlib import Path
import re
import unittest

from qspquest_models import Library

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'species': r'NCBITaxon:\d+', 'indications': r'MONDO:\d{7}', 'routes': r'NCIT:C\d+',
    'modalities': r'NCIT:C\d+', 'drugs': r'NCIT:C\d+', 'targets': r'(HGNC:\d+|UniProt:[A-Z0-9]{6,10}|CHEBI:\d+)'}
ANALYTE = r'(NCIT:C\d+|HGNC:\d+|UniProt:[A-Z0-9]{6,10}|CHEBI:\d+|CL:\d{7})'


class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = Library(ROOT)
        cls.rows = {r['id']: r for r in cls.library.list_models()}
        cls.records = json.loads((ROOT / 'qspquest_models/discovery.json').read_text())['models']

    def ids(self, query):
        return {r['id'] for r in self.library.search(query)}

    def test_every_model_has_a_projected_record(self):
        self.assertEqual(set(self.records), set(self.rows))
        for model_id, row in self.rows.items():
            self.assertEqual(row['discovery'], self.records[model_id], model_id)

    def test_identifiers_follow_their_vocabulary(self):
        for model_id, record in self.records.items():
            self.assertIn(record['context'], ('clinical', 'preclinical', 'in_vitro', 'hypothetical'))
            if record['context'] != 'hypothetical':
                self.assertTrue(record['citations'], model_id)
            for citation in record['citations']:
                self.assertTrue(citation['doi'].startswith('10.') and citation['title'] and citation['year'])
            for group, pattern in PATTERNS.items():
                for item in record[group]:
                    self.assertTrue(item['label'], (model_id, group))
                    if item['id'] is not None:
                        self.assertRegex(item['id'], '^' + pattern + '$')
                    elif group in ('species', 'indications', 'routes'):
                        self.fail(f'{model_id}: {group} without an identifier')
            for name, readout in record['readouts'].items():
                if readout['analyte']['id'] is not None:
                    self.assertRegex(readout['analyte']['id'], '^' + ANALYTE + '$')
                if readout['matrix'] is not None:
                    self.assertRegex(readout['matrix']['id'], r'^UBERON:\d{7}$')

    def test_every_guide_readout_is_annotated(self):
        guides = json.loads((ROOT / 'qspquest_models/user_guides.json').read_text())
        for model_id, row in self.rows.items():
            names = {r['name'] for r in guides[model_id + '/' + row['version']]['readouts']}
            self.assertEqual(names, set(self.records[model_id]['readouts']), model_id)

    def test_li_b_cells_are_a_cell_density_in_blood(self):
        readout = self.records['qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic']['readouts']['cd19_cells_ul']
        self.assertEqual((readout['analyte']['id'], readout['matrix']['id'], readout['ucum']),
                         ('CL:0000236', 'UBERON:0000178', '/uL'))

    def test_search_uses_target_synonyms_species_and_identifiers(self):
        cd20 = self.ids('CD20')
        self.assertTrue({'qspquest_serkland_2025_rituximab_ms_pkpd', 'qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic',
                         'qspquest_pasquiers_2025_rituximab_anca_gammaglobulin_pkpd'} <= cd20)
        self.assertIn('qspquest_yagishita_2024_atezolizumab_jtail_real_world_pk', self.ids('PD-L1'))
        rats = self.ids('NCBITaxon:10116')
        self.assertLessEqual(rats, self.ids('rat'))
        self.assertTrue({'qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp',
                         'qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp'} <= rats)
        self.assertLess(len(rats), 10)
        self.assertGreater(len(self.ids('Homo sapiens')), 40)
        self.assertIn('qspquest_hyams_2022_vedolizumab_pediatric_hubble_pk_nca_er', self.ids('Crohn disease'))
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', self.ids('rituximab'))
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', self.ids('ritux'))
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', self.ids('ximab'))
        self.assertEqual(self.ids('rat'), self.ids('Rat'))

    def test_catalog_stays_within_the_engine_limit(self):
        self.assertLess((ROOT / 'catalog.json').stat().st_size, 700_000)

    def test_scenario_metadata_matches_the_presets(self):
        metadata = json.loads((ROOT / 'qspquest_models/scenarios.json').read_text())['models']
        self.assertEqual(set(metadata), set(self.rows))
        for model_id, row in self.rows.items():
            self.assertEqual((metadata[model_id]['version'], metadata[model_id]['archive_sha256']),
                             (row['version'], row['omex_sha256']))
            scenarios = {s['id']: s for s in metadata[model_id]['scenarios']}
            self.assertTrue(set(row['scenario_ids']) <= set(scenarios), model_id)
            model = self.library.load(model_id)
            native = model.index['native_execution']['scenarios']
            for sid, scenario in scenarios.items():
                self.assertIn(scenario['kind'], ('simulation', 'held', 'inspection_only'))
                self.assertEqual(scenario['kind'] == 'simulation', sid in row['scenario_ids'], (model_id, sid))
                self.assertEqual(scenario['hold_reason'] is None, scenario['kind'] == 'simulation')
                if sid not in row['scenario_ids']:
                    self.assertEqual(scenario['input_basis'], 'scientific_source')
                    continue
                self.assertEqual(scenario['input_basis'], 'native_request')
                regimen = json.loads(model.members[native[sid]])['regimen']
                time_range = scenario['time_range']
                self.assertEqual((time_range['end'], time_range['unit']),
                                 (regimen['end']['value'], regimen['end']['unit']))
                self.assertEqual((time_range['start'], time_range.get('start_unit', time_range['unit'])),
                                 (regimen['start']['value'], regimen['start']['unit']))
                administrations = regimen.get('administrations', [])
                self.assertEqual(scenario['regimen']['administrations'], len(administrations))
                doses = scenario['regimen']['doses']
                self.assertEqual(len(doses), min(50, len(administrations)))
                self.assertEqual(scenario['regimen']['truncated'], len(doses) < len(administrations))
                for reported, requested in zip(doses, administrations[:50], strict=True):
                    self.assertEqual((reported['time'], reported['time_unit'], reported['amount'],
                                      reported['unit'], reported['target'], reported['delivery'],
                                      reported.get('duration')),
                                     (requested['time']['value'], requested['time']['unit'], requested['amount']['value'],
                                      requested['amount']['unit'], requested['target'], requested['delivery']['kind'],
                                      requested['delivery'].get('duration')))


if __name__ == '__main__':
    unittest.main()
