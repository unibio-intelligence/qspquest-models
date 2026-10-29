# Quartino 2017 Pertuzumab Neoadjuvant PK/Exposure-Response Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore pertuzumab exposure and neoadjuvant response summaries.

**Runnable · 7 experiments.** Version 0.1.0.

## Run an experiment

Reference covariate dynamic shell using historical PopPK median LBW and albumin.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_quartino_2017_pertuzumab_neoadjuvant_pk_er', version='0.1.0')
result = model.run('historical-reference-840-420-q3w-4cycles')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `dose-selection-checks` | Approved 840/420 mg q3w regimen, target trough threshold, and dose-selection context. | 0–1 h | 2 |
| `exposure-response-checks` | Cycle 2 Ctrough target attainment, logit ER analysis population, and pCR slope p-value. | 0–1 h | 2 |
| `historical-reference-840-420-q3w-4cycles` | Reference covariate dynamic shell using historical PopPK median LBW and albumin. | 0–84 h | 89 |
| `neosphere-design-baseline-checks` | Arm definitions, baseline covariates, serum samples, and pCR counts from Table 1. | 0–1 h | 2 |
| `poppk-model-ddi-checks` | Published PK structure, VPC/NPC setup, Ctrough ANOVA, and CL/Vc DDI p-values. | 0–1 h | 2 |
| `source-status-checks` | Source retrieval, citation, and route-audit values. | 0–1 h | 2 |
| `typical-neosphere-840-420-q3w-4cycles` | Source-limited deterministic PK shell for the approved neoadjuvant regimen; not a patient-level VPC reproduction. | 0–84 h | 89 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `pertuzumab_concentration_ug_mL` | Pertuzumab concentration | `1` |
| `AUC_ug_day_mL` | Accumulated pertuzumab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_quartino_2017_pertuzumab_neoadjuvant_pk_er --model-version 0.1.0 --scenario historical-reference-840-420-q3w-4cycles --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 157 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_day_mL` | `1` |
| `CL_L_day` | `1` |
| `CL_cov_L_day` | `1` |
| `Q_L_day` | `1` |
| `Vc_L` | `1` |
| `Vc_cov_L` | `1` |
| `Vp_L` | `1` |
| `Vp_cov_L` | `1` |
| `age_total_max_year` | `1` |
| `age_total_median_year` | `1` |
| `age_total_min_year` | `1` |
| `albumin_g_dL` | `1` |
| `albumin_ref_g_dL` | `1` |
| `albumin_total_max_g_dL` | `1` |
| `albumin_total_median_g_dL` | `1` |
| `albumin_total_min_g_dL` | `1` |
| `approved_loading_dose_mg` | `1` |
| `approved_maintenance_dose_mg` | `1` |
| `arm_A_B_D_total_cycles_n` | `1` |
| `arm_A_docetaxel_flag` | `1` |
| `arm_A_patients_n` | `1` |
| `arm_A_pertuzumab_flag` | `1` |
| `arm_A_trastuzumab_flag` | `1` |
| `arm_B_above_target_n` | `1` |
| `arm_B_above_target_percent` | `1` |
| `arm_B_docetaxel_flag` | `1` |
| `arm_B_patients_n` | `1` |
| `arm_B_pcr_percent_runtime` | `1` |
| `arm_B_pertuzumab_flag` | `1` |
| `arm_B_target_assessed_n` | `1` |
| `arm_B_target_fraction_percent_runtime` | `1` |
| `arm_B_trastuzumab_flag` | `1` |
| `arm_C_docetaxel_flag` | `1` |
| `arm_C_patients_n` | `1` |
| `arm_C_pertuzumab_flag` | `1` |
| `arm_C_total_cycles_n` | `1` |
| `arm_C_trastuzumab_flag` | `1` |
| `arm_D_docetaxel_flag` | `1` |
| `arm_D_patients_n` | `1` |
| `arm_D_pertuzumab_flag` | `1` |
| `arm_D_trastuzumab_flag` | `1` |
| `arms_n` | `1` |
| `baseline_weight_total_max_kg` | `1` |
| `baseline_weight_total_median_kg` | `1` |
| `baseline_weight_total_min_kg` | `1` |
| `ddi_anova_pvalue_threshold` | `1` |
| `docetaxel_effect_CL_pvalue_B_vs_C` | `1` |
| `docetaxel_effect_Vc_pvalue_B_vs_C` | `1` |
| `elisa_lLOQ_ug_mL` | `1` |
| `er_ctrough_max_ug_mL` | `1` |
| `er_ctrough_min_ug_mL` | `1` |
| `er_population_pk_pcr_available_n` | `1` |
| `er_primary_arms_A_B_n` | `1` |
| `historical_albumin_median_g_dL` | `1` |
| `historical_lbw_median_kg` | `1` |
| `lbw_total_max_kg` | `1` |
| `lbw_total_median_kg` | `1` |
| `lbw_total_min_kg` | `1` |
| `lean_body_weight_kg` | `1` |
| `lean_body_weight_ref_kg` | `1` |
| `logit_slope_pvalue` | `1` |
| `main_pdf_pages` | `1` |
| `model_replicates_npc_per_patient_n` | `1` |
| `model_replicates_vpc_n` | `1` |
| `mtd_reached_flag` | `1` |
| `neosphere_albumin_median_g_dL` | `1` |
| `neosphere_countries_n` | `1` |
| `neosphere_lbw_median_kg` | `1` |
| `neosphere_total_patients_n` | `1` |
| `npc_25th_sim_percentile_percent` | `1` |
| `npc_50th_sim_percentile_percent` | `1` |
| `npc_5th_sim_percentile_percent` | `1` |
| `npc_75th_sim_percentile_percent` | `1` |
| `npc_95th_sim_percentile_percent` | `1` |
| `observed_ctrough_anova_p_cycle2` | `1` |
| `observed_ctrough_anova_p_cycle4` | `1` |
| `observed_cycle2_above_target_n` | `1` |
| `observed_cycle2_above_target_percent` | `1` |
| `observed_cycle2_assessed_n` | `1` |
| `observed_cycle2_ctrough_mean_ug_mL` | `1` |
| `observed_target_fraction_percent_runtime` | `1` |
| `pcr_arm_B_vs_A_significant_flag` | `1` |
| `pcr_assessment_cycle` | `1` |
| `pcr_evaluable_arm_A_n` | `1` |
| `pcr_evaluable_arm_B_n` | `1` |
| `pcr_evaluable_arm_C_n` | `1` |
| `pcr_evaluable_arm_D_n` | `1` |
| `pcr_evaluable_total_n` | `1` |
| `pcr_na_arm_A_n` | `1` |
| `pcr_na_arm_B_n` | `1` |
| `pcr_na_arm_C_n` | `1` |
| `pcr_na_arm_D_n` | `1` |
| `pcr_na_total_n` | `1` |
| `pcr_no_arm_A_n` | `1` |
| `pcr_no_arm_B_n` | `1` |
| `pcr_no_arm_C_n` | `1` |
| `pcr_no_arm_D_n` | `1` |
| `pcr_no_total_n` | `1` |
| `pcr_yes_arm_A_evaluable_percent` | `1` |
| `pcr_yes_arm_A_n` | `1` |
| `pcr_yes_arm_A_of_all_percent` | `1` |
| `pcr_yes_arm_B_n` | `1` |
| `pcr_yes_arm_B_percent` | `1` |
| `pcr_yes_arm_C_evaluable_percent` | `1` |
| `pcr_yes_arm_C_n` | `1` |
| `pcr_yes_arm_D_evaluable_percent` | `1` |
| `pcr_yes_arm_D_n` | `1` |
| `pcr_yes_total_n` | `1` |
| `pertuzumab_concentration_ug_mL` | `1` |
| `phase2_single_agent_high_dose_mg` | `1` |
| `phase2_single_agent_loading_mg` | `1` |
| `phase2_single_agent_maintenance_mg` | `1` |
| `pmc_binary_recaptcha_placeholders_moved_to_audit` | `1` |
| `pmc_full_text_xml_fetched_flag` | `1` |
| `pre_surgery_cycles_n` | `1` |
| `predicted_ctrough_anova_p_cycle2` | `1` |
| `predicted_ctrough_anova_p_cycle4` | `1` |
| `predicted_cycle2_above_target_n` | `1` |
| `predicted_cycle2_above_target_percent` | `1` |
| `predicted_cycle2_assessed_n` | `1` |
| `predicted_cycle2_ctrough_mean_ug_mL` | `1` |
| `predicted_target_fraction_percent_runtime` | `1` |
| `predose_samples_arm_B_n` | `1` |
| `predose_samples_arm_C_n` | `1` |
| `predose_samples_arm_D_n` | `1` |
| `predose_samples_total_n` | `1` |
| `preprint_match_found_flag` | `1` |
| `q3w_interval_day` | `1` |
| `race_asian_total_n` | `1` |
| `race_black_total_n` | `1` |
| `race_hispanic_total_n` | `1` |
| `race_indian_or_alaska_native_total_n` | `1` |
| `race_mixed_total_n` | `1` |
| `race_white_total_n` | `1` |
| `safety_er_conducted_flag` | `1` |
| `serum_pertuzumab_samples_arm_B_n` | `1` |
| `serum_pertuzumab_samples_arm_C_n` | `1` |
| `serum_pertuzumab_samples_arm_D_n` | `1` |
| `serum_pertuzumab_samples_total_n` | `1` |
| `sgpt_total_max_IU_L` | `1` |
| `sgpt_total_median_IU_L` | `1` |
| `sgpt_total_min_IU_L` | `1` |
| `single_ascending_dose_high_mg_kg` | `1` |
| `single_ascending_dose_low_mg_kg` | `1` |
| `springer_article_html_fetched_flag` | `1` |
| `springer_supplement_docx_count` | `1` |
| `supplement_media_emf_count` | `1` |
| `target_ctrough_ug_mL` | `1` |
| `target_population_percent` | `1` |
| `terminal_half_life_day` | `1` |
| `theta_albumin_CL` | `1` |
| `theta_lbw_CL` | `1` |
| `theta_lbw_Vc` | `1` |
| `theta_lbw_Vp` | `1` |
| `total_volume_L` | `1` |
| `trastuzumab_effect_CL_pvalue_B_vs_D` | `1` |
| `trastuzumab_effect_Vc_pvalue_B_vs_D` | `1` |
| `state__AUC_ug_day_mL` | `ug*day/mL` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_day` | `day` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `historical-reference-840-420-q3w-4cycles` starter has **89 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `pertuzumab_concentration_ug_mL` | 0 | 0 (0 h, post) | 268.027 (0.0625 h, pre) | 50.5049 |
| `AUC_ug_day_mL` | 0 | 0 (0 h, post) | 7625.27 (84 h, pre) | 7625.27 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
