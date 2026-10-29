# Ortiz 2024 ravulizumab NMOSD PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore endpoint-constrained ravulizumab exposure and free-C5 response.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation for the Body weight 60 to <100 kg ravulizumab dosing tier, calibrated to Table 3 week-50 Cmax/Ctrough means and the reported free-C5 day-1 median.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_ortiz_2024_ravulizumab_nmosd_pkpd', version='0.1.0')
result = model.run('week50-60-100-pk-free-c5-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `article-ema-exact-anchor` | No-dose scenario exposing article Table 1-3, assay, immunogenicity, free-C5, dosing, and EMA label constants for exact replay. | 0–1 h | 2 |
| `week50-40-60-pk-free-c5-ode` | Full ODE simulation for the Body weight 40 to <60 kg ravulizumab dosing tier, calibrated to Table 3 week-50 Cmax/Ctrough means and the reported free-C5 day-1 median. | 0–352 h | 353 |
| `week50-60-100-pk-free-c5-ode` | Full ODE simulation for the Body weight 60 to <100 kg ravulizumab dosing tier, calibrated to Table 3 week-50 Cmax/Ctrough means and the reported free-C5 day-1 median. | 0–352 h | 353 |
| `week50-ge100-pk-free-c5-ode` | Full ODE simulation for the Body weight >=100 kg ravulizumab dosing tier, calibrated to Table 3 week-50 Cmax/Ctrough means and the reported free-C5 day-1 median. | 0–352 h | 353 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__central_mg` | Ravulizumab amount in the central compartment | `mg` |
| `state__free_c5_ug_ml` | Free complement C5 concentration | `ug/mL` |
| `state__auc_ug_day_ml` | Accumulated central drug exposure | `ug*day/mL` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_ortiz_2024_ravulizumab_nmosd_pkpd --model-version 0.1.0 --scenario week50-60-100-pk-free-c5-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__auc_ug_day_ml` | `ug*day/mL` |
| `state__central_mg` | `mg` |
| `state__free_c5_ug_ml` | `ug/mL` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `week50-60-100-pk-free-c5-ode` starter has **353 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 2700 | 2101.6 (15 h, pre) | 5341.42 (352 h, pre) | 5341.42 |
| `state__free_c5_ug_ml` | 120.1 | -3.55252e-12 (5 h, post) | 120.1 (0 h, post) | -7.06466e-53 |
| `state__auc_ug_day_ml` | 0 | 0 (0 h, post) | 425935 (352 h, pre) | 425935 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
