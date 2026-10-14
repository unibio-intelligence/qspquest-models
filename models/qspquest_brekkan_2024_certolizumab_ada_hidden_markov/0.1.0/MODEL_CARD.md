# Brekkan 2024 certolizumab ADA bivariate hidden-Markov model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect certolizumab exposure and anti-drug-antibody state dynamics.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Continuous-time two-state probability ODE calibrated to the paper-reported 63-day Model 6 mean first SADA transition.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_brekkan_2024_certolizumab_ada_hidden_markov', version='0.1.0')
result = model.run('model6-transition-probability-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `model6-table3-s1-exact-anchor` | Exact API replay of final bivariate Model 6 parameter estimates and data anchors. | 0–1 d | 2 |
| `model6-transition-probability-ode` | Continuous-time two-state probability ODE calibrated to the paper-reported 63-day Model 6 mean first SADA transition. | 0–168 d | 169 |
| `univariate-model-comparison-exact-anchor` | Exact replay of Table 4 hidden-transition estimates for Model 6 reduced to PKRES-only and ADAMES-only univariate models. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `p_ada` | Probability of the anti-drug-antibody state | `1` |
| `p_noada` | Probability of the state without anti-drug antibodies | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_brekkan_2024_certolizumab_ada_hidden_markov --model-version 0.1.0 --scenario model6-transition-probability-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 43 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `expected_ada_measurement_u_ml` | `1` |
| `expected_pkres_weighted_residual` | `1` |
| `first_transition_cdf` | `1` |
| `k_ada_to_noada_day` | `1` |
| `k_noada_to_ada_day` | `1` |
| `observation_interval_day_calibrated` | `1` |
| `p_ada` | `1` |
| `p_noada` | `1` |
| `source__abstract_patients_n` | `1` |
| `source__ada_lloq_u_ml` | `1` |
| `source__ada_measurements_n` | `1` |
| `source__article_patients_n` | `1` |
| `source__clinical_ada_positive_records_fraction` | `1` |
| `source__clinical_ada_positive_records_n` | `1` |
| `source__clinical_ada_positive_threshold_u_ml` | `1` |
| `source__clinical_ada_record_fraction_exact` | `1` |
| `source__czp_lloq_ug_ml` | `1` |
| `source__czp_measurements_n` | `1` |
| `source__model1_predicted_first_sada_day` | `1` |
| `source__model2_predicted_first_sada_day` | `1` |
| `source__model3_predicted_first_sada_day` | `1` |
| `source__model4_predicted_first_sada_day` | `1` |
| `source__model5_predicted_first_sada_day` | `1` |
| `source__model6_adames_sada_u_ml` | `1` |
| `source__model6_adames_snoada_u_ml` | `1` |
| `source__model6_mean_first_transition_day` | `1` |
| `source__model6_pi_ada_ada` | `1` |
| `source__model6_pi_ada_noada` | `1` |
| `source__model6_pi_noada_ada` | `1` |
| `source__model6_pi_noada_noada` | `1` |
| `source__model6_pkres_sada` | `1` |
| `source__model6_pkres_snoada` | `1` |
| `source__model6_rho_sada` | `1` |
| `source__model6_rho_snoada` | `1` |
| `source__model6_sigma2_adames` | `1` |
| `source__model6_sigma2_pkres` | `1` |
| `source__observed_mean_first_clinical_ada_positive_day` | `1` |
| `source__study_count` | `1` |
| `source__univariate_adames_pi_ada_noada` | `1` |
| `source__univariate_adames_pi_noada_ada` | `1` |
| `source__univariate_pkres_pi_ada_noada` | `1` |
| `source__univariate_pkres_pi_noada_ada` | `1` |
| `steady_state_sada_probability` | `1` |
| `state__elapsed_day` | `day` |
| `state__first_transition_survival` | `probability` |
| `state__p_ada` | `probability` |
| `state__p_noada` | `probability` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `model6-transition-probability-ode` starter has **169 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `p_ada` | 0 | 0 (0 d, post) | 0.861599 (168 d, pre) | 0.861599 |
| `p_noada` | 1 | 0.138401 (168 d, pre) | 1 (0 d, post) | 0.138401 |

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
Evidence identity: `sha256:9db599626e8a2502aa27e8ff672445c81e6cb7ca89c38e157d168e22ee1fd292`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-complete, patient-data-limited reconstruction of the final Brekkan et al. bivariate mixed hidden-Markov model for certolizumab anti-drug-antibody dynamics. The runtime represents the two hidden ADA-production states as a continuous-time probability ODE calibrated to the paper-reported Model 6 mean first transition time, while exact scenarios replay the article and SI parameter estimates.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
