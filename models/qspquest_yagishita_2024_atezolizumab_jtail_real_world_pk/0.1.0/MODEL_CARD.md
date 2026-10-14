# Yagishita 2024 Atezolizumab J-TAIL Real-World PopPK Validation

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore atezolizumab exposure against real-world study summaries.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation of 1200 mg q3w IV atezolizumab using the Stroh fixed-effect two-compartment structure and J-TAIL median body weight, albumin, and tumor burden.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yagishita_2024_atezolizumab_jtail_real_world_pk', version='0.1.0')
result = model.run('jtail-1200mg-q3w-median-covariate-exposure-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `jtail-1200mg-q3w-median-covariate-exposure-overlay` | Full ODE simulation of 1200 mg q3w IV atezolizumab using the Stroh fixed-effect two-compartment structure and J-TAIL median body weight, albumin, and tumor burden. | 0–42 d | 2021 |
| `jtail-article-figure1-exploratory-median-ebe` | Separately labeled effective median post-hoc random effects fitted to the digitized Figure 1A prediction median; not the original patient EBEs. | 0–82 d | 1644 |
| `jtail-article-figure1-public-fixed-effect` | Unchanged Stroh/FDA fixed effects at J-TAIL median covariates, with the two infusion timings inferred from the Figure 1 vector curve. | 0–82 d | 1644 |
| `jtail-source-anchors` | Exact replay of model-relevant values extracted from article Tables 1-3, Figures 3, Supplemental Tables 1-6/Figure 2, and the public FDA PopPK review. | 0–0.1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `concentration_ug_per_mL` | Atezolizumab concentration | `1` |
| `AUC_ug_day_per_mL` | Accumulated atezolizumab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_yagishita_2024_atezolizumab_jtail_real_world_pk --model-version 0.1.0 --scenario jtail-1200mg-q3w-median-covariate-exposure-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 171 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_day_per_mL` | `1` |
| `CL_L_day` | `1` |
| `Q_L_day` | `1` |
| `V1_L` | `1` |
| `V2_L` | `1` |
| `Vss_L` | `1` |
| `aesi_total_grade1_percent` | `1` |
| `aesi_total_grade2_percent` | `1` |
| `aesi_total_grade3_percent` | `1` |
| `aesi_total_grade4_percent` | `1` |
| `aesi_total_grade5_percent` | `1` |
| `age_ge_75_n` | `1` |
| `age_median_year` | `1` |
| `albumin_median_g_dl` | `1` |
| `auc_cycle1_geo_cv_percent` | `1` |
| `auc_cycle1_geo_mean_ug_day_ml` | `1` |
| `auc_cycle1_max_ug_day_ml` | `1` |
| `auc_cycle1_mean_ug_day_ml` | `1` |
| `auc_cycle1_median_ug_day_ml` | `1` |
| `auc_cycle1_min_ug_day_ml` | `1` |
| `auc_cycle1_sd_ug_day_ml` | `1` |
| `bmi_median_kg_m2` | `1` |
| `bsa_median_m2` | `1` |
| `calculated_terminal_half_life_day` | `1` |
| `calibration_day1_intercept` | `1` |
| `calibration_day1_r2` | `1` |
| `calibration_day1_slope` | `1` |
| `cmax_cycle1_geo_cv_percent` | `1` |
| `cmax_cycle1_geo_mean_ug_ml` | `1` |
| `cmax_cycle1_max_ug_ml` | `1` |
| `cmax_cycle1_mean_ug_ml` | `1` |
| `cmax_cycle1_median_ug_ml` | `1` |
| `cmax_cycle1_min_ug_ml` | `1` |
| `cmax_cycle1_sd_ug_ml` | `1` |
| `cmin_cycle1_geo_cv_percent` | `1` |
| `cmin_cycle1_geo_mean_ug_ml` | `1` |
| `cmin_cycle1_max_ug_ml` | `1` |
| `cmin_cycle1_mean_ug_ml` | `1` |
| `cmin_cycle1_median_ug_ml` | `1` |
| `cmin_cycle1_min_ug_ml` | `1` |
| `cmin_cycle1_sd_ug_ml` | `1` |
| `cmin_cycle2_geo_cv_percent` | `1` |
| `cmin_cycle2_geo_mean_ug_ml` | `1` |
| `cmin_cycle2_max_ug_ml` | `1` |
| `cmin_cycle2_mean_ug_ml` | `1` |
| `cmin_cycle2_median_ug_ml` | `1` |
| `cmin_cycle2_min_ug_ml` | `1` |
| `cmin_cycle2_sd_ug_ml` | `1` |
| `concentration_ug_per_mL` | `1` |
| `crp_median_mg_dl` | `1` |
| `cycle_3_q1_n` | `1` |
| `cycle_3_q2_q4_n` | `1` |
| `dcr_q1_n` | `1` |
| `dcr_q1_percent` | `1` |
| `dcr_q2_q4_n` | `1` |
| `dcr_q2_q4_percent` | `1` |
| `dose_mg_q3w` | `1` |
| `ecog_0_n` | `1` |
| `ecog_1_n` | `1` |
| `ecog_2_n` | `1` |
| `ecog_ge_2_multivariate_ci_high` | `1` |
| `ecog_ge_2_multivariate_ci_low` | `1` |
| `ecog_ge_2_multivariate_hr` | `1` |
| `ecog_ge_2_multivariate_p` | `1` |
| `excluded_no_blood_samples` | `1` |
| `excluded_timing_violation` | `1` |
| `excluded_total` | `1` |
| `fda_final_objective_function` | `1` |
| `fda_iiv_cl_v1_correlation` | `1` |
| `fda_iiv_cl_v2_correlation` | `1` |
| `fda_iiv_cl_variance` | `1` |
| `fda_iiv_v1_v2_correlation` | `1` |
| `fda_iiv_v1_variance` | `1` |
| `fda_iiv_v2_variance` | `1` |
| `fda_residual_additive_variance_ug_ml2` | `1` |
| `fda_residual_proportional_variance` | `1` |
| `female_overall_n` | `1` |
| `figure3_auc_aesi_probability` | `1` |
| `figure3_auc_aesi_q1_n` | `1` |
| `figure3_auc_aesi_q1_percent` | `1` |
| `figure3_auc_aesi_q2_n` | `1` |
| `figure3_auc_aesi_q2_percent` | `1` |
| `figure3_auc_aesi_q3_n` | `1` |
| `figure3_auc_aesi_q3_percent` | `1` |
| `figure3_auc_aesi_q4_n` | `1` |
| `figure3_auc_aesi_q4_percent` | `1` |
| `figure3_auc_grade3_q1_n` | `1` |
| `figure3_auc_grade3_q1_percent` | `1` |
| `figure3_auc_grade3_q2_n` | `1` |
| `figure3_auc_grade3_q2_percent` | `1` |
| `figure3_auc_grade3_q3_n` | `1` |
| `figure3_auc_grade3_q3_percent` | `1` |
| `figure3_auc_grade3_q4_n` | `1` |
| `figure3_auc_grade3_q4_percent` | `1` |
| `figure3_auc_logistic_p` | `1` |
| `figure3_auc_q1_lower_ug_day_ml` | `1` |
| `figure3_auc_q1_upper_ug_day_ml` | `1` |
| `figure3_auc_q2_upper_ug_day_ml` | `1` |
| `figure3_auc_q3_upper_ug_day_ml` | `1` |
| `figure3_auc_q4_upper_ug_day_ml` | `1` |
| `figure3_cmax_aesi_probability` | `1` |
| `figure3_cmax_aesi_q1_n` | `1` |
| `figure3_cmax_aesi_q1_percent` | `1` |
| `figure3_cmax_aesi_q2_n` | `1` |
| `figure3_cmax_aesi_q2_percent` | `1` |
| `figure3_cmax_aesi_q3_n` | `1` |
| `figure3_cmax_aesi_q3_percent` | `1` |
| `figure3_cmax_aesi_q4_n` | `1` |
| `figure3_cmax_aesi_q4_percent` | `1` |
| `figure3_cmax_grade3_q1_n` | `1` |
| `figure3_cmax_grade3_q1_percent` | `1` |
| `figure3_cmax_grade3_q2_n` | `1` |
| `figure3_cmax_grade3_q2_percent` | `1` |
| `figure3_cmax_grade3_q3_n` | `1` |
| `figure3_cmax_grade3_q3_percent` | `1` |
| `figure3_cmax_grade3_q4_n` | `1` |
| `figure3_cmax_grade3_q4_percent` | `1` |
| `figure3_cmax_logistic_p` | `1` |
| `figure3_cmax_q1_lower_ug_ml` | `1` |
| `figure3_cmax_q1_upper_ug_ml` | `1` |
| `figure3_cmax_q2_upper_ug_ml` | `1` |
| `figure3_cmax_q3_upper_ug_ml` | `1` |
| `figure3_cmax_q4_upper_ug_ml` | `1` |
| `institutions` | `1` |
| `jtail_total_patients` | `1` |
| `male_overall_n` | `1` |
| `mrm_atezolizumab_collision_v` | `1` |
| `mrm_atezolizumab_q1_v` | `1` |
| `mrm_atezolizumab_q3_v` | `1` |
| `nonmem_major_version` | `1` |
| `nonmem_minor_version` | `1` |
| `nonmem_patch_version` | `1` |
| `nonsquamous_n` | `1` |
| `orr_q1_n` | `1` |
| `orr_q1_percent` | `1` |
| `orr_q2_q4_n` | `1` |
| `orr_q2_q4_percent` | `1` |
| `os_concentration_q2_q4_multivariate_ci_high` | `1` |
| `os_concentration_q2_q4_multivariate_ci_low` | `1` |
| `os_concentration_q2_q4_multivariate_hr` | `1` |
| `os_concentration_q2_q4_multivariate_p` | `1` |
| `os_concentration_q2_q4_univariate_ci_high` | `1` |
| `os_concentration_q2_q4_univariate_ci_low` | `1` |
| `os_concentration_q2_q4_univariate_hr` | `1` |
| `os_concentration_q2_q4_univariate_p` | `1` |
| `peripheral_concentration_ug_per_mL` | `1` |
| `pk_assessable_patients` | `1` |
| `pk_consent_patients` | `1` |
| `r_major_version` | `1` |
| `r_minor_version` | `1` |
| `smoking_history_n` | `1` |
| `squamous_n` | `1` |
| `stroh_cl_l_day` | `1` |
| `stroh_high_dose_mg_kg` | `1` |
| `stroh_low_dose_mg_kg` | `1` |
| `stroh_patient_count` | `1` |
| `stroh_phase1_study_count` | `1` |
| `stroh_terminal_half_life_day` | `1` |
| `stroh_vss_l` | `1` |
| `supp_figure2_max_ug_ml` | `1` |
| `supp_figure2_mean_ug_ml` | `1` |
| `supp_figure2_median_ug_ml` | `1` |
| `supp_figure2_min_ug_ml` | `1` |
| `supp_figure2_n` | `1` |
| `supp_figure2_q1_ug_ml` | `1` |
| `supp_figure2_q3_ug_ml` | `1` |
| `supp_figure2_sd_ug_ml` | `1` |
| `supp_table5_n` | `1` |
| `tumor_volume_median_mm` | `1` |
| `validation_run_nonce` | `1` |
| `weight_median_kg` | `1` |
| `state__AUC` | `ug*day/mL` |
| `state__A_central` | `mg` |
| `state__A_peripheral` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `jtail-1200mg-q3w-median-covariate-exposure-overlay` starter has **2021 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `concentration_ug_per_mL` | 0 | 0 (0 d, post) | 517.463 (21.0208 d, pre) | 156.394 |
| `AUC_ug_day_per_mL` | 0 | 0 (0 d, post) | 8180.52 (42 d, pre) | 8180.52 |

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
Evidence identity: `sha256:834a7d42908e8f4ebc792b757f3bd2ac241310d2c7797ff5ead90c1f8a4b6fe4`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

J-TAIL real-world atezolizumab PopPK validation artifact: a full two-compartment IV ODE implementation using the complete public Stroh/FDA mixed-effects structure referenced by the paper, exact replay of public article and supplement values, and full-figure PK, exposure-response, and survival validation.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
