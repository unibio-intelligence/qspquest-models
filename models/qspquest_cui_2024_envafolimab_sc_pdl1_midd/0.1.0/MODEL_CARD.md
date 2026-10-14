# Cui 2024 Envafolimab SC PD-L1 PopPK/MIDD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore subcutaneous envafolimab exposure and published development summaries.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_cui_2024_envafolimab_sc_pdl1_midd', version='0.1.0')
result = model.run('final-model-150mg-qw-20wk-ode-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-anchor` | Exact source table and supplement anchor | 0–0.001 h | 2 |
| `final-model-150mg-qw-20wk-ode-overlay` | Final model 150 mg QW for 20 weeks | 0–140 h | 561 |
| `final-model-2p5mgkg-qw-20wk-endpoint-overlay` | Final model 2.5 mg/kg QW for 20 weeks using mean body weight | 0–140 h | 561 |
| `final-model-300mg-q2w-20wk-ode-overlay` | Final model 300 mg Q2W for 20 weeks | 0–140 h | 561 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `envafolimab_concentration_mg_l` | Envafolimab concentration | `1` |
| `cl_l_day_individual` | Individual clearance under the fixed covariates | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_cui_2024_envafolimab_sc_pdl1_midd --model-version 0.1.0 --scenario final-model-150mg-qw-20wk-ode-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 103 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `auc_mg_h_l` | `1` |
| `cl_l_day_individual` | `1` |
| `cl_l_hr_individual` | `1` |
| `elapsed_hour` | `1` |
| `envafolimab_concentration_mg_l` | `1` |
| `envafolimab_concentration_ng_ml` | `1` |
| `ka_day` | `1` |
| `source_aucinf_er_population_count` | `1` |
| `source_cmax_cmin_cavg_er_population_count` | `1` |
| `source_cmin_overall_er_population_count` | `1` |
| `source_drug_related_teae_count` | `1` |
| `source_er_patient_count` | `1` |
| `source_mean_body_weight_kg` | `1` |
| `source_median_body_weight_kg` | `1` |
| `source_poppk_concentration_count` | `1` |
| `source_poppk_patient_count` | `1` |
| `source_reference_crcl_ml_min` | `1` |
| `source_table1_cl_american_factor` | `1` |
| `source_table1_cl_american_rse_pct` | `1` |
| `source_table1_cl_ci_high_l_hr` | `1` |
| `source_table1_cl_ci_low_l_hr` | `1` |
| `source_table1_cl_crcl_power` | `1` |
| `source_table1_cl_crcl_rse_pct` | `1` |
| `source_table1_cl_iiv_pct` | `1` |
| `source_table1_cl_iiv_rse_pct` | `1` |
| `source_table1_cl_japanese_factor` | `1` |
| `source_table1_cl_japanese_rse_pct` | `1` |
| `source_table1_cl_l_hr` | `1` |
| `source_table1_cl_rse_pct` | `1` |
| `source_table1_cl_shrinkage_pct` | `1` |
| `source_table1_emax` | `1` |
| `source_table1_emax_ci_high` | `1` |
| `source_table1_emax_ci_low` | `1` |
| `source_table1_emax_rse_pct` | `1` |
| `source_table1_epsilon` | `1` |
| `source_table1_epsilon_rse_pct` | `1` |
| `source_table1_epsilon_shrinkage_pct` | `1` |
| `source_table1_ka_ci_high_hr` | `1` |
| `source_table1_ka_ci_low_hr` | `1` |
| `source_table1_ka_hr` | `1` |
| `source_table1_ka_iiv_pct` | `1` |
| `source_table1_ka_iiv_rse_pct` | `1` |
| `source_table1_ka_rse_pct` | `1` |
| `source_table1_ka_shrinkage_pct` | `1` |
| `source_table1_t50_ci_high_day` | `1` |
| `source_table1_t50_ci_low_day` | `1` |
| `source_table1_t50_day` | `1` |
| `source_table1_t50_rse_pct` | `1` |
| `source_table1_v_ci_high_l` | `1` |
| `source_table1_v_ci_low_l` | `1` |
| `source_table1_v_iiv_pct` | `1` |
| `source_table1_v_iiv_rse_pct` | `1` |
| `source_table1_v_l` | `1` |
| `source_table1_v_rse_pct` | `1` |
| `source_table1_v_shrinkage_pct` | `1` |
| `source_table2_150mg_qw_cmin_ss_over_5mg_l_pct` | `1` |
| `source_table2_150mg_qw_r_auc_cv_pct` | `1` |
| `source_table2_150mg_qw_r_auc_mean` | `1` |
| `source_table2_150mg_qw_r_auc_sd` | `1` |
| `source_table2_150mg_qw_r_cmax_cv_pct` | `1` |
| `source_table2_150mg_qw_r_cmax_mean` | `1` |
| `source_table2_150mg_qw_r_cmax_sd` | `1` |
| `source_table2_2p5_mgkg_qw_cmin_ss_over_5mg_l_pct` | `1` |
| `source_table2_2p5_mgkg_qw_r_auc_cv_pct` | `1` |
| `source_table2_2p5_mgkg_qw_r_auc_mean` | `1` |
| `source_table2_2p5_mgkg_qw_r_auc_sd` | `1` |
| `source_table2_2p5_mgkg_qw_r_cmax_cv_pct` | `1` |
| `source_table2_2p5_mgkg_qw_r_cmax_mean` | `1` |
| `source_table2_2p5_mgkg_qw_r_cmax_sd` | `1` |
| `source_table2_300mg_q2w_cmin_ss_over_5mg_l_pct` | `1` |
| `source_table2_300mg_q2w_r_auc_cv_pct` | `1` |
| `source_table2_300mg_q2w_r_auc_mean` | `1` |
| `source_table2_300mg_q2w_r_auc_sd` | `1` |
| `source_table2_300mg_q2w_r_cmax_cv_pct` | `1` |
| `source_table2_300mg_q2w_r_cmax_mean` | `1` |
| `source_table2_300mg_q2w_r_cmax_sd` | `1` |
| `source_table_s5_150mg_qw_overall_auc_cv_pct` | `1` |
| `source_table_s5_150mg_qw_overall_auc_sd` | `1` |
| `source_table_s5_150mg_qw_overall_auc_ss_mg_h_l` | `1` |
| `source_table_s5_150mg_qw_overall_cmax_cv_pct` | `1` |
| `source_table_s5_150mg_qw_overall_cmax_sd` | `1` |
| `source_table_s5_150mg_qw_overall_cmax_ss_mg_l` | `1` |
| `source_table_s5_150mg_qw_overall_cmin_cv_pct` | `1` |
| `source_table_s5_150mg_qw_overall_cmin_sd` | `1` |
| `source_table_s5_150mg_qw_overall_cmin_ss_mg_l` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_auc_cv_pct` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_auc_sd` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_auc_ss_mg_h_l` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmax_cv_pct` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmax_sd` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmax_ss_mg_l` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmin_cv_pct` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmin_sd` | `1` |
| `source_table_s5_2p5_mgkg_qw_overall_cmin_ss_mg_l` | `1` |
| `source_table_s5_300mg_q2w_overall_auc_cv_pct` | `1` |
| `source_table_s5_300mg_q2w_overall_auc_sd` | `1` |
| `source_table_s5_300mg_q2w_overall_auc_ss_mg_h_l` | `1` |
| `source_table_s5_300mg_q2w_overall_cmax_cv_pct` | `1` |
| `source_table_s5_300mg_q2w_overall_cmax_sd` | `1` |
| `source_table_s5_300mg_q2w_overall_cmax_ss_mg_l` | `1` |
| `source_table_s5_300mg_q2w_overall_cmin_cv_pct` | `1` |
| `source_table_s5_300mg_q2w_overall_cmin_sd` | `1` |
| `source_table_s5_300mg_q2w_overall_cmin_ss_mg_l` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `final-model-150mg-qw-20wk-ode-overlay` starter has **561 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `envafolimab_concentration_mg_l` | 0 | 0 (0 h, post) | 27.1409 (135.75 h, post) | 24.4735 |
| `cl_l_day_individual` | 1.1472 | 0.805821 (140 h, pre) | 1.1472 (0 h, post) | 0.805821 |

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
Evidence identity: `sha256:5b132dfcfc660dcca8106450e1163051364ede3fe220653ae45d025b82ac7c59`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

One-compartment subcutaneous envafolimab PopPK ODE with first-order absorption, linear elimination, time-varying clearance, CRCL and country covariates, reconstructed from Cui et al. 2024 main text and supplementary material.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
