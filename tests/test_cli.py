"""User discovery works without an engine and keeps an explicit JSON interface."""
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DiscoveryTests(unittest.TestCase):
    def cli(self, *args):
        return subprocess.run(
            [sys.executable, '-m', 'qspquest_models', '--library', str(ROOT), *args],
            cwd=ROOT, capture_output=True, text=True,
            env={**os.environ, 'QSPQUEST_EXECUTABLE': '/no-engine-needed'},
        )

    def test_search_finds_description_and_filters_runnable_models(self):
        result = self.cli('--search', 'MULTIPLE SCLEROSIS', '--runnable', '--format', 'json')
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = json.loads(result.stdout)
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', [r['id'] for r in rows])
        self.assertTrue(all(r['scenario_ids'] for r in rows))

    def test_machine_readable_listing_and_scenarios(self):
        listing = self.cli('--format', 'json')
        self.assertEqual(listing.returncode, 0, listing.stderr)
        self.assertEqual(len(json.loads(listing.stdout)), 72)
        scenarios = self.cli('--model', 'qspquest_serkland_2025_rituximab_ms_pkpd', '--format', 'json')
        self.assertEqual(scenarios.returncode, 0, scenarios.stderr)
        self.assertIn('population-typical-1000mg-full-ode', json.loads(scenarios.stdout))

    def test_inspection_only_and_empty_search_have_next_steps(self):
        held = self.cli('--model', 'qspquest_poels_2025_elranatamab_mm_qsp')
        self.assertEqual(held.returncode, 0, held.stderr)
        self.assertIn('simulation is unavailable', held.stdout)
        self.assertIn('--runnable', held.stdout)
        empty = self.cli('--search', 'no-such-model-12345')
        self.assertEqual(empty.returncode, 0, empty.stderr)
        self.assertIn('0 models found', empty.stdout)
        self.assertIn('Try a drug name', empty.stdout)

    def test_incomplete_run_is_rejected(self):
        result = self.cli('--scenario', 'anything', '--csv', 'should-not-exist.csv')
        self.assertEqual(result.returncode, 2)
        self.assertIn('--scenario requires --model', result.stderr)

    def test_displayed_summary_is_searchable_with_either_dash(self):
        for phrase in ['B-cell recovery', 'B–cell recovery']:
            result = self.cli('--search', phrase, '--format', 'json')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic',
                          [r['id'] for r in json.loads(result.stdout)])

    def test_unknown_model_suggests_complete_ids_without_traceback(self):
        result = self.cli('--model', 'rituximab')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Matching model IDs', result.stderr)
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def test_source_replay_is_distinct_and_inputs_do_not_need_engine(self):
        result = self.cli('--model', 'qspquest_yarur_2025_ustekinumab_clearance_ibd_pk')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Source replay available; dynamic simulation unavailable', result.stdout)
        inputs = self.cli('--model', 'qspquest_ubi_2026_target_gated_cargo_qsp',
                          '--scenario', 'balanced_gate_30nmol_iv', '--inputs')
        self.assertEqual(inputs.returncode, 0, inputs.stderr)
        self.assertEqual(json.loads(inputs.stdout)['doses'][0]['amount']['value'], 30.0)

    def test_exact_version_selection_preserves_machine_readable_scenarios(self):
        model_id = 'qspquest_serkland_2025_rituximab_ms_pkpd'
        row = next(r for r in json.loads((ROOT / 'catalog.json').read_text())['models'] if r['id'] == model_id)
        pinned = self.cli('--model', model_id, '--model-version', row['version'], '--format', 'json')
        self.assertEqual(pinned.returncode, 0, pinned.stderr)
        self.assertEqual(json.loads(pinned.stdout), row['scenario_ids'])
        selected = self.cli('--model', model_id, '--model-version', row['version'])
        self.assertEqual(selected.returncode, 0, selected.stderr)
        self.assertIn(row['version'], selected.stdout)
        self.assertIn(row['omex_sha256'], selected.stdout)


class ErrorContractTests(unittest.TestCase):
    def invoke(self, *args):
        import contextlib
        import io
        from qspquest_models.cli import main
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as failure:
                main(['--library', str(ROOT), '--json-errors', *args])
        self.assertEqual(stdout.getvalue(), '')
        self.assertNotIn('Traceback', stderr.getvalue())
        error = json.loads(stderr.getvalue())
        self.assertEqual(error['schema'], 'qspquest.library-error/v1')
        self.assertTrue(error['problem'] and error['cause'] and error['fix'])
        return failure.exception.code, error

    def test_argument_and_unknown_ids_keep_usage_status(self):
        for args, code in [(['--scenario', 'missing'], 'invalid_arguments'),
                           (['--unknown-option'], 'invalid_arguments'),
                           (['--model', 'rituximab'], 'unknown_model'),
                           (['--model', 'qspquest_ubi_2026_target_gated_cargo_qsp', '--scenario', 'missing'], 'unknown_scenario')]:
            with self.subTest(code=code):
                status, error = self.invoke(*args)
                self.assertEqual((status, error['code']), (2, code))
        _, error = self.invoke('--model', 'rituximab')
        self.assertIn('qspquest_serkland_2025_rituximab_ms_pkpd', error['fix'])

    def test_unavailable_version_refuses_before_execution_or_output(self):
        import tempfile
        from unittest.mock import patch
        model_id = 'qspquest_serkland_2025_rituximab_ms_pkpd'
        row = next(r for r in json.loads((ROOT / 'catalog.json').read_text())['models'] if r['id'] == model_id)
        # A distributed alternate remains distinct from a catalog selection.
        alternate = '0.1.0'
        self.assertTrue((ROOT / 'models' / model_id / alternate / 'model.omex').is_file())
        with tempfile.TemporaryDirectory() as directory, patch('qspquest_models.ModelArchive.run') as run:
            output = Path(directory) / 'trajectory.csv'
            status, error = self.invoke('--model', model_id, '--model-version', alternate,
                                       '--scenario', row['scenario_ids'][0], '--csv', str(output))
            self.assertEqual((status, error['code']), (2, 'model_version_unavailable'))
            self.assertEqual(error['details']['requested_version'], alternate)
            self.assertEqual(error['details']['available_versions'], [row['version']])
            self.assertIn(alternate, error['cause'])
            self.assertIn(row['version'], error['cause'])
            self.assertIn('load_archive', error['fix'])
            run.assert_not_called()
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_version_pin_requires_model_and_cannot_be_used_for_table_verification(self):
        for args in [('--model-version', '1'),
                     ('--model', 'example', '--model-version', ''),
                     ('--verify-table', 'table.csv', '--model', 'example', '--model-version', '1')]:
            with self.subTest(args=args):
                status, error = self.invoke(*args)
                self.assertEqual((status, error['code']), (2, 'invalid_arguments'))

    def test_missing_catalog_has_a_fix_instead_of_traceback(self):
        import tempfile
        with tempfile.TemporaryDirectory() as root:
            status, error = self.invoke('--library', root)
        self.assertEqual((status, error['code']), (1, 'library_unavailable'))
        self.assertIn('catalog.json', error['fix'])

    def test_archive_digest_failure_is_actionable(self):
        import shutil
        import tempfile
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        row = next(r for r in catalog['models'] if r['id'] == 'qspquest_ubi_2026_target_gated_cargo_qsp')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copyfile(ROOT / 'catalog.json', root / 'catalog.json')
            (root / 'qspquest_models').mkdir()
            shutil.copyfile(ROOT / 'qspquest_models/availability.json', root / 'qspquest_models/availability.json')
            archive = root / row['archive']
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b'corrupt archive')
            status, error = self.invoke('--library', str(root), '--model', row['id'])
        self.assertEqual((status, error['code']), (1, 'archive_invalid'))
        self.assertIn('SHA-256', error['cause'])

    def test_engine_timeout_crosses_the_whole_command_boundary(self):
        from unittest.mock import patch
        with patch('qspquest_models.subprocess.run', side_effect=subprocess.TimeoutExpired('qspquest', 900)):
            status, error = self.invoke('--model', 'qspquest_ubi_2026_target_gated_cargo_qsp',
                                       '--scenario', 'balanced_gate_30nmol_iv', '--executable', sys.executable)
        self.assertEqual((status, error['code']), (1, 'engine_timeout'))
        self.assertIn('900', error['cause'])

    def test_missing_executable_is_actionable(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            status, error = self.invoke('--model', 'qspquest_ubi_2026_target_gated_cargo_qsp',
                                       '--scenario', 'balanced_gate_30nmol_iv', '--executable', str(Path(directory) / 'missing-engine'))
        self.assertEqual((status, error['code']), (1, 'engine_unavailable'))

    def test_uninstalled_engine_is_actionable(self):
        from unittest.mock import patch
        with patch.dict(os.environ, {'QSPQUEST_EXECUTABLE': ''}), patch.dict(sys.modules, {'qspquest': None}), patch('qspquest_models.shutil.which', return_value=None):
            status, error = self.invoke('--model', 'qspquest_ubi_2026_target_gated_cargo_qsp',
                                       '--scenario', 'balanced_gate_30nmol_iv')
        self.assertEqual((status, error['code']), (1, 'engine_unavailable'))

    def test_export_io_errors_are_caught_for_csv_json_and_research(self):
        import tempfile
        from unittest.mock import patch
        result = {'times': [0.0], 'sides': ['right'], 'outputs': [{'name': 'value', 'values': [1.0], 'unit': '1'}]}
        with tempfile.TemporaryDirectory() as directory:
            for flag in ['--csv', '--json', '--save-research']:
                with self.subTest(flag=flag), patch('qspquest_models.ModelArchive._run_request', return_value=result):
                    status, error = self.invoke('--model', 'qspquest_ubi_2026_target_gated_cargo_qsp',
                                               '--scenario', 'balanced_gate_30nmol_iv', flag, directory)
                    self.assertEqual((status, error['code']), (1, 'output_unavailable'))

    def test_environment_library_root_is_used(self):
        import contextlib
        import io
        from unittest.mock import patch
        from qspquest_models.cli import main
        stdout = io.StringIO()
        with patch.dict(os.environ, {'QSPQUEST_LIBRARY_DIR': str(ROOT)}), contextlib.redirect_stdout(stdout):
            main(['--format', 'json'])
        self.assertEqual(len(json.loads(stdout.getvalue())), 72)


if __name__ == '__main__':
    unittest.main()
