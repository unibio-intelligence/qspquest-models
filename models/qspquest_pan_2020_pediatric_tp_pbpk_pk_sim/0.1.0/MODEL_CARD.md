# Pan/Basu 2020 Pediatric Therapeutic Protein PBPK Reduced Validation Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore reduced pediatric therapeutic-protein distribution scenarios.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Reduced two-compartment IV plus target-binding smoke using Table 2 and Table 4 values.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_pan_2020_pediatric_tp_pbpk_pk_sim', version='0.1.0')
result = model.run('bevacizumab-15mgkg-13y-growth-table4-smoke')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `bevacizumab-15mgkg-13y-growth-table4-smoke` | Reduced two-compartment IV plus target-binding smoke using Table 2 and Table 4 values. | 0–120 h | 121 |
| `main-paper-table-scalar-checks` | Exact source checks for Table 2 drug parameters, published comparator equations, and Tables 3-4 reported/PBPK PK summaries. | 0–1 h | 2 |
| `palivizumab-15mgkg-nominal-growth-table3-smoke` | Reduced two-compartment IV smoke using palivizumab equations and Table 3 nominal-age/with-growth AUC target. | 0–120 h | 121 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_ug_ml` | Bevacizumab concentration | `1` |
| `AUC_ug_ml_day` | Accumulated central drug exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_pan_2020_pediatric_tp_pbpk_pk_sim --model-version 0.1.0 --scenario bevacizumab-15mgkg-13y-growth-table4-smoke --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 83 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_ml_day` | `1` |
| `CL_L_day` | `1` |
| `Q_L_day` | `1` |
| `Vc_L` | `1` |
| `Vp_L` | `1` |
| `central_concentration_ug_ml` | `1` |
| `peripheral_concentration_ug_ml` | `1` |
| `reported_auc_ug_ml_day` | `1` |
| `reported_t12_day` | `1` |
| `reported_to_simulated_auc_ratio` | `1` |
| `reported_vss_ml_kg` | `1` |
| `source_allometric_cl_q_exponent` | `1` |
| `source_bevacizumab_auc_pred_13y_growth_15_mgkg` | `1` |
| `source_bevacizumab_auc_pred_13y_growth_5_mgkg` | `1` |
| `source_bevacizumab_auc_reported_15_mgkg` | `1` |
| `source_bevacizumab_auc_reported_5_mgkg` | `1` |
| `source_bevacizumab_auc_reported_sd_15_mgkg` | `1` |
| `source_bevacizumab_auc_reported_sd_5_mgkg` | `1` |
| `source_bevacizumab_male_cl_factor` | `1` |
| `source_bevacizumab_male_vc_factor` | `1` |
| `source_bevacizumab_pop_cl_ml_day_70kg` | `1` |
| `source_bevacizumab_pop_q_ml_day_70kg` | `1` |
| `source_bevacizumab_pop_vc_l_70kg` | `1` |
| `source_bevacizumab_pop_vp_l_70kg` | `1` |
| `source_bevacizumab_primary_cns_cl_factor` | `1` |
| `source_bevacizumab_primary_cns_vc_factor` | `1` |
| `source_bevacizumab_t12_pred_13y_growth_15_mgkg` | `1` |
| `source_bevacizumab_t12_pred_13y_growth_5_mgkg` | `1` |
| `source_bevacizumab_t12_reported_15_mgkg` | `1` |
| `source_bevacizumab_t12_reported_5_mgkg` | `1` |
| `source_bevacizumab_t12_reported_sd_15_mgkg` | `1` |
| `source_bevacizumab_t12_reported_sd_5_mgkg` | `1` |
| `source_bevacizumab_vc_exponent` | `1` |
| `source_bevacizumab_vp_exponent` | `1` |
| `source_bevacizumab_vss_pred_13y_growth_15_mgkg` | `1` |
| `source_bevacizumab_vss_pred_13y_growth_5_mgkg` | `1` |
| `source_bevacizumab_vss_reported_15_mgkg` | `1` |
| `source_bevacizumab_vss_reported_5_mgkg` | `1` |
| `source_bevacizumab_vss_reported_sd_15_mgkg` | `1` |
| `source_bevacizumab_vss_reported_sd_5_mgkg` | `1` |
| `source_citation_rank` | `1` |
| `source_cited_by_count` | `1` |
| `source_complex_degradation_1_day_bevacizumab` | `1` |
| `source_hydrodynamic_radius_nm_bevacizumab` | `1` |
| `source_hydrodynamic_radius_nm_palivizumab` | `1` |
| `source_kd_fcrn_uM_bevacizumab` | `1` |
| `source_kd_fcrn_uM_palivizumab` | `1` |
| `source_kd_target_nM_bevacizumab` | `1` |
| `source_koff_target_s_bevacizumab` | `1` |
| `source_molecular_weight_kda_bevacizumab` | `1` |
| `source_molecular_weight_kda_palivizumab` | `1` |
| `source_palivizumab_auc0_30_pred_nominal_growth_15_mgkg_saez` | `1` |
| `source_palivizumab_auc0_30_pred_nominal_growth_5_mgkg` | `1` |
| `source_palivizumab_auc0_30_pred_nominal_no_growth_15_mgkg_saez` | `1` |
| `source_palivizumab_auc0_30_pred_nominal_no_growth_5_mgkg` | `1` |
| `source_palivizumab_auc0_30_reported_15_mgkg_saez` | `1` |
| `source_palivizumab_auc0_30_reported_5_mgkg` | `1` |
| `source_palivizumab_auc_pred_adjusted_growth_10_mgkg` | `1` |
| `source_palivizumab_auc_pred_adjusted_growth_15_mgkg_subramanian` | `1` |
| `source_palivizumab_auc_pred_adjusted_growth_3_mgkg` | `1` |
| `source_palivizumab_auc_pred_adjusted_no_growth_10_mgkg` | `1` |
| `source_palivizumab_auc_pred_adjusted_no_growth_15_mgkg_subramanian` | `1` |
| `source_palivizumab_auc_pred_adjusted_no_growth_3_mgkg` | `1` |
| `source_palivizumab_auc_pred_nominal_growth_10_mgkg` | `1` |
| `source_palivizumab_auc_pred_nominal_growth_15_mgkg_subramanian` | `1` |
| `source_palivizumab_auc_pred_nominal_growth_3_mgkg` | `1` |
| `source_palivizumab_auc_pred_nominal_no_growth_10_mgkg` | `1` |
| `source_palivizumab_auc_pred_nominal_no_growth_15_mgkg_subramanian` | `1` |
| `source_palivizumab_auc_pred_nominal_no_growth_3_mgkg` | `1` |
| `source_palivizumab_auc_reported_10_mgkg` | `1` |
| `source_palivizumab_auc_reported_15_mgkg_subramanian` | `1` |
| `source_palivizumab_auc_reported_3_mgkg` | `1` |
| `source_palivizumab_pop_cl_ml_day_70kg` | `1` |
| `source_palivizumab_pop_q_ml_day_70kg` | `1` |
| `source_palivizumab_pop_vc_l_70kg` | `1` |
| `source_palivizumab_pop_vp_l_70kg` | `1` |
| `source_palivizumab_vc_exponent` | `1` |
| `source_palivizumab_vp_exponent` | `1` |
| `source_paper_year` | `1` |
| `source_pbpk_organs_tissues` | `1` |
| `source_target_concentration_uM_bevacizumab` | `1` |
| `source_target_synthesis_1_day_bevacizumab` | `1` |
| `vss_ml_kg` | `1` |
| `state__AUC_ug_ml_day` | `ug/mL*day` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__complex_uM` | `uM` |
| `state__elapsed_time_day` | `day` |
| `state__target_free_uM` | `uM` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `bevacizumab-15mgkg-13y-growth-table4-smoke` starter has **121 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_ug_ml` | 322.828 | 1.17503 (120 h, pre) | 322.828 (0 h, post) | 1.17503 |
| `AUC_ug_ml_day` | 0 | 0 (0 h, post) | 3927.8 (120 h, pre) | 3927.8 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
