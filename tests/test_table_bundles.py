"""Verify interpretable exports, corruption refusal and paired-write failures."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import ModelArchive, read_table


def result():
    return {'model_id': 'synthetic', 'model_version': '0.1.0',
            'archive_sha256': 'a' * 64, 'scenario_id': 'dose', 'research_copy': True,
            'times': [0, 1, 1, 2], 'sides': ['post', 'pre', 'post', 'post'], 'time_unit': 'h',
            'outputs': [{'name': 'concentration,"free"', 'unit': 'mg/L', 'native_name': 'cp', 'values': [0, 1, 2, 1]}],
            'identity': {'compiler_source_sha256': 'sha256:' + 'b' * 64, 'backend': 'synthetic_fixture'},
            'effective_request': {'parameters': {'dose': {'value': 2, 'unit': 'mg'}}},
            'effective_outputs': ['cp'], 'coordinates': 'unchanged_source_numeric_values',
            'dimensional_qualification': False,
            'availability': {'current_engine_qualification': 'not_assessed'}}


class TableBundleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'trajectory.csv'
        self.sidecar = Path(str(self.path) + '.manifest.json')

    def export(self, value=None):
        return ModelArchive.write_csv(result() if value is None else value, self.path)

    def update(self, mutate, data=None):
        value = json.loads(self.sidecar.read_text())
        if data is not None:
            self.path.write_bytes(data)
            value['table']['bytes'] = len(data)
            value['table']['sha256'] = hashlib.sha256(data).hexdigest()
        mutate(value)
        self.sidecar.write_text(json.dumps(value))

    def test_roundtrip_quoted_headers_units_inputs_events_and_source_warning(self):
        manifest = self.export()
        bundle = read_table(self.path)
        self.assertEqual(bundle['manifest'], manifest)
        self.assertEqual(bundle['rows'][2]['concentration,"free"'], 2)
        self.assertEqual(manifest['table']['columns'][2]['unit'], 'mg/L')
        self.assertEqual(manifest['table']['columns'][2]['native_name'], 'cp')
        self.assertEqual(manifest['inputs']['effective_request'], result()['effective_request'])
        self.assertTrue(manifest['inputs']['modified'])
        self.assertEqual(manifest['events'], {'rule': 'nondecreasing_time;equal_time_requires_pre_then_post', 'pre': 1, 'post': 3, 'event_pairs': 1})
        self.assertEqual(manifest['qualification']['unit_status'], 'source_scale_unqualified')
        self.assertIs(manifest['qualification']['qualified'], False)

    def test_mcp_receipts_survive_friendly_csv_names_and_refuse_contradictions(self):
        manifest = self.export()
        manifest['producer'] = 'mcp'
        manifest['required_output_receipts'] = [{
            'requirement': {'output': 'friendly concentration', 'analyte': 'drug', 'compartment': 'central'},
            'canonical_output': 'cp', 'returned_column': 'cp', 'returned_unit': 'mg/L',
            'declared_analyte': 'drug', 'declared_compartment': 'central',
            'status': 'computed', 'sample_count': 4}]
        manifest['dose_event_receipts'] = [{
            'stage': 'executed_schedule', 'event_index': 0, 'canonical_target': 'central',
            'delivery': 'bolus', 'time': {'value': 1, 'unit': 'h'},
            'amount_before_model_scaling': {'value': 2, 'unit': 'mg'}, 'duration': None,
            'target_state_unit': 'mg', 'declared_base_scale': {'kind': 'literal', 'value': 1},
            'archive_source_coordinate': {'native_target': 'central', 'amount_unit': 'mg',
                'state_unit': 'mg', 'source_dose_unit': 'mg', 'source_coordinate': 'depot',
                'scaling': 'One mg adds one mg before model scaling.'},
            'notice': 'Archive labels are declarations; qualification is not assessed.'}]
        self.sidecar.write_text(json.dumps(manifest))
        self.assertEqual(read_table(self.path)['manifest'], manifest)
        self.assertNotEqual(manifest['table']['columns'][2]['name'], 'cp')
        changes = [
            lambda v: v['required_output_receipts'][0].update(returned_unit='ug/L'),
            lambda v: v['required_output_receipts'][0].update(sample_count=3),
            lambda v: v['required_output_receipts'][0].update(returned_column='unmapped'),
            lambda v: v['required_output_receipts'][0]['requirement'].update(analyte='other'),
            lambda v: v['dose_event_receipts'][0].update(stage='prepared_schedule'),
            lambda v: v['dose_event_receipts'][0]['time'].update(unit='d'),
            lambda v: v['dose_event_receipts'][0]['archive_source_coordinate'].update(native_target='other'),
            lambda v: v['dose_event_receipts'][0].update(declared_base_scale={
                'kind': 'call', 'name': 'unsupported', 'arguments': []}),
            lambda v: v.update(future_receipts=[]),
            lambda v: v.update(producer='model_library')]
        for i, change in enumerate(changes):
            with self.subTest(case=i):
                altered = deepcopy(manifest)
                change(altered)
                self.sidecar.write_text(json.dumps(altered))
                with self.assertRaises(ValueError):
                    read_table(self.path)
        self.sidecar.write_text(json.dumps(manifest))
        self.assertEqual(read_table(self.path)['manifest'], manifest)

    def test_source_interpretation_survives_export_and_rejects_identity_drift(self):
        from qspquest_models import Library
        record = Library(ROOT).load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp').source_interpretations
        value = result()
        value.update(model_id=record['model_id'], model_version=record['model_version'], archive_sha256=record['archive_sha256'])
        value['model_provenance'] = {'origin': 'synthetic_transport_fixture',
                                     'native_model_sha256': record['native_model_sha256'],
                                     'source_interpretations': record}
        manifest = self.export(value)
        self.assertEqual(read_table(self.path)['manifest']['model']['provenance']['source_interpretations'], record)
        self.assertFalse(manifest['qualification']['qualified'])
        for key, changed in [('model_version', 'wrong'), ('archive_sha256', '0' * 64),
                             ('native_model_sha256', '0' * 64), ('dimensional_qualification', True)]:
            with self.subTest(key=key):
                altered = deepcopy(manifest)
                altered['model']['provenance']['source_interpretations'][key] = changed
                self.sidecar.write_text(json.dumps(altered))
                with self.assertRaises(ValueError):
                    read_table(self.path)

    def test_legacy_manual_result_has_explicit_missing_context(self):
        value = {'times': [0], 'sides': ['post'], 'outputs': []}
        manifest = self.export(value)
        self.assertIsNone(manifest['inputs']['effective_request'])
        self.assertIsNone(manifest['inputs']['modified'])
        self.assertIsNone(manifest['engine_identity'])
        self.assertIsNone(manifest['table']['columns'][0]['unit'])
        self.assertEqual(len(read_table(self.path)['rows']), 1)

    def test_empty_trajectory_remains_a_valid_header_and_zero_counts(self):
        value = result()
        value['times'] = value['sides'] = []
        value['outputs'][0]['values'] = []
        self.export(value)
        self.assertEqual(read_table(self.path)['rows'], [])

    def test_invalid_result_refused_before_files(self):
        for kind in ['length', 'side', 'reverse', 'triple', 'decreasing', 'nan', 'duplicate', 'duplicate_readout', 'source_warning']:
            value = result()
            if kind == 'length': value['sides'].pop()
            elif kind == 'side': value['sides'][0] = 'unknown'
            elif kind == 'reverse': value['sides'][1:3] = ['post', 'pre']
            elif kind == 'triple': value['times'][3] = 1
            elif kind == 'decreasing': value['times'][3] = -1
            elif kind == 'nan': value['outputs'][0]['values'][1] = float('nan')
            elif kind == 'duplicate': value['outputs'][0]['name'] = 'time'
            elif kind == 'duplicate_readout': value['outputs'].append(deepcopy(value['outputs'][0]))
            elif kind == 'source_warning': value['dimensional_qualification'] = 1
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                self.export(value)
            self.assertFalse(self.path.exists())
            self.assertFalse(self.sidecar.exists())

    def test_data_digest_and_metadata_counts_cannot_silently_change(self):
        self.export()
        self.path.write_bytes(self.path.read_bytes() + b'3,post,0\n')
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            read_table(self.path)
        self.path.unlink(); self.sidecar.unlink(); self.export()
        self.update(lambda v: v['table'].update(rows=5))
        with self.assertRaises(ValueError): read_table(self.path)

    def test_rehashed_invalid_event_order_nonfinite_and_width_are_rejected(self):
        for data in [b'time,side,x\n1,post,2\n1,pre,1\n', b'time,side,x\n1,post,2\n0,post,1\n',
                     b'time,side,x\n1,pre,2\n1,post,1\n1,post,1\n', b'time,side,x\n1,post,nan\n',
                     b'time,side,x\n1,post,2,3\n', b'time,side,x\n1,post,"unterminated\n']:
            self.export()
            def change(v):
                v['table']['columns'][2]['name'] = 'x'
                v['table']['rows'] = data.count(b'\n') - 1
                v['events'].update(pre=0, post=v['table']['rows'], event_pairs=0)
            self.update(change, data)
            with self.assertRaises((ValueError, __import__('csv').Error)):
                read_table(self.path)
            self.path.unlink(); self.sidecar.unlink()

    def test_qualification_promotion_unknown_keys_duplicate_json_and_names_refused(self):
        changes = [lambda v: v['qualification'].update(qualified=True),
                   lambda v: v['qualification'].update(qualified=0),
                   lambda v: v['qualification'].update(unit_status='physically_qualified'),
                   lambda v: v['qualification'].update(unit_status='unqualified'),
                   lambda v: v.update(unknown=True),
                   lambda v: v['table']['columns'][2].update(name='time'),
                   lambda v: v['table'].update(filename='../other.csv'),
                   lambda v: v['table'].update(rows=True)]
        for change in changes:
            self.export(); self.update(change)
            with self.assertRaises(ValueError): read_table(self.path)
            self.path.unlink(); self.sidecar.unlink()
        self.export()
        self.sidecar.write_text(self.sidecar.read_text().replace('"schema":', '"schema":"duplicate","schema":', 1))
        with self.assertRaisesRegex(ValueError, 'Duplicate'): read_table(self.path)

    def test_collision_preserves_existing_and_cleans_new_reservation(self):
        self.sidecar.write_bytes(b'existing manifest')
        with self.assertRaises(FileExistsError): self.export()
        self.assertEqual(self.sidecar.read_bytes(), b'existing manifest')
        self.assertFalse(self.path.exists())
        self.sidecar.unlink()
        self.path.write_bytes(b'existing table')
        with self.assertRaises(FileExistsError): self.export()
        self.assertEqual(self.path.read_bytes(), b'existing table')
        self.assertFalse(self.sidecar.exists())

    def test_fsync_failure_removes_both_owned_files(self):
        for stage in [1, 2]:
            calls = 0
            def fail(fd):
                nonlocal calls
                calls += 1
                if calls == stage: raise OSError('synthetic full disk')
            with patch('qspquest_models.tables.os.fsync', side_effect=fail):
                with self.assertRaisesRegex(OSError, 'full disk'): self.export()
            self.assertFalse(self.path.exists()); self.assertFalse(self.sidecar.exists())

    def test_concurrent_writers_have_one_complete_winner(self):
        barrier = threading.Barrier(4)
        def run(index):
            value = result(); value['outputs'][0]['values'][0] = index
            barrier.wait()
            try: self.export(value); return index
            except FileExistsError: return None
        with ThreadPoolExecutor(max_workers=4) as pool:
            winners = [i for i in pool.map(run, range(4)) if i is not None]
        self.assertEqual(len(winners), 1)
        self.assertEqual(read_table(self.path)['rows'][0]['concentration,"free"'], winners[0])

    def test_missing_sidecar_and_symlink_are_refused(self):
        self.export(); self.sidecar.unlink()
        with self.assertRaises(ValueError): read_table(self.path)
        try: self.sidecar.symlink_to(self.path)
        except (OSError, NotImplementedError): self.skipTest('Symlinks unavailable')
        with self.assertRaises(ValueError): read_table(self.path)
        self.path.unlink()
        with self.assertRaises(FileExistsError): self.export()
        self.assertTrue(self.sidecar.is_symlink()); self.assertFalse(self.path.exists())

    def test_cli_verifies_without_library_or_engine_and_reports_corruption(self):
        self.export()
        command = [sys.executable, '-B', '-m', 'qspquest_models', '--verify-table', str(self.path), '--json-errors']
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, env={**os.environ, 'QSPQUEST_LIBRARY_DIR': '/missing-library-should-be-ignored'})
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)['schema'], 'qspquest.table-manifest/v1')
        complete = subprocess.run(command + ['--format', 'json'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(complete.returncode, 0, complete.stderr)
        self.assertEqual(len(json.loads(complete.stdout)['rows']), 4)
        self.path.write_bytes(b'corrupt')
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(json.loads(completed.stderr)['code'], 'table_invalid')
        self.assertNotIn('Traceback', completed.stderr)
        missing = subprocess.run([sys.executable, '-B', '-m', 'qspquest_models', '--verify-table=', '--json-errors'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(missing.returncode, 1)
        self.assertEqual(json.loads(missing.stderr)['code'], 'table_invalid')


if __name__ == '__main__': unittest.main()
