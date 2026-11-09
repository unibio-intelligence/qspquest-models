#!/usr/bin/env python3
"""Write parameters.json next to each selected archive; never rewrite an archive.

Source names come from the archive itself: the explicit native-execution map
when the archive has one, otherwise the generator order of the scientific
source (states, parameters, covariates, definitions) or of its SBML. Every
positional match is checked against the native default value. Roles are assigned
in three steps:

1. A parameter the dynamics use is ``structural`` (dependency graph, not names).
2. A closed set of name rules classifies the remaining parameters.
3. ``parameter_curation.json`` overrides both with reviewed records.

Uncurated provenance says ``not_curated``; a locator is copied only when the
source category names a table, figure, equation, appendix or supplement.
Run with ``--check`` to compare the stored records without writing.
"""
from pathlib import Path
import argparse
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library  # noqa: E402
from qspquest_models import parameters as meta  # noqa: E402

CURATION = ROOT / 'scripts' / 'parameter_curation.json'
SBML = {'s': 'http://www.sbml.org/sbml/level3/version2/core'}
LOCATOR = re.compile(r'(?i)(table|fig\.?|figure|supplement\w*|equation|eq\.|appendix)[\s_]*[a-z]?\d')
# Applied in order to parameters the dynamics do not use. Reported statistics
# (CV%, variance, shrinkage, standard errors, intervals) stay source_check.
STATISTIC = re.compile(r'(?i)(.*_)?(cv|pct|percent|variance|var|shrinkage|se|rse|ci|bootstrap|median|mean|low|high|lower|upper)(_|$).*')
NAME_RULES = (
    ('unit_basis', re.compile(r'legacy_unit_basis_\d+|source_pk_[a-z_]+_basis'), 'native'),
    ('runtime', re.compile(r'(?i)(validation_)?run_nonce|.*_nonce'), 'source'),
    ('information_criterion', re.compile(r'(?i)ofv|aic|aicc|bic|bic_?c|m2ll|minus_?2_?ll'), 'source'),
    ('subject_replay', re.compile(r'(?i)(subject|patient|individual|id)_?\d+_.*'), 'source'),
    ('residual_error', re.compile(r'(?i)residual(_.*)?|(sigma_)?(prop|add|exp)_?err(or)?(_.*)?|sigma_(prop|add|exp)(_.*)?'), 'source'),
    ('iiv_sd', re.compile(r'(?i)(omega|iiv_sd|eta_sd)_(?P<target>.+)'), 'source'),
)


def close(a, b):
    return abs(a - b) <= 1e-12 * max(1.0, abs(a), abs(b))


def authored(members, source_model_id):
    """The source snapshot equal to the archive's scientific documents, in authored order.

    Archives store the scientific documents with sorted keys; the snapshot under
    sources/ keeps the order the library generator numbered.
    """
    expected = {n: json.loads(members['scientific/' + n]) for n in ('model.json', 'equations.json')}
    for folder in sorted((ROOT / 'sources' / str(source_model_id)).glob('*')):
        docs = {n: json.loads((folder / n).read_bytes()) for n in expected if (folder / n).is_file()}
        if docs == expected:
            return docs['model.json'], docs['equations.json']
    return expected['model.json'], expected['equations.json']


def source_order(members, source_model_id):
    """Symbol order the library generator numbered as source_symbol_N, with values."""
    if 'scientific/model.json' in members:
        model, equations = authored(members, source_model_id)
        order = [(n, None) for n in model['states']]
        order += [(n, p['default']) for n, p in model['parameters'].items()]
        order += [(n, None) for n in (model.get('covariates') or {})]
        order += [(n, None) for n in (equations.get('definitions') or {})]
        return order, {n: p for n, p in model['parameters'].items()}
    root = ET.fromstring(members['model.xml'])
    order = [(e.get('id'), None) for e in root.findall('.//s:species', SBML)]
    rows = [e for e in root.findall('.//s:listOfParameters/s:parameter', SBML)
            if not e.get('id').startswith(('Dose_rate_', 'ubi_observable_'))]
    order += [(e.get('id'), float(e.get('value'))) for e in rows if e.get('constant') == 'true']
    order += [(e.get('id'), None) for e in rows if e.get('constant') != 'true']
    return order, {}


def source_names(members, index, model, source_model_id):
    """Map native symbol names to the archive's own source names, checking values."""
    native = index['native_execution']
    explicit = {row['native_name']: alias for alias, row in native.get('parameters', {}).items()}
    explicit_states = {row['native_name']: alias
                       for alias, row in (native.get('input_states') or {}).items()}
    order, scientific = source_order(members, source_model_id)
    defaults = {p['name']: p['default']['value'] for p in model['parameters']}
    declared = native.get('source_symbols')
    if declared is not None:
        # An explicit map preserves stable native names when the source is sparse.
        source_values = dict(order)
        if (not isinstance(declared, dict) or len(set(declared.values())) != len(declared)
                or any(name not in source_values for name in declared.values())):
            raise ValueError(f'{index["model_id"]}: invalid source symbol map')
        if any(declared.get(n) != a for n, a in {**explicit, **explicit_states}.items()):
            raise ValueError(f'{index["model_id"]}: explicit source maps disagree')
        for name, alias in declared.items():
            if name in defaults and (source_values[alias] is None or not close(defaults[name], source_values[alias])):
                raise ValueError(f'{index["model_id"]}: {name} does not match source {alias}')
        names = declared
    else:
        positional = {f'source_symbol_{i}': name for i, (name, _) in enumerate(order)}
        agrees = all(positional.get(n) == a for n, a in {**explicit, **explicit_states}.items())
        names = {}
        if agrees:
            for native_name, (name, value) in zip(positional, order):
                if native_name in defaults and (value is None or not close(defaults[native_name], value)):
                    raise ValueError(f'{index["model_id"]}: {native_name} does not match source {name}')
            names = positional
        elif not explicit:
            raise ValueError(f'{index["model_id"]}: state map disagrees with the generator order')
        names = {**names, **explicit, **explicit_states}
    used = {row['name'] for g in meta.SYMBOL_GROUPS for row in model.get(g, []) or []}
    for name in used:
        if name.startswith('source_symbol_') and name not in names:
            raise ValueError(f'{index["model_id"]}: no source name for {name}')
    outputs = {row['native_name']: alias for key in ('outputs', 'states')
               for alias, row in native.get(key, {}).items()}
    return names, outputs, scientific


def sources_for(library, row):
    reproduction = json.loads((library.root / row['archive']).with_name('SOURCE_REPRODUCTION.json').read_text())
    return [str(d) for d in reproduction.get('source_dois') or []]


def rule_role(native_name, source_name, structural_readable):
    for role, pattern, field in NAME_RULES:
        text = native_name if field == 'native' else source_name
        if text is None:
            continue
        match = pattern.fullmatch(text)
        if not match or (role in ('residual_error', 'iiv_sd') and STATISTIC.fullmatch(text)):
            continue
        variability = None
        if role == 'iiv_sd':
            suffix = readable_key(match.group('target'))
            candidates = [r for k, r in structural_readable.items()
                          if k == suffix or k.startswith(suffix + '_')]
            variability = {'distribution': 'not_curated',
                           'target': candidates[0] if len(candidates) == 1 else None,
                           'scale': 'not_curated'}
        return role, variability
    return 'source_check', None


def readable_key(name):
    return meta.readable(name)


def build_record(library, row, curation):
    archive = library.root / row['archive']
    with zipfile.ZipFile(archive) as z:
        members = {n: z.read(n) for n in z.namelist()}
    index = json.loads(members['index.json'])
    model = json.loads(members[index['native_execution']['model']])
    key = row['id'] + '/' + row['version']
    curated = curation.get(key, {})
    names, output_names, scientific = source_names(members, index, model, row.get('source_model_id'))
    sources = sources_for(library, row)
    source_coordinates = index['native_execution'].get('coordinates') == 'unchanged_source_numeric_values'
    used, record = set(), {
        'schema': meta.SCHEMA, 'model_id': row['id'], 'model_version': row['version'],
        'archive_sha256': row['omex_sha256'], 'sources': sources}
    native = meta.native_symbols(model)
    for group in meta.GROUPS:
        seen = set() if group == 'outputs' else used
        rows = []
        for native_name, unit in native[group]:
            source = (output_names if group == 'outputs' else names).get(native_name)
            override = curated.get('readable_names', {}).get(native_name)
            base = override or meta.readable(source if source is not None else native_name)
            name, n = base, 2
            while name in seen:
                name, n = f'{base}_{n}', n + 1
            seen.add(name)
            rows.append({'native_name': native_name, 'source_name': source,
                         'readable_name': name, 'unit': unit})
        record[group] = rows
    structural = meta.structural_names(model)
    structural_readable = {meta.readable(r['source_name'] or r['native_name']): r['readable_name']
                           for r in record['parameters'] if r['native_name'] in structural}
    by_source = {r['source_name']: r['readable_name'] for r in record['parameters'] if r['source_name']}
    for row_ in record['parameters']:
        native_name, source = row_['native_name'], row_['source_name']
        if native_name in structural:
            role, variability, classification = 'structural', None, 'dependency'
        else:
            role, variability = rule_role(native_name, source, structural_readable)
            classification = 'name_rule'
        category = (scientific.get(source) or {}).get('category') if source else None
        unit_basis = 'source_coordinates' if source_coordinates and row_['unit'] == '1' else 'not_curated'
        paper = sources[0] if len(sources) == 1 and role not in ('runtime', 'unit_basis') else None
        provenance = {'source': paper,
                      'locator': category if category and LOCATOR.search(category) else None,
                      'status': 'not_curated', 'unit_basis': unit_basis}
        reviewed = curated.get('parameters', {}).get(source)
        if reviewed is not None:
            if (reviewed['role'] == 'structural') != (native_name in structural):
                raise ValueError(f'{row["id"]}: curated role of {source} contradicts the dynamics')
            role, classification = reviewed['role'], 'curated'
            variability = reviewed.get('variability')
            if variability is not None:
                variability = {**variability, 'target': by_source[variability['target']]}
            provenance = {'source': reviewed.get('source', provenance['source']),
                          'locator': reviewed.get('locator'), 'status': reviewed['status'],
                          'unit_basis': reviewed['unit_basis']}
        if role == 'iiv_sd' and native_name in structural:
            raise ValueError(f'{row["id"]}: {source} is used by the dynamics but named as IIV')
        row_.update(role=role, variability=variability, provenance=provenance,
                    classification=classification)
    unknown = set(curated.get('parameters', {})) - set(by_source)
    if unknown:
        raise ValueError(f'{key}: curation names unknown parameters {sorted(unknown)}')
    meta.check(record, model, model_id=row['id'], model_version=row['version'],
               archive_sha256=row['omex_sha256'])
    return record


def encoded(record):
    """One symbol per line, so a review diff shows each changed record."""
    dump = lambda v: json.dumps(v, ensure_ascii=False, allow_nan=False)
    lines = ['{']
    keys = list(record)
    for i, key in enumerate(keys):
        end = ',' if i < len(keys) - 1 else ''
        value = record[key]
        if key in meta.GROUPS:
            rows = [' ' + dump(row) for row in value]
            lines.append(f' {dump(key)}: [' + ('\n' + ',\n'.join(rows) + '\n ]' if rows else ']') + end)
        else:
            lines.append(f' {dump(key)}: {dump(value)}{end}')
    return ('\n'.join(lines) + '\n}\n').encode()


def build(check_only=False):
    library = Library(ROOT)
    curation = json.loads(CURATION.read_text())
    curation.pop('_comment', None)
    stale, written = [], 0
    selected = set()
    for row in library.list_models():
        archive = ROOT / row['archive']
        with zipfile.ZipFile(archive) as z:
            index = json.loads(z.read('index.json'))
        if not index.get('native_execution', {}).get('model'):
            continue
        selected.add(row['id'] + '/' + row['version'])
        raw = encoded(build_record(library, row, curation))
        path = archive.with_name(meta.FILENAME)
        if not path.is_file() or path.read_bytes() != raw:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check_only:
                path.write_bytes(raw)
        written += 1
    # Superseded versions carry no record; remove one left by an earlier selection.
    kept = {(ROOT / r['archive']).with_name(meta.FILENAME) for r in library.list_models()}
    for path in sorted(ROOT.glob('models/*/*/' + meta.FILENAME)):
        if path not in kept:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check_only:
                path.unlink()
    unknown = set(curation) - selected
    if unknown:
        raise ValueError('Curation names unselected archives: ' + ', '.join(sorted(unknown)))
    return written, stale


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if a stored record differs; write nothing')
    args = parser.parse_args()
    count, stale = build(check_only=args.check)
    if args.check and stale:
        print('Stale parameter metadata: ' + ', '.join(stale), file=sys.stderr)
        raise SystemExit(2)
    print(f'{count} parameter records; {len(stale)} ' + ('stale' if args.check else 'written'))
