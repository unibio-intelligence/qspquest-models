"""Inspect version-bound inputs and edit the distributed synthetic cargo model."""
import argparse
import json
from pathlib import Path

from qspquest_models import InputBindingError, Library, read_table


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library-dir', default='.')
    parser.add_argument('--engine-cli', help='Absolute path to the installed QSPQuest CLI')
    parser.add_argument('--output-dir', default='research-output/input-bindings')
    parser.add_argument('--inspect-only', action='store_true', help='Inspect and save inputs without running the engine')
    args = parser.parse_args()
    model = Library(args.library_dir, executable=args.engine_cli).load(
        'qspquest_ubi_2026_target_gated_cargo_qsp', version='2.0.0')
    bindings = model.input_bindings
    digest = bindings['context']['input_binding_hash']
    parameter = model.resolve_input_alias('parameters', 'source_symbol_15',
                                         expected_input_binding_hash=digest)
    state = model.resolve_input_alias('initial_states', 'closed_peripheral',
                                     expected_input_binding_hash=digest)
    assert parameter['default'] == {'value': 0.03, 'unit': '1'}
    assert parameter['fixed'] is False
    assert state['native_name'] == 'source_symbol_1' and state['unit'] == '1'
    copy = model.research_copy('balanced_gate_30nmol_iv', expected_input_binding_hash=digest)
    original = json.loads(json.dumps(copy.request))
    copy.set_parameter('source_symbol_15', 0.06, expected_input_binding_hash=digest)
    copy.set_initial_state('closed_peripheral', 2, expected_input_binding_hash=digest)
    assert copy.request['parameters']['source_symbol_15'] == {'value': 0.06, 'unit': '1'}
    assert copy.request['initial_states']['source_symbol_1'] == {'value': 2.0, 'unit': '1'}
    assert copy.request['regimen'] == original['regimen']
    assert all(value == copy.request['initial_states'][name]
               for name, value in original['initial_states'].items() if name != 'source_symbol_1')
    try:
        model.research_copy('balanced_gate_30nmol_iv', expected_input_binding_hash='sha256:' + '0' * 64)
    except InputBindingError as error:
        assert error.diagnostic['code'] == 'input_bindings_changed'
        assert error.diagnostic['migration'] == 'inspect_current_bindings'
    else:
        raise AssertionError('A stale binding context must be refused')
    output = Path(args.output_dir)
    saved = copy.save(output / 'inputs')
    provenance = json.loads((saved / 'provenance.json').read_text())
    assert provenance['input_binding_hash'] == digest
    assert json.loads((saved / 'input-bindings.json').read_text()) == bindings
    print('2.0.0 source_symbol_15 0.03 -> 0.06; closed_peripheral -> source_symbol_1 = 2; native unit 1')
    print('Saved four input files; stale context refused')
    if args.inspect_only:
        print('Inspection only; no simulation performed')
        return
    result = copy.run()
    peripheral = next(row for row in result['states'] if row['name'] == 'closed_peripheral')
    assert len(result['times']) == 57
    assert result['times'][0] == 0 and peripheral['values'][0] == 2
    assert peripheral['unit'] == '1'
    assert result['effective_request'] == copy.request and result['research_copy'] is True
    assert result['dimensional_qualification'] is False
    model.write_csv(result, output / 'trajectory.csv', all_readouts=True)
    table = read_table(output / 'trajectory.csv')
    assert table['manifest']['inputs']['effective_request'] == copy.request
    print(len(result['times']), 'rows; peripheral starting value 2; CSV and manifest preserve the effective request')


if __name__ == '__main__':
    main()
