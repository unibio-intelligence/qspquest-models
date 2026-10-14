# Pasquiers 2025 rituximab ANCA/gammaglobulin PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore rituximab exposure, ANCA and gammaglobulin dynamics.

**Runnable · 5 experiments.** Version 0.1.0.

## Run an experiment

Full ODE fixed-effect induction simulation with Table 3/S1 PR3 paper endpoints overlaid.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_pasquiers_2025_rituximab_anca_gammaglobulin_pkpd', version='0.1.0')
result = model.run('induction-1000mg-d0-d14-6mo-pr3')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-article-supplement-table-anchor` | No-dose exact replay of Pasquiers 2025 Tables 1-4, Supplement Tables S1-S2, model equations, and source-audit counts. | 0–1 d | 2 |
| `induction-1000mg-d0-d14-6mo-pr3` | Full ODE fixed-effect induction simulation with Table 3/S1 PR3 paper endpoints overlaid. | 0–180 d | 183 |
| `induction-375mgm2-q1w-6mo-mpo` | Full ODE fixed-effect induction simulation with Table 3/S1 MPO paper endpoints overlaid. | 0–180 d | 185 |
| `maintenance-1000mg-q4m-24mo-pr3` | Full ODE fixed-effect maintenance simulation with Table 4/S1 PR3 paper endpoints overlaid. | 0–720 d | 368 |
| `maintenance-500mg-q6m-24mo-mpo` | Full ODE fixed-effect maintenance simulation with Table 4/S1 MPO paper endpoints overlaid. | 0–720 d | 366 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__rtx_central_mg` | Rituximab amount in the central compartment | `mg` |
| `state__anca_blood_u_ml` | Circulating ANCA antibody level | `U/mL` |
| `state__gg_g_l` | Gammaglobulin concentration | `g/L` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_pasquiers_2025_rituximab_anca_gammaglobulin_pkpd --model-version 0.1.0 --scenario induction-1000mg-d0-d14-6mo-pr3 --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__anca_blood_u_ml` | `U/mL` |
| `state__anca_prod_u_ml` | `U/mL` |
| `state__auc_rtx_mg_day_l` | `mg*day/L` |
| `state__gg_g_l` | `g/L` |
| `state__rtx_central_mg` | `mg` |
| `state__rtx_peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `induction-1000mg-d0-d14-6mo-pr3` starter has **183 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__rtx_central_mg` | 0 | 0 (0 d, post) | 1311.29 (14.0417 d, pre) | 30.9422 |
| `state__anca_blood_u_ml` | 75.6 | 10.5066 (180 d, pre) | 75.6 (0 d, post) | 10.5066 |
| `state__gg_g_l` | 9.35 | 7.00395 (171 d, post) | 9.35 (0 d, post) | 7.00867 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:f05b950404c8943c085bb129eda2f473f245fbcca94d65529a0790dd4b4a3aa9`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-complete fixed-effect ODE reconstruction of the Pasquiers et al. 2025 real-world rituximab PK/PD model in ANCA-associated vasculitis. Runtime includes two-compartment rituximab PK, indirect gammaglobulin turnover inhibited by rituximab, and the Bensalem/Friberg ANCA production-blood feedback model. Exact API anchors replay the public article and supplement tables; dynamic regimen scenarios attach paper final-model simulation endpoints as overlays. Exact 1000-virtual-patient Monolix parity is source-limited because random-effect draws, patient data, and source simulation outputs are not public.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
