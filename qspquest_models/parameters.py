"""Parameter roles, provenance and readable names for selected model archives.

Each selected archive version has a ``parameters.json`` record next to its
``evidence.json``. The record names every symbol of the archive's native model,
gives each parameter a role and a provenance record, and maps every native name
to a readable name that is a legal QSPQuest model identifier. The record
describes the archive named by ``archive_sha256``; ``check`` verifies it against
that archive's native model without running an engine.
"""
from pathlib import Path
import json
import re

SCHEMA = 'qspquest.models.parameter-metadata/v1'
FILENAME = 'parameters.json'

ROLES = ('structural', 'iiv_sd', 'residual_error', 'information_criterion', 'subject_replay',
         'administration', 'source_check', 'runtime', 'unit_basis')
STATUSES = ('estimated', 'fixed', 'assumed', 'derived', 'reported', 'not_curated')
UNIT_BASES = ('declared', 'ode_inferred', 'source_coordinates', 'not_curated')
DISTRIBUTIONS = ('log_normal', 'additive', 'not_curated')
SCALES = ('sd', 'variance', 'not_curated')
CLASSIFICATIONS = ('curated', 'dependency', 'name_rule')
# Symbols of one namespace in a native model, in the order readable names are assigned.
SYMBOL_GROUPS = ('states', 'parameters', 'covariates', 'definitions', 'switches')
GROUPS = SYMBOL_GROUPS + ('outputs',)
RESERVED = frozenset({'time', 'true', 'false'})
_IDENTIFIER = re.compile(r'[a-z_][a-z0-9_]*')


def legal(name):
    """Return True when ``name`` is a legal QSPQuest model identifier."""
    return (isinstance(name, str) and 0 < len(name) <= 128 and _IDENTIFIER.fullmatch(name) is not None
            and name not in RESERVED and not name.startswith('input_'))


def readable(name):
    """Derive a lowercase snake_case identifier from a source or native name."""
    text = re.sub(r'[^a-z0-9_]+', '_', str(name).lower())
    text = re.sub(r'_+', '_', text).strip('_') or 'p'
    if text[0].isdigit():
        text = 'p_' + text
    if text in RESERVED:
        text += '_value'
    if text.startswith('input_'):
        text = 'v_' + text
    return text[:120].rstrip('_') or 'p'


def symbols(value, found=None):
    """Collect symbol names used anywhere in an expression tree."""
    found = set() if found is None else found
    if isinstance(value, dict):
        if value.get('kind') == 'symbol':
            found.add(value['name'])
        for child in value.values():
            symbols(child, found)
    elif isinstance(value, list):
        for child in value:
            symbols(child, found)
    return found


def structural_names(model):
    """Names reachable from the dynamics: state rhs, initial values and dosing scales.

    Definitions and time switches are followed transitively. Outputs and
    invariants are not dynamics, so a parameter used only there is not structural.
    """
    reached = set()
    for state in model.get('states', []):
        symbols([state.get('rhs'), state.get('initial'), state.get('dosing')], reached)
    dependencies = {row['name']: symbols(row) for key in ('definitions', 'switches')
                    for row in model.get(key, []) or []}
    pending = list(reached)
    while pending:
        name = pending.pop()
        for dependency in dependencies.get(name, ()):
            if dependency not in reached:
                reached.add(dependency)
                pending.append(dependency)
    return reached


def native_symbols(model):
    """Native symbol names and units by group; outputs are a separate namespace."""
    result = {}
    for group in SYMBOL_GROUPS:
        rows = []
        for row in model.get(group, []) or []:
            if group == 'parameters':
                unit = row['default']['unit']
            elif group == 'switches':
                unit = None
            else:
                unit = row.get('unit')
            rows.append((row['name'], unit))
        result[group] = rows
    result['outputs'] = [(row['name'], row['unit']) for row in model.get('outputs', [])]
    return result


def _require(condition, message):
    if not condition:
        raise ValueError('Parameter metadata: ' + message)


def check(record, model, *, model_id, model_version, archive_sha256):
    """Verify a record against the archive's native model; return the record.

    Checks identity, that every native symbol is described exactly once with its
    native unit, closed vocabularies, readable-name legality and uniqueness, and
    that ``structural`` is exactly the set of parameters the dynamics use.
    """
    _require(isinstance(record, dict) and record.get('schema') == SCHEMA, 'unsupported schema')
    _require((record.get('model_id'), record.get('model_version'), record.get('archive_sha256'))
             == (model_id, model_version, archive_sha256), 'record describes another archive')
    _require(isinstance(record.get('sources'), list), 'sources must be a list')
    native = native_symbols(model)
    namespace = set()
    for group in GROUPS:
        rows = record.get(group)
        _require(isinstance(rows, list), group + ' must be a list')
        _require([(r.get('native_name'), r.get('unit')) for r in rows] == native[group],
                 group + ' differ from the native model names, order or units')
        seen = set() if group == 'outputs' else namespace
        for row in rows:
            name = row.get('readable_name')
            _require(legal(name), 'illegal readable name ' + repr(name))
            _require(name not in seen, 'duplicate readable name ' + name)
            seen.add(name)
            _require(row.get('source_name') is None or isinstance(row['source_name'], str),
                     'source_name must be a string or null')
    structural = structural_names(model)
    readable_by_native = {r['native_name']: r['readable_name'] for r in record['parameters']}
    for row in record['parameters']:
        role = row.get('role')
        _require(role in ROLES, 'unknown role ' + repr(role))
        _require((role == 'structural') == (row['native_name'] in structural),
                 row['native_name'] + ': structural role must match the dynamics')
        _require(row.get('classification') in CLASSIFICATIONS, 'unknown classification')
        variability = row.get('variability')
        if role == 'iiv_sd':
            _require(isinstance(variability, dict)
                     and variability.get('distribution') in DISTRIBUTIONS
                     and variability.get('scale') in SCALES, 'iiv_sd needs a variability record')
            target = variability.get('target')
            _require(target is None or target in readable_by_native.values(),
                     'variability target must be a readable parameter name')
        else:
            _require(variability is None, 'variability is only for iiv_sd')
        provenance = row.get('provenance')
        _require(isinstance(provenance, dict) and provenance.get('status') in STATUSES
                 and provenance.get('unit_basis') in UNIT_BASES, 'incomplete provenance')
        for key in ('source', 'locator'):
            _require(provenance.get(key) is None or isinstance(provenance[key], str), key + ' must be text')
        if row['classification'] != 'curated':
            _require(provenance['status'] == 'not_curated', 'uncurated rows must say not_curated')
    return record


def load(archive_path, model, *, model_id, model_version, archive_sha256):
    """Read and check the record next to an archive; None when it has none."""
    path = Path(archive_path).with_name(FILENAME)
    if not path.is_file() or path.is_symlink():
        return None
    _require(path.stat().st_size <= 1_000_000, 'record larger than 1 MB, the engine limit')
    return check(json.loads(path.read_bytes()), model, model_id=model_id,
                 model_version=model_version, archive_sha256=archive_sha256)


def name_map(record):
    """Native-to-readable names: one namespace for model symbols, one for outputs."""
    symbols_ = {row['native_name']: row['readable_name'] for g in SYMBOL_GROUPS for row in record[g]}
    outputs = {row['native_name']: row['readable_name'] for row in record['outputs']}
    return {'symbols': symbols_, 'outputs': outputs}
