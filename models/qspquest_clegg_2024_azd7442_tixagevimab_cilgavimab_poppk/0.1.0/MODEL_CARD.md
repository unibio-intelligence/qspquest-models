# Clegg 2024 AZD7442 serum PK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed tixagevimab/cilgavimab exposure scenarios.

**Runnable · 20 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_clegg_2024_azd7442_tixagevimab_cilgavimab_poppk', version='0.1.0')
result = model.run('fig4-typical-600mg-combination')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 20 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `adolescent-40kg-boundary` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–180 d | 182 |
| `adolescent-95kg-boundary` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–180 d | 182 |
| `fig4-aged-over65-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-black-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-bmi-ge30-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-combined-high-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-combined-low-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-diabetes-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-female-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-high-weight-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-low-weight-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-thigh-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig4-typical-600mg-combination` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |
| `fig5-prep-300mg-single` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–730 d | 732 |
| `fig5-prep-600mg-q6mo` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–730 d | 732 |
| `iv-1000mg-combination-1h-assumption` | One-hour IV infusion is an explicit timing assumption; sequential component infusion times are unavailable. No paper peak-reproduction claim. | 0–360 d | 364 |
| `iv-3000mg-combination-1h-assumption` | One-hour IV infusion is an explicit timing assumption; sequential component infusion times are unavailable. No paper peak-reproduction claim. | 0–360 d | 364 |
| `iv-300mg-combination-1h-assumption` | One-hour IV infusion is an explicit timing assumption; sequential component infusion times are unavailable. No paper peak-reproduction claim. | 0–360 d | 364 |
| `iv-600mg-combination-1h-assumption` | One-hour IV infusion is an explicit timing assumption; sequential component infusion times are unavailable. No paper peak-reproduction claim. | 0–360 d | 364 |
| `table-reference-70kg-female` | Fixed-effect serum PK. Population medians and prediction intervals require the separately recorded IIV simulation. | 0–1000 d | 1002 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ug_ml` | Antibody concentration in the central compartment | `1` |
| `AUC_ug_day_ml` | Accumulated central antibody exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_clegg_2024_azd7442_tixagevimab_cilgavimab_poppk --model-version 0.1.0 --scenario fig4-typical-600mg-combination --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 12 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_day_ml` | `1` |
| `Cavg_cum_ug_ml` | `1` |
| `central_conc_ug_ml` | `1` |
| `cl_eff_l_day` | `1` |
| `elapsed_time_day` | `1` |
| `fim_eff` | `1` |
| `ka_eff_1_day` | `1` |
| `peripheral_conc_ug_ml` | `1` |
| `q_eff_l_day` | `1` |
| `typical_terminal_half_life_day` | `1` |
| `vc_eff_l` | `1` |
| `vp_eff_l` | `1` |
| `state__AUC_ug_day_ml` | `ug*day/mL` |
| `state__A_central_mg` | `mg` |
| `state__A_depot_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `fig4-typical-600mg-combination` starter has **1002 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ug_ml` | 0 | 0 (0 d, post) | 58.7368 (12 d, post) | 0.0067602 |
| `AUC_ug_day_ml` | 0 | 0 (0 d, post) | 7185.73 (1000 d, pre) | 7185.73 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
