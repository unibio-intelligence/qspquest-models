"""Scientific identity tables retain native units and explicit unknown anatomy."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('model_guide_builder', ROOT / 'scripts/build_model_guides.py')
guides = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guides)


class OutputGuideTests(unittest.TestCase):
    def test_workflow_precedes_audit_metadata_without_dropping_scientific_limits(self):
        sections = ['# Model', '', '## Availability and qualification', '', 'Units unqualified.', '',
                    '## Source equation interpretations', '', 'A source equation uses local coordinates.', '',
                    '## Run an experiment', '', 'Run the pinned preset.', '',
                    '## Inputs and outputs', '', 'Read concentration.', '',
                    '## Interpretation and limits', '', 'No population or clinical qualification.', '',
                    '## Sources and technical reference', '', guides.SOURCE_FOOTER]
        ordered = '\n'.join(guides.reader_order(sections))
        self.assertLess(ordered.index('## Run an experiment'), ordered.index('Availability and qualification'))
        self.assertLess(ordered.index('## Interpretation and limits'), ordered.index('## Source equation interpretations'))
        for preserved in ('Units unqualified.', 'A source equation uses local coordinates.',
                          'No population or clinical qualification.', guides.SOURCE_FOOTER):
            self.assertIn(preserved, ordered)
        self.assertIn('<summary>Availability and qualification</summary>', ordered)

    def test_source_label_does_not_replace_returned_unit_or_hide_an_undeclared_compartment(self):
        native = {'outputs': {'IL6': {'native_name': 's7', 'unit': 'pg/mL',
                                      'analyte': 'interleukin_6', 'compartment': None},
                              'clock': {'native_name': 'clock', 'unit': 'h'}}}
        model = {'outputs': [{'name': 's7', 'unit': '1'}, {'name': 'clock', 'unit': 'h'}]}
        rows = guides.output_identity_rows(native, model)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['returned_unit'], '1')
        self.assertEqual(rows[0]['source_label'], 'pg/mL')
        self.assertIsNone(rows[0]['compartment'])
        self.assertEqual(rows[0]['analyte'], 'interleukin_6')

    def test_curated_initialization_and_scoring_side_guidance_survives_regeneration(self):
        note = '## Protocol clocks\n\nInitialize at -1000 h; score the pre-dose side.'
        self.assertEqual(guides.curated_footer('generated\n' + guides.SOURCE_FOOTER + '\n\n' + note), note)
        self.assertEqual(guides.curated_footer('generated without a footer'), '')

    def test_source_only_candidate_cannot_promote_or_reuse_execution_scope(self):
        index = {'model_id': 'example', 'model_version': '1'}
        evidence = {'schema': 'qspquest.models.source-preparation-evidence/v1', 'model_id': 'example', 'model_version': '1', 'cases': [], 'current_engine_qualification': 'not_assessed', 'numerical_qualification_accepted': False}
        self.assertTrue(guides.source_only_candidate(evidence, index))
        self.assertFalse(guides.source_only_candidate({'cases': []}, index))
        for key, value in [('model_version', '2'), ('cases', [{'result': 'old'}]), ('numerical_qualification_accepted', True)]:
            altered = dict(evidence);altered[key] = value
            with self.assertRaises(ValueError):guides.source_only_candidate(altered, index)
        footer = guides.SOURCE_FOOTER.replace('Stored result evidence', 'Archive qualification record')
        self.assertEqual(guides.curated_footer('card\n' + footer + '\n\nScoped biological interpretation'), 'Scoped biological interpretation')

    def test_alternate_version_guide_cannot_run_the_current_default_cli(self):
        alternate = '\n'.join(guides.cli_example(False, 'example', 'old', 'scenario'))
        self.assertNotIn('python -m qspquest_models', alternate)
        self.assertIn('checksum-pinned', alternate)
        current = '\n'.join(guides.cli_example(True, 'example', 'current', 'scenario'))
        self.assertIn('--model example --model-version current', current)

    def test_missing_native_output_cannot_be_documented_as_a_computed_analyte(self):
        with self.assertRaises(ValueError):
            guides.output_identity_rows({'outputs': {'IL6': {'native_name': 'missing',
                                          'unit': 'pg/mL', 'analyte': 'interleukin_6'}}}, {'outputs': []})


if __name__ == '__main__':
    unittest.main()
