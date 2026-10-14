"""Inspect scientific source models and their individual license holds."""

from pathlib import Path
import hashlib
from . import _json


def list_sources(root):
    return list(_json((Path(root) / "source-catalog.json").read_bytes())["models"])



def execution_status(root, row, availability):
    """Bind stored preset claims to the exact selected archive's evidence record.

    This validates declaration consistency, without qualifying trajectories,
    source fidelity, physical units or the installed engine.
    """
    root = Path(root)
    descriptor = row.get('omex')
    if not isinstance(descriptor, dict) or set(descriptor) != {
            'archive', 'model_id', 'omex_sha256', 'source_model_id', 'version'}:
        raise ValueError('Source execution requires an exact archive descriptor')
    if (availability is None or descriptor['source_model_id'] != row['id']
            or descriptor['model_id'] != availability.model_id
            or descriptor['version'] != availability.archive_version
            or descriptor['omex_sha256'] != availability.archive_sha256):
        raise ValueError('Source execution identity differs from the availability registry')
    name = descriptor['archive']
    if (not isinstance(name, str) or not name or '\\' in name or ':' in name
            or any(part in ('', '.', '..') for part in name.split('/'))):
        raise ValueError('Unsafe source execution archive path')
    relative = Path(name)
    if relative.is_absolute():
        raise ValueError('Unsafe source execution archive path')
    path = (root / relative).with_name('evidence.json')
    if (any(p.is_symlink() for p in (path, *path.parents))
            or not path.is_file() or path.stat().st_size > 4_000_000):
        raise ValueError('Missing or unsafe source execution evidence')
    def read_evidence():
        with path.open('rb') as stream:
            data = stream.read(4_000_001)
        if not data or len(data) > 4_000_000:
            raise ValueError('Source execution evidence must be nonempty and at most 4 MB')
        return data
    raw = read_evidence()
    if 'sha256:' + hashlib.sha256(raw).hexdigest() != availability.evidence_id:
        raise ValueError('Source execution evidence digest differs from availability')
    evidence = _json(raw)
    if not isinstance(evidence, dict) or evidence.get('omex_sha256') != descriptor['omex_sha256']:
        raise ValueError('Source execution evidence belongs to another archive')
    if evidence.get('schema') == 'qspquest.models.source-preparation-evidence/v1':
        if (evidence.get('model_id') != descriptor['model_id']
                or evidence.get('model_version') != descriptor['version']
                or evidence.get('current_engine_qualification') != 'not_assessed'
                or evidence.get('numerical_qualification_accepted') is not False
                or evidence.get('cases') != []):
            raise ValueError('Source-only execution evidence cannot assert numerical qualification')
    cases = evidence.get('cases')
    if not isinstance(cases, list) or len(cases) > 4096:
        raise ValueError('Source execution needs a bounded stored-case inventory')
    def ids(values):
        if (not isinstance(values, list) or len(values) > 4096
                or any(not isinstance(v, str) or not v or len(v) > 512 for v in values)
                or len(set(values)) != len(values)):
            raise ValueError('Source execution scenario inventory must contain unique identifiers')
        return set(values)
    case_ids = ids([case.get('scenario_id') if isinstance(case, dict) else None for case in cases])
    source_ids = ids(row.get('scenario_ids'))
    unavailable = ids(row.get('unavailable_scenario_ids'))
    qualified = ids(row.get('qualified_scenario_ids'))
    available = source_ids - unavailable
    if (not unavailable <= source_ids or not qualified <= available
            or available != set(availability.preset_ids) or qualified != case_ids):
        raise ValueError('Source qualified/available preset inventory differs from exact archive evidence: '
                         + str(row['id']) + ', execution ' + str(descriptor['version'])
                         + '. Restore the checksum-verified library and its matching evidence; '
                         'qualification belongs to the recorded archive, not a replacement version.')
    expected = ('source_only_hold' if not available else
                'fixed_presets_qualified' if qualified == available else 'fixed_presets_unqualified')
    if row.get('simulation_status') != expected:
        raise ValueError('Source simulation status differs from stored qualification coverage')
    if read_evidence() != raw:
        raise ValueError('Source execution evidence changed during inspection')
    return {'id': row['id'], 'version': row['version'],
            'model_id': descriptor['model_id'], 'execution_version': descriptor['version'],
            'archive_sha256': descriptor['omex_sha256'], 'evidence_id': availability.evidence_id,
            'available_scenario_ids': [sid for sid in row['scenario_ids'] if sid in available],
            'qualified_scenario_ids': list(row['qualified_scenario_ids']),
            'unavailable_scenario_ids': list(row['unavailable_scenario_ids']),
            'simulation_status': expected, 'qualification_scope': 'stored_archive_evidence_only',
            'current_engine_qualification': 'not_assessed'}


def load_source(root, model_id):
    """Read the three scientific documents; this does not run QSPQuest."""
    root = Path(root)
    matches = [r for r in list_sources(root) if r["id"] == model_id]
    if len(matches) != 1:
        raise ValueError("Unknown or duplicate scientific source")
    row = matches[0]
    if row.get("format") != "scientific_json" or not row["rights"].get(
        "redistribution_permitted_by_audit"
    ):
        raise PermissionError(
            "Source is metadata only pending rights/sanitation review"
        )
    if set(row["files"]) != {"model.json", "equations.json", "scenarios.json"}:
        raise ValueError("Unexpected source inventory")
    chunks = {}
    for name, record in row["files"].items():
        path = Path(record["path"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Unsafe source path")
        full = root / path
        if (
            any(p.is_symlink() for p in (full, *full.parents))
            or not full.is_file()
            or full.stat().st_size > 10_000_000
        ):
            raise ValueError("Invalid source file")
        raw = full.read_bytes()
        if hashlib.sha256(raw).hexdigest() != record["sha256"]:
            raise ValueError("Source digest mismatch")
        chunks[name] = raw
    if (
        hashlib.sha256(
            b"".join(
                chunks[n] for n in ("model.json", "equations.json", "scenarios.json")
            )
        ).hexdigest()
        != row["exported_sha256"]
    ):
        raise ValueError("Source snapshot mismatch")
    docs = {name: _json(raw) for name, raw in chunks.items()}
    if docs["model.json"]["id"] != model_id or any(
        docs[n]["model_id"] != model_id for n in ("equations.json", "scenarios.json")
    ):
        raise ValueError("Source identity mismatch")
    return docs
