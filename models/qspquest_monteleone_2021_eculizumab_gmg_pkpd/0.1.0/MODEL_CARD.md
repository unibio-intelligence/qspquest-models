# Monteleone 2021 Eculizumab gMG PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore reduced eculizumab exposure and free-C5 response in generalized myasthenia gravis.

**Runnable · 7 experiments.** Version 0.1.0.

## Run an experiment

Paper fixed-effect/source scenario using Table 1 Bayesian mean PK parameters. It is intentionally not tuned; Figure 1 overlays show it underpredicts steady troughs.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_monteleone_2021_eculizumab_gmg_pkpd', version='0.1.0')
result = model.run('regain-900-1200mg-iv-pkpd-context')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `baseline-checks` | Exact checks for analysis-set demographics, baseline labs, race/ethnicity, and PLEX events. | 0–1 h | 2 |
| `exploratory-calibrated-fig1-median-clearance-pkpd-context` | Exploratory calibrated scenario that uses the paper-reported Table 1 median clearance (0.00785 L/h) instead of the Table 1 mean clearance (0.0106 L/h). This improves public Figure 1 peak/trough agreement and is not the original population fixed-effect model. | 0–4368.58 h | 199 |
| `pkpd-result-checks` | Exact checks for serum concentration ranges, model flags, C5/hemolysis inhibition, IC50, threshold concentration, clinical deterioration, PLEX, half-life, and safety values. | 0–1 h | 2 |
| `regain-900-1200mg-iv-pkpd-context` | Paper fixed-effect/source scenario using Table 1 Bayesian mean PK parameters. It is intentionally not tuned; Figure 1 overlays show it underpredicts steady troughs. | 0–4368.58 h | 199 |
| `source-status-checks` | Exact checks for source availability and missing SI binary flags. | 0–1 h | 2 |
| `study-design-assay-checks` | Exact checks for REGAIN treatment design, dosing schedule, infusion duration, sample timing, and bioanalytical thresholds. | 0–1 h | 2 |
| `table1-pk-summary-checks` | Exact checks for all Table 1 Bayesian PK summary statistics. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ug_mL` | Eculizumab concentration | `1` |
| `free_c5_ug_mL` | Unbound complement C5 concentration | `1` |
| `hemolysis_pct` | Hemolysis percentage in the reduced response model | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_monteleone_2021_eculizumab_gmg_pkpd --model-version 0.1.0 --scenario regain-900-1200mg-iv-pkpd-context --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 175 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_day_mL` | `1` |
| `c5_inhibition_flag` | `1` |
| `central_conc_ug_mL` | `1` |
| `free_c5_ug_mL` | `1` |
| `hemolysis_pct` | `1` |
| `peripheral_conc_ug_mL` | `1` |
| `source_CL_max_L_h` | `1` |
| `source_CL_mean_L_h` | `1` |
| `source_CL_median_L_h` | `1` |
| `source_CL_min_L_h` | `1` |
| `source_CL_sd_L_h` | `1` |
| `source_Q_max_L_h` | `1` |
| `source_Q_mean_L_h` | `1` |
| `source_Q_median_L_h` | `1` |
| `source_Q_min_L_h` | `1` |
| `source_Q_sd_L_h` | `1` |
| `source_V1_max_L` | `1` |
| `source_V1_mean_L` | `1` |
| `source_V1_median_L` | `1` |
| `source_V1_min_L` | `1` |
| `source_V1_sd_L` | `1` |
| `source_V2_max_L` | `1` |
| `source_V2_mean_L` | `1` |
| `source_V2_median_L` | `1` |
| `source_V2_min_L` | `1` |
| `source_V2_sd_L` | `1` |
| `source_achr_titer_max_nmol_L` | `1` |
| `source_achr_titer_mean_nmol_L` | `1` |
| `source_achr_titer_median_nmol_L` | `1` |
| `source_achr_titer_min_nmol_L` | `1` |
| `source_achr_titer_sd_nmol_L` | `1` |
| `source_ada_screening_sensitivity_ng_mL` | `1` |
| `source_adult_age_min_year` | `1` |
| `source_age_first_dose_mean_year` | `1` |
| `source_age_first_dose_sd_year` | `1` |
| `source_age_mg_diagnosis_mean_year` | `1` |
| `source_age_mg_diagnosis_sd_year` | `1` |
| `source_albumin_mean_g_L` | `1` |
| `source_albumin_sd_g_L` | `1` |
| `source_analysis_set_n` | `1` |
| `source_asian_japanese_n` | `1` |
| `source_asian_japanese_pct` | `1` |
| `source_auc_ss_max_ug_h_mL` | `1` |
| `source_auc_ss_mean_ug_h_mL` | `1` |
| `source_auc_ss_median_ug_h_mL` | `1` |
| `source_auc_ss_min_ug_h_mL` | `1` |
| `source_auc_ss_sd_ug_h_mL` | `1` |
| `source_black_n` | `1` |
| `source_bmi_mean_kg_m2` | `1` |
| `source_bmi_sd_kg_m2` | `1` |
| `source_body_weight_mean_kg` | `1` |
| `source_body_weight_sd_kg` | `1` |
| `source_cdc_case_end_year` | `1` |
| `source_cdc_case_start_year` | `1` |
| `source_cdc_meningococcal_cases_n` | `1` |
| `source_citation_rank` | `1` |
| `source_cited_by_count_in_queue` | `1` |
| `source_clinical_deterioration_eculizumab_n` | `1` |
| `source_clinical_deterioration_eculizumab_pct` | `1` |
| `source_clinical_deterioration_eculizumab_total` | `1` |
| `source_clinical_deterioration_high_auc_n` | `1` |
| `source_clinical_deterioration_high_auc_pct` | `1` |
| `source_clinical_deterioration_high_auc_total` | `1` |
| `source_clinical_deterioration_low_auc_n` | `1` |
| `source_clinical_deterioration_low_auc_pct` | `1` |
| `source_clinical_deterioration_low_auc_total` | `1` |
| `source_clinical_deterioration_placebo_n` | `1` |
| `source_clinical_deterioration_placebo_pct` | `1` |
| `source_clinical_deterioration_placebo_total` | `1` |
| `source_cmax_ss_max_ug_mL` | `1` |
| `source_cmax_ss_mean_ug_mL` | `1` |
| `source_cmax_ss_median_ug_mL` | `1` |
| `source_cmax_ss_min_ug_mL` | `1` |
| `source_cmax_ss_sd_ug_mL` | `1` |
| `source_complete_inhibition_patients_over_pct` | `1` |
| `source_completeness_score` | `1` |
| `source_ctrough_ss_max_ug_mL` | `1` |
| `source_ctrough_ss_mean_ug_mL` | `1` |
| `source_ctrough_ss_median_ug_mL` | `1` |
| `source_ctrough_ss_min_ug_mL` | `1` |
| `source_ctrough_ss_sd_ug_mL` | `1` |
| `source_eculizumab_assay_lloq_ug_mL` | `1` |
| `source_eculizumab_assay_uloq_ug_mL` | `1` |
| `source_eculizumab_n` | `1` |
| `source_egfr_mean_mL_min_1p73m2` | `1` |
| `source_egfr_sd_mL_min_1p73m2` | `1` |
| `source_first_order_elimination_flag` | `1` |
| `source_free_c5_assay_lloq_ug_mL` | `1` |
| `source_free_c5_bloq_imputed_ug_mL` | `1` |
| `source_free_c5_ic50_ug_mL` | `1` |
| `source_free_c5_inhibition_threshold_ug_mL` | `1` |
| `source_free_c5_samples_below_threshold_n` | `1` |
| `source_free_c5_samples_below_threshold_pct` | `1` |
| `source_free_c5_samples_total_n` | `1` |
| `source_frontiers_pdf_available` | `1` |
| `source_frontiers_xml_available` | `1` |
| `source_hemolysis_all_samples_inhibited_patients_n` | `1` |
| `source_hemolysis_all_samples_inhibited_patients_total` | `1` |
| `source_hemolysis_all_samples_inhibited_pct` | `1` |
| `source_hemolysis_inhibition_threshold_pct` | `1` |
| `source_infusion_duration_min` | `1` |
| `source_japanese_n` | `1` |
| `source_loading_dose_count` | `1` |
| `source_loading_dose_mg` | `1` |
| `source_loading_interval_day` | `1` |
| `source_loading_interval_window_day` | `1` |
| `source_maintenance_first_dose_mg` | `1` |
| `source_maintenance_first_dose_week` | `1` |
| `source_maintenance_interval_day` | `1` |
| `source_maintenance_interval_window_day` | `1` |
| `source_median_peak_high_ug_mL` | `1` |
| `source_median_peak_low_ug_mL` | `1` |
| `source_median_trough_high_ug_mL` | `1` |
| `source_median_trough_low_ug_mL` | `1` |
| `source_meningococcal_incidence_per_100py` | `1` |
| `source_meningococcal_mortality_per_100py` | `1` |
| `source_mg_duration_mean_year` | `1` |
| `source_mg_duration_sd_year` | `1` |
| `source_needs_user_si_binaries` | `1` |
| `source_observed_cmax_max_ug_mL` | `1` |
| `source_observed_cmax_mean_ug_mL` | `1` |
| `source_observed_cmax_median_ug_mL` | `1` |
| `source_observed_cmax_min_ug_mL` | `1` |
| `source_observed_cmax_sd_ug_mL` | `1` |
| `source_other_multiple_unknown_n` | `1` |
| `source_other_multiple_unknown_pct` | `1` |
| `source_peak_90ci_lower_high_ug_mL` | `1` |
| `source_peak_90ci_lower_low_ug_mL` | `1` |
| `source_peak_90ci_upper_high_ug_mL` | `1` |
| `source_peak_90ci_upper_low_ug_mL` | `1` |
| `source_peak_sample_after_infusion_min` | `1` |
| `source_placebo_n` | `1` |
| `source_plex_events_n` | `1` |
| `source_plex_patients_n` | `1` |
| `source_plex_regular_dose_after_end_min` | `1` |
| `source_plex_supplemental_dose_mg` | `1` |
| `source_plex_washout_before_study_week` | `1` |
| `source_pmc_html_available` | `1` |
| `source_pmc_oa_package_metadata_available` | `1` |
| `source_postmarketing_exposure_py` | `1` |
| `source_proportional_error_flag` | `1` |
| `source_publication_year` | `1` |
| `source_regain_total_n` | `1` |
| `source_rse_all_below_pct` | `1` |
| `source_rse_cl_v1_v2_below_pct` | `1` |
| `source_steady_state_week` | `1` |
| `source_supplement_docx_binary_available` | `1` |
| `source_supplement_links_detected` | `1` |
| `source_supplement_pdf_binary_available` | `1` |
| `source_target_eculizumab_conc_ug_mL` | `1` |
| `source_terminal_half_life_discussion_day` | `1` |
| `source_terminal_half_life_max_h` | `1` |
| `source_terminal_half_life_mean_h` | `1` |
| `source_terminal_half_life_median_h` | `1` |
| `source_terminal_half_life_min_h` | `1` |
| `source_terminal_half_life_sd_h` | `1` |
| `source_treatment_ae_eculizumab_pct` | `1` |
| `source_treatment_ae_placebo_pct` | `1` |
| `source_treatment_period_week` | `1` |
| `source_trough_90ci_lower_high_ug_mL` | `1` |
| `source_trough_90ci_lower_low_ug_mL` | `1` |
| `source_trough_90ci_upper_high_ug_mL` | `1` |
| `source_trough_90ci_upper_low_ug_mL` | `1` |
| `source_trough_all_visits_c5_inhibited_patients_n` | `1` |
| `source_trough_all_visits_c5_inhibited_patients_total` | `1` |
| `source_trough_all_visits_c5_inhibited_pct` | `1` |
| `source_trough_sample_preinfusion_min_high` | `1` |
| `source_trough_sample_preinfusion_min_low` | `1` |
| `source_two_compartment_model_flag` | `1` |
| `source_wbc_mean_1e9_L` | `1` |
| `source_wbc_sd_1e9_L` | `1` |
| `source_white_n` | `1` |
| `source_white_pct` | `1` |
| `target_margin` | `1` |
| `terminal_half_life_day_from_table1` | `1` |
| `state__AUC_ug_h_mL` | `ug*hour/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_time_h` | `hour` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `regain-900-1200mg-iv-pkpd-context` starter has **199 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ug_mL` | 0 | 0 (0 h, post) | 768.788 (672.583 h, pre) | 692.773 |
| `free_c5_ug_mL` | 20 | 0.00205271 (672.583 h, pre) | 20 (0 h, post) | 0.0027819 |
| `hemolysis_pct` | 100 | 0.0821084 (672.583 h, pre) | 100 (0 h, post) | 0.111276 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
