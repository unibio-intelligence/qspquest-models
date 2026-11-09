"""Selected archives refuse source-acquisition bookkeeping."""
from pathlib import Path
import sys
import unittest

from qspquest_models import Library

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_export_content as gate  # noqa: E402


class ExportContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = Library(ROOT)

    def test_selected_library_has_no_bookkeeping(self):
        refused, runtime = gate.findings(self.library)
        self.assertEqual(refused, [])
        self.assertEqual(runtime, [])

    def test_acquisition_names_are_refused(self):
        for name in ('pmcid_available_flag', 'citation_rank', 'queue_cited_by_count', 'oup_cloudflare_blocked_flag',
                     'source_publication_year', 'supplement_docx_fetched_flag', 'article_pdf_pages',
                     'source_page_start', 'full_text_available', 'main_table_count', 'tumor_curve_pixel_count'):
            self.assertTrue(gate.NAME.search(name), name)

    def test_study_values_are_kept(self):
        for name in ('female_flag', 'source_literature_pubmed_hits', 'er_population_pk_pcr_available_n',
                     'source_supplementary_table_s3_adult_male_ge18_n', 'source_species_count',
                     'supplement_equation_count_anchor', 'corrigendum_table5_kl610023_cmax_ng_ml',
                     'table2_patient_count', 'cl_l_day', 'baseline_easi_score'):
            self.assertFalse(gate.NAME.search(name), name)

    def test_a_planted_flag_is_refused(self):
        row = self.library.list_models()[0]
        original = self.library.parameter_metadata

        def planted(model_id, **kwargs):
            record = original(model_id, **kwargs)
            if record and model_id == row['id']:
                record = {**record, 'outputs': [*record['outputs'], {
                    'native_name': 'source_output_x', 'source_name': 'pmcid_available_flag',
                    'readable_name': 'pmcid_available_flag', 'unit': '1'}]}
            return record
        self.library.parameter_metadata = planted
        try:
            refused, _ = gate.findings(self.library, model_ids=[row['id']])
        finally:
            self.library.parameter_metadata = original
        self.assertIn((row['id'], 'outputs', 'pmcid_available_flag'), refused)

    def test_archive_metadata_cannot_carry_a_replay_token(self):
        from unittest.mock import patch
        from copy import copy
        original = self.library.load
        mid = self.library.list_models()[0]['id']
        def planted(model_id, **kwargs):
            model = copy(original(model_id, **kwargs))
            if model_id == mid:
                model.members = {**model.members, 'index.json': b'{"note":"validation_run_nonce"}'}
            return model
        with patch.object(self.library, 'load', side_effect=planted):
            refused, runtime = gate.findings(self.library, model_ids=[mid])
        self.assertIn((mid, 'index.json', gate.RUNTIME), refused)
        self.assertIn(mid, runtime)

    def test_model_selection_checks_only_requested_ids_and_rejects_typos(self):
        from unittest.mock import patch
        mid = self.library.list_models()[0]['id']
        with patch.object(self.library, 'load', wraps=self.library.load) as load:
            self.assertEqual(gate.findings(self.library, model_ids=[mid]), ([], []))
            self.assertEqual({call.args[0] for call in load.call_args_list}, {mid})
            load.reset_mock()
            with self.assertRaisesRegex(ValueError, 'Select existing model ids'):
                gate.findings(self.library, model_ids=['unknown_model'])
            load.assert_not_called()

    def test_sidecars_and_compressed_tables_cannot_hide_tokens(self):
        import gzip
        import tempfile
        from types import SimpleNamespace
        row = self.library.list_models()[0]
        mid = row['id']
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = (root / row['archive']).parent
            folder.mkdir(parents=True)
            library = SimpleNamespace(root=root, list_models=lambda: [row],
                list_source_models=lambda: [], load=self.library.load,
                parameter_metadata=self.library.parameter_metadata)
            for name, raw in [('results.csv.gz', gzip.compress(b'time,validation_run_nonce\n0,1\n')),
                              ('metadata.json', b'{"note":"replay token"}')]:
                with self.subTest(asset=name):
                    asset = folder / name
                    asset.write_bytes(raw)
                    refused, runtime = gate.findings(library, model_ids=[mid])
                    self.assertIn((str(folder.relative_to(root)), name, 'replay token'), refused)
                    self.assertEqual(runtime, [mid])
                    asset.unlink()

    def test_source_snapshots_cannot_hide_tokens_or_acquisition_covariates(self):
        from unittest.mock import patch
        mid = self.library.list_models()[0]['id']
        source = {'id':'source', 'omex':{'model_id':mid}}
        documents = {'model.json': {'covariates': {'queue_rank': {'default':1}}},
                     'equations.json': {}, 'scenarios.json': {'note':'cache_buster'}}
        with patch.object(self.library, 'list_source_models', return_value=[source]), \
             patch.object(self.library, 'load_source_model', return_value=documents):
            refused, runtime = gate.findings(self.library, model_ids=[mid])
        self.assertIn((mid, 'covariates', 'queue_rank'), refused)
        self.assertIn((mid, 'source scenarios.json', 'replay token'), refused)
        self.assertEqual(runtime, [mid])


if __name__ == '__main__':
    unittest.main()
