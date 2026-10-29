# Chang 2025 Positively Charged Trastuzumab-vc-MMAE ADC Mouse PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare charged and wild-type trastuzumab ADC exposure and mouse study endpoints.

**Runnable · 37 experiments.** Version 0.1.0.

## Run an experiment

Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_chang_2025_charged_trastuzumab_adc_mice_pkpd', version='0.1.0')
result = model.run('ode-charged-liver-free-mmae-aucall-h-nm')
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
| `ode-charged-liver-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-liver-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-liver-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-mcf7-tumor-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-mcf7-tumor-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-mcf7-tumor-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-n87-tumor-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-n87-tumor-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-n87-tumor-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-plasma-free-mmae-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-plasma-total-mab-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-plasma-total-mmae-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-spleen-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-spleen-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-charged-spleen-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-liver-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-liver-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-liver-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-mcf7-tumor-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-mcf7-tumor-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-mcf7-tumor-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-n87-tumor-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-n87-tumor-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-n87-tumor-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-plasma-free-mmae-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-plasma-total-mab-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-plasma-total-mmae-aucinf-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-spleen-free-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-spleen-total-mab-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `ode-wt-spleen-total-mmae-aucall-h-nm` | Reduced first-order exposure ODE initialized at the reported Cmax and scaled so the invariant AUC endpoint equals the paper NCA AUC. | 0–168 h | 169 |
| `source-identity-and-design` | Exact paper anchors from article methods/results text and queue row | 0–1 h | 2 |
| `table-liver-pk` | Exact paper anchors from Table 4, PK parameters in liver. | 0–1 h | 2 |
| `table-mcf7-tumor-pk` | Exact paper anchors from Table 3, PK parameters in MCF-7 tumors. | 0–1 h | 2 |
| `table-n87-tumor-pk` | Exact paper anchors from Table 2, PK parameters in NCI-N87 tumors. | 0–1 h | 2 |
| `table-plasma-pk` | Exact paper anchors from Table 1, plasma PK of WT and positively charged (+5) ADCs in mice. | 0–1 h | 2 |
| `table-spleen-pk` | Exact paper anchors from Table 5, PK parameters in spleen. | 0–1 h | 2 |
| `table6-ratios-and-text-fold-changes` | Exact paper anchors from Table 6 and Results text fold-change checks | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `C_nM` | Selected analyte concentration in the tissue named by this experiment | `1` |
| `AUC_h_nM` | Accumulated exposure to the analyte in the tissue named by this experiment | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_chang_2025_charged_trastuzumab_adc_mice_pkpd --model-version 0.1.0 --scenario ode-charged-liver-free-mmae-aucall-h-nm --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 177 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_h_nM` | `1` |
| `C_nM` | `1` |
| `adc_flag` | `1` |
| `charged_adc_dar` | `1` |
| `charged_adc_tcep_equiv` | `1` |
| `charged_liver_free_mmae_aucall_h_nm` | `1` |
| `charged_liver_free_mmae_cmax_nm` | `1` |
| `charged_liver_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_liver_free_mmae_tmax_h` | `1` |
| `charged_liver_total_mab_aucall_h_nm` | `1` |
| `charged_liver_total_mab_cmax_nm` | `1` |
| `charged_liver_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_liver_total_mab_tmax_h` | `1` |
| `charged_liver_total_mmae_aucall_h_nm` | `1` |
| `charged_liver_total_mmae_cmax_nm` | `1` |
| `charged_liver_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_liver_total_mmae_tmax_h` | `1` |
| `charged_mcf7_tumor_free_mmae_aucall_h_nm` | `1` |
| `charged_mcf7_tumor_free_mmae_cmax_nm` | `1` |
| `charged_mcf7_tumor_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_mcf7_tumor_free_mmae_tmax_h` | `1` |
| `charged_mcf7_tumor_total_mab_aucall_h_nm` | `1` |
| `charged_mcf7_tumor_total_mab_cmax_nm` | `1` |
| `charged_mcf7_tumor_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_mcf7_tumor_total_mab_tmax_h` | `1` |
| `charged_mcf7_tumor_total_mmae_aucall_h_nm` | `1` |
| `charged_mcf7_tumor_total_mmae_cmax_nm` | `1` |
| `charged_mcf7_tumor_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_mcf7_tumor_total_mmae_tmax_h` | `1` |
| `charged_n87_tumor_free_mmae_aucall_h_nm` | `1` |
| `charged_n87_tumor_free_mmae_cmax_nm` | `1` |
| `charged_n87_tumor_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_n87_tumor_free_mmae_tmax_h` | `1` |
| `charged_n87_tumor_total_mab_aucall_h_nm` | `1` |
| `charged_n87_tumor_total_mab_cmax_nm` | `1` |
| `charged_n87_tumor_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_n87_tumor_total_mab_tmax_h` | `1` |
| `charged_n87_tumor_total_mmae_aucall_h_nm` | `1` |
| `charged_n87_tumor_total_mmae_cmax_nm` | `1` |
| `charged_n87_tumor_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_n87_tumor_total_mmae_tmax_h` | `1` |
| `charged_plasma_free_mmae_auc0t_h_nm` | `1` |
| `charged_plasma_free_mmae_aucinf_h_nm` | `1` |
| `charged_plasma_free_mmae_cmax_nm` | `1` |
| `charged_plasma_free_mmae_half_life_h` | `1` |
| `charged_plasma_total_mab_auc0t_h_nm` | `1` |
| `charged_plasma_total_mab_aucinf_h_nm` | `1` |
| `charged_plasma_total_mab_cl_ml_h` | `1` |
| `charged_plasma_total_mab_cmax_nm` | `1` |
| `charged_plasma_total_mab_half_life_h` | `1` |
| `charged_plasma_total_mab_vss_ml` | `1` |
| `charged_plasma_total_mmae_auc0t_h_nm` | `1` |
| `charged_plasma_total_mmae_aucinf_h_nm` | `1` |
| `charged_plasma_total_mmae_cl_ml_h` | `1` |
| `charged_plasma_total_mmae_cmax_nm` | `1` |
| `charged_plasma_total_mmae_half_life_h` | `1` |
| `charged_plasma_total_mmae_vss_ml` | `1` |
| `charged_spleen_free_mmae_aucall_h_nm` | `1` |
| `charged_spleen_free_mmae_cmax_nm` | `1` |
| `charged_spleen_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_spleen_free_mmae_tmax_h` | `1` |
| `charged_spleen_total_mab_aucall_h_nm` | `1` |
| `charged_spleen_total_mab_cmax_nm` | `1` |
| `charged_spleen_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_spleen_total_mab_tmax_h` | `1` |
| `charged_spleen_total_mmae_aucall_h_nm` | `1` |
| `charged_spleen_total_mmae_cmax_nm` | `1` |
| `charged_spleen_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `charged_spleen_total_mmae_tmax_h` | `1` |
| `citation_rank` | `1` |
| `cited_by_count_queue` | `1` |
| `cytotoxicity_incubation_h` | `1` |
| `cytotoxicity_max_conc_nM` | `1` |
| `cytotoxicity_min_conc_nM` | `1` |
| `efficacy_charged_n` | `1` |
| `efficacy_control_n` | `1` |
| `efficacy_dose_mg_kg` | `1` |
| `efficacy_total_n` | `1` |
| `efficacy_wt_n` | `1` |
| `elapsed_h` | `1` |
| `mcf7_ic50_ratio_approx` | `1` |
| `mcf7_tumor_total_mmae_auc_fold_wt_vs_charged` | `1` |
| `mda_mb_468_ic50_ratio_approx` | `1` |
| `n87_ic50_ratio_approx_max` | `1` |
| `n87_tumor_total_mmae_auc_fold_wt_vs_charged` | `1` |
| `ode_auc_endpoint_h_nM` | `1` |
| `ode_cmax_endpoint_nM` | `1` |
| `ode_half_life_h` | `1` |
| `ode_kel_1_h` | `1` |
| `pk_study_dose_mg_kg` | `1` |
| `pk_study_mice_per_adc_per_xenograft_n` | `1` |
| `pk_study_mice_per_xenograft_n` | `1` |
| `pk_study_mice_total_n` | `1` |
| `pk_time_168h` | `1` |
| `pk_time_24h` | `1` |
| `pk_time_6h` | `1` |
| `pk_time_72h` | `1` |
| `pk_time_early_h` | `1` |
| `plasma_total_mab_cl_fold_charged_vs_wt` | `1` |
| `plasma_total_mab_half_life_fold_wt_vs_charged` | `1` |
| `pmcid_available_flag` | `1` |
| `positive_charge_net` | `1` |
| `publication_year` | `1` |
| `supplement_binary_fetched_flag` | `1` |
| `supplement_expected_flag` | `1` |
| `target_auc_h_nM` | `1` |
| `target_cmax_nM` | `1` |
| `target_tmax_h` | `1` |
| `trastuzumab_backbone_flag` | `1` |
| `tumor_volume_stop_mm3` | `1` |
| `validation_run_nonce` | `1` |
| `wt_adc_dar` | `1` |
| `wt_adc_tcep_equiv` | `1` |
| `wt_liver_free_mmae_aucall_h_nm` | `1` |
| `wt_liver_free_mmae_cmax_nm` | `1` |
| `wt_liver_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_liver_free_mmae_tmax_h` | `1` |
| `wt_liver_total_mab_aucall_h_nm` | `1` |
| `wt_liver_total_mab_cmax_nm` | `1` |
| `wt_liver_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_liver_total_mab_tmax_h` | `1` |
| `wt_liver_total_mmae_aucall_h_nm` | `1` |
| `wt_liver_total_mmae_cmax_nm` | `1` |
| `wt_liver_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_liver_total_mmae_tmax_h` | `1` |
| `wt_mcf7_tumor_free_mmae_aucall_h_nm` | `1` |
| `wt_mcf7_tumor_free_mmae_cmax_nm` | `1` |
| `wt_mcf7_tumor_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_mcf7_tumor_free_mmae_tmax_h` | `1` |
| `wt_mcf7_tumor_total_mab_aucall_h_nm` | `1` |
| `wt_mcf7_tumor_total_mab_cmax_nm` | `1` |
| `wt_mcf7_tumor_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_mcf7_tumor_total_mab_tmax_h` | `1` |
| `wt_mcf7_tumor_total_mmae_aucall_h_nm` | `1` |
| `wt_mcf7_tumor_total_mmae_cmax_nm` | `1` |
| `wt_mcf7_tumor_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_mcf7_tumor_total_mmae_tmax_h` | `1` |
| `wt_n87_tumor_free_mmae_aucall_h_nm` | `1` |
| `wt_n87_tumor_free_mmae_cmax_nm` | `1` |
| `wt_n87_tumor_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_n87_tumor_free_mmae_tmax_h` | `1` |
| `wt_n87_tumor_total_mab_aucall_h_nm` | `1` |
| `wt_n87_tumor_total_mab_cmax_nm` | `1` |
| `wt_n87_tumor_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_n87_tumor_total_mab_tmax_h` | `1` |
| `wt_n87_tumor_total_mmae_aucall_h_nm` | `1` |
| `wt_n87_tumor_total_mmae_cmax_nm` | `1` |
| `wt_n87_tumor_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_n87_tumor_total_mmae_tmax_h` | `1` |
| `wt_plasma_free_mmae_auc0t_h_nm` | `1` |
| `wt_plasma_free_mmae_aucinf_h_nm` | `1` |
| `wt_plasma_free_mmae_cmax_nm` | `1` |
| `wt_plasma_free_mmae_half_life_h` | `1` |
| `wt_plasma_total_mab_auc0t_h_nm` | `1` |
| `wt_plasma_total_mab_aucinf_h_nm` | `1` |
| `wt_plasma_total_mab_cl_ml_h` | `1` |
| `wt_plasma_total_mab_cmax_nm` | `1` |
| `wt_plasma_total_mab_half_life_h` | `1` |
| `wt_plasma_total_mab_vss_ml` | `1` |
| `wt_plasma_total_mmae_auc0t_h_nm` | `1` |
| `wt_plasma_total_mmae_aucinf_h_nm` | `1` |
| `wt_plasma_total_mmae_cl_ml_h` | `1` |
| `wt_plasma_total_mmae_cmax_nm` | `1` |
| `wt_plasma_total_mmae_half_life_h` | `1` |
| `wt_plasma_total_mmae_vss_ml` | `1` |
| `wt_spleen_free_mmae_aucall_h_nm` | `1` |
| `wt_spleen_free_mmae_cmax_nm` | `1` |
| `wt_spleen_free_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_spleen_free_mmae_tmax_h` | `1` |
| `wt_spleen_total_mab_aucall_h_nm` | `1` |
| `wt_spleen_total_mab_cmax_nm` | `1` |
| `wt_spleen_total_mab_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_spleen_total_mab_tmax_h` | `1` |
| `wt_spleen_total_mmae_aucall_h_nm` | `1` |
| `wt_spleen_total_mmae_cmax_nm` | `1` |
| `wt_spleen_total_mmae_tissue_to_plasma_auc_ratio_percent` | `1` |
| `wt_spleen_total_mmae_tmax_h` | `1` |
| `state__AUC_h_nM` | `h*nM` |
| `state__C_nM` | `nM` |
| `state__elapsed_h` | `h` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `ode-charged-liver-free-mmae-aucall-h-nm` starter has **169 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `C_nM` | 221 | 7.45092e-09 (168 h, pre) | 221 (0 h, post) | 7.45092e-09 |
| `AUC_h_nM` | 0 | 0 (0 h, post) | 1540 (168 h, pre) | 1540 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
