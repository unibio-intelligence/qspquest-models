# Cheng 2022 SKB264 TROP2 ADC Preclinical PK/PD Table-Replay Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect SKB264 preclinical endpoints and exploratory tumor-growth curves.

**Runnable · 47 experiments.** Version 0.1.0.

## Run an experiment

Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_cheng_2022_skb264_trop2_adc_preclinical_pkpd', version='0.1.0')
result = model.run('exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-blue')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 47 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `corrigendum-table5` | Corrected payload KL610023 monkey plasma NCA table from the 2023 corrigendum. | 0–1 h | 2 |
| `design-affinity-cytotoxicity` | Exact design, affinity, and in vitro activity constants from text/Figures 1-3 and 7. | 0–1 h | 2 |
| `efficacy-pkpd-text` | Reported TGI, release-rate, PDX, and comparator scalars from Results. | 0–1 h | 2 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–24 h | 24 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-blue` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–20 h | 20 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–23 h | 23 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–24 h | 25 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-purple` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–24 h | 24 |
| `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–24 h | 25 |
| `exploratory-calibrated-tumor-figure-4b-hcc1806-cdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–24 h | 24 |
| `exploratory-calibrated-tumor-figure-4b-hcc1806-cdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–17 h | 16 |
| `exploratory-calibrated-tumor-figure-4b-hcc1806-cdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–24 h | 23 |
| `exploratory-calibrated-tumor-figure-4b-hcc1806-cdx-purple` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 5–24 h | 20 |
| `exploratory-calibrated-tumor-figure-4b-hcc1806-cdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–24 h | 25 |
| `exploratory-calibrated-tumor-figure-4d-br1282-pdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–24 h | 24 |
| `exploratory-calibrated-tumor-figure-4d-br1282-pdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 6–18 h | 13 |
| `exploratory-calibrated-tumor-figure-4d-br1282-pdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–24 h | 23 |
| `exploratory-calibrated-tumor-figure-4d-br1282-pdx-purple` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 7–24 h | 18 |
| `exploratory-calibrated-tumor-figure-4d-br1282-pdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–24 h | 23 |
| `exploratory-calibrated-tumor-figure-5a-0406022-pdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5a-0406022-pdx-blue` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 4–21 h | 18 |
| `exploratory-calibrated-tumor-figure-5a-0406022-pdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–21 h | 22 |
| `exploratory-calibrated-tumor-figure-5a-0406022-pdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–21 h | 22 |
| `exploratory-calibrated-tumor-figure-5a-0406022-pdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-blue` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–21 h | 20 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–21 h | 20 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-purple` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 12–19 h | 8 |
| `exploratory-calibrated-tumor-figure-5b-a11068-pdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–21 h | 20 |
| `exploratory-calibrated-tumor-figure-5c-0501116-pdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5c-0501116-pdx-blue` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 4–21 h | 18 |
| `exploratory-calibrated-tumor-figure-5c-0501116-pdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–21 h | 22 |
| `exploratory-calibrated-tumor-figure-5c-0501116-pdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 0–21 h | 22 |
| `exploratory-calibrated-tumor-figure-5c-0501116-pdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-black-vehicle` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-blue` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 4–21 h | 18 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-green` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 1–21 h | 21 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-orange` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–21 h | 20 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-purple` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 3–20 h | 18 |
| `exploratory-calibrated-tumor-figure-5d-a19058-pdx-red` | Exploratory calibrated tumor-volume ODE fitted to the first and last digitized points from a Cheng 2022 Figure 4/5 raster trajectory. This is a display/exploration scenario, not a paper-reported mechanistic PK/PD fit. | 2–21 h | 20 |
| `methods-design` | Dose, sample size, timing, and TGI method constants from Methods. | 0–1 h | 2 |
| `monkey-table2` | Exact mean/SD NCA parameters for ADC and total antibody after SKB264. | 0–1 h | 2 |
| `mouse-tissue-table4` | Exact tumor/plasma payload PK for SKB264/KL610023 and IMMU-132/SN-38. | 0–1 h | 2 |
| `payload-table3` | Exact mean/SD payload parameters after SKB264 and free KL610023. | 0–1 h | 2 |
| `source-identity` | Queue, therapeutic context, and fetched legal source flags. | 0–1 h | 2 |
| `tox-table1` | Exact design, morbidity/death count, and HNSTD from Table 1. | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `tumor_volume_mm3` | Tumor volume in the exploratory calibrated figure overlay | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_cheng_2022_skb264_trop2_adc_preclinical_pkpd --model-version 0.1.0 --scenario exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-blue --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 221 outputs and 2 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `adc_flag` | `1` |
| `approved_context_flag` | `1` |
| `bispecific_flag` | `1` |
| `br1282_pdx_skb264_0p5mg_tgi_percent` | `1` |
| `br1282_pdx_skb264_1p5mg_tgi_percent` | `1` |
| `br1282_pdx_skb264_5mg_tgi_percent` | `1` |
| `cdx_doses_per_week` | `1` |
| `cdx_hcc1806_initial_tumor_volume_mm3` | `1` |
| `cdx_nci_n87_initial_tumor_volume_mm3` | `1` |
| `cdx_total_doses` | `1` |
| `citation_rank` | `1` |
| `cited_by_count_queue` | `1` |
| `corrigendum_pdf_fetched_flag` | `1` |
| `corrigendum_table5_auc0inf_equals_auclast_flag` | `1` |
| `corrigendum_table5_kl610023_auc0inf_h_ng_ml` | `1` |
| `corrigendum_table5_kl610023_auc0inf_h_ng_ml_sd` | `1` |
| `corrigendum_table5_kl610023_auclast_h_ng_ml` | `1` |
| `corrigendum_table5_kl610023_auclast_h_ng_ml_sd` | `1` |
| `corrigendum_table5_kl610023_cl_obs_ml_kg` | `1` |
| `corrigendum_table5_kl610023_cl_obs_ml_kg_sd` | `1` |
| `corrigendum_table5_kl610023_cmax_ng_ml` | `1` |
| `corrigendum_table5_kl610023_cmax_ng_ml_sd` | `1` |
| `corrigendum_table5_kl610023_half_life_h` | `1` |
| `corrigendum_table5_kl610023_half_life_h_sd` | `1` |
| `corrigendum_table5_kl610023_vz_obs_h_ng_ml` | `1` |
| `corrigendum_table5_kl610023_vz_obs_h_ng_ml_sd` | `1` |
| `corrigendum_xml_fetched_flag` | `1` |
| `frontiers_pdf_fetched_flag` | `1` |
| `frontiers_xml_fetched_flag` | `1` |
| `gastric_pdx_positive_models_with_tgi_gt100_n` | `1` |
| `gastric_pdx_total_models_n` | `1` |
| `hcc1806_cdx_group_n` | `1` |
| `hcc1806_cdx_high_dose_mg_kg` | `1` |
| `hcc1806_cdx_low_dose_mg_kg` | `1` |
| `hcc1806_cdx_mid_dose_mg_kg` | `1` |
| `hcc1806_cell_skb264_ec50_nm` | `1` |
| `hcc1806_cell_skb264_mab_ec50_nm` | `1` |
| `hcc1806_compare_3mg_tgi_delta_percent` | `1` |
| `hcc1806_compare_immu132_10mg_tgi_percent` | `1` |
| `hcc1806_compare_immu132_1mg_tgi_percent` | `1` |
| `hcc1806_compare_immu132_3mg_tgi_percent` | `1` |
| `hcc1806_compare_skb264_10mg_tgi_percent` | `1` |
| `hcc1806_compare_skb264_1mg_tgi_percent` | `1` |
| `hcc1806_compare_skb264_3mg_tgi_percent` | `1` |
| `human_trop2_elisa_skb264_ec50_ng_ml` | `1` |
| `human_trop2_elisa_skb264_mab_ec50_ng_ml` | `1` |
| `immu132_human_trop2_spr_kd_nm` | `1` |
| `invitro_immu132_payload_release_48h_percent` | `1` |
| `invitro_skb264_payload_release_144h_percent` | `1` |
| `kl610023_cytotoxicity_ic50_max_nm` | `1` |
| `kl610023_cytotoxicity_ic50_min_nm` | `1` |
| `kl610023_hcc1806_ic50_nm` | `1` |
| `monkey_pk_group_n` | `1` |
| `monkey_pk_sample_end_h` | `1` |
| `monkey_trop2_skb264_ec50_ng_ml` | `1` |
| `monkey_trop2_skb264_mab_ec50_ng_ml` | `1` |
| `mouse_pkpd_endpoint_day` | `1` |
| `mouse_pkpd_endpoint_h` | `1` |
| `mouse_pkpd_immu132_3mg_tgi_percent` | `1` |
| `mouse_pkpd_single_dose_mg_kg` | `1` |
| `mouse_pkpd_skb264_3mg_tgi_percent` | `1` |
| `mouse_pkpd_tgi_ratio_skb264_vs_immu132` | `1` |
| `mouse_rat_trop2_low_affinity_threshold_ng_ml` | `1` |
| `nci_n87_cdx_high_dose_mg_kg` | `1` |
| `nci_n87_cdx_low_dose_mg_kg` | `1` |
| `nci_n87_cdx_mid_dose_mg_kg` | `1` |
| `nci_n87_cell_skb264_ec50_nm` | `1` |
| `nci_n87_cell_skb264_mab_ec50_nm` | `1` |
| `net_tumor_growth_rate_day` | `1` |
| `paper_year` | `1` |
| `pmc_html_fetched_flag` | `1` |
| `pmc_pdf_placeholder_flag` | `1` |
| `pmcid_available_flag` | `1` |
| `refined_rank` | `1` |
| `single_injection_infusion_min` | `1` |
| `skb264_cytotoxicity_ic50_max_nm` | `1` |
| `skb264_cytotoxicity_ic50_min_nm` | `1` |
| `skb264_dar_max` | `1` |
| `skb264_dar_mean` | `1` |
| `skb264_dar_min` | `1` |
| `skb264_human_trop2_spr_kd_nm` | `1` |
| `sn38_hcc1806_ic50_nm` | `1` |
| `summary_marker_final` | `1` |
| `supplement_indexed_flag` | `1` |
| `table2_10mg_adc_auc0inf_h_ug_ml` | `1` |
| `table2_10mg_adc_auc0inf_h_ug_ml_sd` | `1` |
| `table2_10mg_adc_auc0t_h_ug_ml` | `1` |
| `table2_10mg_adc_auc0t_h_ug_ml_sd` | `1` |
| `table2_10mg_adc_cmax_ug_ml` | `1` |
| `table2_10mg_adc_cmax_ug_ml_sd` | `1` |
| `table2_10mg_adc_half_life_h` | `1` |
| `table2_10mg_adc_half_life_h_sd` | `1` |
| `table2_10mg_adc_tmax_h` | `1` |
| `table2_10mg_adc_tmax_h_sd` | `1` |
| `table2_10mg_tab_auc0inf_h_ug_ml` | `1` |
| `table2_10mg_tab_auc0inf_h_ug_ml_sd` | `1` |
| `table2_10mg_tab_auc0t_h_ug_ml` | `1` |
| `table2_10mg_tab_auc0t_h_ug_ml_sd` | `1` |
| `table2_10mg_tab_cmax_ug_ml` | `1` |
| `table2_10mg_tab_cmax_ug_ml_sd` | `1` |
| `table2_10mg_tab_half_life_h` | `1` |
| `table2_10mg_tab_half_life_h_sd` | `1` |
| `table2_10mg_tab_tmax_h` | `1` |
| `table2_10mg_tab_tmax_h_sd` | `1` |
| `table2_1mg_adc_auc0inf_h_ug_ml` | `1` |
| `table2_1mg_adc_auc0inf_h_ug_ml_sd` | `1` |
| `table2_1mg_adc_auc0t_h_ug_ml` | `1` |
| `table2_1mg_adc_auc0t_h_ug_ml_sd` | `1` |
| `table2_1mg_adc_cmax_ug_ml` | `1` |
| `table2_1mg_adc_cmax_ug_ml_sd` | `1` |
| `table2_1mg_adc_half_life_h` | `1` |
| `table2_1mg_adc_half_life_h_sd` | `1` |
| `table2_1mg_adc_tmax_h` | `1` |
| `table2_1mg_adc_tmax_h_sd` | `1` |
| `table2_1mg_tab_auc0inf_h_ug_ml` | `1` |
| `table2_1mg_tab_auc0inf_h_ug_ml_sd` | `1` |
| `table2_1mg_tab_auc0t_h_ug_ml` | `1` |
| `table2_1mg_tab_auc0t_h_ug_ml_sd` | `1` |
| `table2_1mg_tab_cmax_ug_ml` | `1` |
| `table2_1mg_tab_cmax_ug_ml_sd` | `1` |
| `table2_1mg_tab_half_life_h` | `1` |
| `table2_1mg_tab_half_life_h_sd` | `1` |
| `table2_1mg_tab_tmax_h` | `1` |
| `table2_1mg_tab_tmax_h_sd` | `1` |
| `table2_3mg_adc_auc0inf_h_ug_ml` | `1` |
| `table2_3mg_adc_auc0inf_h_ug_ml_sd` | `1` |
| `table2_3mg_adc_auc0t_h_ug_ml` | `1` |
| `table2_3mg_adc_auc0t_h_ug_ml_sd` | `1` |
| `table2_3mg_adc_cmax_ug_ml` | `1` |
| `table2_3mg_adc_cmax_ug_ml_sd` | `1` |
| `table2_3mg_adc_half_life_h` | `1` |
| `table2_3mg_adc_half_life_h_sd` | `1` |
| `table2_3mg_adc_tmax_h` | `1` |
| `table2_3mg_adc_tmax_h_sd` | `1` |
| `table2_3mg_tab_auc0inf_h_ug_ml` | `1` |
| `table2_3mg_tab_auc0inf_h_ug_ml_sd` | `1` |
| `table2_3mg_tab_auc0t_h_ug_ml` | `1` |
| `table2_3mg_tab_auc0t_h_ug_ml_sd` | `1` |
| `table2_3mg_tab_cmax_ug_ml` | `1` |
| `table2_3mg_tab_cmax_ug_ml_sd` | `1` |
| `table2_3mg_tab_half_life_h` | `1` |
| `table2_3mg_tab_half_life_h_sd` | `1` |
| `table2_3mg_tab_tmax_h` | `1` |
| `table2_3mg_tab_tmax_h_sd` | `1` |
| `table3_free_kl610023_0p24mg_auc0inf_h_ng_ml` | `1` |
| `table3_free_kl610023_0p24mg_auc0inf_h_ng_ml_sd` | `1` |
| `table3_free_kl610023_0p24mg_auc0t_h_ng_ml` | `1` |
| `table3_free_kl610023_0p24mg_auc0t_h_ng_ml_sd` | `1` |
| `table3_free_kl610023_0p24mg_half_life_h` | `1` |
| `table3_free_kl610023_0p24mg_half_life_h_sd` | `1` |
| `table3_payload_half_life_extension_3mg_vs_free` | `1` |
| `table3_skb264_10mg_payload_auc0inf_h_ng_ml` | `1` |
| `table3_skb264_10mg_payload_auc0inf_h_ng_ml_sd` | `1` |
| `table3_skb264_10mg_payload_auc0t_h_ng_ml` | `1` |
| `table3_skb264_10mg_payload_auc0t_h_ng_ml_sd` | `1` |
| `table3_skb264_10mg_payload_cmax_ng_ml` | `1` |
| `table3_skb264_10mg_payload_cmax_ng_ml_sd` | `1` |
| `table3_skb264_10mg_payload_half_life_h` | `1` |
| `table3_skb264_10mg_payload_half_life_h_sd` | `1` |
| `table3_skb264_10mg_payload_tmax_h` | `1` |
| `table3_skb264_10mg_payload_tmax_h_sd` | `1` |
| `table3_skb264_1mg_payload_auc0inf_h_ng_ml` | `1` |
| `table3_skb264_1mg_payload_auc0inf_h_ng_ml_sd` | `1` |
| `table3_skb264_1mg_payload_auc0t_h_ng_ml` | `1` |
| `table3_skb264_1mg_payload_auc0t_h_ng_ml_sd` | `1` |
| `table3_skb264_1mg_payload_cmax_ng_ml` | `1` |
| `table3_skb264_1mg_payload_cmax_ng_ml_sd` | `1` |
| `table3_skb264_1mg_payload_half_life_h` | `1` |
| `table3_skb264_1mg_payload_half_life_h_sd` | `1` |
| `table3_skb264_1mg_payload_tmax_h` | `1` |
| `table3_skb264_1mg_payload_tmax_h_sd` | `1` |
| `table3_skb264_3mg_payload_auc0inf_h_ng_ml` | `1` |
| `table3_skb264_3mg_payload_auc0inf_h_ng_ml_sd` | `1` |
| `table3_skb264_3mg_payload_auc0t_h_ng_ml` | `1` |
| `table3_skb264_3mg_payload_auc0t_h_ng_ml_sd` | `1` |
| `table3_skb264_3mg_payload_cmax_ng_ml` | `1` |
| `table3_skb264_3mg_payload_cmax_ng_ml_sd` | `1` |
| `table3_skb264_3mg_payload_half_life_h` | `1` |
| `table3_skb264_3mg_payload_half_life_h_sd` | `1` |
| `table3_skb264_3mg_payload_tmax_h` | `1` |
| `table3_skb264_3mg_payload_tmax_h_sd` | `1` |
| `table4_plasma_half_life_ratio_skb264_vs_immu132` | `1` |
| `table4_plasma_kl610023_auc0inf_h_ng_g_or_ml` | `1` |
| `table4_plasma_kl610023_auclast_h_ng_g_or_ml` | `1` |
| `table4_plasma_kl610023_cmax_ng_g_or_ml` | `1` |
| `table4_plasma_kl610023_half_life_h` | `1` |
| `table4_plasma_kl610023_tmax_h` | `1` |
| `table4_plasma_sn38_auc0inf_h_ng_g_or_ml` | `1` |
| `table4_plasma_sn38_auclast_h_ng_g_or_ml` | `1` |
| `table4_plasma_sn38_cmax_ng_g_or_ml` | `1` |
| `table4_plasma_sn38_half_life_h` | `1` |
| `table4_plasma_sn38_tmax_h` | `1` |
| `table4_tumor_auclast_ratio_skb264_vs_immu132` | `1` |
| `table4_tumor_kl610023_auc0inf_h_ng_g_or_ml` | `1` |
| `table4_tumor_kl610023_auclast_h_ng_g_or_ml` | `1` |
| `table4_tumor_kl610023_cmax_ng_g_or_ml` | `1` |
| `table4_tumor_kl610023_half_life_h` | `1` |
| `table4_tumor_kl610023_tmax_h` | `1` |
| `table4_tumor_sn38_auc0inf_h_ng_g_or_ml` | `1` |
| `table4_tumor_sn38_auclast_h_ng_g_or_ml` | `1` |
| `table4_tumor_sn38_cmax_ng_g_or_ml` | `1` |
| `table4_tumor_sn38_half_life_h` | `1` |
| `table4_tumor_sn38_tmax_h` | `1` |
| `tox_animals_per_sex_per_group` | `1` |
| `tox_control_dose_mg_kg` | `1` |
| `tox_dosing_interval_week` | `1` |
| `tox_high_dose_female_moribund_or_dead_n` | `1` |
| `tox_high_dose_male_moribund_or_dead_n` | `1` |
| `tox_high_dose_mg_kg` | `1` |
| `tox_high_dose_total_moribund_or_dead_n` | `1` |
| `tox_hnstd_mg_kg` | `1` |
| `tox_low_dose_mg_kg` | `1` |
| `tox_mid_dose_mg_kg` | `1` |
| `tox_total_doses` | `1` |
| `trop2_ihc_activity_threshold_score` | `1` |
| `trop2_target_flag` | `1` |
| `tumor_curve_pixel_count` | `1` |
| `tumor_growth_rate_day` | `1` |
| `tumor_kill_rate_day` | `1` |
| `tumor_volume_mm3` | `1` |
| `validation_run_nonce_out` | `1` |
| `state__summary_marker` | `dimensionless` |
| `state__tumor_volume_mm3` | `mm3` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `exploratory-calibrated-tumor-figure-4a-nci-n87-cdx-blue` starter has **20 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `tumor_volume_mm3` | 143.966 | 43.1036 (20 h, pre) | 143.966 (1 h, post) | 43.1036 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
