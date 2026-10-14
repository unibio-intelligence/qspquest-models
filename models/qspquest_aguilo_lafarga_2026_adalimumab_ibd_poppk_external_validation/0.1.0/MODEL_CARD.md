# Aguilo-Lafarga 2026 Adalimumab IBD PopPK External Validation

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare fixed adalimumab regimens and inspect published IBD model-validation summaries.

**Runnable · 13 experiments.** Version 0.1.0.

## Run an experiment

Deterministic full ODE probe using the Berends one-compartment SC adalimumab model from the preprint supplement.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_aguilo_lafarga_2026_adalimumab_ibd_poppk_external_validation', version='0.1.0')
result = model.run('berends-adalimumab-induction-q2w-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 13 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `berends-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the Berends one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |
| `cohort-and-sampling-replay` | Exact final-row replay of Aguilo-Lafarga 2026 source values. | 0–1 h | 2 |
| `fda-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the FDA one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |
| `figure1-gof-digitized-scatter` | Display-only source-limited raster digitization of observed-vs-individual-predicted concentration components from Figure 1. This is not patient-level source data or a new fit. | 0–1 h | 2 |
| `figure2-pcvpc-digitized-observed-markers` | Display-only source-limited raster digitization of red observed-marker components from Figure 2 pcVPC panels plus coverage labels in paper_overlays. | 0–26000 h | 27 |
| `marquez-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the Marquez one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |
| `sanchez-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the Sanchez one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |
| `supplement-model-parameter-replay` | Exact final-row replay of Aguilo-Lafarga 2026 source values. | 0–1 h | 2 |
| `supplementary-figures-1-3-metric-distribution-anchors` | Display-only source-derived anchors for the MPE, MAPE, and RMSE bootstrap-distribution plots. Means and confidence intervals come from Table 3 because bootstrap draws are unavailable. | 0–1 h | 2 |
| `table2-clearance-comparison-replay` | Exact final-row replay of Aguilo-Lafarga 2026 source values. | 0–1 h | 2 |
| `table3-metric-replay` | Exact final-row replay of Aguilo-Lafarga 2026 source values. | 0–1 h | 2 |
| `ternant-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the Ternant one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |
| `vande-adalimumab-induction-q2w-ode` | Deterministic full ODE probe using the Vande one-compartment SC adalimumab model from the preprint supplement. | 0–182 h | 183 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_l` | Adalimumab concentration in the central compartment | `1` |
| `auc_mg_day_l` | Accumulated central drug exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_aguilo_lafarga_2026_adalimumab_ibd_poppk_external_validation --model-version 0.1.0 --scenario berends-adalimumab-induction-q2w-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 186 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `auc_mg_day_l` | `1` |
| `central_conc_mg_l` | `1` |
| `cl_l_day` | `1` |
| `elapsed_day` | `1` |
| `ka_day` | `1` |
| `kel_day` | `1` |
| `source__aaa_positive_pct` | `1` |
| `source__ada_concentration_mean_mg_l` | `1` |
| `source__ada_target_range_pct` | `1` |
| `source__age_mean_year` | `1` |
| `source__age_sd_year` | `1` |
| `source__bmi_mean_kg_m2` | `1` |
| `source__bmi_sd_kg_m2` | `1` |
| `source__citation_rank` | `1` |
| `source__crohns_n` | `1` |
| `source__female_pct` | `1` |
| `source__hla_dqa105_positive_pct` | `1` |
| `source__lbw_mean_kg` | `1` |
| `source__maintenance_conc_mean_mg_l` | `1` |
| `source__model_count` | `1` |
| `source__patients_total_n` | `1` |
| `source__publication_year` | `1` |
| `source__samples_induction_n` | `1` |
| `source__samples_maintenance_n` | `1` |
| `source__samples_total_n` | `1` |
| `source__supp_table1_berends_aaa_cl` | `1` |
| `source__supp_table1_berends_add_error_mg_l` | `1` |
| `source__supp_table1_berends_cl_l_day` | `1` |
| `source__supp_table1_berends_dosing_cl` | `1` |
| `source__supp_table1_berends_iiv_cl` | `1` |
| `source__supp_table1_berends_ka_day` | `1` |
| `source__supp_table1_berends_prop_error` | `1` |
| `source__supp_table1_berends_v_l` | `1` |
| `source__supp_table1_fda_cl_l_day` | `1` |
| `source__supp_table1_fda_iiv_cl` | `1` |
| `source__supp_table1_fda_iiv_v` | `1` |
| `source__supp_table1_fda_ka_day` | `1` |
| `source__supp_table1_fda_prop_error` | `1` |
| `source__supp_table1_fda_v_l` | `1` |
| `source__supp_table1_marquez_aaa_cl` | `1` |
| `source__supp_table1_marquez_alb_cl` | `1` |
| `source__supp_table1_marquez_cl_l_day` | `1` |
| `source__supp_table1_marquez_iiv_cl` | `1` |
| `source__supp_table1_marquez_iiv_v` | `1` |
| `source__supp_table1_marquez_ka_day` | `1` |
| `source__supp_table1_marquez_prop_error` | `1` |
| `source__supp_table1_marquez_v_l` | `1` |
| `source__supp_table1_sanchez_bmi_cl` | `1` |
| `source__supp_table1_sanchez_cl_l_day` | `1` |
| `source__supp_table1_sanchez_fcp_cl` | `1` |
| `source__supp_table1_sanchez_iiv_cl` | `1` |
| `source__supp_table1_sanchez_ka_day` | `1` |
| `source__supp_table1_sanchez_pen_cl` | `1` |
| `source__supp_table1_sanchez_prop_error` | `1` |
| `source__supp_table1_sanchez_udasc_cl` | `1` |
| `source__supp_table1_sanchez_v_l` | `1` |
| `source__supp_table1_ternant_aaa_cl` | `1` |
| `source__supp_table1_ternant_add_error_mg_l` | `1` |
| `source__supp_table1_ternant_cl_l_day` | `1` |
| `source__supp_table1_ternant_iiv_cl` | `1` |
| `source__supp_table1_ternant_iiv_v` | `1` |
| `source__supp_table1_ternant_ka_day` | `1` |
| `source__supp_table1_ternant_prop_error` | `1` |
| `source__supp_table1_ternant_v_l` | `1` |
| `source__supp_table1_vande_aaa_cl` | `1` |
| `source__supp_table1_vande_cl_l_day` | `1` |
| `source__supp_table1_vande_iiv_cl` | `1` |
| `source__supp_table1_vande_iiv_ka` | `1` |
| `source__supp_table1_vande_iiv_v` | `1` |
| `source__supp_table1_vande_ka_day` | `1` |
| `source__supp_table1_vande_lbw_cl` | `1` |
| `source__supp_table1_vande_prop_error` | `1` |
| `source__supp_table1_vande_v_l` | `1` |
| `source__table2_berends_ebe_cl` | `1` |
| `source__table2_berends_ebe_cl_hi` | `1` |
| `source__table2_berends_ebe_cl_lo` | `1` |
| `source__table2_berends_p_lt_0_001` | `1` |
| `source__table2_berends_theoretical_cl` | `1` |
| `source__table2_berends_theoretical_cl_hi` | `1` |
| `source__table2_berends_theoretical_cl_lo` | `1` |
| `source__table2_fda_ebe_cl` | `1` |
| `source__table2_fda_ebe_cl_hi` | `1` |
| `source__table2_fda_ebe_cl_lo` | `1` |
| `source__table2_fda_p_lt_0_001` | `1` |
| `source__table2_fda_theoretical_cl` | `1` |
| `source__table2_fda_theoretical_cl_hi` | `1` |
| `source__table2_fda_theoretical_cl_lo` | `1` |
| `source__table2_marquez_ebe_cl` | `1` |
| `source__table2_marquez_ebe_cl_hi` | `1` |
| `source__table2_marquez_ebe_cl_lo` | `1` |
| `source__table2_marquez_p_lt_0_001` | `1` |
| `source__table2_marquez_theoretical_cl` | `1` |
| `source__table2_marquez_theoretical_cl_hi` | `1` |
| `source__table2_marquez_theoretical_cl_lo` | `1` |
| `source__table2_sanchez_ebe_cl` | `1` |
| `source__table2_sanchez_ebe_cl_hi` | `1` |
| `source__table2_sanchez_ebe_cl_lo` | `1` |
| `source__table2_sanchez_p_gt_0_05` | `1` |
| `source__table2_sanchez_theoretical_cl` | `1` |
| `source__table2_sanchez_theoretical_cl_hi` | `1` |
| `source__table2_sanchez_theoretical_cl_lo` | `1` |
| `source__table2_ternant_ebe_cl` | `1` |
| `source__table2_ternant_ebe_cl_hi` | `1` |
| `source__table2_ternant_ebe_cl_lo` | `1` |
| `source__table2_ternant_p_gt_0_05` | `1` |
| `source__table2_ternant_theoretical_cl` | `1` |
| `source__table2_ternant_theoretical_cl_hi` | `1` |
| `source__table2_ternant_theoretical_cl_lo` | `1` |
| `source__table2_vande_ebe_cl` | `1` |
| `source__table2_vande_ebe_cl_hi` | `1` |
| `source__table2_vande_ebe_cl_lo` | `1` |
| `source__table2_vande_p_lt_0_001` | `1` |
| `source__table2_vande_theoretical_cl` | `1` |
| `source__table2_vande_theoretical_cl_hi` | `1` |
| `source__table2_vande_theoretical_cl_lo` | `1` |
| `source__table3_berends_aic` | `1` |
| `source__table3_berends_gof_r` | `1` |
| `source__table3_berends_mape` | `1` |
| `source__table3_berends_mape_hi` | `1` |
| `source__table3_berends_mape_lo` | `1` |
| `source__table3_berends_mpe` | `1` |
| `source__table3_berends_mpe_hi` | `1` |
| `source__table3_berends_mpe_lo` | `1` |
| `source__table3_berends_rmse` | `1` |
| `source__table3_berends_rmse_hi` | `1` |
| `source__table3_berends_rmse_lo` | `1` |
| `source__table3_fda_aic` | `1` |
| `source__table3_fda_mape` | `1` |
| `source__table3_fda_mape_hi` | `1` |
| `source__table3_fda_mape_lo` | `1` |
| `source__table3_fda_mpe` | `1` |
| `source__table3_fda_mpe_hi` | `1` |
| `source__table3_fda_mpe_lo` | `1` |
| `source__table3_fda_rmse` | `1` |
| `source__table3_fda_rmse_hi` | `1` |
| `source__table3_fda_rmse_lo` | `1` |
| `source__table3_marquez_aic` | `1` |
| `source__table3_marquez_mape` | `1` |
| `source__table3_marquez_mape_hi` | `1` |
| `source__table3_marquez_mape_lo` | `1` |
| `source__table3_marquez_mpe` | `1` |
| `source__table3_marquez_mpe_hi` | `1` |
| `source__table3_marquez_mpe_lo` | `1` |
| `source__table3_marquez_rmse` | `1` |
| `source__table3_marquez_rmse_hi` | `1` |
| `source__table3_marquez_rmse_lo` | `1` |
| `source__table3_sanchez_aic` | `1` |
| `source__table3_sanchez_gof_r` | `1` |
| `source__table3_sanchez_mape` | `1` |
| `source__table3_sanchez_mape_hi` | `1` |
| `source__table3_sanchez_mape_lo` | `1` |
| `source__table3_sanchez_mpe` | `1` |
| `source__table3_sanchez_mpe_hi` | `1` |
| `source__table3_sanchez_mpe_lo` | `1` |
| `source__table3_sanchez_rmse` | `1` |
| `source__table3_sanchez_rmse_hi` | `1` |
| `source__table3_sanchez_rmse_lo` | `1` |
| `source__table3_ternant_aic` | `1` |
| `source__table3_ternant_gof_r` | `1` |
| `source__table3_ternant_mape` | `1` |
| `source__table3_ternant_mape_hi` | `1` |
| `source__table3_ternant_mape_lo` | `1` |
| `source__table3_ternant_mpe` | `1` |
| `source__table3_ternant_mpe_hi` | `1` |
| `source__table3_ternant_mpe_lo` | `1` |
| `source__table3_ternant_rmse` | `1` |
| `source__table3_ternant_rmse_hi` | `1` |
| `source__table3_ternant_rmse_lo` | `1` |
| `source__table3_vande_aic` | `1` |
| `source__table3_vande_gof_r` | `1` |
| `source__table3_vande_mape` | `1` |
| `source__table3_vande_mape_hi` | `1` |
| `source__table3_vande_mape_lo` | `1` |
| `source__table3_vande_mpe` | `1` |
| `source__table3_vande_mpe_hi` | `1` |
| `source__table3_vande_mpe_lo` | `1` |
| `source__table3_vande_rmse` | `1` |
| `source__table3_vande_rmse_hi` | `1` |
| `source__table3_vande_rmse_lo` | `1` |
| `source__ulcerative_colitis_n` | `1` |
| `source__week2_conc_mean_mg_l` | `1` |
| `source__week6_conc_mean_mg_l` | `1` |
| `source__weight_mean_kg` | `1` |
| `source__weight_sd_kg` | `1` |
| `summary_marker` | `1` |
| `v_l` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__summary_marker` | `1` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `berends-adalimumab-induction-q2w-ode` starter has **183 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_l` | 0 | 0 (0 h, post) | 23.058 (18 h, post) | 7.02292 |
| `auc_mg_day_l` | 0 | 0 (0 h, post) | 2027.58 (182 h, pre) | 2027.58 |

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
Evidence identity: `sha256:741b955122af7c154528b92a9a33ded1bf450a185c9d9bf14110b2beff3e81a6`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-complete preprint replay of six published adalimumab IBD one-compartment PopPK models, with exact table/metric replay and source-limited deterministic ODE scenarios.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
