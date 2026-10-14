#!/usr/bin/env python3
"""Verify distributed archives, source snapshots and stored preset evidence."""
from pathlib import Path
import csv
import gzip
import io
import re
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, load_archive
from qspquest_models.availability import require_publication_review


def verify(root=ROOT, *, for_publication=False, native_fitting=False):
    root = Path(root).resolve()
    library = Library(root)
    if for_publication:
        require_publication_review(library.availability_records)
    selected = {}
    for row in library.list_models():
        assert re.fullmatch(
            r"[0-9]+\.[0-9]+\.[0-9]+", row["version"]
        ), "non-release version"
        loaded = library.load(row["id"])
        assert (
            loaded.index["model_version"] == row["version"]
        ), "archive version mismatch"
        selected[row["archive"]] = row["omex_sha256"]
    for row in library.list_source_models():
        library.load_source_model(row["id"])
        library.load_source_execution(row["id"])
        selected[row["omex"]["archive"]] = row["omex"]["omex_sha256"]
    registered = {
        f"models/{record.model_id}/{record.archive_version}/model.omex": record.archive_sha256
        for record in library.availability_records.values()
    }
    assert all(registered.get(path) == digest for path, digest in selected.items()), "selected archive registry mismatch"
    source_index = json.loads((root / "source-omex-catalog.json").read_text())
    for row in source_index["models"]:
        assert registered.get(row["archive"]) == row["omex_sha256"], "source catalog mismatch"
    archives = {
        p.relative_to(root).as_posix() for p in root.glob("models/*/*/model.omex")
    }
    assert archives == set(registered), "archive inventory mismatch"
    for row in library.list_models():
        source = json.loads((root / row['archive']).with_name('SOURCE_REPRODUCTION.json').read_bytes())
        assert row.get('source_interpretations') == source.get('source_interpretations'), 'source interpretation projection mismatch'
        if row.get('source_interpretations'):
            assert library.load(row['id']).source_interpretations == row['source_interpretations']
    cases = 0
    csv_paths = set()
    archives_with_evidence = 0
    selected_cases = 0
    for relative, digest in sorted(registered.items()):
        archive = root / relative
        model = load_archive(archive, expected_sha256=digest)
        if native_fitting:
            model.fitting_contract
        evidence_raw = archive.with_name("evidence.json").read_bytes()
        record = library.availability_records[model.model_id + "/" + model.index["model_version"]]
        assert record.evidence_id == "sha256:" + hashlib.sha256(evidence_raw).hexdigest(), "availability evidence digest mismatch"
        record.verify_archive(model.index, digest, json.loads(model.members.get("fitting.json", b"{}")))
        evidence = json.loads(evidence_raw)
        assert evidence["omex_sha256"] == digest, "evidence archive mismatch"
        seen = set()
        for case in evidence["cases"]:
            assert case["scenario_id"] not in seen, "duplicate preset evidence"
            seen.add(case["scenario_id"])
            file_keys = set(case["files"])
            assert file_keys == {"qspquest_csv"}, "unexpected result inventory"
            record = case["files"][next(iter(file_keys))]
            path = Path(record["path"])
            assert (
                not path.is_absolute() and ".." not in path.parts
            ), "unsafe result path"
            path = archive.parent / path
            assert path.is_file() and not path.is_symlink(), "invalid result file"
            raw = path.read_bytes()
            assert (
                hashlib.sha256(raw).hexdigest() == record["sha256"]
            ), "result digest mismatch"
            assert (
                record.get("compression") == "gzip"
            ), "unsupported trajectory compression"
            decoded = gzip.decompress(raw)
            assert (
                hashlib.sha256(decoded).hexdigest() == record["uncompressed_sha256"]
            ), "original CSV digest mismatch"
            with io.StringIO(decoded.decode()) as stream:
                reader = csv.reader(stream)
                assert next(reader)[:2] == [
                    "time",
                    "side",
                ], "unexpected trajectory columns"
                assert next(reader, None) is not None, "empty trajectory"
            assert case.get("engine_identity"), "missing engine identity"
            csv_paths.add(path.relative_to(root).as_posix())
            cases += 1
        if evidence.get("schema") == "qspquest.models.source-preparation-evidence/v1":
            assert not seen and evidence.get("numerical_qualification_accepted") is False, "source-only evidence cannot claim numerical qualification"
            assert evidence.get("current_engine_qualification") == "not_assessed", "source-only current qualification differs"
            assert set(evidence["source_scenarios"]) == set(model.scenario_ids), "source-only scenario inventory mismatch"
        else:
            assert seen == set(model.scenario_ids), "preset evidence coverage mismatch"
        archives_with_evidence += bool(seen)
        if library.availability_records[model.model_id + "/" + model.index["model_version"]].selected:
            selected_cases += len(seen)
    stored = {
        p.relative_to(root).as_posix()
        for pattern in ("models/*/*/results/*/qspquest.csv.gz",)
        for p in root.glob(pattern)
    }
    assert stored == csv_paths, "trajectory inventory mismatch"
    assert not list(
        [p for pattern in ("models/*/*/results/*/qspquest.json",) for p in root.glob(pattern)]
    ), "duplicate JSON trajectories"
    result = {
        "availability_counts": library.availability_counts,
        "publication_ready": all(r.publication_review == "approved" for r in library.availability_records.values()),
        "archives": len(archives),
        "model_identities": len(library.list_models()),
        "selected_scientific_sources": len(library.list_source_models()),
        "archives_with_stored_preset_evidence": archives_with_evidence,
        "stored_preset_evidence_cases": cases,
        "selected_stored_preset_evidence_cases": selected_cases,
        "current_engine_qualification": "not_assessed",
        "fitting_native_identity": "verified" if native_fitting else "not_assessed",
        "csv_trajectories": len(csv_paths),
    }
    assert (
        result["archives"],
        result["model_identities"],
        library.availability_counts["selected_preset_requests"],
        cases,
    ) == (81, 72, 644, 647), "release scope changed"
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--for-publication", action="store_true", help="Require every archive publication review to be approved")
    parser.add_argument("--native-fitting", action="store_true", help="Also verify native fitting identities with the matching QSPQuest Python binding")
    args = parser.parse_args()
    try:
        print(json.dumps(verify(for_publication=args.for_publication, native_fitting=args.native_fitting), indent=2))
    except (ValueError, AssertionError, RuntimeError, ImportError) as error:
        print("Library verification rejected: " + str(error), file=sys.stderr)
        raise SystemExit(2)
