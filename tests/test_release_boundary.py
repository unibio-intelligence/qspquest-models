"""Archive integrity, rights holds and qualified-source route regressions."""

import hashlib, io, json, sys, tempfile, unittest, zipfile, importlib.util, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, load_archive


class ReleaseBoundaryTests(unittest.TestCase):
    def verifier(self):
        spec = importlib.util.spec_from_file_location("model_release_verifier", ROOT / "scripts/verify_library.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_complete_versioned_inventory_preserves_source_only_and_stored_evidence_scope(self):
        result = self.verifier().verify(ROOT)
        self.assertEqual((result["archives"], result["stored_preset_evidence_cases"],
                          result["selected_stored_preset_evidence_cases"]), (81, 647, 607))
        self.assertEqual(result["current_engine_qualification"], "not_assessed")
        self.assertFalse(result["publication_ready"])
        self.assertEqual(result["fitting_native_identity"], "not_assessed")

    def test_native_fitting_verification_cannot_fall_back_to_archive_only(self):
        from unittest.mock import patch
        with patch.dict('sys.modules', {'qspquest': None}):
            with self.assertRaisesRegex(RuntimeError, 'Fitting requires the matching'):
                self.verifier().verify(ROOT, native_fitting=True)

    def test_referenced_retained_trajectory_cannot_be_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "candidate"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            path = root / "models/qspquest_diffdose_2026_idr_benchmark/0.3.0/results/untreated/qspquest.csv.gz"
            path.unlink()
            with self.assertRaisesRegex(AssertionError, "invalid result file"):
                self.verifier().verify(root)

    def test_source_archive_index_cannot_hide_a_stale_archive_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "candidate"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            path = root / "source-omex-catalog.json"
            index = json.loads(path.read_text())
            index["models"][0]["omex_sha256"] = "0" * 64
            path.write_text(json.dumps(index))
            with self.assertRaisesRegex(AssertionError, "source catalog mismatch"):
                self.verifier().verify(root)

    def test_recomputed_outer_hash_cannot_hide_changed_native_member(self):
        library = Library(ROOT)
        row = library.list_models()[0]
        raw = (ROOT / row["archive"]).read_bytes()
        out = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(raw)) as original, zipfile.ZipFile(
            out, "w"
        ) as changed:
            for n in original.namelist():
                changed.writestr(
                    n, original.read(n) + (b" " if n == "native/model.json" else b"")
                )
        edited = out.getvalue()
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "changed.omex"
            p.write_bytes(edited)
            with self.assertRaisesRegex(ValueError, "member digest"):
                load_archive(p, expected_sha256=hashlib.sha256(edited).hexdigest())

    def test_restricted_source_metadata_cannot_load_scientific_documents(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            root.joinpath("catalog.json").write_text('{"models":[]}')
            root.joinpath("source-catalog.json").write_text(
                json.dumps(
                    {
                        "models": [
                            {
                                "id": "restricted",
                                "format": "metadata_only",
                                "rights": {"redistribution_permitted_by_audit": False},
                            }
                        ]
                    }
                )
            )
            library = Library(root)
            with self.assertRaises(PermissionError):
                library.load_source_model("restricted")
            with self.assertRaises(PermissionError):
                library.load_source_execution("restricted")

    def test_source_parser_hold_fails_before_simulator_dispatch(self):
        library = Library(ROOT, executable="/unavailable/simulator")
        model = library.load_source_execution(
            "qspquest-gupta-2025-erenumab-immune-tolerance-pkpd"
        )
        self.assertEqual(model.scenario_ids, ())
        sid = model.index["unavailable_scenario_ids"][0]
        with self.assertRaisesRegex(ValueError, "no qualified execution"):
            model.run(sid)

    def test_source_discovery_distinguishes_available_and_evidence_bound_presets(self):
        library = Library(ROOT)
        rows = library.list_source_executions()
        self.assertEqual(len(rows), 65)
        selected = {'qspquest_serkland_2025_rituximab_ms_pkpd': ('0.3.0', 3),
                    'qspquest_besbassi_2026_crs_qsp_locked_cytokine_network': ('0.1.1', 5),
                    'qspquest_shemesh_2019_atezolizumab_pediatric_poppk_safety': ('0.2.1', 16)}
        for row in rows:
            self.assertEqual(row['current_engine_qualification'], 'not_assessed')
            self.assertEqual(row['qualification_scope'], 'stored_archive_evidence_only')
            if row['model_id'] in selected:
                version, count = selected[row['model_id']]
                self.assertEqual(row['execution_version'], version)
                self.assertEqual(len(row['available_scenario_ids']), count)
                self.assertEqual(row['qualified_scenario_ids'], [])
                self.assertEqual(row['simulation_status'], 'fixed_presets_unqualified')
                self.assertEqual(row['version'], '0.1.0')
                self.assertEqual(library.load(row['model_id']).archive_sha256, row['archive_sha256'])

    def test_stale_source_qualification_refuses_before_archive_activation(self):
        from copy import deepcopy
        from unittest.mock import patch
        library = Library(ROOT)
        row = deepcopy(next(r for r in library.list_source_models() if r['id'] == 'qspquest-serkland-2025-rituximab-ms-pkpd'))
        row['qualified_scenario_ids'] = list(row['scenario_ids'])
        row['simulation_status'] = 'fixed_presets_qualified'
        with patch('qspquest_models.sources.list_sources', return_value=[row]), patch('qspquest_models.load_archive') as activate:
            with self.assertRaisesRegex(ValueError, 'preset inventory differs'):
                library.load_source_execution(row['id'])
            activate.assert_not_called()

    def test_source_qualification_evidence_cannot_drift_or_change_identity(self):
        from copy import deepcopy
        from dataclasses import replace
        from qspquest_models.sources import execution_status
        library = Library(ROOT)
        row = deepcopy(next(r for r in library.list_source_models() if r['id'] == 'qspquest-serkland-2025-rituximab-ms-pkpd'))
        descriptor = row['omex']
        record = library.availability_records[descriptor['model_id'] + '/' + descriptor['version']]
        with self.assertRaisesRegex(ValueError, 'identity differs'):
            execution_status(ROOT, row, replace(record, archive_version='other'))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = (root / descriptor['archive']).with_name('evidence.json')
            path.parent.mkdir(parents=True)
            original = (ROOT / descriptor['archive']).with_name('evidence.json').read_bytes()
            path.write_bytes(original + b' ')
            with self.assertRaisesRegex(ValueError, 'evidence digest differs'):
                execution_status(root, row, record)
            evidence = json.loads(original)
            evidence['omex_sha256'] = '0' * 64
            raw = json.dumps(evidence).encode();path.write_bytes(raw)
            with self.assertRaisesRegex(ValueError, 'another archive'):
                execution_status(root, row, replace(record, evidence_id='sha256:' + hashlib.sha256(raw).hexdigest()))
            path.unlink();path.symlink_to((ROOT / descriptor['archive']).with_name('evidence.json'))
            with self.assertRaisesRegex(ValueError, 'unsafe source execution evidence'):
                execution_status(root, row, record)

    def test_selected_source_route_uses_its_pinned_version(self):
        library = Library(ROOT)
        sid = "qspquest-serkland-2025-rituximab-ms-pkpd"
        model = library.load_source_execution(sid)
        row = next(r for r in library.list_source_models() if r["id"] == sid)
        self.assertEqual(model.archive_sha256, row["omex"]["omex_sha256"])
        self.assertTrue(model.scenario_ids)


if __name__ == "__main__":
    unittest.main()
