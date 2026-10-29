# Yang 2021 Cemiplimab Advanced-Malignancy PopPK Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed cemiplimab exposure in advanced malignancy scenarios.

**Runnable · 33 experiments.** Version 0.1.0.

## Run an experiment

Individual latent serum PK with stated covariates; not the source population summary. Deterministic fixed-effect 30-minute infusion probe for the approved fixed dose selected by the paper.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yang_2021_cemiplimab_advanced_malignancies_poppk', version='0.1.0')
result = model.run('dynamic-typical-350mg-q3w')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 33 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `dynamic-high-weight-350mg-q3w` | Individual latent serum PK with stated covariates; not the source population summary. Paper Table 4 shows lower fixed-dose exposure in Q4 body weight; this dynamic probe sets 122.3 kg body weight. | 0–168 d | 33 |
| `dynamic-low-weight-350mg-q3w` | Individual latent serum PK with stated covariates; not the source population summary. Paper Table 4 shows higher fixed-dose exposure in Q1 body weight; this dynamic probe sets 50 kg body weight. | 0–168 d | 33 |
| `dynamic-typical-10mgkg-q2w` | Individual latent serum PK with stated covariates; not the source population summary. Figure 5 dose-panel source-limited dynamic probe. | 0–168 d | 37 |
| `dynamic-typical-1mgkg-q2w` | Individual latent serum PK with stated covariates; not the source population summary. Figure 5 dose-panel source-limited dynamic probe. | 0–168 d | 37 |
| `dynamic-typical-200mg-q2w` | Individual latent serum PK with stated covariates; not the source population summary. Figure 5 dose-panel source-limited dynamic probe. | 0–168 d | 37 |
| `dynamic-typical-350mg-q3w` | Individual latent serum PK with stated covariates; not the source population summary. Deterministic fixed-effect 30-minute infusion probe for the approved fixed dose selected by the paper. | 0–168 d | 33 |
| `dynamic-typical-3mgkg-q2w` | Individual latent serum PK with stated covariates; not the source population summary. Deterministic fixed-effect 30-minute infusion probe using the Table 3 model and the paper simulation covariates. | 0–168 d | 37 |
| `dynamic-typical-3mgkg-q3w` | Individual latent serum PK with stated covariates; not the source population summary. Figure 5 dose-panel source-limited dynamic probe. | 0–168 d | 33 |
| `source-10mgkg-q2w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 181 |
| `source-1mgkg-q2w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 181 |
| `source-200mg-q2w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 181 |
| `source-350mg-q3w-albumin-g-L-high` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-albumin-g-L-low` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-alt-IU-L-high` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-alt-IU-L-low` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-bmi-kg-m2-high` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-bmi-kg-m2-low` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-body-weight-kg-high` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-body-weight-kg-low` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-clq-minus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-clq-plus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-emax-minus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-emax-plus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-t50-minus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-t50-plus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-vss-minus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-eta-vss-plus-sd` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-igg-g-L-high` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-igg-g-L-low` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-350mg-q3w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `source-3mgkg-q2w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 181 |
| `source-3mgkg-q3w-median-covariates` | 30-minute IV infusions with fixed baseline covariates and explicit individual log-effects. No residual noise or race effect; not a population summary. | 0–168 d | 177 |
| `suppfig1-clearance-timecourse-fixed-effect-probe` | Individual latent serum PK with stated covariates; not the source population summary. No-dose probe exposing the Table 3 sigmoid time-varying clearance curve so it can be compared with the digitized Supplementary Figure 1 post hoc clearance traces. | 0–504 d | 19 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_L` | Cemiplimab concentration | `1` |
| `CL_ind_L_day` | Individual clearance as it changes over time | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_yang_2021_cemiplimab_advanced_malignancies_poppk --model-version 0.1.0 --scenario dynamic-typical-350mg-q3w --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 12 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `CL_ind_L_day` | `1` |
| `Emax_ind` | `1` |
| `Q_ind_L_day` | `1` |
| `T50_ind_day` | `1` |
| `V2_ind_L` | `1` |
| `V3_ind_L` | `1` |
| `central_conc_mg_L` | `1` |
| `clearance_time_factor` | `1` |
| `dose_3mgkg_mg` | `1` |
| `frozen_clearance_terminal_half_life_day` | `1` |
| `peripheral_conc_mg_L` | `1` |
| `vss_clearance_half_life_approx_day` | `1` |
| `state__AUC_day_mg_L` | `day*mg/L` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `dynamic-typical-350mg-q3w` starter has **33 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_L` | 0 | 0 (0 d, post) | 160.968 (147.021 d, pre) | 54.7093 |
| `CL_ind_L_day` | 0.286971 | 0.19102 (168 d, pre) | 0.286971 (0 d, post) | 0.19102 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
