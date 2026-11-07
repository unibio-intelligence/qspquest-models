# Compare experiments and change an input

[Choose a model](../MODEL_CATALOG.md) · [Understand results](understand-results.md) · [Technical reference](model-format.md)

Start by comparing existing experiments: their inputs and expected results are
already supplied. For a condition outside those experiments, make a research copy
of the input request. The example below changes a single bolus in the synthetic
cargo model from 30 to 15 source dose units.

To pick an exact version or look up input names and units, see the
[input-binding tutorial](input-bindings.md).

To switch the Yuan model between the paper's rounding conventions, see the
[source precision profile tutorial](precision-profiles.md). For serotype presets,
barrier inputs and output identities in the rat AAV model, see
[Explore the rat AAV brain model](rat-aav-brain-model.md).

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

Expected simulated values at 24 h are approximately **37.65** with the tumor gate and **1.37**
without it. The [QSP tutorial](qsp-gated-cargo.md) plots both tumor and central occupancy.

## Change the dose in a research copy

Continue in the same Python session. `research_copy` copies an experiment so you
can change one dose and rerun it with the same outputs. Dose indexes start at zero. `copy.doses` shows the amounts and units
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
`provenance.json`, which record what you changed. Results from a copy are marked
`research_copy: true`. The original experiment is unchanged.

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

At 24 h, the 30-unit dose gives a simulated tumor occupancy of about **37.65%** and the
15-unit dose about **21.85%**. Occupancy need not scale linearly with dose.
Experiment names say nmol, but the stored dose has unit `1`: the engine uses the
source's number as-is and converts nothing, and a physical unit such as `nmol`
is refused for this input. This example does not check units or biological
efficacy.

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

The value uses the same scale as the stored model. In R, pass
`initial_states = c(C = 175.40808349401845)` to `models$run()`. In the CLI, use
`--initial C=175.40808349401845`.

Stored reference results cover only the original experiments, not your edits. See
[archive editing](model-format.md#research-copies) if you plan to contribute a new
library version.

## Inspect a lanadelumab dose and its PK units

Purpose: check how the dose is entered in this pharmacokinetic (PK) model and distinguish a dose amount from a plasma
concentration. Complete the [Python setup](../README.md#setup), including the
QSPQuest engine, and run from the library root:

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
The schedule has 13 doses; the first is at 3016 h, after the source's preparation
period. `set_dose` keeps the mg unit, so a 150 mg dose is entered as 150. mg/L and
ug/mL give the same number, so do not multiply the dose by 1000; a concentration
is not a dose amount. With the model's molecular mass of 150000 g/mol, multiply
ug/mL by `1e6 / 150000` to get nmol/L. Other contact-system readouts have unit
`1`; their names do not make them physical concentrations. This example is not
for population fitting or clinical use.
