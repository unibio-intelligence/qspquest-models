"""Contract disagreements and historical qualification must fail explicitly."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, load_archive
from qspquest_models.availability import Availability, load_records, require_publication_review, verify_catalog, project_catalog, SourceFamily, family_projections, project_source_families, verify_source_families


class AvailabilityTests(unittest.TestCase):
    def setUp(self):
        self.library = Library(ROOT)
        self.records = self.library.availability_records
        self.value = json.loads((ROOT / 'qspquest_models/availability.json').read_text())
        self.first = next(iter(self.value['records'].values()))

    def test_discovery_archive_and_generated_card_agree_for_every_version(self):
        for row in self.library.list_models():
            model = self.library.load(row['id'])
            self.assertEqual(row['availability'], model.availability)
        for key, record in self.records.items():
            path = ROOT / 'models' / record.model_id / record.archive_version / 'model.omex'
            model = load_archive(path, expected_sha256=record.archive_sha256)
            self.assertEqual(model.availability, record.describe())
            card = path.with_name('MODEL_CARD.md').read_text()
            self.assertIn('Version ' + record.archive_version, card)
            self.assertNotIn('Evidence identity:', card)
            self.assertNotIn('Publication review:', card)
            if record.availability == 'inspection_only':
                self.assertIn('Inspection only', card)
            elif record.availability == 'source_replay':
                self.assertIn('Source replay available', card)
            else:
                self.assertIn('Runnable', card)
        self.assertEqual(self.library.availability_counts['selected_model_identities'], 72)
        self.assertEqual(self.library.availability_counts['versioned_archives'], 81)
        self.assertEqual(self.library.availability_counts['selected_preset_requests'], 644)

    def test_rat_serotype_receptor_pools_are_coupled_across_all_execution_surfaces(self):
        from xml.etree import ElementTree as ET
        model = self.library.load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
        mapping = model.index['native_execution']
        native = json.loads(model.members[mapping['model']])
        readout_symbols = {o['name']: o['expression']['name'] for o in native['outputs']
                           if o['name'].startswith('library_state_')}
        for sid in ('icm_5e12_aav5', 'icm_5e12_aav9'):
            row = next(r for r in model.index['scenarios'] if r['scenario_id'] == sid)
            source = json.loads(model.members[row['request']])
            request = json.loads(model.members[mapping['scenarios'][sid]])
            tree = ET.fromstring(model.members[row['sbml']])
            checked = 0
            for node in tree.iter():
                if not node.tag.endswith('}species') or 'receptor' not in node.attrib['name'] or float(node.attrib['initialAmount']) == 0:
                    continue
                name = node.attrib['id']
                if name.startswith('aav_bc_'):
                    parameter = 'rtot_blood_copy_L'
                elif name.startswith('aav_men_'):
                    parameter = 'rtot_meningeal_copy_L'
                else:
                    candidates = [p for p in source['parameters'] if p.startswith('rtot_')
                                  and name.startswith('aav_' + p.removeprefix('rtot_').removesuffix('_copy_L') + '_')]
                    self.assertEqual(len(candidates), 1)
                    parameter = candidates[0]
                expected = source['parameters'][parameter]
                symbol = readout_symbols[mapping['states'][name]['native_name']]
                with self.subTest(scenario=sid, receptor=name):
                    self.assertEqual(float(node.attrib['initialAmount']), expected)
                    self.assertEqual(source['initial_states'][name], expected)
                    self.assertEqual(request['initial_states'][symbol]['value'], expected)
                checked += 1
            self.assertEqual(checked, 65)
        self.assertFalse(mapping['dimensional_qualification'])

    def test_rat_barrier_inputs_separate_source_native_and_all_presets(self):
        from xml.etree import ElementTree as ET
        model = self.library.load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
        native = json.loads(model.members['native/model.json'])
        effects = model.parameter_effects
        expected = {'sigma_vector_bbb': (0.9975, ['aav'], 2),
                    'sigma_vector_bcsfb': (0.9973, ['aav'], 3),
                    'sigma_protein_bbb': (0.9975, ['mab', 'target', 'complex'], 6),
                    'sigma_protein_bcsfb': (0.9973, ['mab', 'target', 'complex'], 9)}
        self.assertEqual(set(effects), set(expected))
        def references(value):
            if isinstance(value, dict):
                return ({value['name']} if value.get('kind') == 'symbol' else set()) | set().union(*(references(v) for v in value.values()))
            if isinstance(value, list):
                return set().union(*(references(v) for v in value))
            return set()
        readouts = {o['name']: o['expression'].get('name') for o in native['outputs']}
        states = {name: readouts[row['native_name']] for name, row in model.index['native_execution']['states'].items()}
        nodes = {r['name']: references(r['rhs']) for r in native['states']}
        nodes.update({r['name']: references(r['expression']) for r in native['definitions']})
        for name, (value, modalities, count) in expected.items():
            self.assertEqual(effects[name]['affected_modalities'], modalities)
            self.assertEqual(len(effects[name]['direct_states']), count)
            actual = {source for source, alias in states.items() if name in nodes[alias]}
            self.assertEqual(actual, set(effects[name]['direct_states']))
        vector = {alias for name, alias in states.items() if name.startswith('aav_')}
        closure, pending = set(vector), list(vector)
        while pending:
            for ref in nodes.get(pending.pop(), set()):
                if ref not in closure:
                    closure.add(ref); pending.append(ref)
        self.assertEqual(len(vector), 364)
        self.assertFalse(closure & {'sigma_protein_bbb', 'sigma_protein_bcsfb'})
        self.assertEqual(closure & set(states.values()), vector)
        for scenario in model.index['scenarios']:
            request = json.loads(model.members[scenario['request']])
            copy = model.research_copy(scenario['scenario_id'])
            source = ET.fromstring(model.members[scenario['sbml']])
            source_params = {p.attrib['id']: float(p.attrib['value']) for p in source.iter() if p.tag.endswith('}parameter') and 'value' in p.attrib}
            for name, (value, _, _) in expected.items():
                with self.subTest(scenario=scenario['scenario_id'], parameter=name):
                    self.assertEqual(request['parameters'][name], value)
                    self.assertEqual(source_params[name], value)
                    self.assertEqual(copy.parameters[name], {'value': value, 'unit': '1'})
            self.assertFalse({'sigma_bbb', 'sigma_bcsfb'} & set(request['parameters']))
        effects['sigma_vector_bbb']['default'] = 0.1
        self.assertEqual(model.parameter_effects['sigma_vector_bbb']['default'], 0.9975)

    def test_research_parameter_edits_are_bounded_atomic_and_preserve_vector_inputs(self):
        model = self.library.load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
        copy = model.research_copy('icm_5e12_aav9')
        original = deepcopy(copy.request)
        observed = copy.parameters
        observed['sigma_protein_bbb']['value'] = 0.3
        self.assertEqual(copy.parameters['sigma_protein_bbb']['value'], 0.9975)
        for name, value in [('sigma_bbb', 0.98), ('sigma_bcsfb', 0.98), ('source_symbol_872', 0.98),
                            ('legacy_unit_basis_0', 2), ('sigma_protein_bbb', -0.1), ('sigma_protein_bbb', 1.1),
                            ('sigma_protein_bbb', float('nan')), ('sigma_protein_bbb', True), ({}, 0.98)]:
            with self.subTest(name=name, value=value):
                with self.assertRaises(ValueError):
                    copy.set_parameter(name, value)
                self.assertEqual(copy.request, original)
        self.assertIs(copy.set_parameter('sigma_protein_bbb', 0.98).set_parameter('sigma_protein_bcsfb', 0.98), copy)
        expected = deepcopy(original)
        for name in ('sigma_protein_bbb', 'sigma_protein_bcsfb'):
            expected['parameters'][name]['value'] = 0.98
        self.assertEqual(copy.request, expected)
        self.assertEqual(model.research_copy('icm_5e12_aav9').request, original)

    def test_source_interpretation_is_bound_and_exposes_the_actual_local_binding(self):
        from xml.etree import ElementTree as ET
        ident = 'qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp'
        model = self.library.load(ident)
        row = next(row for row in self.library.list_models() if row['id'] == ident)
        record = model.source_interpretations
        self.assertEqual(record, row['source_interpretations'])
        self.assertEqual(record['archive_sha256'], model.archive_sha256)
        self.assertEqual(record['model_version'], model.index['model_version'])
        self.assertFalse(record['dimensional_qualification'])
        self.assertEqual(record['author_code_qualification'], 'not_assessed')
        source = json.loads((ROOT / row['archive']).with_name('SOURCE_REPRODUCTION.json').read_text())
        self.assertEqual(source['source_interpretations'], record)
        native = json.loads(model.members['native/model.json'])
        definitions = {r['name']: r['expression'] for r in native['definitions']}
        symbols = {r['name']: r['expression']['name'] for r in native['outputs'] if r['name'].startswith('library_state_')}
        source_rules = {n.attrib['variable']: n for n in ET.fromstring(model.members['model.xml']).iter() if n.tag.endswith('}assignmentRule')}
        def references(value):
            if isinstance(value, dict):
                return ({value['name']} if value.get('kind') == 'symbol' else set()) | set().union(*(references(v) for v in value.values()))
            if isinstance(value, list):
                return set().union(*(references(v) for v in value))
            return set()
        choice = record['entries'][0]
        self.assertEqual(choice['printed_coordinates'], ['mab_plasma', 'target_plasma', 'complex_plasma'])
        self.assertEqual(choice['adopted_coordinates'], ['mab_lymph', 'target_lymph', 'complex_lymph'])
        state_names = {s['name'] for s in native['states']}
        expected = {symbols[model.index['native_execution']['states'][n]['native_name']] for n in choice['adopted_coordinates']}
        for source_name, native_name in zip(choice['source_definitions'], choice['native_definitions']):
            self.assertEqual(references(definitions[native_name]) & state_names, expected)
            source_refs = {n.text.strip() for n in source_rules[source_name].iter() if n.tag.endswith('}ci')}
            self.assertTrue(set(choice['adopted_coordinates']) <= source_refs)
            self.assertFalse(set(choice['printed_coordinates']) & source_refs)
        unrecorded = load_archive(ROOT / row['archive'], expected_sha256=model.archive_sha256)
        self.assertIsNone(unrecorded.source_interpretations)

    def test_corrupt_source_interpretation_is_rejected_before_engine_execution(self):
        from unittest.mock import patch
        from qspquest_models import ModelArchive
        ident = 'qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp'
        original = next(row for row in self.library.catalog['models'] if row['id'] == ident)['source_interpretations']
        changes = []
        for field, value in [('model_version', 'wrong'), ('archive_sha256', '0' * 64),
                             ('native_model_sha256', '0' * 64), ('dimensional_qualification', True),
                             ('author_code_qualification', 'passed'), ('entries', [])]:
            altered = deepcopy(original); altered[field] = value; changes.append(altered)
        altered = deepcopy(original); altered['entries'][0]['native_definitions'][0] = 'missing_definition'; changes.append(altered)
        altered = deepcopy(original); altered['entries'][0]['source_definitions'][0] = 'binding_mab_plasma'; changes.append(altered)
        altered = deepcopy(original); altered['entries'][0]['adopted_coordinates'] = altered['entries'][0]['printed_coordinates']; changes.append(altered)
        altered = deepcopy(original); altered['entries'][0]['unknown'] = True; changes.append(altered)
        altered = deepcopy(original); altered['entries'][0]['source_locator'] = 'x' * 2001; changes.append(altered)
        for altered in changes:
            with self.subTest(altered=altered):
                library = Library(ROOT)
                next(row for row in library.catalog['models'] if row['id'] == ident)['source_interpretations'] = altered
                with patch.object(ModelArchive, '_cli') as execute, self.assertRaises(ValueError):
                    library.load(ident).run('figure3_mab_iv_3mgkg')
                execute.assert_not_called()

    def test_false_readiness_or_current_qualification_is_rejected(self):
        for field, value in [('fit_ready', True), ('fitting_supported', 'false'),
                             ('availability', 'inspection_only'), ('preset_ids', ['x', 'x']),
                             ('current_engine_qualification', 'passed'), ('archive_sha256', 'bad')]:
            record = deepcopy(self.first)
            record[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): Availability.parse(record)

    def test_selected_catalog_disagreements_are_rejected(self):
        for field, value in [('version', '999'), ('scenario_ids', []), ('publication_status', 'approved'),
                             ('omex_sha256', '0' * 64), ('fitting_supported', True)]:
            catalog = deepcopy(self.library.catalog)
            catalog['models'][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): verify_catalog(catalog, self.records)

    def test_unit_or_archive_qualification_does_not_transfer(self):
        row = self.library.list_models()[0]
        model = self.library.load(row['id'])
        record = self.records[row['id'] + '/' + row['version']]
        for field, value in [('dimensional_qualification', True), ('scenarios', {})]:
            index = deepcopy(model.index)
            index['native_execution'][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): record.verify_archive(index, model.archive_sha256, {})
        self.assertEqual(record.current_engine_qualification, 'not_assessed')
        self.assertIn('current_engine_qualification_not_assessed', record.blockers)
        self.assertFalse(record.fit_ready)

    def test_catalog_projection_uses_canonical_status_without_changing_descriptions(self):
        stale = deepcopy(self.library.catalog)
        stale['models'][0].update(version='999', publication_status='approved', fit_ready=True)
        projected = project_catalog(stale, self.records)
        self.assertEqual(projected, self.library.catalog)
        self.assertEqual(projected['models'][0]['name'], stale['models'][0]['name'])

    def test_pinned_source_family_agrees_in_catalog_source_record_and_guides(self):
        families = family_projections(self.library.catalog, self.records)
        self.assertEqual(len(families), 2)
        expected = self.library.catalog['source_families'][0]
        family = SourceFamily.parse(expected, self.records)
        rows = {r['id']: r for r in self.library.list_models()}
        for member in family.members:
            row = rows[member.model_id]
            self.assertEqual(row['source_family'], family.declaration)
            self.assertEqual(row['model_fidelity'], member.model_fidelity)
            self.assertEqual(row['version'], member.version)
            self.assertEqual(row['omex_sha256'], member.archive_sha256)
            self.assertEqual(row['availability']['current_engine_qualification'], 'not_assessed')
            self.assertNotEqual(row['availability']['unit_status'], 'physically_qualified')
            card = (ROOT / row['archive']).with_name('MODEL_CARD.md').read_text()
            self.assertIn('Source family: `' + family.family_id + '`', card)
            self.assertIn('does not establish physical units', card)
        source = json.loads((ROOT / 'source-catalog.json').read_text())
        verify_source_families(source, self.library.catalog)
        reduced = next(r for r in source['models'] if r.get('omex', {}).get('model_id') == family.members[1].model_id)
        self.assertEqual(reduced['source_family'], family.declaration)
        self.assertEqual(reduced['model_fidelity'], 'reduced')
        self.assertTrue(all('source_family' not in r for r in rows.values() if r['id'] not in families))

    def test_source_family_rejects_stale_pins_ambiguous_members_and_false_qualification(self):
        original = self.library.catalog['source_families'][0]
        changes = []
        for field, value in [('version', '999'), ('archive_sha256', '0' * 64), ('model_fidelity', 'qualified')]:
            item = deepcopy(original); item['members'][0][field] = value; changes.append(item)
        item = deepcopy(original); item['canonical_model'] = {'model_id': item['members'][1]['model_id'], 'version': item['members'][1]['version']}; changes.append(item)
        item = deepcopy(original); item['members'].append(deepcopy(item['members'][0])); changes.append(item)
        item = deepcopy(original); item['current_engine_qualification'] = 'passed'; changes.append(item)
        item = deepcopy(original); item['paper_id'] = ''; changes.append(item)
        item = deepcopy(original); item['family_id'] = 'a' * 129; changes.append(item)
        for item in changes:
            with self.subTest(value=item), self.assertRaises(ValueError): SourceFamily.parse(item, self.records)
        catalog = deepcopy(self.library.catalog)
        catalog['source_families'].append(deepcopy(original))
        with self.assertRaisesRegex(ValueError, 'Duplicate source-family'): family_projections(catalog, self.records)
        catalog['source_families'][1]['family_id'] = 'overlap'
        with self.assertRaisesRegex(ValueError, 'only one declared source family'): family_projections(catalog, self.records)

    def test_stale_catalog_family_fields_are_regenerated_and_verification_refuses_drift(self):
        catalog = deepcopy(self.library.catalog)
        row = next(r for r in catalog['models'] if r.get('source_family'))
        row['source_family']['canonical_model']['version'] = '999'
        row['model_fidelity'] = 'unrecorded'
        with self.assertRaisesRegex(ValueError, 'source-family fields'): verify_catalog(catalog, self.records)
        self.assertEqual(project_catalog(catalog, self.records), self.library.catalog)
        source = json.loads((ROOT / 'source-catalog.json').read_text())
        row = next(r for r in source['models'] if r.get('source_family'))
        row['model_fidelity'] = 'full'
        with self.assertRaisesRegex(ValueError, 'Source catalog family fields'): verify_source_families(source, self.library.catalog)
        self.assertEqual(project_source_families(source, self.library.catalog), json.loads((ROOT / 'source-catalog.json').read_text()))
        for descriptor in (False, [], 'invalid'):
            bad = {'models': [{'id': 'metadata', 'omex': descriptor}]}
            with self.subTest(descriptor=descriptor), self.assertRaisesRegex(ValueError, 'object or null'):
                project_source_families(bad, self.library.catalog)
        bad = deepcopy(source)
        next(r for r in bad['models'] if r.get('source_family'))['omex']['omex_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'archive digest'):
            project_source_families(bad, self.library.catalog)

    def test_family_registry_cannot_bypass_availability_and_unknown_schema_is_refused(self):
        catalog = deepcopy(self.library.catalog)
        catalog['source_family_schema'] = 'invented'
        with self.assertRaisesRegex(ValueError, 'Unsupported source-family registry'): verify_catalog(catalog, self.records)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            path.joinpath('catalog.json').write_text(json.dumps({'models': [], 'source_family_schema': 'qspquest.source-families/v1', 'source_families': []}))
            with self.assertRaisesRegex(ValueError, 'require the versioned availability'): Library(path)

    def test_pending_review_prevents_publication_without_preventing_inspection(self):
        self.assertTrue(self.library.list_models())
        with self.assertRaisesRegex(ValueError, 'Unresolved publication review'):
            require_publication_review(self.records)

    def test_unknown_schema_and_duplicate_registry_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'availability.json'
            path.write_text('{"schema":"wrong", "records":{}}')
            with self.assertRaises(ValueError): load_records(path)
            path.write_text('{"schema":"wrong", "schema":"qspquest.model-availability/v1", "records":{}}')
            with self.assertRaises(ValueError): load_records(path)


if __name__ == '__main__': unittest.main()
