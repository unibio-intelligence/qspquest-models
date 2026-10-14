# Enfortumab vedotin ADC–payload exposure: exploratory reduced model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore reduced ADC and payload exposure; this is not the original full PBPK mechanism.

**Runnable · 8 experiments.** Version 0.1.0.

## Run an experiment

Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_choules_2024_enfortumab_vedotin_adc_pbpk_ddi', version='0.1.0')
result = model.run('ev-1p0-single-dose-reduced-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `ev-1p0-single-dose-reduced-ode` | Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity. | 0–7 h | 142 |
| `ev-1p25-multiple-dose-reduced-ode` | Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity. | 0–28 h | 564 |
| `ev-1p25-single-dose-reduced-ode` | Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity. | 0–7 h | 142 |
| `ev-mmae-ketoconazole-ddi-reduced-ode` | Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity. | 0–7 h | 142 |
| `ev-mmae-rifampin-ddi-reduced-ode` | Source-limited concentration-domain reduced ODE for enfortumab vedotin conjugated antibody and unconjugated MMAE. The proprietary Simcyp ADC/full PBPK workspace and virtual population are not public, so paper endpoints are overlaid rather than claiming full PBPK parity. | 0–7 h | 142 |
| `exploratory-calibrated-ev-1p0-single-dose-reduced-ode` | Exploratory reduced-ODE scenario calibrated to digitized Choules 2024 paper Simcyp curve samples. This is not the paper fixed-effect Simcyp ADC/PBPK model and does not estimate population/random effects. | 0–7 h | 142 |
| `exploratory-calibrated-ev-1p25-multiple-dose-reduced-ode` | Exploratory reduced-ODE scenario calibrated to digitized Choules 2024 paper Simcyp curve samples. This is not the paper fixed-effect Simcyp ADC/PBPK model and does not estimate population/random effects. | 0–28 h | 564 |
| `exploratory-calibrated-ev-1p25-single-dose-reduced-ode` | Exploratory reduced-ODE scenario calibrated to digitized Choules 2024 paper Simcyp curve samples. This is not the paper fixed-effect Simcyp ADC/PBPK model and does not estimate population/random effects. | 0–7 h | 142 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `adc_conc_ug_ml` | Enfortumab vedotin concentration | `1` |
| `mmae_conc_ng_ml` | Released MMAE payload concentration | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_choules_2024_enfortumab_vedotin_adc_pbpk_ddi --model-version 0.1.0 --scenario ev-1p0-single-dose-reduced-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 394 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `adc_conc_ug_ml` | `1` |
| `auc_adc_ug_day_ml` | `1` |
| `auc_mmae_ng_day_ml` | `1` |
| `citation_rank` | `1` |
| `crossref_is_referenced_by_count` | `1` |
| `europepmc_cited_by_count` | `1` |
| `ev_adc_dar0_percent` | `1` |
| `ev_adc_dar1_percent` | `1` |
| `ev_adc_dar2_percent` | `1` |
| `ev_adc_dar3_percent` | `1` |
| `ev_adc_dar4_percent` | `1` |
| `ev_adc_dar5_percent` | `1` |
| `ev_adc_dar6_percent` | `1` |
| `ev_adc_dar7_percent` | `1` |
| `ev_adc_dar8_percent` | `1` |
| `ev_adc_max_dar` | `1` |
| `ev_adc_mean_dar` | `1` |
| `ev_adc_mw_da` | `1` |
| `ev_additional_systemic_cl_per_dar_l_h` | `1` |
| `ev_clcat_l_h` | `1` |
| `ev_cllymphatic_l_h` | `1` |
| `ev_cycle_dose_day1` | `1` |
| `ev_cycle_dose_day15` | `1` |
| `ev_cycle_dose_day8` | `1` |
| `ev_cycle_length_day` | `1` |
| `ev_fcrn_binding_mode_code_1to1` | `1` |
| `ev_frel_catabolic` | `1` |
| `ev_frel_deconjugation` | `1` |
| `ev_kd1_dar0_uM` | `1` |
| `ev_kdec_plasma_dar1_1_h` | `1` |
| `ev_kdec_tissue_dar1_1_h` | `1` |
| `ev_krc1_1_h` | `1` |
| `ev_krel_catabolic_1_h` | `1` |
| `ev_kup_1_h` | `1` |
| `ev_recommended_dose_mg_kg` | `1` |
| `ev_recommended_infusion_min` | `1` |
| `fda_review_placeholder_flag` | `1` |
| `first_publication_year` | `1` |
| `main_pdf_pages` | `1` |
| `mmae_blood_plasma_ratio` | `1` |
| `mmae_clint_cyp3a4_ul_min_pmol` | `1` |
| `mmae_cliv_l_h` | `1` |
| `mmae_clpd_ml_min_million_hepatocytes` | `1` |
| `mmae_clr_l_h` | `1` |
| `mmae_conc_ng_ml` | `1` |
| `mmae_cyp3a4_kapp_uM` | `1` |
| `mmae_cyp3a4_ki_uM` | `1` |
| `mmae_cyp3a4_kinact_1_h` | `1` |
| `mmae_fcl_bile_percent` | `1` |
| `mmae_fraction_hepatic_metabolic_cyp3a4_percent` | `1` |
| `mmae_fu_hsa` | `1` |
| `mmae_kp_scalar` | `1` |
| `mmae_logp` | `1` |
| `mmae_mw_da` | `1` |
| `mmae_pgp_clint_t_ul_min_million_cells` | `1` |
| `mmae_pka1` | `1` |
| `mmae_raf_ref` | `1` |
| `mmae_vss_l_kg` | `1` |
| `paper_doi_numeric_suffix` | `1` |
| `paper_pmcid_numeric` | `1` |
| `paper_pmid` | `1` |
| `paper_year` | `1` |
| `pmc_recaptcha_blocked_flag` | `1` |
| `queue_cited_by_count` | `1` |
| `si_bv_adc_dar0_percent` | `1` |
| `si_bv_adc_dar1_percent` | `1` |
| `si_bv_adc_dar2_percent` | `1` |
| `si_bv_adc_dar3_percent` | `1` |
| `si_bv_adc_dar4_percent` | `1` |
| `si_bv_adc_dar5_percent` | `1` |
| `si_bv_adc_dar6_percent` | `1` |
| `si_bv_adc_dar7_percent` | `1` |
| `si_bv_adc_dar8_percent` | `1` |
| `si_bv_adc_max_dar` | `1` |
| `si_bv_adc_mean_dar` | `1` |
| `si_bv_adc_mw_da` | `1` |
| `si_bv_additional_systemic_cl_per_dar_l_h` | `1` |
| `si_bv_clcat_l_h` | `1` |
| `si_bv_cllymphatic_l_h` | `1` |
| `si_bv_fcrn_binding_mode_code_2to1` | `1` |
| `si_bv_kd1_uM` | `1` |
| `si_bv_kd2_uM` | `1` |
| `si_bv_kdec_plasma_1_h` | `1` |
| `si_bv_kdec_tissue_1_h` | `1` |
| `si_bv_krc1_1_h` | `1` |
| `si_bv_krc2_1_h` | `1` |
| `si_bv_kup_1_h` | `1` |
| `si_bv_virtual_age_high` | `1` |
| `si_bv_virtual_age_low` | `1` |
| `si_bv_virtual_duration_h` | `1` |
| `si_bv_virtual_participants_per_trial` | `1` |
| `si_bv_virtual_samples` | `1` |
| `si_bv_virtual_trials` | `1` |
| `si_bv_virtual_women_percent` | `1` |
| `si_ddi_age_high` | `1` |
| `si_ddi_age_low` | `1` |
| `si_ddi_digoxin_dose_mg` | `1` |
| `si_ddi_digoxin_duration_h` | `1` |
| `si_ddi_digoxin_samples` | `1` |
| `si_ddi_ev_dose_mg_kg` | `1` |
| `si_ddi_ev_infusion_min` | `1` |
| `si_ddi_ketoconazole_dose_mg` | `1` |
| `si_ddi_ketoconazole_duration_h` | `1` |
| `si_ddi_ketoconazole_samples` | `1` |
| `si_ddi_midazolam_dose_mg` | `1` |
| `si_ddi_midazolam_duration_h` | `1` |
| `si_ddi_midazolam_samples` | `1` |
| `si_ddi_patients_per_trial` | `1` |
| `si_ddi_rifampin_dose_mg` | `1` |
| `si_ddi_rifampin_duration_h` | `1` |
| `si_ddi_rifampin_samples` | `1` |
| `si_ddi_virtual_trials` | `1` |
| `si_ddi_women_percent` | `1` |
| `si_ev_multiple_age_high` | `1` |
| `si_ev_multiple_age_low` | `1` |
| `si_ev_multiple_duration_h` | `1` |
| `si_ev_multiple_participants_per_trial` | `1` |
| `si_ev_multiple_samples` | `1` |
| `si_ev_multiple_trials` | `1` |
| `si_ev_multiple_women_percent` | `1` |
| `si_ev_single_1p0_age_high` | `1` |
| `si_ev_single_1p0_age_low` | `1` |
| `si_ev_single_1p0_women_percent` | `1` |
| `si_ev_single_1p25_age_high` | `1` |
| `si_ev_single_1p25_age_low` | `1` |
| `si_ev_single_1p25_duration_h` | `1` |
| `si_ev_single_1p25_participants_per_trial` | `1` |
| `si_ev_single_1p25_samples` | `1` |
| `si_ev_single_1p25_trials` | `1` |
| `si_ev_single_1p25_women_percent` | `1` |
| `si_s5_fcl60_keto_auc_ratio` | `1` |
| `si_s5_fcl60_keto_cmax_ratio` | `1` |
| `si_s5_fcl60_rif_auc_ratio` | `1` |
| `si_s5_fcl60_rif_cmax_ratio` | `1` |
| `si_s5_fcl70_keto_auc_ratio` | `1` |
| `si_s5_fcl70_keto_cmax_ratio` | `1` |
| `si_s5_fcl70_rif_auc_ratio` | `1` |
| `si_s5_fcl70_rif_cmax_ratio` | `1` |
| `si_s5_fcl80_keto_auc_ratio` | `1` |
| `si_s5_fcl80_keto_cmax_ratio` | `1` |
| `si_s5_fcl80_rif_auc_ratio` | `1` |
| `si_s5_fcl80_rif_cmax_ratio` | `1` |
| `si_table_s4_observed_age_mean` | `1` |
| `si_table_s4_observed_age_sd` | `1` |
| `si_table_s4_observed_albumin_mean` | `1` |
| `si_table_s4_observed_albumin_sd` | `1` |
| `si_table_s4_observed_hematocrit_mean` | `1` |
| `si_table_s4_observed_hematocrit_sd` | `1` |
| `si_table_s4_observed_n` | `1` |
| `si_table_s4_observed_weight_mean` | `1` |
| `si_table_s4_observed_weight_sd` | `1` |
| `si_table_s4_simulated_age_mean` | `1` |
| `si_table_s4_simulated_age_sd` | `1` |
| `si_table_s4_simulated_albumin_mean` | `1` |
| `si_table_s4_simulated_albumin_sd` | `1` |
| `si_table_s4_simulated_hematocrit_mean` | `1` |
| `si_table_s4_simulated_hematocrit_sd` | `1` |
| `si_table_s4_simulated_n` | `1` |
| `si_table_s4_simulated_weight_mean` | `1` |
| `si_table_s4_simulated_weight_sd` | `1` |
| `simcyp_version` | `1` |
| `supplement_docx_count` | `1` |
| `supplement_media_count` | `1` |
| `supplement_table_count` | `1` |
| `t3_ev_1p0_adc_obs_cv_auc_percent` | `1` |
| `t3_ev_1p0_adc_obs_cv_cmax_percent` | `1` |
| `t3_ev_1p0_adc_obs_cv_t12_percent` | `1` |
| `t3_ev_1p0_adc_obs_gm_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p0_adc_obs_gm_cmax_ug_ml` | `1` |
| `t3_ev_1p0_adc_obs_gm_t12_day` | `1` |
| `t3_ev_1p0_adc_obs_mean_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p0_adc_obs_mean_cmax_ug_ml` | `1` |
| `t3_ev_1p0_adc_obs_mean_t12_day` | `1` |
| `t3_ev_1p0_adc_obs_n_auc` | `1` |
| `t3_ev_1p0_adc_obs_n_cmax` | `1` |
| `t3_ev_1p0_adc_obs_n_t12` | `1` |
| `t3_ev_1p0_adc_sim_cv_auc_percent` | `1` |
| `t3_ev_1p0_adc_sim_cv_cmax_percent` | `1` |
| `t3_ev_1p0_adc_sim_cv_t12_percent` | `1` |
| `t3_ev_1p0_adc_sim_gm_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p0_adc_sim_gm_cmax_ug_ml` | `1` |
| `t3_ev_1p0_adc_sim_gm_t12_day` | `1` |
| `t3_ev_1p0_adc_sim_mean_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p0_adc_sim_mean_cmax_ug_ml` | `1` |
| `t3_ev_1p0_adc_sim_mean_t12_day` | `1` |
| `t3_ev_1p0_mmae_obs_cv_auc_percent` | `1` |
| `t3_ev_1p0_mmae_obs_cv_cmax_percent` | `1` |
| `t3_ev_1p0_mmae_obs_cv_t12_percent` | `1` |
| `t3_ev_1p0_mmae_obs_gm_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p0_mmae_obs_gm_cmax_ng_ml` | `1` |
| `t3_ev_1p0_mmae_obs_gm_t12_day` | `1` |
| `t3_ev_1p0_mmae_obs_mean_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p0_mmae_obs_mean_cmax_ng_ml` | `1` |
| `t3_ev_1p0_mmae_obs_mean_t12_day` | `1` |
| `t3_ev_1p0_mmae_obs_n_auc` | `1` |
| `t3_ev_1p0_mmae_obs_n_cmax` | `1` |
| `t3_ev_1p0_mmae_obs_n_t12` | `1` |
| `t3_ev_1p0_mmae_sim_cv_auc_percent` | `1` |
| `t3_ev_1p0_mmae_sim_cv_cmax_percent` | `1` |
| `t3_ev_1p0_mmae_sim_cv_t12_percent` | `1` |
| `t3_ev_1p0_mmae_sim_gm_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p0_mmae_sim_gm_cmax_ng_ml` | `1` |
| `t3_ev_1p0_mmae_sim_gm_t12_day` | `1` |
| `t3_ev_1p0_mmae_sim_mean_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p0_mmae_sim_mean_cmax_ng_ml` | `1` |
| `t3_ev_1p0_mmae_sim_mean_t12_day` | `1` |
| `t3_ev_1p25_adc_obs_cv_auc_percent` | `1` |
| `t3_ev_1p25_adc_obs_cv_cmax_percent` | `1` |
| `t3_ev_1p25_adc_obs_cv_t12_percent` | `1` |
| `t3_ev_1p25_adc_obs_gm_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p25_adc_obs_gm_cmax_ug_ml` | `1` |
| `t3_ev_1p25_adc_obs_gm_t12_day` | `1` |
| `t3_ev_1p25_adc_obs_mean_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p25_adc_obs_mean_cmax_ug_ml` | `1` |
| `t3_ev_1p25_adc_obs_mean_t12_day` | `1` |
| `t3_ev_1p25_adc_obs_n_auc` | `1` |
| `t3_ev_1p25_adc_obs_n_cmax` | `1` |
| `t3_ev_1p25_adc_obs_n_t12` | `1` |
| `t3_ev_1p25_adc_sim_cv_auc_percent` | `1` |
| `t3_ev_1p25_adc_sim_cv_cmax_percent` | `1` |
| `t3_ev_1p25_adc_sim_cv_t12_percent` | `1` |
| `t3_ev_1p25_adc_sim_gm_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p25_adc_sim_gm_cmax_ug_ml` | `1` |
| `t3_ev_1p25_adc_sim_gm_t12_day` | `1` |
| `t3_ev_1p25_adc_sim_mean_auc_d0_7_ug_day_ml` | `1` |
| `t3_ev_1p25_adc_sim_mean_cmax_ug_ml` | `1` |
| `t3_ev_1p25_adc_sim_mean_t12_day` | `1` |
| `t3_ev_1p25_adc_sim_n` | `1` |
| `t3_ev_1p25_mmae_obs_cv_auc_percent` | `1` |
| `t3_ev_1p25_mmae_obs_cv_cmax_percent` | `1` |
| `t3_ev_1p25_mmae_obs_gm_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p25_mmae_obs_gm_cmax_ng_ml` | `1` |
| `t3_ev_1p25_mmae_obs_mean_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p25_mmae_obs_mean_cmax_ng_ml` | `1` |
| `t3_ev_1p25_mmae_obs_mean_t12_day` | `1` |
| `t3_ev_1p25_mmae_obs_n_auc` | `1` |
| `t3_ev_1p25_mmae_obs_n_cmax` | `1` |
| `t3_ev_1p25_mmae_obs_n_t12` | `1` |
| `t3_ev_1p25_mmae_sim_cv_auc_percent` | `1` |
| `t3_ev_1p25_mmae_sim_cv_cmax_percent` | `1` |
| `t3_ev_1p25_mmae_sim_cv_t12_percent` | `1` |
| `t3_ev_1p25_mmae_sim_gm_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p25_mmae_sim_gm_cmax_ng_ml` | `1` |
| `t3_ev_1p25_mmae_sim_gm_t12_day` | `1` |
| `t3_ev_1p25_mmae_sim_mean_auc_d0_7_ng_day_ml` | `1` |
| `t3_ev_1p25_mmae_sim_mean_cmax_ng_ml` | `1` |
| `t3_ev_1p25_mmae_sim_mean_t12_day` | `1` |
| `t4_adc_obs_day15_cv_auc14` | `1` |
| `t4_adc_obs_day15_cv_cmax` | `1` |
| `t4_adc_obs_day15_gm_auc14` | `1` |
| `t4_adc_obs_day15_gm_cmax` | `1` |
| `t4_adc_obs_day15_mean_auc14` | `1` |
| `t4_adc_obs_day15_mean_cmax` | `1` |
| `t4_adc_obs_day1_cv_auc7` | `1` |
| `t4_adc_obs_day1_cv_cmax` | `1` |
| `t4_adc_obs_day1_gm_auc7` | `1` |
| `t4_adc_obs_day1_gm_cmax` | `1` |
| `t4_adc_obs_day1_mean_auc7` | `1` |
| `t4_adc_obs_day1_mean_cmax` | `1` |
| `t4_adc_sim_day15_cv_auc14` | `1` |
| `t4_adc_sim_day15_cv_cmax` | `1` |
| `t4_adc_sim_day15_gm_auc14` | `1` |
| `t4_adc_sim_day15_gm_cmax` | `1` |
| `t4_adc_sim_day15_mean_auc14` | `1` |
| `t4_adc_sim_day15_mean_cmax` | `1` |
| `t4_adc_sim_day1_cv_auc7` | `1` |
| `t4_adc_sim_day1_cv_cmax` | `1` |
| `t4_adc_sim_day1_gm_auc7` | `1` |
| `t4_adc_sim_day1_gm_cmax` | `1` |
| `t4_adc_sim_day1_mean_auc7` | `1` |
| `t4_adc_sim_day1_mean_cmax` | `1` |
| `t4_mmae_obs_day15_cv_auc14` | `1` |
| `t4_mmae_obs_day15_cv_cmax` | `1` |
| `t4_mmae_obs_day15_gm_auc14` | `1` |
| `t4_mmae_obs_day15_gm_cmax` | `1` |
| `t4_mmae_obs_day15_mean_auc14` | `1` |
| `t4_mmae_obs_day15_mean_cmax` | `1` |
| `t4_mmae_obs_day1_cv_auc7` | `1` |
| `t4_mmae_obs_day1_cv_cmax` | `1` |
| `t4_mmae_obs_day1_gm_auc7` | `1` |
| `t4_mmae_obs_day1_gm_cmax` | `1` |
| `t4_mmae_obs_day1_mean_auc7` | `1` |
| `t4_mmae_obs_day1_mean_cmax` | `1` |
| `t4_mmae_sim_day15_cv_auc14` | `1` |
| `t4_mmae_sim_day15_cv_cmax` | `1` |
| `t4_mmae_sim_day15_gm_auc14` | `1` |
| `t4_mmae_sim_day15_gm_cmax` | `1` |
| `t4_mmae_sim_day15_mean_auc14` | `1` |
| `t4_mmae_sim_day15_mean_cmax` | `1` |
| `t4_mmae_sim_day1_cv_auc7` | `1` |
| `t4_mmae_sim_day1_cv_cmax` | `1` |
| `t4_mmae_sim_day1_gm_auc7` | `1` |
| `t4_mmae_sim_day1_gm_cmax` | `1` |
| `t4_mmae_sim_day1_mean_auc7` | `1` |
| `t4_mmae_sim_day1_mean_cmax` | `1` |
| `t5_digoxin_bv_pred_auc_ratio` | `1` |
| `t5_digoxin_bv_pred_cmax_ratio` | `1` |
| `t5_digoxin_ev_pred_auc_ratio` | `1` |
| `t5_digoxin_ev_pred_cmax_ratio` | `1` |
| `t5_keto_bv_obs_auc_ci_high` | `1` |
| `t5_keto_bv_obs_auc_ci_low` | `1` |
| `t5_keto_bv_obs_auc_ratio` | `1` |
| `t5_keto_bv_obs_cmax_ci_high` | `1` |
| `t5_keto_bv_obs_cmax_ci_low` | `1` |
| `t5_keto_bv_obs_cmax_ratio` | `1` |
| `t5_keto_bv_po_auc` | `1` |
| `t5_keto_bv_po_cmax` | `1` |
| `t5_keto_bv_pred_auc_ratio` | `1` |
| `t5_keto_bv_pred_cmax_ratio` | `1` |
| `t5_keto_ev_pred_auc_ci_high` | `1` |
| `t5_keto_ev_pred_auc_ci_low` | `1` |
| `t5_keto_ev_pred_auc_ratio` | `1` |
| `t5_keto_ev_pred_cmax_ci_high` | `1` |
| `t5_keto_ev_pred_cmax_ci_low` | `1` |
| `t5_keto_ev_pred_cmax_ratio` | `1` |
| `t5_mdz_bv_obs_auc_ci_high` | `1` |
| `t5_mdz_bv_obs_auc_ci_low` | `1` |
| `t5_mdz_bv_obs_auc_ratio` | `1` |
| `t5_mdz_bv_obs_cmax_ci_high` | `1` |
| `t5_mdz_bv_obs_cmax_ci_low` | `1` |
| `t5_mdz_bv_obs_cmax_ratio` | `1` |
| `t5_mdz_bv_po_auc` | `1` |
| `t5_mdz_bv_po_cmax` | `1` |
| `t5_mdz_bv_pred_auc_ratio` | `1` |
| `t5_mdz_bv_pred_cmax_ratio` | `1` |
| `t5_mdz_ev_pred_auc_ci_high` | `1` |
| `t5_mdz_ev_pred_auc_ci_low` | `1` |
| `t5_mdz_ev_pred_auc_ratio` | `1` |
| `t5_mdz_ev_pred_cmax_ratio` | `1` |
| `t5_rif_bv_obs_auc_ci_high` | `1` |
| `t5_rif_bv_obs_auc_ci_low` | `1` |
| `t5_rif_bv_obs_auc_ratio` | `1` |
| `t5_rif_bv_obs_cmax_ci_high` | `1` |
| `t5_rif_bv_obs_cmax_ci_low` | `1` |
| `t5_rif_bv_obs_cmax_ratio` | `1` |
| `t5_rif_bv_po_auc` | `1` |
| `t5_rif_bv_po_cmax` | `1` |
| `t5_rif_bv_pred_auc_ratio` | `1` |
| `t5_rif_bv_pred_cmax_ratio` | `1` |
| `t5_rif_ev_pred_auc_ci_high` | `1` |
| `t5_rif_ev_pred_auc_ci_low` | `1` |
| `t5_rif_ev_pred_auc_ratio` | `1` |
| `t5_rif_ev_pred_cmax_ci_high` | `1` |
| `t5_rif_ev_pred_cmax_ci_low` | `1` |
| `t5_rif_ev_pred_cmax_ratio` | `1` |
| `t6_bv18_adc_auc_obs` | `1` |
| `t6_bv18_adc_auc_po` | `1` |
| `t6_bv18_adc_auc_pred` | `1` |
| `t6_bv18_adc_cmax_obs` | `1` |
| `t6_bv18_adc_cmax_po` | `1` |
| `t6_bv18_adc_cmax_pred` | `1` |
| `t6_bv18_mmae_auc_obs` | `1` |
| `t6_bv18_mmae_auc_po` | `1` |
| `t6_bv18_mmae_auc_pred` | `1` |
| `t6_bv18_mmae_cmax_obs` | `1` |
| `t6_bv18_mmae_cmax_po` | `1` |
| `t6_bv18_mmae_cmax_pred` | `1` |
| `t6_bv27_adc_auc_obs` | `1` |
| `t6_bv27_adc_auc_po` | `1` |
| `t6_bv27_adc_auc_pred` | `1` |
| `t6_bv27_adc_cmax_obs` | `1` |
| `t6_bv27_adc_cmax_po` | `1` |
| `t6_bv27_adc_cmax_pred` | `1` |
| `t6_bv27_mmae_auc_obs` | `1` |
| `t6_bv27_mmae_auc_po` | `1` |
| `t6_bv27_mmae_auc_pred` | `1` |
| `t6_bv27_mmae_cmax_obs` | `1` |
| `t6_bv27_mmae_cmax_po` | `1` |
| `t6_bv27_mmae_cmax_pred` | `1` |
| `t6_ev10_adc_auc_obs` | `1` |
| `t6_ev10_adc_auc_po` | `1` |
| `t6_ev10_adc_auc_pred` | `1` |
| `t6_ev10_adc_cmax_obs` | `1` |
| `t6_ev10_adc_cmax_po` | `1` |
| `t6_ev10_adc_cmax_pred` | `1` |
| `t6_ev10_mmae_auc_obs` | `1` |
| `t6_ev10_mmae_auc_po` | `1` |
| `t6_ev10_mmae_auc_pred` | `1` |
| `t6_ev10_mmae_cmax_obs` | `1` |
| `t6_ev10_mmae_cmax_po` | `1` |
| `t6_ev10_mmae_cmax_pred` | `1` |
| `t6_ev125_adc_auc_obs` | `1` |
| `t6_ev125_adc_auc_po` | `1` |
| `t6_ev125_adc_auc_pred` | `1` |
| `t6_ev125_adc_cmax_obs` | `1` |
| `t6_ev125_adc_cmax_po` | `1` |
| `t6_ev125_adc_cmax_pred` | `1` |
| `t6_ev125_mmae_auc_obs` | `1` |
| `t6_ev125_mmae_auc_po` | `1` |
| `t6_ev125_mmae_auc_pred` | `1` |
| `t6_ev125_mmae_cmax_obs` | `1` |
| `t6_ev125_mmae_cmax_po` | `1` |
| `t6_ev125_mmae_cmax_pred` | `1` |
| `title_model_rank` | `1` |
| `state__adc_conc_ug_ml` | `ug/mL` |
| `state__auc_adc_ug_day_ml` | `ug*day/mL` |
| `state__auc_mmae_ng_day_ml` | `ng*day/mL` |
| `state__elapsed_day` | `day` |
| `state__mmae_conc_ng_ml` | `ng/mL` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `ev-1p0-single-dose-reduced-ode` starter has **142 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `adc_conc_ug_ml` | 0 | 0 (0 h, post) | 20.0355 (0.0208333 h, pre) | 0.0830725 |
| `mmae_conc_ng_ml` | 0 | 0 (0 h, post) | 1.91795 (2.25 h, post) | 0.897199 |

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
Evidence identity: `sha256:42a97014e5c697944aa9bf4c316633e81a10bdca05374bd15fb718b54792234d`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Exploratory one-compartment antibody decay coupled to one-compartment MMAE formation and elimination. This historical reduction lacks the DAR/FcRn, organ, transporter and enzyme structure of the Choules Simcyp PBPK model. Table constants and DDI proxy ratios are not simulation validation; calibrated curves do not reproduce the original mechanism.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
