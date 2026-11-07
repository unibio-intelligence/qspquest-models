# Gu 2017 BAY 1093884 TFPI QSS-TMDD and Exploratory SC/Human PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore TFPI binding, target-mediated disposition and exploratory BAY 1093884 exposure.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.1.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_gu_2017_bay1093884_tfpi_qss_tmdd/0.1.0/model.omex',
    expected_sha256='ead0a065a9944f7e54554c26bfc611849e863576ac15ddc8071a02c1bb92ad42',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Archived experiment ID | Purpose | Time range | Rows |
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

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `central_total_mg_L` | Total BAY 1093884 concentration | `1` |
| `free_tfpi_percent_baseline` | Free TFPI as a percentage of baseline | `1` |
| `tfpi_inhibition_percent` | Percentage inhibition of TFPI | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 137 outputs and 8 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `gu-2017-cyno-iv20mgkg-qss-tmdd-probe` starter has **1009 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_total_mg_L` | 407.332 | 0.0101706 (1008 h, pre) | 407.332 (0 h, post) | 0.0101706 |
| `free_tfpi_percent_baseline` | 7.87251 | 0.642512 (1 h, post) | 99.6078 (1008 h, pre) | 99.6078 |
| `tfpi_inhibition_percent` | 92.1275 | 0.3922 (1008 h, pre) | 99.3575 (1 h, post) | 0.3922 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
