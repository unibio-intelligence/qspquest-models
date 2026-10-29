# Frank 2023 sutimlimab CAD PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore sutimlimab exposure and pharmacodynamics in cold agglutinin disease.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect ODE for a 65 kg non-Japanese patient receiving 6.5 g on day 0/day 7 then q14d through week 149.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_frank_2023_sutimlimab_cad_pkpd', version='0.1.0')
result = model.run('approved-65kg-6p5g-q2w')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `approved-65kg-6p5g-q2w` | Fixed-effect ODE for a 65 kg non-Japanese patient receiving 6.5 g on day 0/day 7 then q14d through week 149. | 0–25032 h | 1119 |
| `approved-80kg-7p5g-q2w` | Fixed-effect ODE for an 80 kg non-Japanese patient receiving 7.5 g on day 0/day 7 then q14d through week 149. | 0–25032 h | 1119 |
| `approved-all-source-limited-population` | Representative fixed-effect population-proxy ODE using 71.85 kg; paper comparators are stochastic population endpoints from Supp. Table 7 and abstract text. | 0–25032 h | 1119 |
| `article-supplement-source-anchor` | No-dose exact replay of article/supplement model parameters, study counts, quality criteria, covariate settings, and reported simulation endpoints. | 0–0.001 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ug_ml` | Sutimlimab concentration | `1` |
| `cp_activity_percent` | Complement pathway activity | `1` |
| `hb_g_dl` | Hemoglobin concentration | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_frank_2023_sutimlimab_cad_pkpd --model-version 0.1.0 --scenario approved-65kg-6p5g-q2w --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 165 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `ada_positive_phase3_n` | `1` |
| `approved_regimen_below_100_ci_high_percent` | `1` |
| `approved_regimen_below_100_ci_low_percent` | `1` |
| `approved_regimen_below_100_percent` | `1` |
| `approved_regimen_predicted_above_target_percent` | `1` |
| `article_license_cc_by` | `1` |
| `article_pages_n` | `1` |
| `auc_h_ug_ml` | `1` |
| `below_100_proxy_percent` | `1` |
| `blood_transfusion_phase3_n` | `1` |
| `central_conc_ug_ml` | `1` |
| `cl_ml_h_cov` | `1` |
| `cp_activity_percent` | `1` |
| `cp_hill_factor` | `1` |
| `cp_ic50_ug_ml` | `1` |
| `cp_ic90_ug_ml` | `1` |
| `derived_hb_half_life_day` | `1` |
| `derived_kout_h_inv` | `1` |
| `distribution_mg_h` | `1` |
| `dose_6p5_mgkg_mean` | `1` |
| `dose_6p5_mgkg_sd` | `1` |
| `dose_7p5_mgkg_mean` | `1` |
| `dose_7p5_mgkg_sd` | `1` |
| `drug_effect_fraction` | `1` |
| `elapsed_h` | `1` |
| `emax_fraction` | `1` |
| `emax_no_transfusion_calc` | `1` |
| `emax_transfusion_calc` | `1` |
| `hb0_cov_g_dl` | `1` |
| `hb_change_clcr_174_vs_24_fold` | `1` |
| `hb_change_g_dl` | `1` |
| `hb_change_no_transfusion_vs_transfusion_fold` | `1` |
| `hb_change_weight_39_vs_112_fold` | `1` |
| `hb_g_dl` | `1` |
| `infusion_max_h` | `1` |
| `infusion_min_h` | `1` |
| `kin_g_dl_h` | `1` |
| `kout_h_inv` | `1` |
| `linear_clearance_mg_h` | `1` |
| `loading_dose_day0` | `1` |
| `loading_dose_day7` | `1` |
| `maintenance_interval_day` | `1` |
| `near_max_cp_inhibition_conc_ug_ml` | `1` |
| `nonlinear_clearance_mg_h` | `1` |
| `observed_below_100_phase3_n` | `1` |
| `observed_below_100_phase3_percent` | `1` |
| `observed_bilirubin_change_steady_mg_dl` | `1` |
| `observed_bilirubin_steady_mg_dl` | `1` |
| `observed_c4_change_steady_g_l` | `1` |
| `observed_c4_steady_g_l` | `1` |
| `observed_hb_change_steady_g_dl` | `1` |
| `observed_hb_steady_g_dl` | `1` |
| `observed_phase3_patients_n` | `1` |
| `peripheral_conc_ug_ml` | `1` |
| `pk_development_blq_percent` | `1` |
| `pk_development_observations_n` | `1` |
| `pk_development_participants_n` | `1` |
| `pk_evaluation_blq_percent` | `1` |
| `pk_evaluation_observations_n` | `1` |
| `pk_evaluation_participants_n` | `1` |
| `pk_quality_pred_aafe` | `1` |
| `pk_quality_pred_mpe_percent_observed` | `1` |
| `pk_quality_pred_mpe_ug_ml` | `1` |
| `pk_quality_pred_rmse_percent_observed` | `1` |
| `pk_quality_pred_rmse_ug_ml` | `1` |
| `pkpd_development_hb_observations_n` | `1` |
| `pkpd_development_patients_n` | `1` |
| `pkpd_evaluation_hb_observations_n` | `1` |
| `pkpd_evaluation_patients_n` | `1` |
| `pkpd_quality_pred_aafe` | `1` |
| `pkpd_quality_pred_mpe_g_dl` | `1` |
| `pkpd_quality_pred_mpe_percent_observed` | `1` |
| `pkpd_quality_pred_rmse_g_dl` | `1` |
| `pkpd_quality_pred_rmse_percent_observed` | `1` |
| `projected_hb_change_g_dl` | `1` |
| `recommended_dose_high_weight_g` | `1` |
| `recommended_dose_low_weight_g` | `1` |
| `reference_age_year` | `1` |
| `reference_body_weight_kg` | `1` |
| `reference_clcr_ml_min` | `1` |
| `simulation_hb_virtual_participants_n` | `1` |
| `simulation_pk_virtual_participants_n` | `1` |
| `simulation_replicates_per_participant` | `1` |
| `supp_table7_approved_65_75_median_trough_ug_ml` | `1` |
| `supp_table7_approved_75_85_median_trough_ug_ml` | `1` |
| `supp_table7_approved_85_95_median_trough_ug_ml` | `1` |
| `supp_table7_approved_all_below_100_percent` | `1` |
| `supp_table7_approved_all_below_20_percent` | `1` |
| `supp_table7_approved_all_median_trough_ug_ml` | `1` |
| `supp_table7_approved_all_pi_high_ug_ml` | `1` |
| `supp_table7_approved_all_pi_low_ug_ml` | `1` |
| `supp_table7_approved_ge95_median_trough_ug_ml` | `1` |
| `supplement_pages_n` | `1` |
| `table3_age_effect_vc` | `1` |
| `table3_age_effect_vc_rse_percent` | `1` |
| `table3_bivv009_03_additive_residual_rse_percent` | `1` |
| `table3_bivv009_03_additive_residual_ug_ml` | `1` |
| `table3_bivv009_03_prop_residual` | `1` |
| `table3_bivv009_03_prop_residual_rse_percent` | `1` |
| `table3_body_weight_on_cl_exponent` | `1` |
| `table3_body_weight_on_cl_rse_percent` | `1` |
| `table3_body_weight_on_vc_exponent` | `1` |
| `table3_body_weight_on_vc_rse_percent` | `1` |
| `table3_cl_eta_shrinkage_percent` | `1` |
| `table3_cl_iiv_cv_percent` | `1` |
| `table3_cl_iiv_rse_percent` | `1` |
| `table3_cl_ml_h` | `1` |
| `table3_cl_rse_percent` | `1` |
| `table3_japanese_effect_vc` | `1` |
| `table3_japanese_effect_vc_rse_percent` | `1` |
| `table3_japanese_effect_vmax` | `1` |
| `table3_japanese_effect_vmax_rse_percent` | `1` |
| `table3_km_rse_percent` | `1` |
| `table3_km_ug_ml` | `1` |
| `table3_non_bivv009_03_additive_residual_rse_percent` | `1` |
| `table3_non_bivv009_03_additive_residual_ug_ml` | `1` |
| `table3_non_bivv009_03_prop_residual` | `1` |
| `table3_non_bivv009_03_prop_residual_rse_percent` | `1` |
| `table3_q_ml_h` | `1` |
| `table3_q_rse_percent` | `1` |
| `table3_vc_eta_shrinkage_percent` | `1` |
| `table3_vc_iiv_cv_percent` | `1` |
| `table3_vc_iiv_rse_percent` | `1` |
| `table3_vc_l` | `1` |
| `table3_vc_rse_percent` | `1` |
| `table3_vmax_eta_shrinkage_percent` | `1` |
| `table3_vmax_iiv_cv_percent` | `1` |
| `table3_vmax_iiv_rse_percent` | `1` |
| `table3_vmax_mg_h` | `1` |
| `table3_vmax_rse_percent` | `1` |
| `table3_vp_eta_shrinkage_percent` | `1` |
| `table3_vp_iiv_cv_percent` | `1` |
| `table3_vp_iiv_rse_percent` | `1` |
| `table3_vp_l` | `1` |
| `table3_vp_rse_percent` | `1` |
| `table4_additive_residual_g_dl` | `1` |
| `table4_additive_residual_rse_percent` | `1` |
| `table4_clcr_on_hb0_exponent` | `1` |
| `table4_clcr_on_hb0_rse_percent` | `1` |
| `table4_ec50_rse_percent` | `1` |
| `table4_ec50_ug_ml` | `1` |
| `table4_emax_eta_shrinkage_percent` | `1` |
| `table4_emax_iiv_cv_percent` | `1` |
| `table4_emax_iiv_rse_percent` | `1` |
| `table4_emax_logit_parameter` | `1` |
| `table4_emax_no_transfusion_fraction` | `1` |
| `table4_emax_rse_percent` | `1` |
| `table4_emax_transfusion_fraction` | `1` |
| `table4_hb0_eta_shrinkage_percent` | `1` |
| `table4_hb0_g_dl` | `1` |
| `table4_hb0_iiv_cv_percent` | `1` |
| `table4_hb0_iiv_rse_percent` | `1` |
| `table4_hb0_rse_percent` | `1` |
| `table4_transfusion_effect_on_emax_logit` | `1` |
| `table4_transfusion_effect_rse_percent` | `1` |
| `table4_turnover_time_h` | `1` |
| `table4_turnover_time_rse_percent` | `1` |
| `target_100_ratio` | `1` |
| `target_trough_ug_ml` | `1` |
| `vc_l_cov` | `1` |
| `vmax_mg_h_cov` | `1` |
| `vpc_subproblem_simulations_n` | `1` |
| `weight_cutoff_kg` | `1` |
| `weight_max_sim_kg` | `1` |
| `weight_min_sim_kg` | `1` |
| `state__auc_h_ug_ml` | `h*ug/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_h` | `h` |
| `state__hb_g_dl` | `g/dL` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `approved-65kg-6p5g-q2w` starter has **1119 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ug_ml` | 0 | 0 (0 h, post) | 3127.33 (24697 h, pre) | 1345.47 |
| `cp_activity_percent` | 100 | 3.26079e-05 (24697 h, pre) | 100 (0 h, post) | 0.000246857 |
| `hb_g_dl` | 8.99 | 8.99 (0 h, post) | 11.637 (24840 h, post) | 11.6043 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
