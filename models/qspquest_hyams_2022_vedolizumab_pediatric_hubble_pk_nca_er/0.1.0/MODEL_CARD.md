# Hyams 2022 Vedolizumab Pediatric HUBBLE PK/NCA/Exposure-Response Intake

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect pediatric vedolizumab exposure, NCA and response endpoints.

**Runnable · 11 experiments.** Version 0.1.0.

## Run an experiment

Reduced one-compartment IV trajectory smoke scenario. Exact validation checks only regimen, dose-per-kg, selected reported Ctrough target, and reported response scalar.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_hyams_2022_vedolizumab_pediatric_hubble_pk_nca_er', version='0.1.0')
result = model.run('ge30-high-300mg-week14-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `ada-and-safety-checks` | Exact main-text immunogenicity, exposure duration, hypersensitivity, and Table 4 safety checks. | 0–1 h | 2 |
| `baseline-population-checks` | Exact sample-size and high-level age checks from the abstract and Tables 1/3/4. | 0–1 h | 2 |
| `ge30-high-300mg-week14-probe` | Reduced one-compartment IV trajectory smoke scenario. Exact validation checks only regimen, dose-per-kg, selected reported Ctrough target, and reported response scalar. | 0–98 h | 53 |
| `ge30-low-150mg-week14-probe` | Reduced one-compartment IV trajectory smoke scenario. Exact validation checks only regimen, dose-per-kg, selected reported Ctrough target, and reported response scalar. | 0–98 h | 53 |
| `lt30-high-200mg-week14-probe` | Reduced one-compartment IV trajectory smoke scenario. Exact validation checks only regimen, dose-per-kg, selected reported Ctrough target, and reported response scalar. | 0–98 h | 53 |
| `lt30-low-100mg-week14-probe` | Reduced one-compartment IV trajectory smoke scenario. Exact validation checks only regimen, dose-per-kg, selected reported Ctrough target, and reported response scalar. | 0–98 h | 53 |
| `source-status-and-identity-checks` | Exact citation rank, corrected PMID, source-status, and article identity checks. | 0–1 h | 2 |
| `study-design-and-dosing-checks` | Exact phase 2 randomization, dosing, sampling, and analysis-population checks. | 0–1 h | 2 |
| `supplement-referenced-range-checks` | Main-text ranges for endpoints whose full by-arm tables are in the blocked DOCX supplement. | 0–1 h | 2 |
| `table3-adult-measure-response-checks` | Exact Week 14 Mayo/CDAI response counts, percentages, and exact confidence intervals. | 0–1 h | 2 |
| `week14-ctrough-checks` | Exact main-text Ctrough mean/SD checks for combined UC/CD by weight and dose. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_ug_mL` | Vedolizumab concentration | `1` |
| `cumulative_auc_ug_day_mL` | Accumulated vedolizumab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_hyams_2022_vedolizumab_pediatric_hubble_pk_nca_er --model-version 0.1.0 --scenario ge30-high-300mg-week14-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 170 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `ada_ge30_cd_n` | `1` |
| `ada_ge30_cd_percent` | `1` |
| `ada_ge30_uc_n` | `1` |
| `ada_ge30_uc_percent` | `1` |
| `ada_lt30_cd_n` | `1` |
| `ada_lt30_uc_n` | `1` |
| `ada_lt30_uc_percent` | `1` |
| `ada_persistent_n` | `1` |
| `ada_persistent_uc_n` | `1` |
| `ada_positive_n` | `1` |
| `ada_positive_percent` | `1` |
| `adult_gemini1_uc_week6_response_percent` | `1` |
| `adult_gemini2_cd_week6_cdaid100_response_percent` | `1` |
| `age_ge30_mean` | `1` |
| `age_ge30_sd` | `1` |
| `age_lt30_mean` | `1` |
| `age_lt30_sd` | `1` |
| `anaphylaxis_n` | `1` |
| `cavg_fold_increase_ge30_approx` | `1` |
| `cavg_fold_increase_lt30_approx` | `1` |
| `cd_ge30_fas_table3_n` | `1` |
| `cd_ge30_randomized_n` | `1` |
| `cd_lt30_n` | `1` |
| `cdai_remission_max_percent` | `1` |
| `cdai_remission_min_percent` | `1` |
| `cdaid100_response_max_percent` | `1` |
| `cdaid100_response_min_percent` | `1` |
| `central_concentration_ug_mL` | `1` |
| `citation_rank` | `1` |
| `cited_by_count_queue` | `1` |
| `correct_pmid` | `1` |
| `crossref_cited_by_count_fetch` | `1` |
| `csv_pmid_incorrect_flag` | `1` |
| `csv_pmid_stale_value` | `1` |
| `ctrough_ge30_high_mean_ug_mL` | `1` |
| `ctrough_ge30_high_sd_ug_mL` | `1` |
| `ctrough_ge30_high_to_low_ratio` | `1` |
| `ctrough_ge30_low_mean_ug_mL` | `1` |
| `ctrough_ge30_low_sd_ug_mL` | `1` |
| `ctrough_high_ge30_to_lt30_ratio` | `1` |
| `ctrough_low_ge30_to_lt30_ratio` | `1` |
| `ctrough_lt30_high_mean_ug_mL` | `1` |
| `ctrough_lt30_high_sd_ug_mL` | `1` |
| `ctrough_lt30_high_to_low_ratio` | `1` |
| `ctrough_lt30_low_mean_ug_mL` | `1` |
| `ctrough_lt30_low_sd_ug_mL` | `1` |
| `cumulative_auc_ug_day_mL` | `1` |
| `current_cd_ge30_combined_cdaid100_response_percent` | `1` |
| `current_cd_lt30_combined_cdaid100_response_percent` | `1` |
| `current_uc_ge30_combined_response_percent` | `1` |
| `current_uc_lt30_combined_response_percent` | `1` |
| `death_n` | `1` |
| `discontinued_due_ae_n` | `1` |
| `discontinued_due_worsening_disease_n` | `1` |
| `discontinued_total_n` | `1` |
| `dose_day1_day` | `1` |
| `dose_mg` | `1` |
| `dose_per_kg_mg_kg` | `1` |
| `dose_week14_day` | `1` |
| `dose_week2_day` | `1` |
| `dose_week6_day` | `1` |
| `europepmc_xml_fetched_flag` | `1` |
| `exposure_duration_max_day` | `1` |
| `exposure_duration_median_day` | `1` |
| `exposure_duration_min_day` | `1` |
| `final_safety_visit_after_last_dose_weeks` | `1` |
| `fit_placeholder_observed_ctrough_ug_mL` | `1` |
| `ge30_non_us_sites_n` | `1` |
| `ge30_safety_n` | `1` |
| `ge30_us_sites_n` | `1` |
| `high_dose_ge30_mg` | `1` |
| `high_dose_lt30_mg` | `1` |
| `hypersensitivity_ge30_n` | `1` |
| `hypersensitivity_ge30_percent` | `1` |
| `hypersensitivity_lt30_n` | `1` |
| `hypersensitivity_lt30_percent` | `1` |
| `infusion_reaction_n` | `1` |
| `low_dose_ge30_mg` | `1` |
| `low_dose_lt30_mg` | `1` |
| `lt30_non_us_sites_n` | `1` |
| `lt30_safety_n` | `1` |
| `lt30_us_sites_n` | `1` |
| `mayo_remission_max_percent` | `1` |
| `mayo_remission_min_percent` | `1` |
| `min_body_weight_kg` | `1` |
| `oup_cloudflare_blocked_flag` | `1` |
| `paper_year` | `1` |
| `pcdai_remission_max_percent` | `1` |
| `pcdai_remission_min_percent` | `1` |
| `pcdai_response_max_percent` | `1` |
| `pcdai_response_min_percent` | `1` |
| `pk_analysis_set_n` | `1` |
| `pk_sampling_between_week2_week6_flag` | `1` |
| `pk_sampling_postdose_day1_flag` | `1` |
| `pk_sampling_week10_flag` | `1` |
| `pk_sampling_week14_flag` | `1` |
| `pk_sampling_week1_flag` | `1` |
| `pk_sampling_week22_flag` | `1` |
| `pk_sampling_week2_flag` | `1` |
| `pk_sampling_week6_flag` | `1` |
| `planned_sample_size_n` | `1` |
| `pmc_full_text_fetched_flag` | `1` |
| `pmc_oa_tgz_advertised_flag` | `1` |
| `pmc_oa_tgz_https_404_flag` | `1` |
| `pmc_pdf_binary_fetched_flag` | `1` |
| `pucai_remission_max_percent` | `1` |
| `pucai_remission_min_percent` | `1` |
| `pucai_response_max_percent` | `1` |
| `pucai_response_min_percent` | `1` |
| `randomized_not_treated_n` | `1` |
| `reported_clinical_response_percent` | `1` |
| `reported_week14_ctrough_ug_mL` | `1` |
| `runtime_clearance_L_day` | `1` |
| `runtime_half_life_day` | `1` |
| `runtime_volume_L` | `1` |
| `safety_analysis_set_n` | `1` |
| `safety_ge30_cd_any_ae_percent` | `1` |
| `safety_ge30_cd_related_percent` | `1` |
| `safety_ge30_cd_serious_percent` | `1` |
| `safety_ge30_uc_any_ae_percent` | `1` |
| `safety_ge30_uc_related_percent` | `1` |
| `safety_ge30_uc_serious_percent` | `1` |
| `safety_lt30_cd_any_ae_percent` | `1` |
| `safety_lt30_cd_related_percent` | `1` |
| `safety_lt30_cd_serious_percent` | `1` |
| `safety_lt30_uc_any_ae_percent` | `1` |
| `safety_lt30_uc_related_percent` | `1` |
| `safety_lt30_uc_serious_percent` | `1` |
| `supplement_docx_binary_fetched_flag` | `1` |
| `supplement_docx_blocked_flag` | `1` |
| `supplement_figure_binary_fetched_flag` | `1` |
| `table3_cd_ge30_150_exact_ci_high` | `1` |
| `table3_cd_ge30_150_exact_ci_low` | `1` |
| `table3_cd_ge30_150_responder_n` | `1` |
| `table3_cd_ge30_150_responder_percent` | `1` |
| `table3_cd_ge30_300_exact_ci_high` | `1` |
| `table3_cd_ge30_300_exact_ci_low` | `1` |
| `table3_cd_ge30_300_responder_n` | `1` |
| `table3_cd_ge30_300_responder_percent` | `1` |
| `table3_cd_lt30_100_exact_ci_high` | `1` |
| `table3_cd_lt30_100_exact_ci_low` | `1` |
| `table3_cd_lt30_100_responder_n` | `1` |
| `table3_cd_lt30_100_responder_percent` | `1` |
| `table3_cd_lt30_200_exact_ci_high` | `1` |
| `table3_cd_lt30_200_exact_ci_low` | `1` |
| `table3_cd_lt30_200_responder_n` | `1` |
| `table3_cd_lt30_200_responder_percent` | `1` |
| `table3_uc_ge30_150_exact_ci_high` | `1` |
| `table3_uc_ge30_150_exact_ci_low` | `1` |
| `table3_uc_ge30_150_responder_n` | `1` |
| `table3_uc_ge30_150_responder_percent` | `1` |
| `table3_uc_ge30_300_exact_ci_high` | `1` |
| `table3_uc_ge30_300_exact_ci_low` | `1` |
| `table3_uc_ge30_300_responder_n` | `1` |
| `table3_uc_ge30_300_responder_percent` | `1` |
| `table3_uc_lt30_100_exact_ci_high` | `1` |
| `table3_uc_lt30_100_exact_ci_low` | `1` |
| `table3_uc_lt30_100_responder_n` | `1` |
| `table3_uc_lt30_100_responder_percent` | `1` |
| `table3_uc_lt30_200_exact_ci_high` | `1` |
| `table3_uc_lt30_200_exact_ci_low` | `1` |
| `table3_uc_lt30_200_responder_n` | `1` |
| `table3_uc_lt30_200_responder_percent` | `1` |
| `total_randomized_n` | `1` |
| `treatment_related_ae_n` | `1` |
| `treatment_related_ae_percent` | `1` |
| `uc_ge30_n` | `1` |
| `uc_lt30_n` | `1` |
| `week22_day` | `1` |
| `weight_threshold_kg` | `1` |
| `state__AUC_ug_day_mL` | `ug*day/mL` |
| `state__A_central_mg` | `mg` |
| `state__elapsed_time_day` | `day` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `ge30-high-300mg-week14-probe` starter has **53 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_ug_mL` | 0 | 0 (0 h, post) | 140.774 (14.0208 h, pre) | 7.91348 |
| `cumulative_auc_ug_day_mL` | 0 | 0 (0 h, post) | 5501.61 (98 h, pre) | 5501.61 |

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
Evidence identity: `sha256:cf45229f15ff5d9da46fe2949bb5c457f61d839e564719f00e501dc9f7679aa6`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-limited pediatric vedolizumab HUBBLE phase 2 PK/NCA and exposure-response intake model. Exact scenarios reproduce main-text dosing, sampling, Ctrough, response, ADA, and safety values. The dynamic runtime is a reduced one-compartment IV shell for dose/smoke testing and must not be treated as the unpublished compartmental/NCA analysis until the DOCX supplement is available.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
