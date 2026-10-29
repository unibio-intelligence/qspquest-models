# Hurkmans 2019 Nivolumab Real-World PopPK Clearance-Response

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore nivolumab clearance and response relationships with fixed inputs.

**Runnable · 8 experiments.** Version 0.1.0.

## Run an experiment

A deterministic fixed-effect simulation using the final two-compartment model, 80 kg receiving the average 240 mg every 14 days for 12 cycles.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_hurkmans_2019_nivolumab_real_world_poppk_cl_response', version='0.1.0')
result = model.run('typical-male-3mgkg-q2w-dynamic-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `low-albumin-high-bsa-dynamic-probe` | A fixed-effect simulation at the reported albumin and BSA threshold values associated with higher clearance. | 0–168 d | 181 |
| `source-status-checks` | Exact replay of source status checks. | 0–1 d | 2 |
| `study-design-and-clearance-response-checks` | Exact replay of study design and clearance response checks. | 0–1 d | 2 |
| `supplement-s1-and-appendix-checks` | Exact replay of supplement s1 and appendix checks. | 0–1 d | 2 |
| `supplement-s2-response-toxicity-checks` | Exact replay of supplement s2 response toxicity checks. | 0–1 d | 2 |
| `supplement-s3-quartile-checks` | Exact replay of supplement s3 quartile checks. | 0–1 d | 2 |
| `table2-final-parameter-checks` | Exact replay of table2 final parameter checks. | 0–1 d | 2 |
| `typical-male-3mgkg-q2w-dynamic-probe` | A deterministic fixed-effect simulation using the final two-compartment model, 80 kg receiving the average 240 mg every 14 days for 12 cycles. | 0–168 d | 181 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_L` | Nivolumab concentration in the central compartment | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_hurkmans_2019_nivolumab_real_world_poppk_cl_response --model-version 0.1.0 --scenario typical-male-3mgkg-q2w-dynamic-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 215 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `BSA_m2` | `1` |
| `BSA_ref_m2` | `1` |
| `CL_L_day` | `1` |
| `CL_covariate_factor` | `1` |
| `CL_individual_L_day` | `1` |
| `Q_L_day` | `1` |
| `V1_L` | `1` |
| `V2_L` | `1` |
| `albumin_g_L` | `1` |
| `albumin_ref_g_L` | `1` |
| `appendix_final_cl_l_day` | `1` |
| `appendix_final_cl_l_day_from_l_h` | `1` |
| `appendix_final_cl_l_h` | `1` |
| `appendix_final_clalb` | `1` |
| `appendix_final_clbsa` | `1` |
| `appendix_final_clsex` | `1` |
| `appendix_final_omega_iiv_cl` | `1` |
| `appendix_final_q_l_day` | `1` |
| `appendix_final_q_l_day_from_l_h` | `1` |
| `appendix_final_q_l_h` | `1` |
| `appendix_final_sigma_prop` | `1` |
| `appendix_final_v1_l` | `1` |
| `appendix_initial_cl_l_day` | `1` |
| `appendix_initial_cl_l_day_from_l_h` | `1` |
| `appendix_initial_cl_l_h` | `1` |
| `appendix_initial_omega_iiv_cl` | `1` |
| `appendix_initial_q_l_day` | `1` |
| `appendix_initial_q_l_day_from_l_h` | `1` |
| `appendix_initial_q_l_h` | `1` |
| `appendix_initial_sigma_prop` | `1` |
| `appendix_initial_v1_l` | `1` |
| `article_pdf_fetched_flag` | `1` |
| `article_pdf_pages` | `1` |
| `average_cycles_per_patient` | `1` |
| `average_dose_mg` | `1` |
| `average_pk_measurements_per_patient` | `1` |
| `baseline_covariates_significant_n` | `1` |
| `central_conc_mg_L` | `1` |
| `central_conc_ug_mL` | `1` |
| `cl_albumin_threshold_factor` | `1` |
| `cl_bsa_threshold_factor` | `1` |
| `cl_female_ref_L_day` | `1` |
| `cl_female_ref_ratio` | `1` |
| `crossref_cited_by_count` | `1` |
| `dose_interval_days` | `1` |
| `dose_iqr_high_mg` | `1` |
| `dose_iqr_low_mg` | `1` |
| `dose_mg_per_kg` | `1` |
| `europepmc_cited_by_count` | `1` |
| `europepmc_fulltext_xml_available_flag` | `1` |
| `female_indicator` | `1` |
| `female_n` | `1` |
| `female_percent` | `1` |
| `followup_iqr_high_days` | `1` |
| `followup_iqr_low_days` | `1` |
| `intensive_sampling_patients_n` | `1` |
| `later_sampling_interval_weeks` | `1` |
| `male_n` | `1` |
| `male_percent` | `1` |
| `median_followup_days` | `1` |
| `nsclc_pd_cl_ci_high` | `1` |
| `nsclc_pd_cl_ci_low` | `1` |
| `nsclc_pd_cl_mean_l_day` | `1` |
| `nsclc_pd_vs_prcr_higher_percent` | `1` |
| `nsclc_pr_cr_cl_ci_high` | `1` |
| `nsclc_pr_cr_cl_ci_low` | `1` |
| `nsclc_pr_cr_cl_mean_l_day` | `1` |
| `patients_total_n` | `1` |
| `pk_samples_total_n` | `1` |
| `pmc_fulltext_html_available_flag` | `1` |
| `pmc_pow_placeholders_quarantined_count` | `1` |
| `pmcid_numeric` | `1` |
| `pmid` | `1` |
| `preprint_found_flag` | `1` |
| `publication_year` | `1` |
| `queue_citation_rank` | `1` |
| `queue_cited_by_count` | `1` |
| `queue_refined_rank` | `1` |
| `reported_albumin_threshold_g_l` | `1` |
| `reported_bsa_threshold_m2` | `1` |
| `reported_men_mean_cl_l_day` | `1` |
| `reported_threshold_cl_increase_percent` | `1` |
| `reported_women_cl_lower_percent` | `1` |
| `reported_women_mean_cl_l_day` | `1` |
| `scenario_body_weight_kg` | `1` |
| `scenario_dose_amount_mg` | `1` |
| `scenario_dose_mg_per_kg` | `1` |
| `scenario_doses_count` | `1` |
| `scenario_dosing_interval_days` | `1` |
| `scenario_infusion_duration_h` | `1` |
| `supp_s1_age_dofd` | `1` |
| `supp_s1_age_estimate` | `1` |
| `supp_s1_albumin_dofd` | `1` |
| `supp_s1_albumin_estimate` | `1` |
| `supp_s1_bsa_dofd` | `1` |
| `supp_s1_bsa_estimate` | `1` |
| `supp_s1_ckd_dofd` | `1` |
| `supp_s1_ckd_estimate` | `1` |
| `supp_s1_creatinine_dofd` | `1` |
| `supp_s1_creatinine_estimate` | `1` |
| `supp_s1_female_vs_male_dofd` | `1` |
| `supp_s1_female_vs_male_estimate` | `1` |
| `supp_s1_ld_estimate` | `1` |
| `supp_s1_leucocytes_dofd` | `1` |
| `supp_s1_leucocytes_estimate` | `1` |
| `supp_s1_melanoma_vs_other_dofd` | `1` |
| `supp_s1_melanoma_vs_other_estimate` | `1` |
| `supp_s1_nsclc_vs_other_dofd` | `1` |
| `supp_s1_nsclc_vs_other_estimate` | `1` |
| `supp_s1_total_protein_dofd` | `1` |
| `supp_s1_total_protein_estimate` | `1` |
| `supp_s1_tumor_burden_dofd` | `1` |
| `supp_s1_tumor_burden_estimate` | `1` |
| `supp_s1_weight_dofd` | `1` |
| `supp_s1_weight_estimate` | `1` |
| `supp_s1_weight_loss_dofd` | `1` |
| `supp_s1_weight_loss_estimate` | `1` |
| `supp_s1_who0_dofd` | `1` |
| `supp_s1_who0_estimate` | `1` |
| `supp_s2_irae_grade0_2_total_n` | `1` |
| `supp_s2_irae_grade0_2_total_percent` | `1` |
| `supp_s2_irae_grade_gt3_total_n` | `1` |
| `supp_s2_irae_grade_gt3_total_percent` | `1` |
| `supp_s2_irae_unknown_total_n` | `1` |
| `supp_s2_irae_unknown_total_percent` | `1` |
| `supp_s2_melanoma_pd_n` | `1` |
| `supp_s2_melanoma_prcr_n` | `1` |
| `supp_s2_melanoma_sd_n` | `1` |
| `supp_s2_nonevaluable_total_n` | `1` |
| `supp_s2_nonevaluable_total_percent` | `1` |
| `supp_s2_nsclc_nonevaluable_n` | `1` |
| `supp_s2_nsclc_pd_n` | `1` |
| `supp_s2_nsclc_prcr_n` | `1` |
| `supp_s2_nsclc_sd_n` | `1` |
| `supp_s2_pd_total_n` | `1` |
| `supp_s2_pd_total_percent` | `1` |
| `supp_s2_prcr_total_n` | `1` |
| `supp_s2_prcr_total_percent` | `1` |
| `supp_s2_rcc_nonevaluable_n` | `1` |
| `supp_s2_rcc_pd_n` | `1` |
| `supp_s2_rcc_prcr_n` | `1` |
| `supp_s2_rcc_sd_n` | `1` |
| `supp_s2_sd_total_n` | `1` |
| `supp_s2_sd_total_percent` | `1` |
| `supp_s3_q1_albumin_median_g_l` | `1` |
| `supp_s3_q1_bsa_median_m2` | `1` |
| `supp_s3_q1_female_n` | `1` |
| `supp_s3_q1_male_n` | `1` |
| `supp_s3_q1_nsclc_n` | `1` |
| `supp_s3_q2_albumin_median_g_l` | `1` |
| `supp_s3_q2_bsa_median_m2` | `1` |
| `supp_s3_q2_female_n` | `1` |
| `supp_s3_q2_male_n` | `1` |
| `supp_s3_q2_nsclc_n` | `1` |
| `supp_s3_q3_albumin_median_g_l` | `1` |
| `supp_s3_q3_bsa_median_m2` | `1` |
| `supp_s3_q3_female_n` | `1` |
| `supp_s3_q3_male_n` | `1` |
| `supp_s3_q3_nsclc_n` | `1` |
| `supp_s3_q4_albumin_median_g_l` | `1` |
| `supp_s3_q4_bsa_median_m2` | `1` |
| `supp_s3_q4_female_n` | `1` |
| `supp_s3_q4_male_n` | `1` |
| `supp_s3_q4_nsclc_n` | `1` |
| `supplement_docx_fetched_flag` | `1` |
| `supplement_media_images_count` | `1` |
| `table2_albumin_cl_effect` | `1` |
| `table2_albumin_cl_effect_ci_high` | `1` |
| `table2_albumin_cl_effect_ci_low` | `1` |
| `table2_albumin_cl_effect_rse_percent` | `1` |
| `table2_bsa_cl_effect` | `1` |
| `table2_bsa_cl_effect_ci_high` | `1` |
| `table2_bsa_cl_effect_ci_low` | `1` |
| `table2_bsa_cl_effect_rse_percent` | `1` |
| `table2_cl_bootstrap` | `1` |
| `table2_cl_ci_high` | `1` |
| `table2_cl_ci_low` | `1` |
| `table2_cl_l_day` | `1` |
| `table2_cl_rse_percent` | `1` |
| `table2_cl_shrinkage_percent` | `1` |
| `table2_female_cl_effect` | `1` |
| `table2_female_cl_effect_ci_high` | `1` |
| `table2_female_cl_effect_ci_low` | `1` |
| `table2_female_cl_effect_rse_percent` | `1` |
| `table2_iiv_cl_bootstrap` | `1` |
| `table2_iiv_cl_ci_high` | `1` |
| `table2_iiv_cl_ci_low` | `1` |
| `table2_iiv_cl_cv_percent` | `1` |
| `table2_iiv_cl_rse_percent` | `1` |
| `table2_prop_error_bootstrap` | `1` |
| `table2_prop_error_ci_high` | `1` |
| `table2_prop_error_ci_low` | `1` |
| `table2_prop_error_cv_percent` | `1` |
| `table2_prop_error_rse_percent` | `1` |
| `table2_prop_error_shrinkage_percent` | `1` |
| `table2_q_bootstrap` | `1` |
| `table2_q_ci_high` | `1` |
| `table2_q_ci_low` | `1` |
| `table2_q_l_day` | `1` |
| `table2_q_rse_upper_percent` | `1` |
| `table2_v1_bootstrap` | `1` |
| `table2_v1_ci_high` | `1` |
| `table2_v1_ci_low` | `1` |
| `table2_v1_l` | `1` |
| `table2_v1_rse_percent` | `1` |
| `table2_v2_bootstrap` | `1` |
| `table2_v2_ci_high` | `1` |
| `table2_v2_ci_low` | `1` |
| `table2_v2_l` | `1` |
| `table2_v2_rse_percent` | `1` |
| `theta_BSA_CL` | `1` |
| `theta_albumin_CL` | `1` |
| `theta_female_CL` | `1` |
| `trough_sampling_weeks_initial` | `1` |
| `validation_run_nonce` | `1` |
| `state__AUC` | `mg*day/L` |
| `state__A_central` | `mg` |
| `state__A_peripheral` | `mg` |
| `state__elapsed_time` | `day` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `typical-male-3mgkg-q2w-dynamic-probe` starter has **181 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_L` | 0 | 0 (0 d, post) | 127.514 (154.042 d, pre) | 58.7931 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
