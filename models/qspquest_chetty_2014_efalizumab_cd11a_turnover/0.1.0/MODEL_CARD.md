# Efalizumab-driven CD11a turnover

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore how efalizumab changes CD11a turnover.

**Runnable · 6 experiments.** Version 0.1.0.

## Run an experiment

Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_chetty_2014_efalizumab_cd11a_turnover', version='0.1.0')
result = model.run('moderate-driver')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `drug-free` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |
| `high-driver` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |
| `low-driver` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |
| `moderate-driver` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |
| `qss-half-occupancy` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |
| `washout-recovery` | Mechanistic constant-input probe; effect-site matrix must be specified by the user. No original virtual cohort or clinical regimen is implied. | 0–672 h | 337 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `free_cd11a_pct` | Free CD11a as a percentage of baseline | `1` |
| `occupancy_pct` | Percentage of CD11a occupied by drug | `1` |
| `total_cd11a_pct` | Total CD11a as a percentage of baseline | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_chetty_2014_efalizumab_cd11a_turnover --model-version 0.1.0 --scenario moderate-driver --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 6 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `bound_cd11a` | `1` |
| `free_cd11a` | `1` |
| `free_cd11a_pct` | `1` |
| `occupancy_pct` | `1` |
| `target_balance` | `1` |
| `total_cd11a_pct` | `1` |
| `state__complex_loss_total` | `umol/L` |
| `state__elapsed_h` | `hour` |
| `state__free_loss_total` | `umol/L` |
| `state__synthesis_total` | `umol/L` |
| `state__target_total` | `umol/L` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `moderate-driver` starter has **337 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `free_cd11a_pct` | 7.85838 | 1.55328 (264 h, post) | 7.85838 (0 h, post) | 1.55328 |
| `occupancy_pct` | 92.1416 | 92.1416 (0 h, post) | 92.1416 (0 h, post) | 92.1416 |
| `total_cd11a_pct` | 100 | 19.7659 (264 h, post) | 100 (0 h, post) | 19.7659 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
