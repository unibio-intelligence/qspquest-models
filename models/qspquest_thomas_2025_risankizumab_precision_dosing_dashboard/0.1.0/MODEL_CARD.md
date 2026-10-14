# Thomas 2025 risankizumab precision-dosing dashboard

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect fixed risankizumab exposure; this is not a clinical dosing service.

**Source replay available; dynamic simulation unavailable · 2 unavailable.** Version 0.1.0.

## Run an experiment

Replays Thomas 2025 paper metrics, Table 1/Table 2 values, model-performance metrics, and the median dosing-interval equation.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_thomas_2025_risankizumab_precision_dosing_dashboard', version='0.1.0')
result = model.run('dashboard-exact-replay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `dashboard-exact-replay` | Replays Thomas 2025 paper metrics, Table 1/Table 2 values, model-performance metrics, and the median dosing-interval equation. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `source__CL_L_day` | Retained reference clearance, constant source value | `L/day` |
| `source__target_average_concentration_mg_l` | Retained dashboard concentration target, constant source value | `mg/L` |
| `source__dashboard_dose_mg` | Retained dashboard dose, constant source value | `mg` |

**This starter is a source replay.** Its retained values are constant or short source checks.
No qualified dynamic simulation is available in this version. Zero drug states do not demonstrate a treatment response.

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_thomas_2025_risankizumab_precision_dosing_dashboard --model-version 0.1.0 --scenario dashboard-exact-replay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__AUC_mg_day_L` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `dashboard-exact-replay` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `source__CL_L_day` | 0.243 | 0.243 (0 d, post) | 0.243 (0 d, post) | 0.243 |
| `source__target_average_concentration_mg_l` | 5.4 | 5.4 (0 d, post) | 5.4 (0 d, post) | 5.4 |
| `source__dashboard_dose_mg` | 150 | 150 (0 d, post) | 150 (0 d, post) | 150 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**2 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

<details>
<summary>Availability and qualification</summary>

Execution: `source_replay`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:7719bd9400ee5fb0e3fda29a88c1371dedb86ec59781d43303a895e5ff159cc0`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Dashboard-layer ODE/exact replay for Thomas et al. 2025 risankizumab model-informed precision dosing in psoriasis. The executable PK uses the Suleiman 2019 two-compartment risankizumab PopPK model selected by Thomas, and the dashboard interval rule is replayed from the Thomas paper.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
