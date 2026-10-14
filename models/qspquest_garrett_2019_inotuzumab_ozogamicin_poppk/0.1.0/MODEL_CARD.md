# Garrett 2019 Inotuzumab Ozogamicin PopPK Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed inotuzumab exposure with time-dependent clearance and covariates.

**Runnable · 11 experiments.** Version 0.1.0.

## Run an experiment

Deterministic fixed-effect smoke simulation for the published ALL regimen. This exercises the ODE and can be compared visually with Figure 7 behavior, but it is not a NONMEM population-percentile or VPC reproduction.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_garrett_2019_inotuzumab_ozogamicin_poppk', version='0.1.0')
result = model.run('fractionated-all-three-cycle-dynamic-smoke')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `all-reference-day78-formula-checks` | Deterministic fixed-effect equation check for ALL, no rituximab, BBSA 1.84 m2, BLSTPB 5.25%, evaluated at 1848 h (reported Day 78/C4D1). | 0–1848 h | 2 |
| `bbsa-covariate-formula-checks` | Fixed-effect formula checks for the text-reported 10th percentile BBSA 1.55 m2 and 90th percentile BBSA 2.21 m2 effects on CL1, CL2, and V1. | 0–1 h | 2 |
| `fractionated-all-three-cycle-dynamic-smoke` | Deterministic fixed-effect smoke simulation for the published ALL regimen. This exercises the ODE and can be compared visually with Figure 7 behavior, but it is not a NONMEM population-percentile or VPC reproduction. | 0–1848 h | 87 |
| `source-review-all-high-joint-covariates` | Paper Figure 7/8 covariate condition. Typical fixed effects only; not the population median or interval. One-hour infusion approximation. | 0–1848 h | 87 |
| `source-review-all-low-joint-covariates` | Paper Figure 7/8 covariate condition. Typical fixed effects only; not the population median or interval. One-hour infusion approximation. | 0–1848 h | 87 |
| `source-review-all-median-joint-covariates` | Paper Figure 7/8 covariate condition. Typical fixed effects only; not the population median or interval. One-hour infusion approximation. | 0–1848 h | 87 |
| `source-review-nhl-with-rituximab` | Supplement Online Resource 1 NHL Q4W regimen and Resource 3 missing-blast sentinel. Rituximab acts only as a PK covariate; no rituximab PK simulation. One-hour infusion approximation. | 0–2016 h | 172 |
| `source-review-nhl-without-rituximab` | Supplement Online Resource 1 NHL Q4W regimen and Resource 3 missing-blast sentinel. Rituximab acts only as a PK covariate; no rituximab PK simulation. One-hour infusion approximation. | 0–2016 h | 172 |
| `source-status-checks` | Exact flags for the official paper, PDF, supplement, preprint, and figure-digitization status. | 0–1 h | 2 |
| `study-design-and-simulation-text-checks` | Exact study population, observation count, VPC count, fractionated dose design, and published C4D1 AUC/half-life/accumulation source targets. | 0–1 h | 2 |
| `table2-final-parameter-estimate-checks` | Exact article Table 2 fixed-effect, uncertainty, random-effect, covariance, residual-error, and bootstrap scalar values. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_ng_mL` | Inotuzumab ozogamicin concentration | `1` |
| `CL_total_L_h` | Total clearance including its time-dependent component | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_garrett_2019_inotuzumab_ozogamicin_poppk --model-version 0.1.0 --scenario fractionated-all-three-cycle-dynamic-smoke --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 149 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `CL1_L_h` | `1` |
| `CL2_L_h` | `1` |
| `CL_total_L_h` | `1` |
| `CLt_L_h` | `1` |
| `K10_1_h` | `1` |
| `K12_1_h` | `1` |
| `K21_1_h` | `1` |
| `KDES_1_h` | `1` |
| `Q_L_h` | `1` |
| `V1_L` | `1` |
| `V2_L` | `1` |
| `alpha_1_h` | `1` |
| `beta_1_h` | `1` |
| `central_concentration_mg_L` | `1` |
| `central_concentration_ng_mL` | `1` |
| `high_BBSA_CL1_ratio` | `1` |
| `high_BBSA_CL2_ratio` | `1` |
| `high_BBSA_V1_ratio` | `1` |
| `kdes_half_time_h` | `1` |
| `low_BBSA_CL1_ratio` | `1` |
| `low_BBSA_CL2_ratio` | `1` |
| `low_BBSA_V1_ratio` | `1` |
| `peripheral_concentration_mg_L` | `1` |
| `source_CL1_L_h` | `1` |
| `source_CL1_bootstrap_ci_lower_L_h` | `1` |
| `source_CL1_bootstrap_ci_upper_L_h` | `1` |
| `source_CL1_bootstrap_median_L_h` | `1` |
| `source_CL1_ci_lower_L_h` | `1` |
| `source_CL1_ci_upper_L_h` | `1` |
| `source_CL2_L_h` | `1` |
| `source_CL2_bootstrap_ci_lower_L_h` | `1` |
| `source_CL2_bootstrap_ci_upper_L_h` | `1` |
| `source_CL2_bootstrap_median_L_h` | `1` |
| `source_CL2_ci_lower_L_h` | `1` |
| `source_CL2_ci_upper_L_h` | `1` |
| `source_Q_L_h` | `1` |
| `source_Q_bootstrap_ci_lower_L_h` | `1` |
| `source_Q_bootstrap_ci_upper_L_h` | `1` |
| `source_Q_bootstrap_median_L_h` | `1` |
| `source_Q_ci_lower_L_h` | `1` |
| `source_Q_ci_upper_L_h` | `1` |
| `source_V1_L` | `1` |
| `source_V1_bootstrap_ci_lower_L` | `1` |
| `source_V1_bootstrap_ci_upper_L` | `1` |
| `source_V1_bootstrap_median_L` | `1` |
| `source_V1_ci_lower_L` | `1` |
| `source_V1_ci_upper_L` | `1` |
| `source_V2_L` | `1` |
| `source_V2_bootstrap_ci_lower_L` | `1` |
| `source_V2_bootstrap_ci_upper_L` | `1` |
| `source_V2_bootstrap_median_L` | `1` |
| `source_V2_ci_lower_L` | `1` |
| `source_V2_ci_upper_L` | `1` |
| `source_all_median_BBSA_m2` | `1` |
| `source_all_median_BLSTPB_pct` | `1` |
| `source_all_patients_n` | `1` |
| `source_analysis_patients_n` | `1` |
| `source_completeness_score` | `1` |
| `source_cov_CL1_CL2` | `1` |
| `source_cov_CL1_V1` | `1` |
| `source_cov_CL2_V1` | `1` |
| `source_cycle1_day15_dose_mg_m2` | `1` |
| `source_cycle1_day1_dose_mg_m2` | `1` |
| `source_cycle1_day8_dose_mg_m2` | `1` |
| `source_cycle1_duration_day` | `1` |
| `source_eta_shrinkage_CL1_pct` | `1` |
| `source_eta_shrinkage_CL2_pct` | `1` |
| `source_eta_shrinkage_V1_pct` | `1` |
| `source_eta_shrinkage_kdes_pct` | `1` |
| `source_figure_digitization_available` | `1` |
| `source_fixed_regimen_total_cycle_mg_m2` | `1` |
| `source_full_text_available` | `1` |
| `source_kdes_1_h` | `1` |
| `source_kdes_bootstrap_ci_lower_1_h` | `1` |
| `source_kdes_bootstrap_ci_upper_1_h` | `1` |
| `source_kdes_bootstrap_median_1_h` | `1` |
| `source_kdes_ci_lower_1_h` | `1` |
| `source_kdes_ci_upper_1_h` | `1` |
| `source_later_cycle_duration_day` | `1` |
| `source_nhl_median_BBSA_m2` | `1` |
| `source_nhl_patients_n` | `1` |
| `source_ofv_final_model` | `1` |
| `source_ofv_reduction_time_dependent_vs_linear` | `1` |
| `source_omega2_CL1_cv_pct` | `1` |
| `source_omega2_CL1_lower` | `1` |
| `source_omega2_CL1_upper` | `1` |
| `source_omega2_CL2_cv_pct` | `1` |
| `source_omega2_CL2_lower` | `1` |
| `source_omega2_CL2_upper` | `1` |
| `source_omega2_V1_cv_pct` | `1` |
| `source_omega2_V1_lower` | `1` |
| `source_omega2_V1_upper` | `1` |
| `source_omega2_kdes_cv_pct` | `1` |
| `source_omega2_kdes_lower` | `1` |
| `source_omega2_kdes_upper` | `1` |
| `source_pdf_available` | `1` |
| `source_pk_observations_n` | `1` |
| `source_preprint_available` | `1` |
| `source_reference_BBSA_m2` | `1` |
| `source_reference_BLSTPB_pct` | `1` |
| `source_residual_error_ALL` | `1` |
| `source_residual_error_ALL_ci_lower` | `1` |
| `source_residual_error_ALL_ci_upper` | `1` |
| `source_residual_error_NHL` | `1` |
| `source_residual_error_NHL_ci_lower` | `1` |
| `source_residual_error_NHL_ci_upper` | `1` |
| `source_source_accumulation_ratio` | `1` |
| `source_source_accumulation_ratio_ci_lower` | `1` |
| `source_source_accumulation_ratio_ci_upper` | `1` |
| `source_source_c4d1_AUCtau_ng_h_mL` | `1` |
| `source_source_c4d1_day` | `1` |
| `source_source_c4d1_time_h` | `1` |
| `source_source_high_BBSA_CL1_increase_pct` | `1` |
| `source_source_high_BBSA_CL2_increase_pct` | `1` |
| `source_source_high_BBSA_V1_increase_pct` | `1` |
| `source_source_high_BBSA_m2` | `1` |
| `source_source_kdes_half_time_BLSTPB_5p25_h` | `1` |
| `source_source_kdes_half_time_low_high_range_lower_h` | `1` |
| `source_source_kdes_half_time_low_high_range_upper_h` | `1` |
| `source_source_low_BBSA_CL1_decrease_pct` | `1` |
| `source_source_low_BBSA_CL2_decrease_pct` | `1` |
| `source_source_low_BBSA_V1_decrease_pct` | `1` |
| `source_source_low_BBSA_m2` | `1` |
| `source_source_terminal_beta_half_life_h` | `1` |
| `source_supplement_available` | `1` |
| `source_theta_BLSTPB_on_kdes` | `1` |
| `source_theta_BLSTPB_on_kdes_ci_lower` | `1` |
| `source_theta_BLSTPB_on_kdes_ci_upper` | `1` |
| `source_theta_CL1_BBSA` | `1` |
| `source_theta_CL1_BBSA_ci_lower` | `1` |
| `source_theta_CL1_BBSA_ci_upper` | `1` |
| `source_theta_CL2_BBSA` | `1` |
| `source_theta_CL2_BBSA_ci_lower` | `1` |
| `source_theta_CL2_BBSA_ci_upper` | `1` |
| `source_theta_V1_BBSA` | `1` |
| `source_theta_V1_BBSA_ci_lower` | `1` |
| `source_theta_V1_BBSA_ci_upper` | `1` |
| `source_theta_all_on_CL1` | `1` |
| `source_theta_all_on_CL1_ci_lower` | `1` |
| `source_theta_all_on_CL1_ci_upper` | `1` |
| `source_theta_all_on_kdes` | `1` |
| `source_theta_all_on_kdes_ci_lower` | `1` |
| `source_theta_all_on_kdes_ci_upper` | `1` |
| `source_theta_no_rituximab_on_CL1` | `1` |
| `source_theta_no_rituximab_on_CL1_ci_lower` | `1` |
| `source_theta_no_rituximab_on_CL1_ci_upper` | `1` |
| `source_total_median_BBSA_m2` | `1` |
| `source_vpc_simulations_n` | `1` |
| `terminal_beta_half_life_h` | `1` |
| `state__AUC_ng_h_mL` | `ng*h/mL` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_h` | `h` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `fractionated-all-three-cycle-dynamic-smoke` starter has **87 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_ng_mL` | 0 | 0 (0 h, post) | 265.806 (1177 h, pre) | 66.9616 |
| `CL_total_L_h` | 0.402281 | 0.0333416 (1848 h, pre) | 0.402281 (0 h, post) | 0.0333416 |

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
Evidence identity: `sha256:9f43417863ba529e4b497bc5092e50c886469ef4846ddf5c972cdaf71a9a9760`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Paper-derived fixed-effect implementation of the Garrett et al. 2019 inotuzumab ozogamicin population PK model in relapsed/refractory B-cell ALL and NHL. The runtime implements the two-compartment structural PK model with linear plus exponentially declining time-dependent clearance, BBSA/BLSTPB/disease/rituximab covariate equations, and exact scalar checks from Table 1, Table 2, the supplement NONMEM control stream, and simulation text. It does not reproduce NONMEM M3 censored-data likelihood, interindividual effects, covariance, BLQ handling, or VPC envelopes.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
