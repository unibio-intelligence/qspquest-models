# Explore the rat AAV brain model

[Choose a model](../MODEL_CATALOG.md) · [Change an input](change-inputs.md) · [Technical reference](model-format.md)

These examples use the full rat adeno-associated virus (AAV) brain model
[`qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp`](../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.2.0/MODEL_CARD.md).
Complete [Python setup](../README.md#setup), including the engine, and run each
example from the library checkout (the output-inspection example does not need
the engine). Read [Change an input](change-inputs.md) first for the general
research-copy workflow.

## Select a coupled serotype preset

The model has separate AAV5 and AAV9 presets. Each preset sets its serotype
parameters and receptor starting values together:

```sh
python - <<'SEROTYPE'
from qspquest_models import Library

model = Library('.').load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
for scenario in ('icm_5e12_aav5', 'icm_5e12_aav9'):
    copy = model.research_copy(scenario)
    print(scenario, copy.initial_states['aav_brain_p_cm_r'])
    result = model.run(scenario)
    print(result['model_version'], len(result['times']),
          result['dimensional_qualification'])
SEROTYPE
```

Expect receptor values of `2e15` for AAV5 and `6.6e13` for AAV9, each with unit
`1`. Both runs report version `2.2.0`, 101 rows and `False` for dimensional
qualification (units not independently checked).

The presets start at -1000 h and dose at 0 h. Receptor-total parameters only set
starting values; they do not appear in the rate (derivative) equations. Changing one alone
does not reset the receptors or switch serotype. Use the named preset, or edit
all linked starting states yourself.

## Inspect the rat model's source interpretation before running

Purpose: see how this model's lymph binding differs from the equations printed
in the paper:

```sh
python - <<'LYMPH'
from qspquest_models import Library

model = Library('.').load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
record = model.source_interpretations
assert record['archive_sha256'] == model.archive_sha256
choice = next(e for e in record['entries'] if e['id'] == 'lymph-binding-locality')
print(choice['source_locator'])
print('printed:', ', '.join(choice['printed_coordinates']))
print('adopted:', ', '.join(choice['adopted_coordinates']))
print('author code:', record['author_code_qualification'])
result = model.run('figure3_mab_iv_3mgkg')
print(model.index['model_version'], len(result['times']), 'rows')
model.write_csv(result, 'lymph-source.csv')
from qspquest_models import read_table
saved = read_table('lymph-source.csv')
print(saved['manifest']['model']['provenance']['source_interpretations']['entries'][0]['id'])
LYMPH
```

Expected: printed coordinates `mab_plasma, target_plasma, complex_plasma`;
adopted coordinates `mab_lymph, target_lymph, complex_lymph`; author-code status
`not_assessed`; version `2.2.0`, `253 rows` and `lymph-binding-locality`.
The CSV's `.manifest.json` records this choice. Use a new filename if that pair
already exists; files are never overwritten.

In the source paper's supplement, equations 134-136 (page 32) use plasma concentrations for both plasma
and lymph binding. This model uses local lymph concentrations instead. A model
that follows the printed equations literally is not wrong for that reason alone.

The record lists selected choices, not every assumption in the paper.
`source_interpretations is None` means no record exists; it does not mean the
model reproduces the paper exactly. Standalone `load_archive` includes a record
only when you pass one explicitly. Discovery JSON shows the same record; the MCP
interface states the choice in `metadata.limitations`. Units, whole-body mass
balance and clinical use have not been checked.

## Change protein barriers without changing vector barriers

Purpose: simulate a protein intervention at the blood–brain barrier (BBB) and the
blood–cerebrospinal fluid barrier (BCSFB) in the full rat model while keeping the AAV vector inputs. No animal data is needed.

The four reflection inputs are dimensionless numbers between 0 and 1:

| Input | Affected modality | Default |
| --- | --- | ---: |
| `sigma_vector_bbb` | AAV vector at BBB | 0.9975 |
| `sigma_vector_bcsfb` | AAV vector at BCSFB | 0.9973 |
| `sigma_protein_bbb` | mAb, TargetX and complex at BBB | 0.9975 |
| `sigma_protein_bcsfb` | mAb, TargetX and complex at BCSFB | 0.9973 |

The protein inputs act on the monoclonal antibody (mAb), TargetX and complex together; they cannot
target TargetX alone. `model.parameter_effects` lists what each input affects.
`copy.parameters` shows editable inputs with their values and units;
`set_parameter` keeps the unit and rejects unknown names, fixed inputs, non-finite
values and out-of-range values. Changing parameters does not recompute linked
starting states (see the serotype section above).

```sh
python - <<'BARRIERS'
from qspquest_models import Library, read_table

model = Library('.').load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
scenario = 'icm_5e12_aav9'
baseline = model.run(scenario)
copy = model.research_copy(scenario)
for name in ('sigma_protein_bbb', 'sigma_protein_bcsfb'):
    print(name, copy.parameters[name], model.parameter_effects[name]['affected_modalities'])
    copy.set_parameter(name, 0.98)
protein_only = copy.run()
assert copy.parameters['sigma_vector_bbb']['value'] == 0.9975
assert copy.parameters['sigma_vector_bcsfb']['value'] == 0.9973
assert protein_only['times'] == baseline['times']
reference = {s['name']: s['values'] for s in baseline['states']}
vector_states = [s for s in protein_only['states'] if s['name'].startswith('aav_')]
assert len(vector_states) == 364
for state in vector_states:
    assert all(abs(a-b) <= 1e-18 + 1e-6 * abs(b)
               for a, b in zip(state['values'], reference[state['name']]))
print(model.index['model_version'], '364 vector states preserved', len(baseline['times']), 'rows')
for label, result in [('baseline', baseline), ('protein-only', protein_only)]:
    values = {o['name']: o['values'][-1] for o in result['outputs']}
    print(label, 'final ISF mAb:', round(values['mab_isf_nM'], 4),
          'final CSF target percentage:', round(values['target_csf_pct_baseline'], 4))
model.write_csv(protein_only, 'protein-barrier.csv', all_readouts=True)
table = read_table('protein-barrier.csv')
assert table['manifest']['inputs']['effective_request']['parameters']['sigma_protein_bbb']['value'] == 0.98
assert table['manifest']['inputs']['effective_request']['parameters']['sigma_vector_bbb']['value'] == 0.9975
assert table['manifest']['qualification']['qualified'] is False

# A shared perturbation explicitly names every affected modality.
shared = model.research_copy(scenario)
for name in ('sigma_vector_bbb', 'sigma_vector_bcsfb',
             'sigma_protein_bbb', 'sigma_protein_bcsfb'):
    shared.set_parameter(name, 0.98)
shared_result = shared.run()
print('Shared perturbation affects AAV, mAb, TargetX and complex')
model.write_csv(shared_result, 'shared-barrier.csv')
BARRIERS
```

Expect version `2.2.0`, 101 rows and `364 vector states preserved`. The final simulated
brain interstitial fluid (ISF) mAb readout is about **8.5530** at baseline and **9.8047** with the protein-only
override; the final cerebrospinal fluid (CSF) TargetX percentage readout is about **88.3685** and
**121.3294**, respectively. Lowering reflection changes both antibody and target
transport, so stronger target suppression is not guaranteed. These are exploratory
simulated values; a percentage above 100 is relative to the model's baseline value and
has not been checked against physiology. The vector states stay the same within
solver rounding (absolute tolerance `1e-18`, relative tolerance `1e-6`). Keep each
CSV with its `.manifest.json`, which records the inputs used.

An agent using the Model Context Protocol (MCP) can inspect these inputs with `get_model`, then use this complete
`simulate` arguments object for the same protein-only request:

```json
{
  "model": {"scenario": {
    "model_id": "qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp",
    "scenario_id": "icm_5e12_aav9"
  }},
  "parameters": {
    "sigma_protein_bbb": {"value": 0.98, "unit": "1"},
    "sigma_protein_bcsfb": {"value": 0.98, "unit": "1"}
  },
  "outputs": ["aav_brain_Vg_mL", "mab_isf_nM", "target_csf_pct_baseline"]
}
```

For this large model, `parameters_used` only gives a count. To confirm all four
barrier values, open the full result linked in the response and check
`effective_request.parameters`. For a shared intervention, add both vector
parameters too. Values outside 0–1 are rejected before the run.
The older `sigma_bbb`/`sigma_bcsfb` names (native `source_symbol_872`/`source_symbol_873`)
no longer work in this version. Use the four names above, or load the older
archive version for an old request.

## Inspect analytes and compartments before choosing outputs

Purpose: distinguish vector, antibody and target readouts, and identify the CSF
compartment represented by each column. This example does not need the engine.

```sh
python - <<'SEMANTICS'
from qspquest_models import Library

model = Library('.').load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp')
outputs = model.output_semantics
assert outputs['aav_brain_Vg_mL']['analyte'] == 'aav_vector'
assert outputs['mab_isf_nM']['analyte'] == 'anti_targetx_mab'
assert outputs['mab_isf_nM']['compartment'] == 'brain_interstitial_fluid'
assert outputs['target_csf_pM']['compartment'] == 'cisterna_magna_csf'
assert outputs['target_lv_pM']['compartment'] == 'brain_lateral_ventricle_csf'
for name in ('aav_brain_Vg_mL', 'mab_isf_nM', 'target_csf_pM', 'target_lv_pM'):
    column = outputs[name]
    print(name, column['analyte'], column['compartment'], column['returned_unit'])
assert all(column['returned_unit'] == '1' for column in outputs.values())
print(model.index['model_version'], '24 biological output identities declared')
SEMANTICS
```

Expect version `2.2.0`, the four analyte/compartment pairs above and returned unit
`1`. The `*_csf_*` readouts represent cisterna magna, rather than every CSF
compartment. The `*_lv_*` readouts represent lateral-ventricle CSF. Tissue
aggregates sum only the states named in their expressions; they are not
single-compartment concentrations. The `mab` and `target` readouts exclude
mAb–TargetX complex states.

An analyte or compartment that is not declared is `None`; do not guess it from the
column name. These labels do not change values or convert units: a suffix such as
`nM` does not make unit `1` a concentration. The [model card](../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.2.0/MODEL_CARD.md)
lists every readout and its limits.

