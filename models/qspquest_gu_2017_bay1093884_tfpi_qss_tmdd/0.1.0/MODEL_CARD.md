# Gu 2017 BAY 1093884 TFPI QSS-TMDD and Exploratory SC/Human PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore TFPI binding, target-mediated disposition and exploratory BAY 1093884 exposure.

**Runnable · 6 experiments.** Version 0.1.0.

## Run an experiment

Paper-fixed Figure 7 IV parameterization with Figure 2/4/7 overlays. No exploratory parameter overrides.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_gu_2017_bay1093884_tfpi_qss_tmdd', version='0.1.0')
result = model.run('gu-2017-cyno-iv20mgkg-qss-tmdd-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `gu-2017-cyno-iv20mgkg-qss-tmdd-probe` | Paper-fixed Figure 7 IV parameterization with Figure 2/4/7 overlays. No exploratory parameter overrides. | 0–1008 h | 1009 |
| `gu-2017-cyno-iv5mgkg-qss-tmdd-probe` | Paper-fixed Figure 7 IV parameterization with complete Figure 2/4/5/6/7 overlays. No exploratory parameter overrides. | 0–720 h | 721 |
| `gu-2017-exact-table-parameter-anchor` | Exact replay of Tables I-III, Figure 7 parameters/CVs, Figure 3 IC50s, narrative anchors, license/source status, and human endpoint statements. | 0–1 h | 2 |
| `gu-2017-exploratory-calibrated-cyno-sc5mgkg-joint-figures2-4-5-6-table2` | Aggregate dual-path SC absorption extension constrained jointly by Figure 2 PK, Figures 4-6 early/late PD, and Table II Cmax/Tmax/AUC. Separate from the paper-fixed IV model. | 0–528 h | 1057 |
| `gu-2017-exploratory-calibrated-human-0p4mgkg-endpoints` | Effective endpoint-matched human scenario reproducing reported Cmax, AUC0-168, and central-concentration inhibition at 24 h. It does not recover the omitted paper human scaling parameters. | 0–168 h | 337 |
| `gu-2017-human-0p4mgkg-iv-source-limited` | Diagnostic transfer of the cynomolgus fixed effects to the reported human dose. The paper's human scaled values were not reported, so mismatch is expected and informative. | 0–168 h | 169 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_total_mg_L` | Total BAY 1093884 concentration | `1` |
| `free_tfpi_percent_baseline` | Free TFPI as a percentage of baseline | `1` |
| `tfpi_inhibition_percent` | Percentage inhibition of TFPI | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_gu_2017_bay1093884_tfpi_qss_tmdd --model-version 0.1.0 --scenario gu-2017-cyno-iv20mgkg-qss-tmdd-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 137 outputs and 8 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `article_pdf_page_count` | `1` |
| `auc_mg_h_L` | `1` |
| `bay1093884_fully_human_igg2_flag` | `1` |
| `central_free_mg_L` | `1` |
| `central_free_nM` | `1` |
| `central_total_mg_L` | `1` |
| `central_total_nM` | `1` |
| `citation_rank` | `1` |
| `cited_by_count` | `1` |
| `cl_L_h_kg` | `1` |
| `cld_L_h_kg` | `1` |
| `complex_nM` | `1` |
| `creative_commons_by_4_flag` | `1` |
| `crossref_metadata_flag` | `1` |
| `day7_dpt_half_effect_drug_nM` | `1` |
| `day7_tfpi_half_effect_drug_nM` | `1` |
| `dose_mg_kg` | `1` |
| `dpt_clotting_time_sec_joint_observation` | `1` |
| `europepmc_metadata_flag` | `1` |
| `exploratory_human_target_inhibition_percent` | `1` |
| `fig7_cl_L_h_kg` | `1` |
| `fig7_cl_cv_percent` | `1` |
| `fig7_cld_L_h_kg` | `1` |
| `fig7_cld_cv_percent` | `1` |
| `fig7_kdeg_cv_percent` | `1` |
| `fig7_kdeg_h` | `1` |
| `fig7_kint_cv_percent` | `1` |
| `fig7_kint_h` | `1` |
| `fig7_kss_cv_percent` | `1` |
| `fig7_kss_nM` | `1` |
| `fig7_ksyn_cv_percent` | `1` |
| `fig7_ksyn_nM_h` | `1` |
| `fig7_vc_L_kg` | `1` |
| `fig7_vc_cv_percent` | `1` |
| `fig7_vss_model_L_kg` | `1` |
| `fig7_vt_L_kg` | `1` |
| `fig7_vt_cv_percent` | `1` |
| `free_tfpi_nM` | `1` |
| `free_tfpi_ng_mL_joint_observation` | `1` |
| `free_tfpi_percent_baseline` | `1` |
| `free_tfpi_percent_joint_observation` | `1` |
| `human_circulating_tfpi_nM` | `1` |
| `human_sim_auc0_168_mg_h_L` | `1` |
| `human_sim_cmax_mg_L` | `1` |
| `human_sim_duration_h` | `1` |
| `human_sim_initial_central_mg_L_from_cyno_vc` | `1` |
| `human_sim_iv_dose_mg_kg` | `1` |
| `human_sim_tfpi_inhibition_max_percent` | `1` |
| `human_sim_tfpi_inhibition_min_percent` | `1` |
| `invitro_dpt_clotting_time_sec_response` | `1` |
| `invitro_dpt_ic50_nM` | `1` |
| `invitro_free_tfpi_ic50_nM` | `1` |
| `invitro_free_tfpi_percent_response` | `1` |
| `iv20_initial_central_mg_L` | `1` |
| `iv20_tfpi_below10_duration_day` | `1` |
| `iv5_initial_central_mg_L` | `1` |
| `iv5_tfpi_low_duration_max_day` | `1` |
| `iv5_tfpi_low_duration_min_day` | `1` |
| `iv_dose_high_mg_kg` | `1` |
| `iv_dose_low_mg_kg` | `1` |
| `kdeg_h` | `1` |
| `kel_linear_h` | `1` |
| `kint_h` | `1` |
| `kss_nM` | `1` |
| `ksyn_nM_h` | `1` |
| `main_figure_count` | `1` |
| `main_table_count` | `1` |
| `model_baseline_tfpi_nM` | `1` |
| `model_baseline_tfpi_runtime_nM` | `1` |
| `molecular_weight_kDa` | `1` |
| `nM_per_mg_L` | `1` |
| `normal_monkey_tfpi_max_ng_mL` | `1` |
| `normal_monkey_tfpi_min_ng_mL` | `1` |
| `official_web_text_extraction_flag` | `1` |
| `paper_year` | `1` |
| `peripheral_free_nM` | `1` |
| `permissive_license_flag` | `1` |
| `preprint_exact_search_checked_flag` | `1` |
| `real_article_pdf_binary_count` | `1` |
| `refined_rank` | `1` |
| `sc_absorption_nmol_h_kg` | `1` |
| `sc_dose_mg_kg` | `1` |
| `sc_tfpi_below10_time_h` | `1` |
| `sc_tfpi_half_baseline_time_h` | `1` |
| `supplement_indexed_count` | `1` |
| `table1_apt_post_sec` | `1` |
| `table1_apt_pre_sec` | `1` |
| `table1_dpt_post_sec` | `1` |
| `table1_dpt_pre_sec` | `1` |
| `table1_pt_post_sec` | `1` |
| `table1_pt_pre_sec` | `1` |
| `table1_tfpi_post_below_lloq_flag` | `1` |
| `table1_tfpi_post_lloq_ng_mL` | `1` |
| `table1_tfpi_pre_ng_mL` | `1` |
| `table2_igg_iv20_aucnorm_kg_h_L` | `1` |
| `table2_igg_iv20_cl_mL_h_kg` | `1` |
| `table2_igg_iv20_half_life_h` | `1` |
| `table2_igg_iv20_mrt_h` | `1` |
| `table2_igg_iv20_vss_mL_kg` | `1` |
| `table2_igg_iv5_aucnorm_kg_h_L` | `1` |
| `table2_igg_iv5_cl_mL_h_kg` | `1` |
| `table2_igg_iv5_half_life_h` | `1` |
| `table2_igg_iv5_mrt_h` | `1` |
| `table2_igg_iv5_vss_mL_kg` | `1` |
| `table2_igg_sc5_aucnorm_kg_h_L` | `1` |
| `table2_igg_sc5_bioavailability_percent` | `1` |
| `table2_igg_sc5_cmax_ug_mL` | `1` |
| `table2_igg_sc5_half_life_h` | `1` |
| `table2_igg_sc5_mrt_h` | `1` |
| `table2_igg_sc5_tmax_h` | `1` |
| `table2_tfpi_iv5_aucnorm_kg_h_L` | `1` |
| `table2_tfpi_iv5_cl_mL_h_kg` | `1` |
| `table2_tfpi_iv5_half_life_h` | `1` |
| `table2_tfpi_iv5_mrt_h` | `1` |
| `table2_tfpi_iv5_vss_mL_kg` | `1` |
| `table2_tfpi_sc5_aucnorm_kg_h_L` | `1` |
| `table2_tfpi_sc5_bioavailability_percent` | `1` |
| `table2_tfpi_sc5_cmax_ug_mL` | `1` |
| `table2_tfpi_sc5_half_life_h` | `1` |
| `table2_tfpi_sc5_mrt_h` | `1` |
| `table2_tfpi_sc5_tmax_h` | `1` |
| `table3_cyn82245_free_tfpi_mean_ng_mL` | `1` |
| `table3_cyn82245_free_tfpi_sd_ng_mL` | `1` |
| `table3_cyn91464_free_tfpi_mean_ng_mL` | `1` |
| `table3_cyn91464_free_tfpi_sd_ng_mL` | `1` |
| `table3_cyn91465_free_tfpi_mean_ng_mL` | `1` |
| `table3_cyn91465_free_tfpi_sd_ng_mL` | `1` |
| `table3_cyn93315_free_tfpi_mean_ng_mL` | `1` |
| `table3_cyn93315_free_tfpi_sd_ng_mL` | `1` |
| `table3_cyn97393_free_tfpi_mean_ng_mL` | `1` |
| `table3_cyn97393_free_tfpi_sd_ng_mL` | `1` |
| `tfpi_depleted_plasma_lloq_flag` | `1` |
| `tfpi_inhibition_percent` | `1` |
| `validation_run_nonce` | `1` |
| `vc_L_kg` | `1` |
| `vss_L_kg_runtime` | `1` |
| `vt_L_kg` | `1` |
| `state__auc_mg_h_L` | `mg*h/L` |
| `state__central_total_nmol_kg` | `nmol/kg` |
| `state__elapsed_h` | `h` |
| `state__peripheral_free_nmol_kg` | `nmol/kg` |
| `state__sc_fast_depot_nmol_kg` | `nmol/kg` |
| `state__sc_slow_depot_nmol_kg` | `nmol/kg` |
| `state__sc_slow_transit_nmol_kg` | `nmol/kg` |
| `state__target_total_nM` | `nM` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `gu-2017-cyno-iv20mgkg-qss-tmdd-probe` starter has **1009 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_total_mg_L` | 407.332 | 0.0101706 (1008 h, pre) | 407.332 (0 h, post) | 0.0101706 |
| `free_tfpi_percent_baseline` | 7.87251 | 0.642512 (1 h, post) | 99.6078 (1008 h, pre) | 99.6078 |
| `tfpi_inhibition_percent` | 92.1275 | 0.3922 (1008 h, pre) | 99.3575 (1 h, post) | 0.3922 |

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
Evidence identity: `sha256:4cfdb4cd8258e62becf8312df0bbe4cc0615e20d0d9e91c09efc09c9efcb2cd1`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Paper-fixed cynomolgus IV QSS-TMDD model for BAY 1093884/befovacimab, augmented with digitized Figures 2-7, Figure 3 assay observation functions, and separately labelled exploratory SC absorption and human endpoint-calibrated scenarios.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
