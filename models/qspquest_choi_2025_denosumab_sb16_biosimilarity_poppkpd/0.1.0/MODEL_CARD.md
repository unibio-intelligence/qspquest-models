# Choi 2025 Denosumab SB16 Biosimilarity PopPK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare fixed denosumab/SB16 exposure and pharmacodynamic experiments.

**Runnable · 11 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect public ODE simulation for reference denosumab after 60 mg SC at months 0, 6, and 12. Paper comparators are the Table 5 population median and 90 percent PI endpoints.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_choi_2025_denosumab_sb16_biosimilarity_poppkpd', version='0.1.0')
result = model.run('den-60mg-q6mo-three-doses-table5-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `den-60mg-q6mo-three-doses-table5-overlay` | Fixed-effect public ODE simulation for reference denosumab after 60 mg SC at months 0, 6, and 12. Paper comparators are the Table 5 population median and 90 percent PI endpoints. | 0–13140 h | 551 |
| `figure6-7-hv-64kg-caucasian-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `figure6-7-pmo-45kg-caucasian-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `figure6-7-pmo-64kg-asian-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `figure6-7-pmo-64kg-black-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `figure6-7-pmo-64kg-caucasian-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `figure6-7-pmo-90kg-caucasian-typical` | Deterministic fixed-effect projection for the covariate conditions in Figures 6 and 7. Population medians and prediction intervals are not reproduced. PMO is an explicit assumption for the weight/race panels. BMD in healthy volunteers is a model extrapolation, not observed Phase I PD. | 0–13140 h | 551 |
| `phase1-hv-single-60mg-typical` | Typical healthy-volunteer PK over the Phase I sampling window. Reference weight 64 kg and Caucasian clearance are explicit assumptions, not the Phase I cohort distribution. BMD is an unobserved model extrapolation. | 0–4704 h | 393 |
| `sb16-60mg-q6mo-three-doses-table5-overlay` | Fixed-effect public ODE simulation for SB16 after 60 mg SC at months 0, 6, and 12. Paper comparators are the Table 5 population median and 90 percent PI endpoints. | 0–13140 h | 551 |
| `untreated-hv-baseline` | No-dose structural control: RANKL and BMD must remain at their population-specific steady state. This checks the implementation, not a reported clinical control arm. | 0–13140 h | 551 |
| `untreated-pmo-baseline` | No-dose structural control: RANKL and BMD must remain at their population-specific steady state. This checks the implementation, not a reported clinical control arm. | 0–13140 h | 551 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `Ctot_nM` | Total denosumab concentration | `1` |
| `Rfree_nM` | Free RANKL target concentration | `1` |
| `bmd_change_percent` | Percentage change in bone mineral density | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_choi_2025_denosumab_sb16_biosimilarity_poppkpd --model-version 0.1.0 --scenario den-60mg-q6mo-three-doses-table5-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 139 outputs and 7 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_total_nM_h` | `1` |
| `Cfree_nM` | `1` |
| `Cperipheral_nM` | `1` |
| `Ctot_nM` | `1` |
| `RANKL_total_nM` | `1` |
| `RC_nM` | `1` |
| `Rfree_nM` | `1` |
| `absorption_half_life_hv_day` | `1` |
| `absorption_half_life_hv_day_runtime` | `1` |
| `absorption_half_life_pmo_day` | `1` |
| `absorption_half_life_pmo_day_runtime` | `1` |
| `absorption_half_life_pmo_h` | `1` |
| `article_pdf_pages` | `1` |
| `asian_auc_decrease_percent` | `1` |
| `black_auc_decrease_percent` | `1` |
| `blq_postdose_fraction` | `1` |
| `bmd0_g_cm2` | `1` |
| `bmd0_iiv_percent` | `1` |
| `bmd_change_percent` | `1` |
| `bmd_inhibition_fraction` | `1` |
| `bmd_measurements` | `1` |
| `bmd_response_45kg_percent` | `1` |
| `bmd_response_64kg_percent` | `1` |
| `bmd_response_90kg_percent` | `1` |
| `bmd_response_asian_percent` | `1` |
| `bmd_response_black_percent` | `1` |
| `bmd_response_caucasian_percent` | `1` |
| `citation_rank` | `1` |
| `cl_asian_L_h` | `1` |
| `cl_black_L_h` | `1` |
| `cl_caucasian_L_h` | `1` |
| `cl_iiv_percent` | `1` |
| `cl_ind_L_h` | `1` |
| `cl_ratio_runtime` | `1` |
| `cl_sb16_L_h` | `1` |
| `corr_vp_cl` | `1` |
| `denosumab_mw_g_mol` | `1` |
| `dose_60mg_nmol` | `1` |
| `dose_60mg_nmol_derived` | `1` |
| `dosing_interval_h` | `1` |
| `dosing_interval_months` | `1` |
| `figure_image_count` | `1` |
| `hill_coeff` | `1` |
| `ic50_iiv_percent` | `1` |
| `ic50_nM` | `1` |
| `imax_f` | `1` |
| `imax_fraction` | `1` |
| `imax_fraction_runtime` | `1` |
| `implementation_priority_score` | `1` |
| `ka_hv_h` | `1` |
| `ka_iiv_percent` | `1` |
| `ka_ind_h` | `1` |
| `ka_pmo_h` | `1` |
| `kin_bmd_derived_g_cm2_h` | `1` |
| `kin_bmd_g_cm2_h` | `1` |
| `kin_bmd_runtime_g_cm2_h` | `1` |
| `kint_h` | `1` |
| `kint_iiv_percent` | `1` |
| `kout_bmd_h` | `1` |
| `kss_iiv_percent` | `1` |
| `kss_nM` | `1` |
| `ksyn_flux_nM_h` | `1` |
| `ksyn_iiv_percent` | `1` |
| `ksyn_reported_nM_h` | `1` |
| `lloq_ng_ml` | `1` |
| `lumbar_bmd_g_cm2` | `1` |
| `modeled_subjects` | `1` |
| `nmol_per_mg_denosumab` | `1` |
| `pd_additive_error_g_cm2` | `1` |
| `phase1_single_dose_mg` | `1` |
| `phase1_subjects` | `1` |
| `phase3_den_then_den_subjects` | `1` |
| `phase3_den_then_sb16_subjects` | `1` |
| `phase3_repeated_dose_mg` | `1` |
| `phase3_sb16_subjects` | `1` |
| `phase3_subjects` | `1` |
| `pk_additive_error_nM` | `1` |
| `pk_proportional_error` | `1` |
| `pmc_html_table_count` | `1` |
| `pmcid_numeric` | `1` |
| `pmid_numeric` | `1` |
| `postdose_blq_samples` | `1` |
| `postdose_quantifiable_samples` | `1` |
| `postdose_samples` | `1` |
| `preprint_hit_count` | `1` |
| `publication_year` | `1` |
| `q_hv_L_h` | `1` |
| `q_iiv_percent` | `1` |
| `q_ind_L_h` | `1` |
| `q_pmo_L_h` | `1` |
| `quantifiable_postdose_fraction` | `1` |
| `queue_cited_by_count` | `1` |
| `r0_hv_nM` | `1` |
| `r0_iiv_percent` | `1` |
| `r0_ind_nM` | `1` |
| `r0_pmo_nM` | `1` |
| `rankl_kdeg_from_ksyn_over_r0_pmo_h` | `1` |
| `rankl_kdeg_h` | `1` |
| `serum_concentration_records` | `1` |
| `steady_state_vd_L` | `1` |
| `steady_state_vd_runtime_L` | `1` |
| `supplement_docx_count` | `1` |
| `table5_den_auc_tau_ss_nM_h` | `1` |
| `table5_den_auc_tau_ss_pi_high_nM_h` | `1` |
| `table5_den_auc_tau_ss_pi_low_nM_h` | `1` |
| `table5_den_bmd_change_percent` | `1` |
| `table5_den_bmd_change_pi_high_percent` | `1` |
| `table5_den_bmd_change_pi_low_percent` | `1` |
| `table5_den_cmax_nM` | `1` |
| `table5_den_cmax_pi_high_nM` | `1` |
| `table5_den_cmax_pi_low_nM` | `1` |
| `table5_den_tmax_h` | `1` |
| `table5_den_tmax_pi_high_h` | `1` |
| `table5_den_tmax_pi_low_h` | `1` |
| `table5_sb16_auc_tau_ss_nM_h` | `1` |
| `table5_sb16_auc_tau_ss_pi_high_nM_h` | `1` |
| `table5_sb16_auc_tau_ss_pi_low_nM_h` | `1` |
| `table5_sb16_bmd_change_percent` | `1` |
| `table5_sb16_bmd_change_pi_high_percent` | `1` |
| `table5_sb16_bmd_change_pi_low_percent` | `1` |
| `table5_sb16_cmax_nM` | `1` |
| `table5_sb16_cmax_pi_high_nM` | `1` |
| `table5_sb16_cmax_pi_low_nM` | `1` |
| `table5_sb16_tmax_h` | `1` |
| `table5_sb16_tmax_pi_high_h` | `1` |
| `table5_sb16_tmax_pi_low_h` | `1` |
| `theta_weight_cl` | `1` |
| `theta_weight_vc` | `1` |
| `theta_weight_vp` | `1` |
| `treatment_cl_ratio_sb16_to_den` | `1` |
| `vc_f_L` | `1` |
| `vc_f_iiv_percent` | `1` |
| `vc_ind_L` | `1` |
| `vp_f_L` | `1` |
| `vp_f_iiv_percent` | `1` |
| `vp_ind_L` | `1` |
| `vpc_replicates` | `1` |
| `weight_45kg_auc_increase_percent` | `1` |
| `weight_90kg_auc_decrease_percent` | `1` |
| `state__AUC_total_nM_h` | `nmol*h/L` |
| `state__A_central_total_nmol` | `nmol` |
| `state__A_depot_nmol` | `nmol` |
| `state__A_peripheral_free_nmol` | `nmol` |
| `state__RANKL_total_nM` | `nmol/L` |
| `state__elapsed_h` | `h` |
| `state__lumbar_bmd_g_cm2` | `g/cm2` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `den-60mg-q6mo-three-doses-table5-overlay` starter has **551 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `Ctot_nM` | 0 | 0 (0 h, post) | 40.2172 (9048 h, post) | 0.130075 |
| `Rfree_nM` | 15.23 | 0.0179991 (9096 h, post) | 15.23 (0 h, post) | 3.20644 |
| `bmd_change_percent` | 0 | 0 (0 h, post) | 6.87563 (12240 h, post) | 6.73937 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
