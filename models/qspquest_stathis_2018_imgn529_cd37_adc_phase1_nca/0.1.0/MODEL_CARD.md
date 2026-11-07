# Stathis 2018 IMGN529 NCA Replay and Exploratory Dose-Level PK Surrogate

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect IMGN529 NCA endpoints and exploratory exposure curves.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.1.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_stathis_2018_imgn529_cd37_adc_phase1_nca/0.1.0/model.omex',
    expected_sha256='6cc51e679c77270f4881e1e86747e89ff79b1c555ec807155d23c51721519197',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

<details>
<summary>Browse all 17 runnable experiments</summary>

| Archived experiment ID | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `stathis-dose-0p1-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-0p2-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-0p4-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-0p7-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-0p8-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-1p0-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-1p4-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-dose-1p8-exponential-probe` | Paper-endpoint probe initialized at the reported Cmax and eliminated with the reported half-life. It is not a paper-reported structural model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-0p1-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-0p2-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-0p4-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-0p7-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-0p8-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-1p0-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-1p4-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-exploratory-calibrated-dose-1p8-joint-table4` | Exploratory aggregate one-state ODE using the same five global dose-trend parameters fitted jointly to all eight Table 4 cohorts. Separate from the paper-endpoint probe and not a paper model. | 0–504 h | 253 |
| `stathis-table-exact-anchor` | Exact API replay of 377 numeric fields from Tables 1-5, Supplement Table S1, and source availability. | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `state__plasma_imgn529_ug_mL` | IMGN529 plasma concentration in the exponential probe | `ug/mL` |
| `state__auc_h_ug_mL` | Accumulated IMGN529 plasma exposure | `h*ug/mL` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 399 outputs and 3 states</summary>

| Technical column | Unit |
| --- | --- |
| `age_max_year` | `1` |
| `age_median_year` | `1` |
| `age_min_year` | `1` |
| `calibrated_aucinf_h_ug_mL` | `1` |
| `calibrated_cl_linear_per_kg` | `1` |
| `calibrated_cl_tmdd_per_kg` | `1` |
| `calibrated_clearance_per_kg_L_h_kg` | `1` |
| `calibrated_cmax_power` | `1` |
| `calibrated_cmax_scale` | `1` |
| `calibrated_cmax_ug_mL` | `1` |
| `calibrated_ec50_mg_kg` | `1` |
| `calibrated_half_life_h` | `1` |
| `calibrated_hill` | `1` |
| `calibrated_kel_h_inv` | `1` |
| `citation_rank` | `1` |
| `cited_by_count` | `1` |
| `clinicaltrials_nct1534715_flag` | `1` |
| `complete_response_total_n` | `1` |
| `cycle1_day` | `1` |
| `cycles_ge3_n` | `1` |
| `cycles_ge3_percent` | `1` |
| `cycles_range_max` | `1` |
| `cycles_range_min` | `1` |
| `dexamethasone_iv_premed_mg` | `1` |
| `dlbcl_n` | `1` |
| `dlbcl_percent` | `1` |
| `dlbcl_response_rate_percent` | `1` |
| `dose_interval_days` | `1` |
| `europepmc_fulltext_xml_flag` | `1` |
| `female_n` | `1` |
| `female_percent` | `1` |
| `figure1_pdf_embedded_raster_count` | `1` |
| `figure1a_new_lesion_asterisk_count` | `1` |
| `figure1a_patient_bar_count` | `1` |
| `follicular_lymphoma_n` | `1` |
| `follicular_lymphoma_percent` | `1` |
| `grade34_neutropenia_percent` | `1` |
| `growth_factor_start_day_max` | `1` |
| `growth_factor_start_day_min` | `1` |
| `home_dexamethasone_mg` | `1` |
| `initial_dose_mg_kg` | `1` |
| `kel_h_inv` | `1` |
| `male_n` | `1` |
| `male_percent` | `1` |
| `mantle_cell_lymphoma_n` | `1` |
| `mantle_cell_lymphoma_percent` | `1` |
| `marginal_zone_lymphoma_n` | `1` |
| `marginal_zone_lymphoma_percent` | `1` |
| `mt_d_not_reached_flag` | `1` |
| `mtd_mg_kg` | `1` |
| `overall_response_rate_percent` | `1` |
| `paper_exponential_aucinf_h_ug_mL` | `1` |
| `paper_kel_h_inv` | `1` |
| `paper_year` | `1` |
| `partial_response_total_n` | `1` |
| `patients_enrolled_n` | `1` |
| `pk_assay_lloq_ng_mL` | `1` |
| `pmc_html_available_flag` | `1` |
| `prior_systemic_therapy_max_n` | `1` |
| `prior_systemic_therapy_median_n` | `1` |
| `prior_systemic_therapy_min_n` | `1` |
| `progressive_disease_total_n` | `1` |
| `r2pd_mg_kg` | `1` |
| `real_article_pdf_binary_count` | `1` |
| `real_supplement_binary_count` | `1` |
| `refined_rank` | `1` |
| `response_evaluable_n` | `1` |
| `safety_population_n` | `1` |
| `selected_aucinf_h_ug_mL` | `1` |
| `selected_cl_L_h` | `1` |
| `selected_cmax_ug_mL` | `1` |
| `selected_dose_mg_kg` | `1` |
| `selected_half_life_h` | `1` |
| `selected_vz_L` | `1` |
| `stable_disease_total_n` | `1` |
| `steroid_prophylaxis_start_dose_mg_kg` | `1` |
| `supp_s1_cr_n` | `1` |
| `supp_s1_dlbcl_n` | `1` |
| `supp_s1_duration_max_months` | `1` |
| `supp_s1_duration_median_months` | `1` |
| `supp_s1_duration_min_months` | `1` |
| `supp_s1_fl_n` | `1` |
| `supp_s1_gcb_dlbcl_n` | `1` |
| `supp_s1_non_gcb_dlbcl_n` | `1` |
| `supp_s1_pr_n` | `1` |
| `supp_s1_responder_1_dose_mg_kg` | `1` |
| `supp_s1_responder_1_duration_months` | `1` |
| `supp_s1_responder_2_dose_mg_kg` | `1` |
| `supp_s1_responder_2_duration_months` | `1` |
| `supp_s1_responder_3_dose_mg_kg` | `1` |
| `supp_s1_responder_3_duration_months` | `1` |
| `supp_s1_responder_4_dose_mg_kg` | `1` |
| `supp_s1_responder_4_duration_months` | `1` |
| `supp_s1_responder_5_dose_mg_kg` | `1` |
| `supp_s1_responder_5_duration_months` | `1` |
| `supp_s1_responder_n` | `1` |
| `supp_s1_unclassified_dlbcl_n` | `1` |
| `supplement_links_detected_count` | `1` |
| `table1_previous_autologous_transplant_n` | `1` |
| `table1_previous_autologous_transplant_percent` | `1` |
| `table1_previous_radiotherapy_n` | `1` |
| `table1_previous_radiotherapy_percent` | `1` |
| `table1_prior_therapy_1_n` | `1` |
| `table1_prior_therapy_1_percent` | `1` |
| `table1_prior_therapy_2_n` | `1` |
| `table1_prior_therapy_2_percent` | `1` |
| `table1_prior_therapy_ge3_n` | `1` |
| `table1_prior_therapy_ge3_percent` | `1` |
| `table1_stage_i_n` | `1` |
| `table1_stage_i_percent` | `1` |
| `table1_stage_ii_n` | `1` |
| `table1_stage_ii_percent` | `1` |
| `table1_stage_iii_n` | `1` |
| `table1_stage_iii_percent` | `1` |
| `table1_stage_iv_n` | `1` |
| `table1_stage_iv_percent` | `1` |
| `table2_dlt_evaluable_n` | `1` |
| `table2_dose_0p1_none_dlt_n` | `1` |
| `table2_dose_0p1_none_n` | `1` |
| `table2_dose_0p2_none_dlt_n` | `1` |
| `table2_dose_0p2_none_n` | `1` |
| `table2_dose_0p4_none_dlt_n` | `1` |
| `table2_dose_0p4_none_n` | `1` |
| `table2_dose_0p4_steroids_dlt_n` | `1` |
| `table2_dose_0p4_steroids_n` | `1` |
| `table2_dose_0p7_steroids_dlt_n` | `1` |
| `table2_dose_0p7_steroids_n` | `1` |
| `table2_dose_0p8_none_dlt_n` | `1` |
| `table2_dose_0p8_none_n` | `1` |
| `table2_dose_1p0_steroids_dlt_n` | `1` |
| `table2_dose_1p0_steroids_gcsf_dlt_n` | `1` |
| `table2_dose_1p0_steroids_gcsf_n` | `1` |
| `table2_dose_1p0_steroids_n` | `1` |
| `table2_dose_1p4_steroids_gcsf_dlt_n` | `1` |
| `table2_dose_1p4_steroids_gcsf_n` | `1` |
| `table2_dose_1p8_steroids_gcsf_dlt_n` | `1` |
| `table2_dose_1p8_steroids_gcsf_n` | `1` |
| `table3_anemia_g12_n` | `1` |
| `table3_anemia_g12_percent` | `1` |
| `table3_anemia_g3_n` | `1` |
| `table3_anemia_g3_percent` | `1` |
| `table3_anemia_g4_n` | `1` |
| `table3_anemia_g4_percent` | `1` |
| `table3_asthenia_g12_n` | `1` |
| `table3_asthenia_g12_percent` | `1` |
| `table3_asthenia_g3_n` | `1` |
| `table3_asthenia_g3_percent` | `1` |
| `table3_asthenia_g4_n` | `1` |
| `table3_asthenia_g4_percent` | `1` |
| `table3_chills_g12_n` | `1` |
| `table3_chills_g12_percent` | `1` |
| `table3_chills_g3_n` | `1` |
| `table3_chills_g3_percent` | `1` |
| `table3_chills_g4_n` | `1` |
| `table3_chills_g4_percent` | `1` |
| `table3_constipation_g12_n` | `1` |
| `table3_constipation_g12_percent` | `1` |
| `table3_constipation_g3_n` | `1` |
| `table3_constipation_g3_percent` | `1` |
| `table3_constipation_g4_n` | `1` |
| `table3_constipation_g4_percent` | `1` |
| `table3_decreased_appetite_g12_n` | `1` |
| `table3_decreased_appetite_g12_percent` | `1` |
| `table3_decreased_appetite_g3_n` | `1` |
| `table3_decreased_appetite_g3_percent` | `1` |
| `table3_decreased_appetite_g4_n` | `1` |
| `table3_decreased_appetite_g4_percent` | `1` |
| `table3_decreased_platelet_count_g12_n` | `1` |
| `table3_decreased_platelet_count_g12_percent` | `1` |
| `table3_decreased_platelet_count_g3_n` | `1` |
| `table3_decreased_platelet_count_g3_percent` | `1` |
| `table3_decreased_platelet_count_g4_n` | `1` |
| `table3_decreased_platelet_count_g4_percent` | `1` |
| `table3_diarrhea_g12_n` | `1` |
| `table3_diarrhea_g12_percent` | `1` |
| `table3_diarrhea_g3_n` | `1` |
| `table3_diarrhea_g3_percent` | `1` |
| `table3_diarrhea_g4_n` | `1` |
| `table3_diarrhea_g4_percent` | `1` |
| `table3_dyspnea_g12_n` | `1` |
| `table3_dyspnea_g12_percent` | `1` |
| `table3_dyspnea_g3_n` | `1` |
| `table3_dyspnea_g3_percent` | `1` |
| `table3_dyspnea_g4_n` | `1` |
| `table3_dyspnea_g4_percent` | `1` |
| `table3_fatigue_g12_n` | `1` |
| `table3_fatigue_g12_percent` | `1` |
| `table3_fatigue_g3_n` | `1` |
| `table3_fatigue_g3_percent` | `1` |
| `table3_fatigue_g4_n` | `1` |
| `table3_fatigue_g4_percent` | `1` |
| `table3_febrile_neutropenia_g12_n` | `1` |
| `table3_febrile_neutropenia_g12_percent` | `1` |
| `table3_febrile_neutropenia_g3_n` | `1` |
| `table3_febrile_neutropenia_g3_percent` | `1` |
| `table3_febrile_neutropenia_g4_n` | `1` |
| `table3_febrile_neutropenia_g4_percent` | `1` |
| `table3_hyperglycemia_g12_n` | `1` |
| `table3_hyperglycemia_g12_percent` | `1` |
| `table3_hyperglycemia_g3_n` | `1` |
| `table3_hyperglycemia_g3_percent` | `1` |
| `table3_hyperglycemia_g4_n` | `1` |
| `table3_hyperglycemia_g4_percent` | `1` |
| `table3_hypokalemia_g12_n` | `1` |
| `table3_hypokalemia_g12_percent` | `1` |
| `table3_hypokalemia_g3_n` | `1` |
| `table3_hypokalemia_g3_percent` | `1` |
| `table3_hypokalemia_g4_n` | `1` |
| `table3_hypokalemia_g4_percent` | `1` |
| `table3_increased_alt_g12_n` | `1` |
| `table3_increased_alt_g12_percent` | `1` |
| `table3_increased_alt_g3_n` | `1` |
| `table3_increased_alt_g3_percent` | `1` |
| `table3_increased_alt_g4_n` | `1` |
| `table3_increased_alt_g4_percent` | `1` |
| `table3_increased_ast_g12_n` | `1` |
| `table3_increased_ast_g12_percent` | `1` |
| `table3_increased_ast_g3_n` | `1` |
| `table3_increased_ast_g3_percent` | `1` |
| `table3_increased_ast_g4_n` | `1` |
| `table3_increased_ast_g4_percent` | `1` |
| `table3_leukopenia_g12_n` | `1` |
| `table3_leukopenia_g12_percent` | `1` |
| `table3_leukopenia_g3_n` | `1` |
| `table3_leukopenia_g3_percent` | `1` |
| `table3_leukopenia_g4_n` | `1` |
| `table3_leukopenia_g4_percent` | `1` |
| `table3_muscular_weakness_g12_n` | `1` |
| `table3_muscular_weakness_g12_percent` | `1` |
| `table3_muscular_weakness_g3_n` | `1` |
| `table3_muscular_weakness_g3_percent` | `1` |
| `table3_muscular_weakness_g4_n` | `1` |
| `table3_muscular_weakness_g4_percent` | `1` |
| `table3_nausea_g12_n` | `1` |
| `table3_nausea_g12_percent` | `1` |
| `table3_nausea_g3_n` | `1` |
| `table3_nausea_g3_percent` | `1` |
| `table3_nausea_g4_n` | `1` |
| `table3_nausea_g4_percent` | `1` |
| `table3_neutropenia_g12_n` | `1` |
| `table3_neutropenia_g12_percent` | `1` |
| `table3_neutropenia_g3_n` | `1` |
| `table3_neutropenia_g3_percent` | `1` |
| `table3_neutropenia_g4_n` | `1` |
| `table3_neutropenia_g4_percent` | `1` |
| `table3_odema_peripheral_g12_n` | `1` |
| `table3_odema_peripheral_g12_percent` | `1` |
| `table3_odema_peripheral_g3_n` | `1` |
| `table3_odema_peripheral_g3_percent` | `1` |
| `table3_odema_peripheral_g4_n` | `1` |
| `table3_odema_peripheral_g4_percent` | `1` |
| `table3_pneumonia_g12_n` | `1` |
| `table3_pneumonia_g12_percent` | `1` |
| `table3_pneumonia_g3_n` | `1` |
| `table3_pneumonia_g3_percent` | `1` |
| `table3_pneumonia_g4_n` | `1` |
| `table3_pneumonia_g4_percent` | `1` |
| `table3_pyrexia_g12_n` | `1` |
| `table3_pyrexia_g12_percent` | `1` |
| `table3_pyrexia_g3_n` | `1` |
| `table3_pyrexia_g3_percent` | `1` |
| `table3_pyrexia_g4_n` | `1` |
| `table3_pyrexia_g4_percent` | `1` |
| `table3_thrombocytopenia_g12_n` | `1` |
| `table3_thrombocytopenia_g12_percent` | `1` |
| `table3_thrombocytopenia_g3_n` | `1` |
| `table3_thrombocytopenia_g3_percent` | `1` |
| `table3_thrombocytopenia_g4_n` | `1` |
| `table3_thrombocytopenia_g4_percent` | `1` |
| `table4_dose_0p1_aucinf_h_ug_mL` | `1` |
| `table4_dose_0p1_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_0p1_cl_L_h` | `1` |
| `table4_dose_0p1_cl_sd_L_h` | `1` |
| `table4_dose_0p1_cmax_sd_ug_mL` | `1` |
| `table4_dose_0p1_cmax_ug_mL` | `1` |
| `table4_dose_0p1_half_life_h` | `1` |
| `table4_dose_0p1_half_life_sd_h` | `1` |
| `table4_dose_0p1_mg_kg` | `1` |
| `table4_dose_0p1_n` | `1` |
| `table4_dose_0p1_vz_L` | `1` |
| `table4_dose_0p1_vz_sd_L` | `1` |
| `table4_dose_0p2_aucinf_h_ug_mL` | `1` |
| `table4_dose_0p2_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_0p2_cl_L_h` | `1` |
| `table4_dose_0p2_cl_sd_L_h` | `1` |
| `table4_dose_0p2_cmax_sd_ug_mL` | `1` |
| `table4_dose_0p2_cmax_ug_mL` | `1` |
| `table4_dose_0p2_half_life_h` | `1` |
| `table4_dose_0p2_half_life_sd_h` | `1` |
| `table4_dose_0p2_mg_kg` | `1` |
| `table4_dose_0p2_n` | `1` |
| `table4_dose_0p2_vz_L` | `1` |
| `table4_dose_0p2_vz_sd_L` | `1` |
| `table4_dose_0p4_aucinf_h_ug_mL` | `1` |
| `table4_dose_0p4_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_0p4_cl_L_h` | `1` |
| `table4_dose_0p4_cl_sd_L_h` | `1` |
| `table4_dose_0p4_cmax_sd_ug_mL` | `1` |
| `table4_dose_0p4_cmax_ug_mL` | `1` |
| `table4_dose_0p4_half_life_h` | `1` |
| `table4_dose_0p4_half_life_sd_h` | `1` |
| `table4_dose_0p4_mg_kg` | `1` |
| `table4_dose_0p4_n` | `1` |
| `table4_dose_0p4_vz_L` | `1` |
| `table4_dose_0p4_vz_sd_L` | `1` |
| `table4_dose_0p7_aucinf_h_ug_mL` | `1` |
| `table4_dose_0p7_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_0p7_cl_L_h` | `1` |
| `table4_dose_0p7_cl_sd_L_h` | `1` |
| `table4_dose_0p7_cmax_sd_ug_mL` | `1` |
| `table4_dose_0p7_cmax_ug_mL` | `1` |
| `table4_dose_0p7_half_life_h` | `1` |
| `table4_dose_0p7_half_life_sd_h` | `1` |
| `table4_dose_0p7_mg_kg` | `1` |
| `table4_dose_0p7_n` | `1` |
| `table4_dose_0p7_vz_L` | `1` |
| `table4_dose_0p7_vz_sd_L` | `1` |
| `table4_dose_0p8_aucinf_h_ug_mL` | `1` |
| `table4_dose_0p8_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_0p8_cl_L_h` | `1` |
| `table4_dose_0p8_cl_sd_L_h` | `1` |
| `table4_dose_0p8_cmax_sd_ug_mL` | `1` |
| `table4_dose_0p8_cmax_ug_mL` | `1` |
| `table4_dose_0p8_half_life_h` | `1` |
| `table4_dose_0p8_half_life_sd_h` | `1` |
| `table4_dose_0p8_mg_kg` | `1` |
| `table4_dose_0p8_n` | `1` |
| `table4_dose_0p8_vz_L` | `1` |
| `table4_dose_0p8_vz_sd_L` | `1` |
| `table4_dose_1p0_aucinf_h_ug_mL` | `1` |
| `table4_dose_1p0_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_1p0_cl_L_h` | `1` |
| `table4_dose_1p0_cl_sd_L_h` | `1` |
| `table4_dose_1p0_cmax_sd_ug_mL` | `1` |
| `table4_dose_1p0_cmax_ug_mL` | `1` |
| `table4_dose_1p0_half_life_h` | `1` |
| `table4_dose_1p0_half_life_sd_h` | `1` |
| `table4_dose_1p0_mg_kg` | `1` |
| `table4_dose_1p0_n` | `1` |
| `table4_dose_1p0_vz_L` | `1` |
| `table4_dose_1p0_vz_sd_L` | `1` |
| `table4_dose_1p4_aucinf_h_ug_mL` | `1` |
| `table4_dose_1p4_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_1p4_cl_L_h` | `1` |
| `table4_dose_1p4_cl_sd_L_h` | `1` |
| `table4_dose_1p4_cmax_sd_ug_mL` | `1` |
| `table4_dose_1p4_cmax_ug_mL` | `1` |
| `table4_dose_1p4_half_life_h` | `1` |
| `table4_dose_1p4_half_life_sd_h` | `1` |
| `table4_dose_1p4_mg_kg` | `1` |
| `table4_dose_1p4_n` | `1` |
| `table4_dose_1p4_vz_L` | `1` |
| `table4_dose_1p4_vz_sd_L` | `1` |
| `table4_dose_1p8_aucinf_h_ug_mL` | `1` |
| `table4_dose_1p8_aucinf_sd_h_ug_mL` | `1` |
| `table4_dose_1p8_cl_L_h` | `1` |
| `table4_dose_1p8_cl_sd_L_h` | `1` |
| `table4_dose_1p8_cmax_sd_ug_mL` | `1` |
| `table4_dose_1p8_cmax_ug_mL` | `1` |
| `table4_dose_1p8_half_life_h` | `1` |
| `table4_dose_1p8_half_life_sd_h` | `1` |
| `table4_dose_1p8_mg_kg` | `1` |
| `table4_dose_1p8_n` | `1` |
| `table4_dose_1p8_vz_L` | `1` |
| `table4_dose_1p8_vz_sd_L` | `1` |
| `table4_pk_evaluable_n` | `1` |
| `table5_dlbcl_cr_n` | `1` |
| `table5_dlbcl_n` | `1` |
| `table5_dlbcl_orr_percent` | `1` |
| `table5_dlbcl_pd_n` | `1` |
| `table5_dlbcl_pr_n` | `1` |
| `table5_dlbcl_sd_n` | `1` |
| `table5_fl_cr_n` | `1` |
| `table5_fl_n` | `1` |
| `table5_fl_orr_percent` | `1` |
| `table5_fl_pd_n` | `1` |
| `table5_fl_pr_n` | `1` |
| `table5_fl_sd_n` | `1` |
| `table5_mcl_cr_n` | `1` |
| `table5_mcl_n` | `1` |
| `table5_mcl_orr_percent` | `1` |
| `table5_mcl_pd_n` | `1` |
| `table5_mcl_pr_n` | `1` |
| `table5_mcl_sd_n` | `1` |
| `table5_mzl_cr_n` | `1` |
| `table5_mzl_n` | `1` |
| `table5_mzl_orr_percent` | `1` |
| `table5_mzl_pd_n` | `1` |
| `table5_mzl_pr_n` | `1` |
| `table5_mzl_sd_n` | `1` |
| `table5_total_cr_n` | `1` |
| `table5_total_n` | `1` |
| `table5_total_orr_percent` | `1` |
| `table5_total_pd_n` | `1` |
| `table5_total_pr_n` | `1` |
| `table5_total_sd_n` | `1` |
| `treatment_related_saes_percent` | `1` |
| `use_exploratory_calibrated` | `1` |
| `validation_run_nonce` | `1` |
| `state__auc_h_ug_mL` | `h*ug/mL` |
| `state__elapsed_h` | `h` |
| `state__plasma_imgn529_ug_mL` | `ug/mL` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `stathis-dose-0p1-exponential-probe` starter has **253 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__plasma_imgn529_ug_mL` | 2.3 | -9.19335e-12 (212 h, post) | 2.3 (0 h, post) | -9.08074e-14 |
| `state__auc_h_ug_mL` | 0 | 0 (0 h, post) | 16.2592 (212 h, post) | 16.2592 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
