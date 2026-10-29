# Hemperly 2025 infliximab pediatric IBD PK/ER

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore pediatric infliximab exposure and IBD response summaries.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect two-compartment IV ODE using the reported pediatric reference weight and albumin with 5 mg/kg infusions at weeks 0, 2, and 6.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_hemperly_2025_infliximab_pediatric_ibd_poc_pk_er', version='0.1.0')
result = model.run('standard-5mgkg-induction-typical-full-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-tables-and-figures-anchor` | No-dose exact replay of source scalars from the article tables, Results text, and Figure 4 labels. | 0–0.001 h | 2 |
| `intensified-10mgkg-induction-exploratory-full-ode` | Exploratory 10 mg/kg induction regimen; the article notes physician-judgment dosing and accelerated regimens but does not publish a matching source curve. | 0–98 h | 102 |
| `low-albumin-5mgkg-induction-full-ode` | Same nominal regimen with albumin set to the lower Table 1 IQR value to expose the paper's albumin clearance/volume covariate effect. | 0–98 h | 102 |
| `standard-5mgkg-induction-typical-full-ode` | Fixed-effect two-compartment IV ODE using the reported pediatric reference weight and albumin with 5 mg/kg infusions at weeks 0, 2, and 6. | 0–98 h | 102 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `infliximab_concentration_ug_ml` | Infliximab concentration | `1` |
| `auc_ug_day_ml` | Accumulated infliximab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_hemperly_2025_infliximab_pediatric_ibd_poc_pk_er --model-version 0.1.0 --scenario standard-5mgkg-induction-typical-full-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 11 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `auc_ug_day_ml` | `1` |
| `central_volume_l` | `1` |
| `clearance_l_day` | `1` |
| `distribution_mg_day` | `1` |
| `dose_mg` | `1` |
| `elapsed_day` | `1` |
| `elimination_mg_day` | `1` |
| `infliximab_concentration_ug_ml` | `1` |
| `intercompartmental_clearance_l_day` | `1` |
| `peripheral_concentration_ug_ml` | `1` |
| `peripheral_volume_l` | `1` |
| `state__auc_ug_day_ml` | `ug*day/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `standard-5mgkg-induction-typical-full-ode` starter has **102 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `infliximab_concentration_ug_ml` | 0 | 0 (0 h, post) | 96.667 (14.0833 h, pre) | 5.30377 |
| `auc_ug_day_ml` | 0 | 0 (0 h, post) | 2927.87 (98 h, pre) | 2927.87 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
