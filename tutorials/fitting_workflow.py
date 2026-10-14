#!/usr/bin/env python3
"""List declared fitting support or retain one complete synthetic workflow result."""
import argparse
import json
from pathlib import Path
import sys
from qspquest_models import Library


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library', type=Path, default=Path('.'))
    parser.add_argument('--model')
    parser.add_argument('--version')
    parser.add_argument('--workflow')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    try:
        library = Library(args.library)
        if args.model is None:
            if args.version or args.workflow or args.out:
                raise ValueError('Select --model together with --version, --workflow and --out')
            ready = []
            for row in library.list_models():
                if row.get('availability', {}).get('fit_ready') is True:
                    model = library.load(row['id'], version=row['version'])
                    ready.append({'model_id': row['id'], 'version': row['version'],
                                  'workflows': [{'id': w['id'], 'operation': w['operation'], 'parameters': w['parameters'],
                                                 'qualification': w['qualification']} for w in model.fitting_workflows]})
            print(json.dumps({'fit_ready_models': ready, 'current_engine_qualification': 'not_assessed'}, indent=2, allow_nan=False))
            return 0
        if not all((args.version, args.workflow, args.out)):
            raise ValueError('An execution requires exact --version, --workflow and a new --out JSON file')
        if args.out.exists() or args.out.is_symlink():
            raise ValueError('Choose a new output filename; existing results are never replaced')
        model = library.load(args.model, version=args.version)
        result = model.fit_workflow(args.workflow)
        with args.out.open('x', encoding='utf-8') as stream:
            json.dump(result, stream, indent=2, allow_nan=False)
            stream.write('\n')
        print(json.dumps({'saved': str(args.out.absolute()), **result['checks']}, indent=2, allow_nan=False))
        return 0 if result['checks']['passed'] else 1
    except (ValueError, RuntimeError, OSError, ImportError, KeyError) as error:
        print('Library fitting failed: '+str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
