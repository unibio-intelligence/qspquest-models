# Waterhouse 2024 Vedolizumab allo-HSCT GvHD prophylaxis PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed vedolizumab exposure in transplant prophylaxis scenarios.

**Runnable · 37 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_waterhouse_2024_vedolizumab_gvhd_allohsct_poppk', version='0.1.0')
result = model.run('phase3-300mg-q4w-reference')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 37 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `fig3-age-23y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-27y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-39y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-55y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-64y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-68y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-age-70y-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-29gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-32gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-36gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-40gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-43gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-46gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-albumin-48gl-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-105kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-111kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-51kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-56kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-65kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-75kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-body-weight-88kg-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-intestine-gvhd-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-liver-gvhd-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-0-1kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-0-5kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-0kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-1-7kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-1kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-lymphocyte-2-3kul-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `fig3-skin-gvhd-relative-cl-check` | Published Figure 3 endpoint replay through the final covariate equations. | 0–1 h | 2 |
| `phase1b-300mg-days-m1-13-42-reference` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 184 |
| `phase3-300mg-high-albumin-46gl` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 188 |
| `phase3-300mg-high-weight-105kg` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 188 |
| `phase3-300mg-low-albumin-36gl` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 188 |
| `phase3-300mg-low-weight-51kg` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 188 |
| `phase3-300mg-q4w-reference` | Full ODE simulation with paper dosing regimen and Figure 3/source endpoint overlays where available. | 0–180 h | 188 |
| `tables-methods-figure3-exact-anchor` | No-dose source replay of Waterhouse 2024 Table 1, Table 2, Table 3, Supplementary Table S1, methods, and Figure 3 values. | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_mg_per_L` | Vedolizumab concentration | `1` |
| `cumulative_auc_mg_day_per_L` | Accumulated central vedolizumab exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_waterhouse_2024_vedolizumab_gvhd_allohsct_poppk --model-version 0.1.0 --scenario phase3-300mg-q4w-reference --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 271 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `CL_ci_high` | `1` |
| `CL_ci_low` | `1` |
| `CL_l_day` | `1` |
| `CL_rse_percent` | `1` |
| `Q_ci_high` | `1` |
| `Q_ci_low` | `1` |
| `Q_l_day` | `1` |
| `Q_rse_percent` | `1` |
| `Vc_ci_high` | `1` |
| `Vc_ci_low` | `1` |
| `Vc_l` | `1` |
| `Vc_rse_percent` | `1` |
| `Vp_ci_high` | `1` |
| `Vp_ci_low` | `1` |
| `Vp_l` | `1` |
| `Vp_rse_percent` | `1` |
| `analysis_patients` | `1` |
| `article_pdf_fetched_flag` | `1` |
| `auc_relative_to_reference_inverse_cl` | `1` |
| `ava_positive_phase3_patients` | `1` |
| `base_CL_l_day` | `1` |
| `base_Q_l_day` | `1` |
| `base_Vc_l` | `1` |
| `base_Vp_l` | `1` |
| `base_corr_cl_vc` | `1` |
| `base_cov_cl_vc` | `1` |
| `base_iiv_cl_cv_percent` | `1` |
| `base_iiv_cl_variance` | `1` |
| `base_iiv_vc_cv_percent` | `1` |
| `base_iiv_vc_variance` | `1` |
| `base_iov_cl_cv_percent` | `1` |
| `base_iov_cl_variance` | `1` |
| `base_proportional_residual_cv_percent` | `1` |
| `base_proportional_residual_variance` | `1` |
| `blq_samples_excluded` | `1` |
| `blq_samples_percent` | `1` |
| `central_concentration_mg_per_L` | `1` |
| `central_concentration_ug_per_mL` | `1` |
| `citation_rank` | `1` |
| `clinically_meaningful_cl_effect_percent` | `1` |
| `corr_cl_vc` | `1` |
| `corr_cl_vp` | `1` |
| `corr_vc_vp` | `1` |
| `cov_cl_vc` | `1` |
| `cov_cl_vp` | `1` |
| `cov_vc_vp` | `1` |
| `covariate_central_volume_l` | `1` |
| `covariate_clearance_l_per_day` | `1` |
| `covariate_intercompartmental_clearance_l_per_day` | `1` |
| `covariate_peripheral_volume_l` | `1` |
| `cumulative_auc_mg_day_per_L` | `1` |
| `dose_event_amount_mg` | `1` |
| `europepmc_xml_fetched_flag` | `1` |
| `fig3_age_23y_ci_high` | `1` |
| `fig3_age_23y_ci_low` | `1` |
| `fig3_age_23y_covariate_value` | `1` |
| `fig3_age_23y_relative_cl` | `1` |
| `fig3_age_27y_ci_high` | `1` |
| `fig3_age_27y_ci_low` | `1` |
| `fig3_age_27y_covariate_value` | `1` |
| `fig3_age_27y_relative_cl` | `1` |
| `fig3_age_39y_ci_high` | `1` |
| `fig3_age_39y_ci_low` | `1` |
| `fig3_age_39y_covariate_value` | `1` |
| `fig3_age_39y_relative_cl` | `1` |
| `fig3_age_55y_ci_high` | `1` |
| `fig3_age_55y_ci_low` | `1` |
| `fig3_age_55y_covariate_value` | `1` |
| `fig3_age_55y_relative_cl` | `1` |
| `fig3_age_64y_ci_high` | `1` |
| `fig3_age_64y_ci_low` | `1` |
| `fig3_age_64y_covariate_value` | `1` |
| `fig3_age_64y_relative_cl` | `1` |
| `fig3_age_68y_ci_high` | `1` |
| `fig3_age_68y_ci_low` | `1` |
| `fig3_age_68y_covariate_value` | `1` |
| `fig3_age_68y_relative_cl` | `1` |
| `fig3_age_70y_ci_high` | `1` |
| `fig3_age_70y_ci_low` | `1` |
| `fig3_age_70y_covariate_value` | `1` |
| `fig3_age_70y_relative_cl` | `1` |
| `fig3_albumin_29gl_ci_high` | `1` |
| `fig3_albumin_29gl_ci_low` | `1` |
| `fig3_albumin_29gl_covariate_value` | `1` |
| `fig3_albumin_29gl_relative_cl` | `1` |
| `fig3_albumin_32gl_ci_high` | `1` |
| `fig3_albumin_32gl_ci_low` | `1` |
| `fig3_albumin_32gl_covariate_value` | `1` |
| `fig3_albumin_32gl_relative_cl` | `1` |
| `fig3_albumin_36gl_ci_high` | `1` |
| `fig3_albumin_36gl_ci_low` | `1` |
| `fig3_albumin_36gl_covariate_value` | `1` |
| `fig3_albumin_36gl_relative_cl` | `1` |
| `fig3_albumin_40gl_ci_high` | `1` |
| `fig3_albumin_40gl_ci_low` | `1` |
| `fig3_albumin_40gl_covariate_value` | `1` |
| `fig3_albumin_40gl_relative_cl` | `1` |
| `fig3_albumin_43gl_ci_high` | `1` |
| `fig3_albumin_43gl_ci_low` | `1` |
| `fig3_albumin_43gl_covariate_value` | `1` |
| `fig3_albumin_43gl_relative_cl` | `1` |
| `fig3_albumin_46gl_ci_high` | `1` |
| `fig3_albumin_46gl_ci_low` | `1` |
| `fig3_albumin_46gl_covariate_value` | `1` |
| `fig3_albumin_46gl_relative_cl` | `1` |
| `fig3_albumin_48gl_ci_high` | `1` |
| `fig3_albumin_48gl_ci_low` | `1` |
| `fig3_albumin_48gl_covariate_value` | `1` |
| `fig3_albumin_48gl_relative_cl` | `1` |
| `fig3_body_weight_105kg_ci_high` | `1` |
| `fig3_body_weight_105kg_ci_low` | `1` |
| `fig3_body_weight_105kg_covariate_value` | `1` |
| `fig3_body_weight_105kg_relative_cl` | `1` |
| `fig3_body_weight_111kg_ci_high` | `1` |
| `fig3_body_weight_111kg_ci_low` | `1` |
| `fig3_body_weight_111kg_covariate_value` | `1` |
| `fig3_body_weight_111kg_relative_cl` | `1` |
| `fig3_body_weight_51kg_ci_high` | `1` |
| `fig3_body_weight_51kg_ci_low` | `1` |
| `fig3_body_weight_51kg_covariate_value` | `1` |
| `fig3_body_weight_51kg_relative_cl` | `1` |
| `fig3_body_weight_56kg_ci_high` | `1` |
| `fig3_body_weight_56kg_ci_low` | `1` |
| `fig3_body_weight_56kg_covariate_value` | `1` |
| `fig3_body_weight_56kg_relative_cl` | `1` |
| `fig3_body_weight_65kg_ci_high` | `1` |
| `fig3_body_weight_65kg_ci_low` | `1` |
| `fig3_body_weight_65kg_covariate_value` | `1` |
| `fig3_body_weight_65kg_relative_cl` | `1` |
| `fig3_body_weight_75kg_ci_high` | `1` |
| `fig3_body_weight_75kg_ci_low` | `1` |
| `fig3_body_weight_75kg_covariate_value` | `1` |
| `fig3_body_weight_75kg_relative_cl` | `1` |
| `fig3_body_weight_88kg_ci_high` | `1` |
| `fig3_body_weight_88kg_ci_low` | `1` |
| `fig3_body_weight_88kg_covariate_value` | `1` |
| `fig3_body_weight_88kg_relative_cl` | `1` |
| `fig3_intestine_gvhd_ci_high` | `1` |
| `fig3_intestine_gvhd_ci_low` | `1` |
| `fig3_intestine_gvhd_covariate_value` | `1` |
| `fig3_intestine_gvhd_relative_cl` | `1` |
| `fig3_liver_gvhd_ci_high` | `1` |
| `fig3_liver_gvhd_ci_low` | `1` |
| `fig3_liver_gvhd_covariate_value` | `1` |
| `fig3_liver_gvhd_relative_cl` | `1` |
| `fig3_lymphocyte_0_1kul_ci_high` | `1` |
| `fig3_lymphocyte_0_1kul_ci_low` | `1` |
| `fig3_lymphocyte_0_1kul_covariate_value` | `1` |
| `fig3_lymphocyte_0_1kul_relative_cl` | `1` |
| `fig3_lymphocyte_0_5kul_ci_high` | `1` |
| `fig3_lymphocyte_0_5kul_ci_low` | `1` |
| `fig3_lymphocyte_0_5kul_covariate_value` | `1` |
| `fig3_lymphocyte_0_5kul_relative_cl` | `1` |
| `fig3_lymphocyte_0kul_ci_high` | `1` |
| `fig3_lymphocyte_0kul_ci_low` | `1` |
| `fig3_lymphocyte_0kul_covariate_value` | `1` |
| `fig3_lymphocyte_0kul_relative_cl` | `1` |
| `fig3_lymphocyte_1_7kul_ci_high` | `1` |
| `fig3_lymphocyte_1_7kul_ci_low` | `1` |
| `fig3_lymphocyte_1_7kul_covariate_value` | `1` |
| `fig3_lymphocyte_1_7kul_relative_cl` | `1` |
| `fig3_lymphocyte_1kul_ci_high` | `1` |
| `fig3_lymphocyte_1kul_ci_low` | `1` |
| `fig3_lymphocyte_1kul_covariate_value` | `1` |
| `fig3_lymphocyte_1kul_relative_cl` | `1` |
| `fig3_lymphocyte_2_3kul_ci_high` | `1` |
| `fig3_lymphocyte_2_3kul_ci_low` | `1` |
| `fig3_lymphocyte_2_3kul_covariate_value` | `1` |
| `fig3_lymphocyte_2_3kul_relative_cl` | `1` |
| `fig3_skin_gvhd_ci_high` | `1` |
| `fig3_skin_gvhd_ci_low` | `1` |
| `fig3_skin_gvhd_covariate_value` | `1` |
| `fig3_skin_gvhd_relative_cl` | `1` |
| `iiv_cl_cv_percent` | `1` |
| `iiv_cl_shrinkage_percent` | `1` |
| `iiv_cl_variance` | `1` |
| `iiv_vc_cv_percent` | `1` |
| `iiv_vc_shrinkage_percent` | `1` |
| `iiv_vc_variance` | `1` |
| `iiv_vp_cv_percent` | `1` |
| `iiv_vp_shrinkage_percent` | `1` |
| `iiv_vp_variance` | `1` |
| `infusion_duration_min` | `1` |
| `iov_cl_cv_percent` | `1` |
| `iov_cl_shrinkage_percent` | `1` |
| `iov_cl_variance` | `1` |
| `linear_half_life_days` | `1` |
| `lymphocyte_zero_replacement_k_ul` | `1` |
| `phase1b_300mg_patients` | `1` |
| `phase1b_75mg_patients` | `1` |
| `phase1b_patients` | `1` |
| `phase3_300mg_patients` | `1` |
| `phase3_patients` | `1` |
| `pmcid_numeric` | `1` |
| `pmid_numeric` | `1` |
| `preprint_hits` | `1` |
| `proportional_residual_cv_percent` | `1` |
| `proportional_residual_shrinkage_percent` | `1` |
| `proportional_residual_variance` | `1` |
| `publication_year` | `1` |
| `queue_cited_by_count` | `1` |
| `reference_age_year` | `1` |
| `reference_albumin_g_l` | `1` |
| `reference_cl_l_per_day` | `1` |
| `reference_lymphocyte_k_ul` | `1` |
| `reference_weight_kg` | `1` |
| `relative_clearance_to_reference` | `1` |
| `supplement_docx_fetched_flag` | `1` |
| `table1_all_patients` | `1` |
| `table1_asian_all` | `1` |
| `table1_asian_all_percent` | `1` |
| `table1_cyclosporine_all` | `1` |
| `table1_cyclosporine_all_percent` | `1` |
| `table1_dose_300mg_all` | `1` |
| `table1_dose_300mg_all_percent` | `1` |
| `table1_dose_75mg_all` | `1` |
| `table1_dose_75mg_all_percent` | `1` |
| `table1_female_all` | `1` |
| `table1_female_all_percent` | `1` |
| `table1_intestine_gvhd_all` | `1` |
| `table1_intestine_gvhd_all_percent` | `1` |
| `table1_liver_gvhd_all` | `1` |
| `table1_liver_gvhd_all_percent` | `1` |
| `table1_male_all` | `1` |
| `table1_male_all_percent` | `1` |
| `table1_methotrexate_all` | `1` |
| `table1_methotrexate_all_percent` | `1` |
| `table1_skin_gvhd_all` | `1` |
| `table1_skin_gvhd_all_percent` | `1` |
| `table1_tacrolimus_all` | `1` |
| `table1_tacrolimus_all_percent` | `1` |
| `table1_ursodeoxycholic_acid_all` | `1` |
| `table1_ursodeoxycholic_acid_all_percent` | `1` |
| `table1_white_all` | `1` |
| `table1_white_all_percent` | `1` |
| `table2_printed_theta_weight_q` | `1` |
| `theta_age_cl` | `1` |
| `theta_age_cl_ci_high` | `1` |
| `theta_age_cl_ci_low` | `1` |
| `theta_age_cl_rse_percent` | `1` |
| `theta_albumin_cl` | `1` |
| `theta_albumin_cl_ci_high` | `1` |
| `theta_albumin_cl_ci_low` | `1` |
| `theta_albumin_cl_rse_percent` | `1` |
| `theta_intestine_gvhd_cl` | `1` |
| `theta_intestine_gvhd_cl_ci_high` | `1` |
| `theta_intestine_gvhd_cl_ci_low` | `1` |
| `theta_intestine_gvhd_cl_rse_percent` | `1` |
| `theta_liver_gvhd_cl` | `1` |
| `theta_liver_gvhd_cl_ci_high` | `1` |
| `theta_liver_gvhd_cl_ci_low` | `1` |
| `theta_liver_gvhd_cl_rse_percent` | `1` |
| `theta_lymphocyte_cl` | `1` |
| `theta_lymphocyte_cl_ci_high` | `1` |
| `theta_lymphocyte_cl_ci_low` | `1` |
| `theta_lymphocyte_cl_rse_percent` | `1` |
| `theta_skin_gvhd_cl` | `1` |
| `theta_skin_gvhd_cl_ci_high` | `1` |
| `theta_skin_gvhd_cl_ci_low` | `1` |
| `theta_skin_gvhd_cl_rse_percent` | `1` |
| `theta_weight_cl` | `1` |
| `theta_weight_cl_ci_high` | `1` |
| `theta_weight_cl_ci_low` | `1` |
| `theta_weight_cl_rse_percent` | `1` |
| `theta_weight_q` | `1` |
| `theta_weight_vc` | `1` |
| `theta_weight_vc_ci_high` | `1` |
| `theta_weight_vc_ci_low` | `1` |
| `theta_weight_vc_rse_percent` | `1` |
| `theta_weight_vp` | `1` |
| `vedolizumab_observations` | `1` |
| `state__AUC_mg_day_L` | `mg*day/L` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `phase3-300mg-q4w-reference` starter has **188 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_mg_per_L` | 0 | 0 (0 h, post) | 143.905 (154.021 h, pre) | 50.5294 |
| `cumulative_auc_mg_day_per_L` | 0 | 0 (0 h, post) | 11537.3 (180 h, pre) | 11537.3 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
