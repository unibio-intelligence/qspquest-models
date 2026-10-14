# Han 2026 Sim2Real-PK Daratumumab Public TMDD ODE

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore daratumumab target-mediated drug disposition.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Early label-like 16 mg/kg IV induction-window schedule using the public ODE and median infusion durations, overlaid with paper Fig. 5A trough/peak constraints.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_han_2026_sim2real_pk_daratumumab_tmdd', version='0.1.0')
result = model.run('label-like-16mgkg-window-ode-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `label-like-16mgkg-window-ode-overlay` | Early label-like 16 mg/kg IV induction-window schedule using the public ODE and median infusion durations, overlaid with paper Fig. 5A trough/peak constraints. | 0–14 h | 143 |
| `low-albumin-16mgkg-covariate-ode-overlay` | A covariate perturbation from the public ODE showing albumin-dependent clearance direction; paper/SI provides qualitative covariate sensitivity but not digitizable coordinates. | 0–14 h | 143 |
| `single-dose-16mgkg-ode-dose-exposure-anchor` | Public ODE short-horizon single-dose daratumumab trajectory used as one point in a dose-exposure scan. Paper Fig. 2E only reports the fitted exponent/R2, not extractable per-dose AUC points. | 0–2 h | 42 |
| `source-parameter-and-performance-exact-replay` | Zero-dose exact replay of the public daratumumab ODE parameters and reported Sim2Real-PK performance endpoints. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_mg_l` | Daratumumab concentration | `1` |
| `vmax_t_mg_model_time` | Time-varying maximum saturable elimination rate | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_han_2026_sim2real_pk_daratumumab_tmdd --model-version 0.1.0 --scenario label-like-16mgkg-window-ode-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 11 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `central_concentration_mg_l` | `1` |
| `cl_l_model_time` | `1` |
| `daratumumab_f20_absolute_gain_pct` | `1` |
| `daratumumab_f20_relative_gain_pct` | `1` |
| `ibrutinib_f50_absolute_gain_pct` | `1` |
| `linear_elimination_mg_model_time` | `1` |
| `peripheral_concentration_mg_l` | `1` |
| `saturable_elimination_mg_model_time` | `1` |
| `single_dose_mg` | `1` |
| `v1_l` | `1` |
| `vmax_t_mg_model_time` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `label-like-16mgkg-window-ode-overlay` starter has **143 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_mg_l` | 0 | 0 (0 h, post) | 408.827 (7.14167 h, pre) | 224.308 |
| `vmax_t_mg_model_time` | 49.92 | 32.2533 (14 h, pre) | 49.92 (0 h, post) | 32.2533 |

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
Evidence identity: `sha256:34e8a8b339c8eaf5e21ee8e5dc3a212172e8a791e47142bf6c65f4499c198ecb`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-limited runtime reconstruction of the public daratumumab two-compartment TMDD ODE generator used to pretrain Sim2Real-PK. Exact source constants and reported performance endpoints are replayed through the API; clinical fine-tuned neural results remain source-limited because YODA IPD and trained checkpoints are unavailable.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
