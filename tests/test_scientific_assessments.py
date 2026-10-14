"""Model-bound scientific axes and defensive SDK declaration guards."""
from pathlib import Path
import unittest
from qspquest_models import Library

ROOT=Path(__file__).resolve().parents[1]
MID='qspquest_rajwade_2026_aav8_trastuzumab_nonlinear_pbpk'
class ScientificAssessmentTests(unittest.TestCase):
    def model(self):return Library(ROOT).load(MID,version='0.1.0')
    def test_conservation_discrepancy_does_not_grant_other_scientific_statuses(self):
        model=self.model();declaration=model.scientific_assessments
        self.assertEqual(declaration['manifest']['archive_sha256'],model.archive_sha256)
        axes={a['axis']:a for a in declaration['manifest']['assessments']}
        self.assertEqual(set(axes),{'numerical_parity','source_fidelity','conservation','author_code_parity','clinical_validation','physical_dimensions'})
        self.assertEqual(axes['conservation']['outcome'],'discrepancy_observed')
        self.assertEqual(axes['conservation']['findings'][0]['value'],-5.238e-6)
        self.assertTrue(all(a['outcome']=='not_assessed' for k,a in axes.items() if k!='conservation'))
    def test_returned_declaration_is_a_defensive_copy(self):
        model=self.model();model.scientific_assessments['manifest']['assessments'][2]['findings'].clear()
        self.assertEqual(len(model.scientific_assessments['manifest']['assessments'][2]['findings']),1)
    def test_stale_native_hash_is_refused(self):
        model=self.model();model._scientific_assessments['manifest']['native_model_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'native model SHA-256'):model.scientific_assessments
    def test_general_validated_label_and_unknown_native_symbols_are_refused(self):
        model=self.model();model._scientific_assessments['manifest']['assessments'][0]['outcome']='validated'
        with self.assertRaises(ValueError):model.scientific_assessments
        model=self.model();model._scientific_assessments['manifest']['assessments'][2]['findings'][0]['description']='control'+chr(0x85)
        with self.assertRaisesRegex(ValueError,'assessment text'):model.scientific_assessments
        model=self.model();model._scientific_assessments['manifest']['assessments'][2]['findings'][0]['native_symbols']=['invented']
        with self.assertRaisesRegex(ValueError,'unknown native symbols'):model.scientific_assessments
if __name__=='__main__':unittest.main()
