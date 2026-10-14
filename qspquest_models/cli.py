"""Shared discovery and execution command for the model library."""
import argparse
import difflib
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile
from xml.etree.ElementTree import ParseError

from . import Library, read_table
from .input_bindings import InputBindingError

ERROR_SCHEMA = 'qspquest.library-error/v1'


class _Parser(argparse.ArgumentParser):
    def __init__(self, *, json_errors=False, **kwargs):
        super().__init__(**kwargs)
        self.json_errors = json_errors

    def fail(self, code, problem, cause, fix, status=1, *, details=None):
        error = {'schema': ERROR_SCHEMA, 'code': code, 'problem': problem,
                 'cause': str(cause), 'fix': fix}
        if details is not None:
            error['details'] = details
        message = (json.dumps(error, allow_nan=False) if self.json_errors else
                   f"{problem} [{code}]: {cause}\nFix: {fix}")
        self.exit(status, message + '\n')

    def error(self, message):
        self.fail('invalid_arguments', 'Invalid command arguments', message,
                  'Use --help for supported options and combinations.', status=2)


def _parser(argv, prog):
    parser = _Parser(prog=prog, json_errors='--json-errors' in argv,
                     description='Browse pharmacology models and run experiments')
    verify_table = any(arg == '--verify-table' or arg.startswith('--verify-table=') for arg in argv)
    parser.add_argument('--library', default=None if verify_table else os.environ.get('QSPQUEST_LIBRARY_DIR'),
                        help='Library directory (default: QSPQUEST_LIBRARY_DIR, then package checkout)')
    parser.add_argument('--executable', help='Path to the QSPQuest executable')
    parser.add_argument('--search', help='Find models by name, ID, browsing summary or description')
    parser.add_argument('--runnable', action='store_true', help='Show only models with runnable experiments, including source replays')
    parser.add_argument('--format', choices=['table', 'json'], default='table', help='Discovery format; with --verify-table, json includes validated rows (default: table)')
    parser.add_argument('--json-errors', action='store_true', help='Write a structured error object to stderr on failure')
    parser.add_argument('--model', help='Model ID; omit --scenario to list its experiments')
    parser.add_argument('--model-version', help='Exact catalog model version; requires --model and never selects a replacement')
    parser.add_argument('--scenario', help='Experiment ID to run')
    parser.add_argument('--csv', help='Create primary-readout CSV and .manifest.json; never overwrite')
    parser.add_argument('--verify-table', help='Validate a CSV bundle and print its manifest without an engine or library')
    parser.add_argument('--json', help='Write the full simulation result to this JSON file')
    parser.add_argument('--all-readouts', action='store_true', help='CSV: include all outputs and states instead of primary readouts')
    parser.add_argument('--dose', action='append', default=[], metavar='INDEX=AMOUNT', help='Run a research copy with a zero-based dose amount changed; may be repeated')
    parser.add_argument('--initial', action='append', default=[], metavar='STATE=VALUE', help='Change an initial biological state in a research copy')
    parser.add_argument('--inputs', action='store_true', help='Inspect dose indexes and initial states without running an engine')
    parser.add_argument('--save-research', help='Save edited inputs and provenance to a new directory')
    return parser


def _validate(parser, args):
    if args.verify_table is not None and any((args.library, args.executable, args.model, args.model_version, args.scenario,
                                 args.search, args.runnable, args.csv, args.json, args.dose,
                                 args.initial, args.inputs, args.save_research, args.all_readouts)):
        parser.error('--verify-table accepts only a CSV path, --format and --json-errors')
    if args.model_version is not None and (not args.model or not args.model_version):
        parser.error('--model-version requires --model and a nonempty exact version')
    if args.scenario and not args.model:
        parser.error('--scenario requires --model')
    if (args.csv or args.json) and not args.scenario:
        parser.error('--csv and --json require --model and --scenario')
    if (args.dose or args.initial or args.inputs or args.save_research or args.all_readouts) and not args.scenario:
        parser.error('--dose, --initial, --inputs, --save-research and --all-readouts require --model and --scenario')
    if args.inputs and (args.csv or args.json or args.dose or args.initial or args.save_research):
        parser.error('--inputs inspects the original preset; omit result paths and changes')
    if args.model and (args.search or args.runnable):
        parser.error('--search and --runnable are model-list filters; omit --model')


def _list(library, args):
    rows = library.search(args.search) if args.search else library.list_models()
    if args.runnable:
        rows = [row for row in rows if row['scenario_ids']]
    if args.format == 'json':
        print(json.dumps(rows, indent=2, allow_nan=False))
        return
    print(f'{len(rows)} models found. Browse MODEL_CATALOG.md for descriptions and guides.\n')
    for row in rows:
        availability = row.get('availability', {}).get('availability')
        if availability is None:
            guide = library.load(row['id']).guide
            availability = guide.get('availability') if guide else None
        status = ('Source replay available; dynamic simulation unavailable' if availability == 'source_replay'
                  else f"{len(row['scenario_ids'])} runnable experiments" if row['scenario_ids'] else 'Inspection only; simulation unavailable')
        print(f"{row['name']} — {status}\n  {row['id']}")
    if not rows:
        print('Try a drug name such as rituximab, a mechanism such as QSP, or omit the filters.')
    else:
        print('\nNext: --model MODEL_ID lists experiments; add --scenario EXPERIMENT_ID --csv result.csv to run one.')


def _select_model(library, parser, model_id):
    rows = library.list_models()
    if model_id not in {row['id'] for row in rows}:
        matches = library.search(model_id)
        if not matches:
            ids = difflib.get_close_matches(model_id, [row['id'] for row in rows], n=3, cutoff=0.4)
            matches = [row for row in rows if row['id'] in ids]
        suggestions = ('Matching model IDs:\n' + '\n'.join('  ' + row['id'] for row in matches[:8])
                       if matches else 'Use --search DRUG_OR_MECHANISM to find a model ID.')
        parser.fail('unknown_model', 'Unknown model', model_id,
                    'Use a complete model ID. ' + suggestions, status=2)


def _scenarios(model, args):
    if args.format == 'json':
        print(json.dumps(list(model.scenario_ids)))
    elif model.scenario_ids:
        if model.availability and model.availability['availability'] == 'source_replay':
            print('Source replay available; dynamic simulation unavailable.')
        print(f'Selected archive: {model.model_id} {model.index["model_version"]} (SHA-256 {model.archive_sha256})')
        print('Suggested starter: ' + str(model.starter_scenario))
        print('Runnable experiment IDs (use with --scenario):')
        for sid in model.scenario_ids:
            print('  ' + sid)
        print(f'\nPurpose, inputs and outputs: models/{model.model_id}/{model.index["model_version"]}/MODEL_CARD.md')
    else:
        print('Inspection only: simulation is unavailable for this version. Choose a runnable model with --runnable.')
        print(f'Details: models/{model.model_id}/{model.index["model_version"]}/INTERCHANGE_AND_EXECUTION_HOLDS.json')


_FAILURES = {
    'table': ('table_invalid', 'Cannot validate the table bundle', 'Keep the CSV and its .manifest.json together; use the original bytes and inspect units and qualification scope in the manifest.'),
    'library': ('library_unavailable', 'Cannot load the model library', 'Pass --library to an extracted library directory containing catalog.json; check its files and permissions.'),
    'discovery': ('discovery_failed', 'Cannot search the model library', 'Check the catalog and source metadata; use a complete, checksum-verified library archive.'),
    'archive': ('archive_invalid', 'Cannot load the selected model archive', 'Restore the checksum-verified archive selected by catalog.json; do not edit archived files.'),
    'inputs': ('invalid_inputs', 'Cannot prepare the experiment inputs', 'List experiments with --model MODEL_ID, inspect --inputs, and use INDEX=AMOUNT or STATE=VALUE with finite supported values.'),
    'engine': ('execution_failed', 'Cannot run the experiment', 'Check the engine error and the model guide; use the matching engine release and supported inputs.'),
    'output': ('output_unavailable', 'Cannot write the result', 'Choose a new writable file path with an existing parent directory; CSV and its .manifest.json must both be absent. Use a new directory for --save-research.'),
}


def main(argv=None, *, prog=None):
    """Run the shared command; failures exit 1, usage and unknown IDs exit 2."""
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = _parser(argv, prog)
    args = parser.parse_args(argv)
    _validate(parser, args)
    stage = 'library'
    try:
        if args.verify_table is not None:
            stage = 'table'
            bundle = read_table(args.verify_table)
            print(json.dumps(bundle if args.format == 'json' else bundle['manifest'], indent=2, allow_nan=False))
            return
        library = Library(args.library, executable=args.executable)
        if not args.model:
            stage = 'discovery'
            _list(library, args)
            return
        stage = 'discovery'
        _select_model(library, parser, args.model)
        stage = 'archive'
        model = library.load(args.model, version=args.model_version)
        if not args.scenario:
            _scenarios(model, args)
            return
        if args.scenario not in model.scenario_ids:
            parser.fail('unknown_scenario', 'Unknown or unavailable experiment', args.scenario,
                        'List exact experiment IDs with --model ' + args.model + ' and choose a runnable preset.', status=2)
        stage = 'inputs'
        if args.inputs or args.dose or args.initial or args.save_research:
            copy = model.research_copy(args.scenario)
            if args.inputs:
                print(json.dumps({'doses': copy.doses, 'initial_states': copy.initial_states}, indent=2, allow_nan=False))
                return
            for dose in args.dose:
                index, amount = dose.split('=', 1)
                copy.set_dose(int(index), float(amount))
            for initial in args.initial:
                name, value = initial.split('=', 1)
                copy.set_initial_state(name, float(value))
            stage = 'engine'
            result = copy.run()
        else:
            stage = 'engine'
            result = model.run(args.scenario)
        stage = 'output'
        if args.save_research:
            copy.save(args.save_research)
        if args.csv:
            model.write_csv(result, args.csv, all_readouts=args.all_readouts)
        if args.json:
            Path(args.json).write_text(json.dumps(result, allow_nan=False), encoding='utf-8')
        if not args.csv and not args.json:
            print(json.dumps(result, allow_nan=False))
    except (OSError, ValueError, RuntimeError, ImportError, KeyError, zipfile.BadZipFile,
            subprocess.SubprocessError, ParseError, TypeError, IndexError) as error:
        if isinstance(error, (TypeError, IndexError)) and stage not in ('library', 'discovery', 'archive'):
            raise
        if (stage == 'archive' and isinstance(error, InputBindingError)
                and error.diagnostic.get('code') == 'model_version_unavailable'):
            diagnostic = error.diagnostic
            available = ', '.join(diagnostic['available_versions']) or '(none)'
            parser.fail('model_version_unavailable', 'The exact model version is unavailable',
                        f"Model {diagnostic['model_id']}, requested version {diagnostic['requested_version']}; available catalog versions: {available}",
                        'Inspect --format json discovery and the versioned model guide before explicitly changing --model-version. Use the checksum-pinned Python load_archive command for a distributed alternate archive.',
                        status=2, details=diagnostic)
        code, problem, fix = _FAILURES[stage]
        if stage == 'engine' and isinstance(error, subprocess.TimeoutExpired):
            code, problem = 'engine_timeout', 'The engine exceeded its time limit'
            fix = 'Check the executable and model guide; reduce the experiment workload before retrying.'
        elif stage == 'engine' and (isinstance(error, (FileNotFoundError, PermissionError, ImportError)) or
                                    'install qspquest' in str(error).casefold()):
            code, problem = 'engine_unavailable', 'The QSPQuest engine is unavailable'
            fix = 'Install the matching QSPQuest Python binding or set --executable / QSPQUEST_EXECUTABLE to an executable you can run.'
        parser.fail(code, problem, error, fix)
