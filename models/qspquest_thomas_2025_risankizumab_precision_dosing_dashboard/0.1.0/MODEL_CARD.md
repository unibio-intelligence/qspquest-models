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

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `dashboard-exact-replay` | Replays Thomas 2025 paper metrics, Table 1/Table 2 values, model-performance metrics, and the median dosing-interval equation. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `source__CL_L_day` | Retained reference clearance, constant source value | `L/day` |
| `source__target_average_concentration_mg_l` | Retained dashboard concentration target, constant source value | `mg/L` |
| `source__dashboard_dose_mg` | Retained dashboard dose, constant source value | `mg` |

**This starter is a source replay.** Its values are stored constants or short checks from the source.
This version cannot simulate over time. Zero drug states do not show a treatment response.

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

| Technical column | Unit |
| --- | --- |
| `state__AUC_mg_day_L` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `dashboard-exact-replay` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `source__CL_L_day` | 0.243 | 0.243 (0 d, post) | 0.243 (0 d, post) | 0.243 |
| `source__target_average_concentration_mg_l` | 5.4 | 5.4 (0 d, post) | 5.4 (0 d, post) | 5.4 |
| `source__dashboard_dose_mg` | 150 | 150 (0 d, post) | 150 (0 d, post) | 150 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) was produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

**2 experiments cannot be simulated.** See [why they are unavailable](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
