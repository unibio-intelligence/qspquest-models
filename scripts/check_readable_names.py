#!/usr/bin/env python3
"""Run each selected native model under its readable names and compare with the native run.

For every archive with a ``parameters.json`` record, this renames the native
model and its preset requests through the record's name map, compiles the
renamed model with the installed QSPQuest engine, runs the presets, and checks
that every output column equals the native run. It needs the matching QSPQuest
Python binding. It does not qualify the models; it checks that the readable
names form a valid model that computes the same trajectories.
"""
from pathlib import Path
import argparse
import copy
import json
import math
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library  # noqa: E402
from qspquest_models import parameters as meta  # noqa: E402

REQUEST_MAPS = ('initial_states', 'parameters', 'covariates')


def rename_expression(value, names):
    if isinstance(value, dict):
        value = {k: rename_expression(v, names) for k, v in value.items()}
        if value.get('kind') == 'symbol':
            name = value['name']
            if name.startswith('input_') and name[6:] in names:
                value['name'] = 'input_' + names[name[6:]]
            else:
                value['name'] = names.get(name, name)
        return value
    if isinstance(value, list):
        return [rename_expression(v, names) for v in value]
    return value


def rename_model(model, names, outputs):
    model = rename_expression(copy.deepcopy(model), names)
    for group in meta.SYMBOL_GROUPS:
        for row in model.get(group, []) or []:
            row['name'] = names[row['name']]
    for row in model['outputs']:
        row['name'] = outputs[row['name']]
    return model


def rename_request(request, names):
    request = copy.deepcopy(request)
    for key in REQUEST_MAPS:
        if isinstance(request.get(key), dict):
            request[key] = {names.get(k, k): v for k, v in request[key].items()}
    regimen = request.get('regimen') or {}
    for key in ('covariates', 'absolute_tolerances'):
        if isinstance(regimen.get(key), dict):
            regimen[key] = {names.get(k, k): v for k, v in regimen[key].items()}
    for row in regimen.get('administrations', []) or []:
        row['target'] = names.get(row['target'], row['target'])
    for row in regimen.get('covariate_changes', []) or []:
        for key in ('covariate', 'name'):
            if key in row:
                row[key] = names.get(row[key], row[key])
    return request


def same(a, b):
    return a == b or (isinstance(a, float) and isinstance(b, float)
                      and (math.isnan(a) and math.isnan(b) or abs(a - b) <= 1e-12 * max(1.0, abs(a))))


def check(library, row, record, scenarios):
    from qspquest import CompiledModel
    with zipfile.ZipFile(library.root / row['archive']) as z:
        index = json.loads(z.read('index.json'))
        native = index['native_execution']
        model = json.loads(z.read(native['model']))
        requests = {sid: json.loads(z.read(path)) for sid, path in native['scenarios'].items()}
    names = meta.name_map(record)
    renamed = rename_model(model, names['symbols'], names['outputs'])
    base, readable = CompiledModel(model), CompiledModel(renamed)
    chosen = list(requests) if scenarios == 'all' else [library.load(row['id']).starter_scenario or next(iter(requests))]
    for sid in chosen:
        if sid in index.get('unavailable_scenario_ids', []):
            continue
        expected = base.run(requests[sid])
        actual = readable.run(rename_request(requests[sid], names['symbols']))
        if expected['times'] != actual['times'] or expected['sides'] != actual['sides']:
            raise ValueError(f'{row["id"]} {sid}: sample rows differ')
        got = {o['name']: o for o in actual['outputs']}
        for output in expected['outputs']:
            other = got[names['outputs'][output['name']]]
            if other['unit'] != output['unit'] or not all(map(same, output['values'], other['values'])):
                raise ValueError(f'{row["id"]} {sid}: output {output["name"]} differs')
    return len(chosen)


def main(scenarios):
    library = Library(ROOT)
    models = runs = 0
    for row in library.list_models():
        path = (ROOT / row['archive']).with_name(meta.FILENAME)
        if not path.is_file():
            continue
        record = json.loads(path.read_bytes())
        runs += check(library, row, record, scenarios)
        models += 1
    return {'models': models, 'preset_runs': runs, 'readable_names': 'equivalent'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scenarios', choices=['starter', 'all'], default='starter',
                        help='Run only each starter preset (default) or every available preset')
    print(json.dumps(main(parser.parse_args().scenarios), indent=2))
