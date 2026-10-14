# Lobet 2026 panitumumab body-composition PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore panitumumab exposure with body-composition covariates.

**Runnable · 2 experiments.** Version 0.1.0.

## Run an experiment

Deterministic typical-subject ODE using median 62 kg body weight and Table 2 fixed effects; paper AUC0-14 median/range is carried as comparator data.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_lobet_2026_panitumumab_body_composition_poppk', version='0.1.0')
result = model.run('ffcd0904-typical-3mgkg-q2w-ode-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-anchor` | No-dose exact replay of Table 1, Table 2, Supplement Table S1, and Results scalar values. | 0–0.001 h | 2 |
| `ffcd0904-typical-3mgkg-q2w-ode-overlay` | Deterministic typical-subject ODE using median 62 kg body weight and Table 2 fixed effects; paper AUC0-14 median/range is carried as comparator data. | 0–70 h | 281 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_l` | Panitumumab concentration | `1` |
| `auc_mg_day_l` | Accumulated panitumumab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_lobet_2026_panitumumab_body_composition_poppk --model-version 0.1.0 --scenario ffcd0904-typical-3mgkg-q2w-ode-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 9 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `auc_mg_day_l` | `1` |
| `central_conc_mg_l` | `1` |
| `dose_mg` | `1` |
| `linear_elimination_mg_day` | `1` |
| `michaelis_menten_elimination_mg_day` | `1` |
| `paper_auc0_14_median_mg_day_l` | `1` |
| `paper_auc0_14_p05_mg_day_l` | `1` |
| `paper_auc0_14_p95_mg_day_l` | `1` |
| `peripheral_conc_mg_l` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `ffcd0904-typical-3mgkg-q2w-ode-overlay` starter has **281 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_l` | 74.1036 | 0.0547415 (14 h, pre) | 74.1036 (0 h, post) | 1.91396 |
| `auc_mg_day_l` | 0 | 0 (0 h, post) | 1462.26 (70 h, pre) | 1462.26 |

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
Evidence identity: `sha256:b82d16a1b7ff34fa52a01d7cb36e9394b6b7fa377d5dc78c2da773addeee3e9a`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Two-compartment panitumumab PopPK model with parallel linear and Michaelis-Menten elimination from the FFCD0904 anal SCC body-composition ancillary study.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
