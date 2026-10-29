# Li 2024 rituximab pediatric INS B-cell repletion K-PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore B-cell recovery after rituximab in pediatric nephrotic syndrome.

**Runnable · 24 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation of 375 mg/m2 x2 weekly; paper comparator is Table 3 time to CD19+ B-cell repletion.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic', version='0.1.0')
result = model.run('standard-375mgm2-x2')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 24 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-table-anchor` | No-dose replay of article Table 1, Table 2, Table 3, text, and Supplementary Table S2/S3 values. | 0–0.001 d | 2 |
| `iga-max-two-weekly-375mgm2-x2` | Full ODE simulation of Two weekly 375 mg/m2 at high IgA; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `iga-median-two-weekly-375mgm2-x2` | Full ODE simulation of Two weekly 375 mg/m2 at median IgA; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `iga-min-two-weekly-375mgm2-x2` | Full ODE simulation of Two weekly 375 mg/m2 at low IgA; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `mini-six-monthly-100mg` | Full ODE simulation of Six monthly 100 mg; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `mini-six-monthly-100mg-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `mini-three-100mg-q2mo` | Full ODE simulation of Three 100 mg every 2 months; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `mini-three-100mg-q2mo-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `mini-three-150mg-q2mo` | Full ODE simulation of Three 150 mg every 2 months; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `mini-three-150mg-q2mo-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `mini-three-200mg-q2mo` | Full ODE simulation of Three 200 mg every 2 months; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `mini-three-200mg-q2mo-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `single-100mg` | Full ODE simulation of 100 mg x1; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `single-100mg-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `standard-375mgm2-x1` | Full ODE simulation of 375 mg/m2 x1; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `standard-375mgm2-x1-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `standard-375mgm2-x2` | Full ODE simulation of 375 mg/m2 x2 weekly; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `standard-375mgm2-x2-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `standard-375mgm2-x4` | Full ODE simulation of 375 mg/m2 x4 weekly; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `standard-375mgm2-x4-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `standard-750mgm2-x1` | Full ODE simulation of 750 mg/m2 x1; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `standard-750mgm2-x1-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |
| `standard-750mgm2-x2` | Full ODE simulation of 750 mg/m2 x2 weekly; paper comparator is Table 3 time to CD19+ B-cell repletion. | 0–365 d | 366 |
| `standard-750mgm2-x2-calibrated-endpoint-replay` | Exploratory/source-limited K-PD endpoint replay calibrated with an ED50 multiplier to match the public Table 3/Figure 5 CD19+ B-cell repletion endpoint. The original paper fixed-effect scenario is retained separately. | 0–365 d | 366 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__A1_mg` | Rituximab amount driving the kinetic PD model | `mg` |
| `state__cd19_cells_ul` | CD19-positive B-cell count during depletion and recovery | `cells/uL` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic --model-version 0.1.0 --scenario standard-375mgm2-x2 --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 1 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `validation_run_nonce` | `1` |
| `state__A1_mg` | `mg` |
| `state__cd19_cells_ul` | `cells/uL` |
| `state__elapsed_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `standard-375mgm2-x2` starter has **366 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__A1_mg` | 307.5 | 1.26578e-05 (365 d, pre) | 500.575 (8 d, post) | 1.26578e-05 |
| `state__cd19_cells_ul` | 591.429 | 1.51377 (13 d, post) | 591.429 (0 d, post) | 471.117 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
