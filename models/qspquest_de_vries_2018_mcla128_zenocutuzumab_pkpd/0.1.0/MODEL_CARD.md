# de Vries Schultink 2018 MCLA-128/Zenocutuzumab Translational PK-PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore translational zenocutuzumab exposure and pharmacodynamic scenarios.

**Runnable · 10 experiments · 5 unavailable.** Version 0.1.0.

## Run an experiment

Single 360 mg human flat dose using Table 1 70 kg parameters, exercising receptor occupancy and nonlinear clearance.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_de_vries_2018_mcla128_zenocutuzumab_pkpd', version='0.1.0')
result = model.run('human-360mg-q3wk-ro-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `figure1-cyno-100mgkg-vpc-digitized-source-limited` | Digitized observed median VPC curve only; runtime simulation is intentionally not claimed because raw cynomolgus records, weights, random effects, and VPC replicates are not public. | 0–1008 h | 43 |
| `figure1-cyno-10mgkg-vpc-digitized-source-limited` | Digitized observed median VPC curve only; runtime simulation is intentionally not claimed because raw cynomolgus records, weights, random effects, and VPC replicates are not public. | 0–336 h | 15 |
| `figure1-cyno-30mgkg-vpc-digitized-source-limited` | Digitized observed median VPC curve only; runtime simulation is intentionally not claimed because raw cynomolgus records, weights, random effects, and VPC replicates are not public. | 0–504 h | 22 |
| `human-360mg-q3wk-ro-probe` | Single 360 mg human flat dose using Table 1 70 kg parameters, exercising receptor occupancy and nonlinear clearance. | 0–504 h | 23 |
| `mouse-vehicle-fig4-population-probe` | Figure 4 vehicle red population prediction curve; no MCLA-128 dosing. | 0–1440 h | 61 |
| `source-status-and-identity` | Legal source retrieval and supplement/preprint audit checks. | 0–1 h | 2 |
| `study-design-and-methods` | Exact checks for animal study design, assay, software, allometry, NOAEL, and receptor-occupancy methods. | 0–1 h | 2 |
| `table1-pk-parameters` | Exact checks for allometrically reported PK parameters and variability. | 0–1 h | 2 |
| `table2-tumor-pd-parameters` | Exact checks for JIMT-1 xenograft tumor-growth parameters and variability. | 0–1 h | 2 |
| `table3-human-dose-predictions` | Exact checks for all dose/AUC/safety-margin/receptor-occupancy rows. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_L` | Zenocutuzumab concentration in the central compartment | `1` |
| `receptor_occupancy_percent` | Percentage of receptor occupied by antibody | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_de_vries_2018_mcla128_zenocutuzumab_pkpd --model-version 0.1.0 --scenario human-360mg-q3wk-ro-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 201 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `central_conc_mg_L` | `1` |
| `linear_clearance_mg_h` | `1` |
| `nonlinear_clearance_mg_h` | `1` |
| `peripheral_conc_mg_L` | `1` |
| `receptor_occupancy_percent` | `1` |
| `source_CL_L_h` | `1` |
| `source_CL_rse_percent` | `1` |
| `source_EC50_KD_rse_percent` | `1` |
| `source_EC50_KD_ug_L` | `1` |
| `source_EC50_Kio_mg_L` | `1` |
| `source_EC50_Kio_rse_percent` | `1` |
| `source_KD_1_h` | `1` |
| `source_KD_rse_percent` | `1` |
| `source_KG_mm3_h` | `1` |
| `source_KG_rse_percent` | `1` |
| `source_Kio_1_h` | `1` |
| `source_Kio_rse_percent` | `1` |
| `source_Km_mg_L` | `1` |
| `source_Q_L_h` | `1` |
| `source_Q_rse_percent` | `1` |
| `source_V1_L` | `1` |
| `source_V1_rse_percent` | `1` |
| `source_V2_L` | `1` |
| `source_V2_rse_percent` | `1` |
| `source_Vmax_mg_h` | `1` |
| `source_Vmax_rse_percent` | `1` |
| `source_biorxiv_medrxiv_preprint_found_flag` | `1` |
| `source_citation_rank` | `1` |
| `source_cited_by_count_in_queue` | `1` |
| `source_cl_q_vmax_allometric_factor` | `1` |
| `source_completeness_score` | `1` |
| `source_crossref_metadata_available` | `1` |
| `source_cyno_dose_high_mg_kg` | `1` |
| `source_cyno_dose_low_mg_kg` | `1` |
| `source_cyno_dose_mid_mg_kg` | `1` |
| `source_cyno_lloq_ng_mL` | `1` |
| `source_cynomolgus_monkeys_total_n` | `1` |
| `source_doi_available` | `1` |
| `source_dose1000_auc_g_h_L` | `1` |
| `source_dose1000_cave_ro_percent` | `1` |
| `source_dose1000_cmax_ro_percent` | `1` |
| `source_dose1000_ctrough_ro_percent` | `1` |
| `source_dose1000_safety_margin` | `1` |
| `source_dose10_auc_g_h_L` | `1` |
| `source_dose10_cave_ro_percent` | `1` |
| `source_dose10_cmax_ro_percent` | `1` |
| `source_dose10_ctrough_ro_percent` | `1` |
| `source_dose10_safety_margin` | `1` |
| `source_dose1200_auc_g_h_L` | `1` |
| `source_dose1200_cave_ro_percent` | `1` |
| `source_dose1200_cmax_ro_percent` | `1` |
| `source_dose1200_ctrough_ro_percent` | `1` |
| `source_dose1200_safety_margin` | `1` |
| `source_dose160_auc_g_h_L` | `1` |
| `source_dose160_cave_ro_percent` | `1` |
| `source_dose160_cmax_ro_percent` | `1` |
| `source_dose160_ctrough_ro_percent` | `1` |
| `source_dose160_safety_margin` | `1` |
| `source_dose20_auc_g_h_L` | `1` |
| `source_dose20_cave_ro_percent` | `1` |
| `source_dose20_cmax_ro_percent` | `1` |
| `source_dose20_ctrough_ro_percent` | `1` |
| `source_dose20_safety_margin` | `1` |
| `source_dose240_auc_g_h_L` | `1` |
| `source_dose240_cave_ro_percent` | `1` |
| `source_dose240_cmax_ro_percent` | `1` |
| `source_dose240_ctrough_ro_percent` | `1` |
| `source_dose240_safety_margin` | `1` |
| `source_dose360_auc_g_h_L` | `1` |
| `source_dose360_cave_ro_percent` | `1` |
| `source_dose360_cmax_ro_percent` | `1` |
| `source_dose360_ctrough_ro_percent` | `1` |
| `source_dose360_safety_margin` | `1` |
| `source_dose40_auc_g_h_L` | `1` |
| `source_dose40_cave_ro_percent` | `1` |
| `source_dose40_cmax_ro_percent` | `1` |
| `source_dose40_ctrough_ro_percent` | `1` |
| `source_dose40_safety_margin` | `1` |
| `source_dose480_auc_g_h_L` | `1` |
| `source_dose480_cave_ro_percent` | `1` |
| `source_dose480_cmax_ro_percent` | `1` |
| `source_dose480_ctrough_ro_percent` | `1` |
| `source_dose480_safety_margin` | `1` |
| `source_dose600_auc_g_h_L` | `1` |
| `source_dose600_cave_ro_percent` | `1` |
| `source_dose600_cmax_ro_percent` | `1` |
| `source_dose600_ctrough_ro_percent` | `1` |
| `source_dose600_safety_margin` | `1` |
| `source_dose750_auc_g_h_L` | `1` |
| `source_dose750_cave_ro_percent` | `1` |
| `source_dose750_cmax_ro_percent` | `1` |
| `source_dose750_ctrough_ro_percent` | `1` |
| `source_dose750_safety_margin` | `1` |
| `source_dose80_auc_g_h_L` | `1` |
| `source_dose80_cave_ro_percent` | `1` |
| `source_dose80_cmax_ro_percent` | `1` |
| `source_dose80_ctrough_ro_percent` | `1` |
| `source_dose80_safety_margin` | `1` |
| `source_dose900_auc_g_h_L` | `1` |
| `source_dose900_cave_ro_percent` | `1` |
| `source_dose900_cmax_ro_percent` | `1` |
| `source_dose900_ctrough_ro_percent` | `1` |
| `source_dose900_safety_margin` | `1` |
| `source_efficacious_dose_threshold_mg` | `1` |
| `source_europepmc_fulltext_xml_available` | `1` |
| `source_first_cycle_day` | `1` |
| `source_focei_flag` | `1` |
| `source_human_reference_weight_kg` | `1` |
| `source_iiv_CL_cv_percent` | `1` |
| `source_iiv_CL_shrinkage_percent` | `1` |
| `source_iiv_KD_cv_percent` | `1` |
| `source_iiv_KD_shrinkage_percent` | `1` |
| `source_iiv_KG_cv_percent` | `1` |
| `source_iiv_KG_shrinkage_percent` | `1` |
| `source_iiv_V1_cv_percent` | `1` |
| `source_iiv_V1_shrinkage_percent` | `1` |
| `source_iiv_baseline_cv_percent` | `1` |
| `source_iiv_baseline_shrinkage_percent` | `1` |
| `source_jimt1_cells_injected_n` | `1` |
| `source_km_scaled_flag` | `1` |
| `source_km_sensitivity_high_dose_ro99_mg` | `1` |
| `source_km_sensitivity_high_mg_L` | `1` |
| `source_km_sensitivity_low_dose_ro99_mg` | `1` |
| `source_km_sensitivity_low_mg_L` | `1` |
| `source_mouse_CL_L_h` | `1` |
| `source_mouse_Km_mg_L` | `1` |
| `source_mouse_Q_L_h` | `1` |
| `source_mouse_V1_L` | `1` |
| `source_mouse_V2_L` | `1` |
| `source_mouse_Vmax_mg_h` | `1` |
| `source_mouse_age_max_week` | `1` |
| `source_mouse_age_min_week` | `1` |
| `source_mouse_auc_matched_dose_360mg_mg_kg` | `1` |
| `source_mouse_auc_matched_dose_750mg_mg_kg` | `1` |
| `source_mouse_auc_matched_dose_900mg_mg_kg` | `1` |
| `source_mouse_euthanasia_day` | `1` |
| `source_mouse_euthanasia_tumor_mm3` | `1` |
| `source_mouse_group_n` | `1` |
| `source_mouse_high_dose_mg_kg` | `1` |
| `source_mouse_low_dose_mg_kg` | `1` |
| `source_mouse_reference_weight_kg` | `1` |
| `source_mouse_treatment_doses_n` | `1` |
| `source_mouse_tumor_volume_start_max_mm3` | `1` |
| `source_mouse_tumor_volume_start_min_mm3` | `1` |
| `source_noael_auc_g_h_L` | `1` |
| `source_noael_mg_kg` | `1` |
| `source_nonmem_version_major` | `1` |
| `source_nonmem_version_minor` | `1` |
| `source_ofv_drop_significant` | `1` |
| `source_ofv_p_threshold` | `1` |
| `source_page_count` | `1` |
| `source_page_end` | `1` |
| `source_page_start` | `1` |
| `source_pirana_version_major` | `1` |
| `source_pirana_version_minor` | `1` |
| `source_pk_add_error_sd` | `1` |
| `source_pk_prop_error_rse_percent` | `1` |
| `source_pk_prop_error_sd` | `1` |
| `source_pk_prop_error_shrinkage_percent` | `1` |
| `source_pmc_html_available` | `1` |
| `source_pmc_xml_available` | `1` |
| `source_pmcid_available` | `1` |
| `source_pmid_available` | `1` |
| `source_progression_factor_1_week` | `1` |
| `source_progression_factor_rse_percent` | `1` |
| `source_psn_version_major` | `1` |
| `source_psn_version_minor` | `1` |
| `source_publication_year` | `1` |
| `source_r_version_major` | `1` |
| `source_r_version_minor` | `1` |
| `source_repeated_dose_animals_n` | `1` |
| `source_repeated_dose_first_week_included_flag` | `1` |
| `source_repeated_dose_samples_per_animal_n` | `1` |
| `source_repeated_dose_sampling_end_h` | `1` |
| `source_ro_cmax_cave_gt99_from_mg` | `1` |
| `source_ro_ctrough_gt99_from_mg` | `1` |
| `source_ro_target_percent` | `1` |
| `source_safe_margin_threshold_fold` | `1` |
| `source_safe_starting_dose_max_mg` | `1` |
| `source_safe_starting_dose_min_mg` | `1` |
| `source_single_dose_samples_per_animal_n` | `1` |
| `source_single_dose_sampling_end_h` | `1` |
| `source_single_dose_toxicity_animals_n` | `1` |
| `source_springer_html_available` | `1` |
| `source_springer_pdf_available` | `1` |
| `source_supplement_links_detected_flag` | `1` |
| `source_supplement_listed_by_europepmc_flag` | `1` |
| `source_treatment_start_day` | `1` |
| `source_tumor_baseline_mm3` | `1` |
| `source_tumor_baseline_rse_percent` | `1` |
| `source_tumor_extraction_after_last_dose_h` | `1` |
| `source_tumor_prop_error_cv_percent` | `1` |
| `source_tumor_prop_error_rse_percent` | `1` |
| `source_tumor_prop_error_shrinkage_percent` | `1` |
| `source_tumor_stasis_evaluation_day` | `1` |
| `source_tumor_stasis_q1wk_doses_n` | `1` |
| `source_volume_allometric_factor` | `1` |
| `source_vpc_replicates_n` | `1` |
| `target_mediated_clearance_fraction` | `1` |
| `tumor_death_rate_mm3_h` | `1` |
| `tumor_growth_rate_mm3_h` | `1` |
| `state__AUC_mg_h_L` | `mg*h/L` |
| `state__central_mg` | `mg` |
| `state__elapsed_h` | `h` |
| `state__growth_effect` | `fraction` |
| `state__peripheral_mg` | `mg` |
| `state__tumor_mm3` | `mm3` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `human-360mg-q3wk-ro-probe` starter has **23 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_L` | 0 | 0 (0 h, post) | 113.096 (0.5 h, pre) | 0.0685735 |
| `receptor_occupancy_percent` | 0 | 0 (0 h, post) | 99.8067 (0.5 h, pre) | 23.8456 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**5 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
