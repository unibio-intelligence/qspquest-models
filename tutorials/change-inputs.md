# Compare experiments and change an input

[Choose a model](../MODEL_CATALOG.md) · [Understand results](understand-results.md) · [Technical reference](model-format.md)

Start by comparing existing experiments: their inputs and expected results are
already supplied. For a condition outside those experiments, make a research copy
of the input request. The example below changes a single bolus in the synthetic
cargo model from 30 to 15 source dose units.

For exact version selection, parameter and state aliases, native units and stale
context recovery, run the [input-binding tutorial](input-bindings.md).

For complete source rounding conventions in the Yuan model, use the
[source precision profile tutorial](precision-profiles.md).

## Compare two existing conditions

Complete [setup](../README.md#setup), then run from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_ubi_2026_target_gated_cargo_qsp')
for scenario in ['balanced_gate_30nmol_iv', 'no_tumor_gate_30nmol_iv']:
    result = model.run(scenario)
    column = next(c for c in result['outputs']
                  if c['name'] == 'tumor_receptor_occupancy_percent')
    at_24h = result['times'].index(24.0)
    print(scenario, round(column['values'][at_24h], 2))
```

Expected values at 24 h are approximately **37.65** with the tumor gate and **1.37**
without it. The [QSP tutorial](qsp-gated-cargo.md) plots both tumor and central occupancy.

## Change the dose in a research copy

Continue in the same Python session. The supported helper copies the verified
request, changes one scheduled dose and runs through the same engine and familiar
readout names. Dose indexes start at zero. `copy.doses` shows the amounts and units
before editing.

```python
copy = model.research_copy('balanced_gate_30nmol_iv')
print(copy.doses[0]['amount'])  # {'unit': '1', 'value': 30.0}
copy.set_dose(0, 15.0)
changed = copy.run()
model.write_csv(changed, 'dose15.csv')
copy.save('research-output/dose15')  # choose a new directory for each saved copy

from qspquest_models import result_columns
for label, result in [('dose30', model.run('balanced_gate_30nmol_iv')),
                      ('dose15', changed)]:
    column = next(c for c in result_columns(result)
                  if c['name'] == 'tumor_receptor_occupancy_percent')
    at_24h = result['times'].index(24.0)
    print(label, 'tumor occupancy at 24 h:', column['values'][at_24h])
```

`copy.save()` writes `model.json`, `request.json`, `input-bindings.json` and
`provenance.json`, including the inspected input-binding hash,
the base archive checksum and edited request checksum. Research results carry
`research_copy: true` and identify the original preset. The original preset and
archive keep their original inputs.

### Use the same interface from R

Complete [R setup](r-quickstart.md), then:

```r
source('tutorials/qspquest-models.R')
models <- qspquest_library(getwd())
model <- 'qspquest_ubi_2026_target_gated_cargo_qsp'
scenario <- 'balanced_gate_30nmol_iv'
models$inputs(model, scenario)$doses[[1]]$amount
changed <- models$run(model, scenario, dose_index = 0, dose_amount = 15,
                      save_research = 'research-output/r-dose15', csv = 'r-dose15.csv')
trajectory <- qspquest_data_frame(changed)
saved <- qspquest_read_table('r-dose15.csv')
stopifnot(nrow(saved) == nrow(trajectory))
trajectory$tumor_receptor_occupancy_percent[trajectory$time == 24]
```

### Use the CLI

```sh
python -m qspquest_models --library . --model qspquest_ubi_2026_target_gated_cargo_qsp \
  --scenario balanced_gate_30nmol_iv --inputs
python -m qspquest_models --library . --model qspquest_ubi_2026_target_gated_cargo_qsp \
  --scenario balanced_gate_30nmol_iv --dose 0=15 --csv cli-dose15.csv \
  --save-research research-output/cli-dose15
```

At 24 h, the 30-unit result is about **37.65%** tumor occupancy and the
15-unit result is about **21.85%** in the source scale. The smaller dose explores
dose dependence under the same synthetic assumptions;
occupancy need not scale linearly with dose. The dose names use the source's
nmol convention, while the native request uses numerical coordinates with unit
label `1`. This exercise does not establish physical-unit validity or biological efficacy.

Inspect the saved requests to confirm the intended change. When studying another
model, identify how its dose is represented first: for example, the rituximab
quickstart encodes its starting dose in the initial concentration. Inspect and edit
that state by its biological name instead:

```python
rituximab = Library('.').load('qspquest_serkland_2025_rituximab_ms_pkpd')
copy = rituximab.research_copy('population-typical-1000mg-full-ode')
print(copy.initial_states)
copy.set_initial_state('C', 175.40808349401845)  # half the original concentration
changed = copy.run()
```

The state value uses the archived numerical scale. In R, pass
`initial_states = c(C = 175.40808349401845)` to `models$run()`. In the CLI, use
`--initial C=175.40808349401845`. Summary-only models reject research copies because
editing a retained source replay would not provide a qualified dynamic simulation.

These research results apply to your edited inputs. The library's stored comparisons
cover the original named experiments. See [archive editing](model-format.md#research-copies)
if you intend to contribute a new library version.

## Select a coupled serotype preset

Complete the Python setup above and run from the library checkout. The full rat
AAV model supplies separate AAV5 and AAV9 presets. Each preset includes its
serotype parameters and receptor starting values as one versioned experiment:

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

Expect receptor values of `2e15` for AAV5 and `6.6e13` for AAV9, each with native
unit `1`. Both runs report version `2.1.2`, 101 observation rows and physical
qualification `False`. These are numerical source coordinates; the receptor
values retain the source concentration convention and require the documented
interpretation boundaries.

The presets retain equilibration from -1000 h before dosing at 0 h. Receptor-total
parameters are initialization inputs and are absent from the derivative
equations. Editing one such parameter alone does not reinitialize receptors or
represent a serotype change. Select the named preset, or explicitly edit all
coupled initial states for a declared research experiment. Edited research
requests do not inherit physical or scientific qualification.

## Inspect the rat model's source interpretation before running

Purpose: distinguish the adopted local lymph binding rule from the printed
plasma-coordinate rule before using this model. Complete the setup above and
run from the library checkout with the built engine selected.

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
`not_assessed`; version `2.1.2`, `253 rows` and `lymph-binding-locality`.
The CSV and its `.manifest.json` preserve the selected source interpretation
with the run identity. Use a new output directory or filename if that pair
already exists; the exporter refuses to replace either file.
Equations 134-136 on supplement
page 32 print plasma concentrations for both plasma and lymph binding. The
selected archive evaluates the reaction with local concentrations. These are
different source conventions; a literal reconstruction is not a scientific
failure solely for that choice.

The record is bound to the exact archive and native model hashes. Its entries
cover selected disclosed choices, rather than every source assumption.
`source_interpretations is None` means no record is available; it does not mean
literal source reproduction or complete scientific qualification. Standalone
`load_archive` calls carry an interpretation only when one is explicitly passed
and validated. Discovery JSON exposes the same `source_interpretations` record;
the compact MCP model interface states the choice in `metadata.limitations`.
Read the source details and qualification limits before comparing conventions.
Physical units, whole-body conservation and clinical use remain unqualified.

## Change protein barriers without changing vector barriers

Purpose: explore a BBB/BCSFB protein intervention in the full rat model while
retaining the AAV vector inputs. Complete [Python setup](../README.md#setup),
including the standalone engine, and run this complete command from the library
checkout. It uses the archived synthetic input request; no animal data is needed.

The four reflection inputs are dimensionless numbers between 0 and 1:

| Input | Affected modality | Default |
| --- | --- | ---: |
| `sigma_vector_bbb` | AAV vector at BBB | 0.9975 |
| `sigma_vector_bcsfb` | AAV vector at BCSFB | 0.9973 |
| `sigma_protein_bbb` | mAb, TargetX and complex at BBB | 0.9975 |
| `sigma_protein_bcsfb` | mAb, TargetX and complex at BCSFB | 0.9973 |

The protein inputs deliberately group antibody, TargetX and complex. This is
not a TargetX-only intervention. `model.parameter_effects` discloses the affected
modalities, source locator and directly affected state equations. `copy.parameters`
shows mutable native input names, effective values and units; `set_parameter`
retains the archived unit and refuses unknown names, fixed inputs, nonfinite
values and declared out-of-bounds values. Other parameter edits do not recompute
coupled initial states; follow the serotype initialization guidance above.

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

Expect version `2.1.2`, 101 rows and `364 vector states preserved`. The final
ISF mAb readout is about **8.5530** at baseline and **9.8047** with the protein-only
override; the final CSF TargetX percentage readout is about **88.3685** and
**121.3294**, respectively. Lowering reflection can change both antibody and
target transport, so stronger target suppression is not guaranteed. These are
source-scale exploratory predictions; a percentage above 100 is relative to the
retained baseline denominator and does not establish physiological validation.
Vector equations and coefficients are identical under the protein-only override;
adaptive solver rounding is checked with absolute tolerance `1e-18` and relative
tolerance `1e-6`. Keep each CSV with its `.manifest.json` sidecar to retain effective
inputs, source interpretation, archive identity and qualification limits.

An MCP agent can inspect these inputs with `get_model`, then use this complete
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

For this large model `parameters_used` is a count summary. Read the complete
result resource linked by the response and inspect its `effective_request.parameters`
to confirm all four effective barrier inputs, including retained vector defaults. For a shared intervention add both vector
parameters explicitly. A unit of `1` here is the retained source numerical
coordinate; it does not grant physical qualification to the other quantities.
The old ambiguous `sigma_bbb`/`sigma_bcsfb` names and their prior native
`source_symbol_872`/`source_symbol_873` names are unavailable in this version.
Use the four explicit names; use an exact pinned historical archive for an old
request. Values outside 0–1 fail before execution. Author-code reproduction,
physical units and whole-body conservation remain unqualified.

## Inspect analytes and compartments before choosing outputs

Purpose: distinguish vector, antibody and target readouts, and identify the CSF
compartment represented by each column. Complete the [Python setup](../README.md#setup)
and run this example from the library root. This inspection uses the Python
standard library and does not require an engine installation.

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

Expect version `2.1.2`, the four analyte/compartment pairs above and returned unit
`1`. The `*_csf_*` readouts represent cisterna magna, rather than every CSF
compartment. The `*_lv_*` readouts represent lateral-ventricle CSF. Tissue
aggregates contain only the states specified by the archived expressions;
they are not individual compartment concentrations. The `mab` and `target`
readouts exclude mAb–TargetX complex states.

An undeclared analyte or compartment is `None`. Do not invent an identity from
a column name. These declarations do not change numerical values or convert
units. A suffix such as `nM` does not qualify native unit `1` as a physical
concentration. Inspect the [model card](../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.1.2/MODEL_CARD.md)
for the complete declared readout inventory and qualification limits.

## Inspect a lanadelumab dose and its PK units

Purpose: verify the dose coordinate and distinguish an amount from a plasma
concentration. Complete the [Python setup](../README.md#setup), install the
QSPQuest engine using the documented CLI or Python route, and run from the
library root. The inspection uses only the Python standard library. Execution
uses the installed engine; no additional source files are required.

```sh
python - <<'PK_DOSE'
import math
from qspquest_models import Library

model = Library('.').load('qspquest_sexton_2024_lanadelumab_hae_kks_qsp')
contract = model.dose_contracts['PK_Amount_SC']
assert contract['native_target'] == 'source_symbol_0'
assert contract['amount_unit'] == contract['state_unit'] == contract['source_dose_unit'] == 'mg'
assert model.output_semantics['PK_Amount_SC']['returned_unit'] == 'mg'
assert model.output_semantics['PK_Conc_Central_in_ugml']['returned_unit'] == 'ug/mL'
assert model.output_semantics['PK_Conc_Central_in_nM']['returned_unit'] == 'nmol/L'
copy = model.research_copy(model.starter_scenario)
assert all(dose['amount'] == {'value': 150.0, 'unit': 'mg'} for dose in copy.doses)
copy.set_dose(0, 150.0)
result = copy.run()
columns = {column['name']: column for column in result['outputs']}
mass = columns['PK_Conc_Central_in_ugml']['values']
molar = columns['PK_Conc_Central_in_nM']['values']
assert all(math.isclose(n, c * 1e6 / 150000, rel_tol=1e-10, abs_tol=1e-10) for c, n in zip(mass, molar))
print(model.index['model_version'], contract['native_target'], '150 mg dose')
print(len(result['times']), 'rows; plasma units ug/mL and nmol/L')
PK_DOSE
```

Expect version `0.2.0`, target `source_symbol_0`, a `150 mg dose` and 147 rows.
The stored schedule contains 13 doses; its first dose occurs at 3016 h after the
source preparation period. `set_dose` retains the archived mg unit. A dose of
150 mg is 150 in this depot coordinate. Converting a mass concentration from
mg/L to ug/mL leaves its numerical value unchanged; do not multiply the dose by
1000. A concentration such as mg/L is not a dose amount. For the retained
150000 g/mol molecular mass, multiply ug/mL by `1e6 / 150000` to obtain nmol/L.
Other contact-system readouts retain native unit `1`; a unit-looking name does
not qualify them as physical concentrations. This workflow does not establish
population-fitting, complete publication reproduction or clinical use.
