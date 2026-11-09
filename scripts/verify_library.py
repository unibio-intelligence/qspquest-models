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
from qspquest_models.fitting import FittingEngineMismatch
from qspquest_models.availability import require_publication_review
from qspquest_models import parameters as parameter_metadata
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_export_content  # noqa: E402


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(root=ROOT, *, for_publication=False, native_fitting=False):
    root = Path(root).resolve()
    library = Library(root)
    if for_publication:
        require_publication_review(library.availability_records)
    selected = {}
    for row in library.list_models():
        require((re.fullmatch(
            r"[0-9]+\.[0-9]+\.[0-9]+", row["version"]
        )), "non-release version")
        loaded = library.load(row["id"])
        require((loaded.index["model_version"] == row["version"]), "archive version mismatch")
        selected[row["archive"]] = row["omex_sha256"]
    for row in library.list_source_models():
        source = library.load_source_model(row["id"])
        model = library.load_source_execution(row["id"])
        relative = row["omex"]["archive"]
        revision = model.index.get("source_revision")
        if revision is not None:
            provenance_name = "SOURCE_REPRODUCTION.json"
            embedded = json.loads(model.members[provenance_name])
            adjacent = json.loads((root / relative).with_name(provenance_name).read_bytes())
            require(revision["source_version"] == row["version"] == source["model.json"]["version"]
                    == adjacent["source_version"], "selected source version differs: " + row["id"])
            require(adjacent["source_model_id"] == embedded["source_model_id"] == row["id"],
                    "source provenance identity differs: " + row["id"])
            # Archives may preserve the base provenance in their embedded record.
            base = embedded.get("base_source_version", embedded["source_version"])
            require(adjacent.get("base_source_version") == base
                    and embedded["source_version"] in (base, row["version"]),
                    "base source version differs: " + row["id"])
            require(all(json.loads(model.members["scientific/" + name]) == value
                        for name, value in source.items()), "archived source snapshot differs: " + row["id"])
            for name, raw in model.members.items():
                if name.startswith('scenarios/') and name.endswith('/request.json'):
                    request = json.loads(raw)
                    require(request.get('model_version', row['version']) == row['version'],
                            'source request version differs: ' + row['id'])
        selected[relative] = row["omex"]["omex_sha256"]
    registered = {
        f"models/{record.model_id}/{record.archive_version}/model.omex": record.archive_sha256
        for record in library.availability_records.values()
    }
    require((all(registered.get(path) == digest for path, digest in selected.items())), "selected archive registry mismatch")
    source_index = json.loads((root / "source-omex-catalog.json").read_text())
    for row in source_index["models"]:
        require((registered.get(row["archive"]) == row["omex_sha256"]), "source catalog mismatch")
    archives = {
        p.relative_to(root).as_posix() for p in root.glob("models/*/*/model.omex")
    }
    require((archives == set(registered)), "archive inventory mismatch")
    for row in library.list_models():
        source = json.loads((root / row['archive']).with_name('SOURCE_REPRODUCTION.json').read_bytes())
        require((row.get('source_interpretations') == source.get('source_interpretations')), 'source interpretation projection mismatch')
        if row.get('source_interpretations'):
            require((library.load(row['id']).source_interpretations == row['source_interpretations']), 'library integrity check failed')
    cases = 0
    csv_paths = set()
    coordinate_only_tables = 0
    archives_with_evidence = 0
    selected_cases = 0
    historical_fitting_holds = []
    for relative, digest in sorted(registered.items()):
        archive = root / relative
        model = load_archive(archive, expected_sha256=digest)
        if native_fitting:
            # Selected versions must match the engine. A superseded archive is
            # immutable; its mismatch is reported, and fitting it stays refused.
            try:
                model.fitting_contract
            except FittingEngineMismatch:
                if library.availability_records[model.model_id + "/" + model.index["model_version"]].selected:
                    raise
                historical_fitting_holds.append(model.model_id + "/" + model.index["model_version"])
        evidence_raw = archive.with_name("evidence.json").read_bytes()
        record = library.availability_records[model.model_id + "/" + model.index["model_version"]]
        require((record.evidence_id == "sha256:" + hashlib.sha256(evidence_raw).hexdigest()), "availability evidence digest mismatch")
        record.verify_archive(model.index, digest, json.loads(model.members.get("fitting.json", b"{}")))
        evidence = json.loads(evidence_raw)
        require((evidence["omex_sha256"] == digest), "evidence archive mismatch")
        comparison = evidence.get("preset_checks", {}).get("against_stored_trajectories", {})
        for check in comparison.get("scenarios", {}).values():
            if check["compared_values"] == 0:
                require(check.get("status") == "no_comparable_readouts"
                        and check.get("max_relative_difference") is None
                        and check.get("outside_starter_tolerance") is None,
                        "stored comparison without readouts cannot report numerical agreement")
        seen = set()
        for case in evidence["cases"]:
            require((case["scenario_id"] not in seen), "duplicate preset evidence")
            seen.add(case["scenario_id"])
            file_keys = set(case["files"])
            require((file_keys == {"qspquest_csv"}), "unexpected result inventory")
            record = case["files"][next(iter(file_keys))]
            path = Path(record["path"])
            require((not path.is_absolute() and ".." not in path.parts), "unsafe result path")
            path = archive.parent / path
            require((path.is_file() and not path.is_symlink()), "invalid result file")
            raw = path.read_bytes()
            require((hashlib.sha256(raw).hexdigest() == record["sha256"]), "result digest mismatch")
            require((record.get("compression") == "gzip"), "unsupported trajectory compression")
            decoded = gzip.decompress(raw)
            require((hashlib.sha256(decoded).hexdigest() == record["uncompressed_sha256"]), "original CSV digest mismatch")
            with io.StringIO(decoded.decode()) as stream:
                reader = csv.reader(stream)
                columns = next(reader, [])
                require(columns[:2] == ["time", "side"], "unexpected stored table columns")
                require(next(reader, None) is not None, "empty stored table")
                coordinate_only_tables += len(columns) == 2
            require((case.get("engine_identity")), "missing engine identity")
            csv_paths.add(path.relative_to(root).as_posix())
            cases += 1
        if evidence.get("schema") == "qspquest.models.source-preparation-evidence/v1":
            require((not seen and evidence.get("numerical_qualification_accepted") is False), "source-only evidence cannot claim numerical qualification")
            require((evidence.get("current_engine_qualification") == "not_assessed"), "source-only current qualification differs")
            require((set(evidence["source_scenarios"]) == set(model.scenario_ids)), "source-only scenario inventory mismatch")
        else:
            require((seen == set(model.scenario_ids)), "preset evidence coverage mismatch")
        archives_with_evidence += bool(seen)
        if library.availability_records[model.model_id + "/" + model.index["model_version"]].selected:
            selected_cases += len(seen)
    described = set()
    for row in library.list_models():
        model = library.load(row["id"])
        if model.index["native_execution"].get("model"):
            # Every selected executable archive describes each native symbol.
            require((library.parameter_metadata(row["id"]) is not None), "missing parameter metadata")
            described.add((root / row["archive"]).with_name(parameter_metadata.FILENAME).relative_to(root).as_posix())
    require(({p.relative_to(root).as_posix() for p in root.glob("models/*/*/" + parameter_metadata.FILENAME)}
             == described), "parameter metadata inventory mismatch")
    # Selected archives carry model content only, not source-acquisition records.
    refused, runtime_tokens = check_export_content.findings(library)
    require((not refused), "source-acquisition bookkeeping in selected archives: "
            + "; ".join(f"{m}: {w}: {n}" for m, w, n in refused[:10]))
    stored = {
        p.relative_to(root).as_posix()
        for pattern in ("models/*/*/results/*/qspquest.csv.gz",)
        for p in root.glob(pattern)
    }
    require((stored == csv_paths), "trajectory inventory mismatch")
    require((not list(
        [p for pattern in ("models/*/*/results/*/qspquest.json",) for p in root.glob(pattern)]
    )), "duplicate JSON trajectories")
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
        "historical_fitting_holds": historical_fitting_holds,
        "csv_trajectories": len(csv_paths) - coordinate_only_tables,
        "csv_coordinate_only_tables": coordinate_only_tables,
        "parameter_metadata_records": len(described),
        "archives_with_replay_token": len(runtime_tokens),
    }
    require(((
        result["archives"],
        result["model_identities"],
        library.availability_counts["selected_preset_requests"],
        cases,
    ) == (62, 62, 631, 501)), "release scope changed: " + repr((result["archives"], result["model_identities"], library.availability_counts["selected_preset_requests"], cases)))
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
