"""Select complete Yuan source conventions and retain reproducible receipts."""
import argparse
import json
from pathlib import Path
from qspquest_models import Library, read_table


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library-dir', default='.')
    parser.add_argument('--engine-cli')
    parser.add_argument('--output-dir', default='research-output/precision-profiles')
    parser.add_argument('--inspect-only', action='store_true')
    args = parser.parse_args()
    model = Library(args.library_dir, executable=args.engine_cli).load(
        'qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.1')
    manifest = model.precision_profiles
    print('8 named profiles; 11 scenarios; 33 mutable parameters per condition')
    assert len(manifest['profiles']) == 8 and len(model.scenario_ids) == 11
    sid = 'mda_mb_468_duobody_6_86nm_et8'
    ids = [manifest['default_profile_id'], 'covariate_table_ii-geometric_eq1-exact_ln2']
    output = Path(args.output_dir)
    results = []
    for profile_id in ids:
        research = model.research_copy(sid, precision_profile_id=profile_id)
        receipt = research.precision_profile
        assert receipt['parameters_status'] == 'matches_profile'
        assert receipt['effective_parameters_sha256'] == receipt['profile_parameters_sha256']
        assert len(research.parameters) == 33
        research.request['regimen']['end'] = {'value': 72, 'unit': 'h'}
        research.request['regimen']['samples'] = []
        research.request['regimen']['observations'] = [
            {'time': {'value': t, 'unit': 'h'}, 'side': 'post'}
            for t in [0, .25, 2, 6, 12, 18, 24, 36, 48, 60, 72]]
        research.request['solver'] = 'diffsol_bdf'
        research.request['regimen']['rtol'] = 1e-10
        research.request['regimen']['atol'] = 1e-12
        research.save(output / profile_id / 'inputs')
        print(profile_id, receipt['effective_parameters_sha256'])
        if not args.inspect_only:
            result = research.run()
            assert len(result['times']) == 11
            assert result['precision_profile'] == research.precision_profile
            model.write_csv(result, output / profile_id / 'trajectory.csv', all_readouts=True)
            table = read_table(output / profile_id / 'trajectory.csv')
            assert table['manifest']['model']['provenance']['precision_profile'] == result['precision_profile']
            results.append(result)
    modified = model.research_copy(sid)
    modified.set_parameter('source_symbol_46', modified.parameters['source_symbol_46']['value'] * 2)
    assert modified.precision_profile['parameters_status'] == 'modified'
    try:
        model.research_copy(sid, precision_profile_id='invented')
    except ValueError:
        pass
    else:
        raise AssertionError('Unknown profiles must fail before execution')
    if results:
        assert results[0]['precision_profile']['effective_parameters_sha256'] != results[1]['precision_profile']['effective_parameters_sha256']
        assert results[0]['outputs'] != results[1]['outputs']
        print('2 runs; 11 time points each; complete profile receipts retained in paired CSV manifests')
    else:
        print('Inspection only; complete native inputs and profile receipts saved')
    print('Modified profile labelled; unknown profile refused')


if __name__ == '__main__':
    main()
