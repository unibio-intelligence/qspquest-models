#!/usr/bin/env python3
"""Execute every introductory experiment and verify useful Python/CLI/R exports.

The small checked-in starter previews complement immutable archived evidence,
especially when that evidence omitted states. Run again after editing profiles.
"""
import argparse
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, result_columns, _finite_number


def preview(result):
    columns = []
    for column in result_columns(result):
        values = column['values']
        low = min(range(len(values)), key=values.__getitem__)
        high = max(range(len(values)), key=values.__getitem__)
        columns.append({
            'name': column['name'], 'unit': column['unit'],
            'first': values[0], 'last': values[-1],
            'minimum': values[low], 'minimum_time': result['times'][low], 'minimum_side': result['sides'][low],
            'maximum': values[high], 'maximum_time': result['times'][high], 'maximum_side': result['sides'][high],
        })
    return {'scenario_id': result['scenario_id'], 'archive_sha256': result['archive_sha256'],
            'engine_identity': result['identity'], 'rows': len(result['times']),
            'time_unit': result['time_unit'], 'columns': columns}



def compare_csv(path, result, columns, *, ordered=False, coordinates_only=False):
    """Compare a complete named table, including every row coordinate."""
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', newline='') as stream:
        reader = csv.DictReader(stream)
        names = ['time', 'side'] + [c['name'] for c in columns]
        if ((not columns and not coordinates_only) or not reader.fieldnames or len(reader.fieldnames) != len(names)
                or set(reader.fieldnames) != set(names) or (ordered and reader.fieldnames != names)):
            raise ValueError(f'{path}: duplicate, missing or unexpected CSV columns')
        rows = list(reader)
    if not rows or len(rows) != len(result['times']):
        raise ValueError(f'{path}: CSV row count differs')
    for i, row in enumerate(rows):
        if (None in row or None in row.values() or float(row['time']) != result['times'][i]
                or row['side'] != result['sides'][i]):
            raise ValueError(f'{path}: CSV row coordinates or width differ at row {i}')
        for column in columns:
            actual, expected = column['values'][i], float(row[column['name']])
            if (not _finite_number(actual) or not _finite_number(expected)
                    or not math.isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-8)):
                raise ValueError(f'{path}: CSV value differs for {column["name"]} at row {i}')


def compare_preview(saved, generated):
    for key in ('scenario_id', 'archive_sha256', 'rows', 'time_unit'):
        if type(saved.get(key)) is not type(generated[key]) or saved[key] != generated[key]:
            raise ValueError('Starter preview differs: ' + key)
    expected, actual = saved.get('columns'), generated['columns']
    if not isinstance(expected, list) or not expected or len(expected) != len(actual):
        raise ValueError('Starter preview column count differs')
    for old, new in zip(expected, actual):
        for key in ('name', 'unit', 'minimum_time', 'minimum_side', 'maximum_time', 'maximum_side'):
            if type(old.get(key)) is bool or old.get(key) != new[key]:
                raise ValueError('Starter preview differs: ' + key)
        for key in ('first', 'last', 'minimum', 'maximum'):
            if (not _finite_number(old.get(key)) or not _finite_number(new[key])
                    or not math.isclose(old[key], new[key], rel_tol=1e-6, abs_tol=1e-8)):
                raise ValueError('Starter preview differs: ' + key)


def reference_path(archive, model):
    evidence = json.loads(archive.with_name('evidence.json').read_text())
    cases = [c for c in evidence['cases'] if c['scenario_id'] == model.starter_scenario]
    if not cases:
        if evidence.get('schema') != 'qspquest.models.source-preparation-evidence/v1':
            raise ValueError('Missing starter reference in simulation evidence: ' + str(archive))
        return None
    if len(cases) != 1 or evidence.get('omex_sha256') != model.archive_sha256:
        raise ValueError('Starter reference identity differs: ' + str(archive))
    reference = cases[0]['files']['qspquest_csv']
    path = (archive.parent / reference['path']).resolve()
    if not path.is_relative_to(archive.parent.resolve()) or reference.get('compression') != 'gzip':
        raise ValueError('Invalid starter reference path or compression')
    raw = path.read_bytes()
    if (hashlib.sha256(raw).hexdigest() != reference['sha256']
            or hashlib.sha256(gzip.decompress(raw)).hexdigest() != reference['uncompressed_sha256']):
        raise ValueError('Starter reference checksum differs')
    return path


def validate(root=ROOT, *, executable=None, write_previews=False, check_interfaces=False):
    library = Library(root, executable=executable)
    counts = {'starters': 0, 'dynamic': 0, 'source_replay': 0, 'state_exports': 0, 'cli_exports': 0, 'r_exports': 0, 'reference_compared': 0, 'reference_coordinates_only': [], 'reference_unavailable': []}
    with tempfile.TemporaryDirectory(prefix='qspquest-starters-') as tmp:
        folder = Path(tmp)
        for row in library.list_models():
            model = library.load(row['id'])
            if not model.scenario_ids:
                continue
            assert model.starter_scenario in model.scenario_ids
            result = model.run(model.starter_scenario)
            columns = result_columns(result)
            assert 1 <= len(columns) <= 6, row['id']
            assert all(c.get('meaning') for c in columns), row['id']
            assert all(len(c['values']) == len(result['times']) for c in columns)
            assert all(math.isfinite(v) for c in columns for v in c['values'])
            changing = [c for c in columns if not math.isclose(min(c['values']), max(c['values']), rel_tol=1e-8, abs_tol=1e-10)]
            if model.guide['availability'] == 'dynamic':
                assert len(result['times']) > 2 and changing, ('no biological trajectory', row['id'])
            else:
                assert model.guide['availability'] == 'source_replay'
            counts[model.guide['availability']] += 1
            counts['state_exports'] += any(c['name'].startswith('state__') for c in columns)
            # Compare retained outputs against their immutable stored reference.
            path = library.root / row['archive']
            reference = reference_path(path, model)
            if reference is None:
                counts['reference_unavailable'].append({'model_id': model.model_id,
                    'model_version': model.index['model_version'], 'scenario_id': model.starter_scenario,
                    'reason': 'Source-only version has no retained numerical reference; execution and exports only'})
            else:
                compare_csv(reference, result, result['outputs'], coordinates_only=not result['outputs'])
                if result['outputs']:
                    counts['reference_compared'] += 1
                else:
                    counts['reference_coordinates_only'].append(row['id'])
            primary_path = folder / (row['id'] + '.csv')
            model.write_csv(result, primary_path)
            compare_csv(primary_path, result, columns, ordered=True)
            if check_interfaces:
                json_path = folder / (row['id'] + '.result.json')
                cli_path = folder / (row['id'] + '-cli.csv')
                command = [sys.executable, '-m', 'qspquest_models', '--library', str(library.root),
                           '--model', row['id'], '--model-version', model.index['model_version'], '--scenario', model.starter_scenario,
                           '--csv', str(cli_path), '--json', str(json_path)]
                if executable:
                    command += ['--executable', executable]
                subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
                assert cli_path.read_bytes() == primary_path.read_bytes(), row['id']
                counts['cli_exports'] += 1
            if reference is not None:
                generated = preview(result)
                if write_previews:
                    path.with_name('starter-preview.json').write_text(json.dumps(generated, indent=2, allow_nan=False) + '\n')
                else:
                    saved = json.loads(path.with_name('starter-preview.json').read_text())
                    compare_preview(saved, generated)
            counts['starters'] += 1
            print(row['id'], len(columns), 'readouts', len(changing), 'changing', flush=True)
        if check_interfaces:
            r_script = folder / 'check.R'
            r_script.write_text('''args <- commandArgs(trailingOnly=TRUE)
source(args[1])
files <- list.files(args[2], pattern="\\\\.result\\\\.json$", full.names=TRUE)
stopifnot(length(files) == as.integer(args[3]))
for (path in files) {
  result <- jsonlite::fromJSON(path, simplifyVector=FALSE)
  frame <- qspquest_data_frame(result)
  reference <- read.csv(sub("\\\\.result\\\\.json$", ".csv", path), check.names=FALSE)
  stopifnot(identical(names(frame), names(reference)))
  for (name in names(frame)) {
    if (is.numeric(frame[[name]])) stopifnot(isTRUE(all.equal(frame[[name]], reference[[name]], tolerance=1e-12)))
    else stopifnot(identical(frame[[name]], reference[[name]]))
  }
  complete <- qspquest_data_frame(result, all_readouts=TRUE)
  stopifnot(all(vapply(result$states, function(s) paste0("state__", s$name), "") %in% names(complete)))
}
''')
            subprocess.run(['Rscript', str(r_script), str(ROOT / 'tutorials/qspquest-models.R'), str(folder), str(counts['starters'])], check=True)
            counts['r_exports'] = counts['starters']
    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable')
    parser.add_argument('--write-previews', action='store_true')
    parser.add_argument('--check-interfaces', action='store_true')
    args = parser.parse_args()
    print(json.dumps(validate(executable=args.executable, write_previews=args.write_previews,
                              check_interfaces=args.check_interfaces), indent=2))
