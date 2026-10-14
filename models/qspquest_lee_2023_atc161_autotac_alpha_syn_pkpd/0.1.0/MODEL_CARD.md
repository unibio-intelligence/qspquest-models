# Lee 2023 ATC161 AUTOTAC alpha-synuclein source-limited PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect ATC161 degradation endpoints and an exploratory reduced PK/PD model.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Source-limited ODE initialized from AUC*kel for the reported 20 mg/kg PO ATC161 AUC and half-life, linked to normalized aggregate degradation through the reported DC50.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_lee_2023_atc161_autotac_alpha_syn_pkpd', version='0.1.0')
result = model.run('po20mgkg-first-order-pk-degradation-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `atc161-pk-pd-anchor-exact-replay` | Reported PK, DC50, dosing, and text endpoint anchors from the article and Supplementary Figure 1. | 0–0.01 h | 2 |
| `po20mgkg-first-order-pk-degradation-probe` | Source-limited ODE initialized from AUC*kel for the reported 20 mg/kg PO ATC161 AUC and half-life, linked to normalized aggregate degradation through the reported DC50. | 0–24 h | 241 |
| `source-availability-exact-replay` | Queue, bibliographic, and source-route scalar checks for Lee 2023. | 0–0.01 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `plasma_atc161_ng_mL` | ATC161 plasma concentration | `1` |
| `aggregate_fraction` | Remaining alpha-synuclein aggregate fraction | `1` |
| `degradation_effect_fraction` | Drug-driven degradation effect | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_lee_2023_atc161_autotac_alpha_syn_pkpd --model-version 0.1.0 --scenario po20mgkg-first-order-pk-degradation-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 56 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `aggregate_fraction` | `1` |
| `article_pdf_binary_fetched_flag` | `1` |
| `atc161_aggregate_degradation_low_nM_primary_neuron` | `1` |
| `atc161_cell_assay_concentration_nM` | `1` |
| `atc161_cell_assay_duration_h` | `1` |
| `atc161_concentration_nM` | `1` |
| `atc161_dc50_nM` | `1` |
| `atc161_dc50_ng_mL` | `1` |
| `atc161_ip_20mgkg_auc_last_h_ng_mL` | `1` |
| `atc161_ip_20mgkg_half_life_h` | `1` |
| `atc161_lamp1_lysosome_fold_increase` | `1` |
| `atc161_long_mouse_duration_weeks` | `1` |
| `atc161_mw_mh_plus_mz` | `1` |
| `atc161_neutral_mw_g_mol_source_limited` | `1` |
| `atc161_p62_oligomerization_low_nM` | `1` |
| `atc161_pff_mouse_doses_per_week` | `1` |
| `atc161_pff_mouse_oral_dose_mg_kg` | `1` |
| `atc161_po_20mgkg_auc_last_h_ng_mL` | `1` |
| `atc161_po_20mgkg_half_life_h` | `1` |
| `atc161_reduced_alpha_syn_puncta_percent` | `1` |
| `atc161_reduced_extracellular_alpha_syn_percent` | `1` |
| `atc161_short_mouse_duration_weeks` | `1` |
| `atl21_oral_auc_last_h_ng_mL` | `1` |
| `atl7_brain_auc_last_h_ng_g` | `1` |
| `atl7_brain_plasma_auc_ratio_from_values` | `1` |
| `atl7_plasma_auc_last_h_ng_mL` | `1` |
| `atl7_reported_brain_plasma_ratio_approx` | `1` |
| `auc_atc161_h_ng_mL` | `1` |
| `degradation_effect_fraction` | `1` |
| `europepmc_fulltext_xml_fetched_flag` | `1` |
| `extracted_table_count` | `1` |
| `ip_auc_infinity_from_c0_h_ng_mL` | `1` |
| `ip_half_life_replayed_h` | `1` |
| `ip_initial_concentration_ng_mL` | `1` |
| `ip_kel_h` | `1` |
| `pff_injection_mass_ug` | `1` |
| `pff_mouse_post_surgery_wait_max_weeks` | `1` |
| `pff_mouse_post_surgery_wait_min_weeks` | `1` |
| `plasma_atc161_ng_mL` | `1` |
| `pmcid_numeric` | `1` |
| `pmid_numeric` | `1` |
| `po_auc_infinity_from_c0_h_ng_mL` | `1` |
| `po_half_life_replayed_h` | `1` |
| `po_initial_concentration_ng_mL` | `1` |
| `po_kel_h` | `1` |
| `preprint_hit_count` | `1` |
| `publication_year` | `1` |
| `queue_citation_rank` | `1` |
| `queue_cited_by_count` | `1` |
| `queue_refined_rank` | `1` |
| `rotarod_improvement_percent` | `1` |
| `summary_marker` | `1` |
| `supplement_docx_fetched_count` | `1` |
| `supplement_eps_fetched_count` | `1` |
| `supplement_expected_count` | `1` |
| `validation_run_nonce` | `1` |
| `state__aggregate_fraction` | `fraction of baseline` |
| `state__auc_atc161_h_ng_mL` | `h*ng/mL` |
| `state__plasma_atc161_ng_mL` | `ng/mL` |
| `state__summary_marker` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `po20mgkg-first-order-pk-degradation-probe` starter has **241 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `plasma_atc161_ng_mL` | 618.081 | 6.89322 (24 h, pre) | 618.081 (0 h, post) | 6.89322 |
| `aggregate_fraction` | 1 | 0.619693 (24 h, pre) | 1 (0 h, post) | 0.619693 |
| `degradation_effect_fraction` | 0.908264 | 0.0994396 (24 h, pre) | 0.908264 (0 h, post) | 0.0994396 |

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
Evidence identity: `sha256:ba1a9d1b0c2af7125f9540e72e7cc9d1362d3a82cda4f9222bf3f50c20072b69`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Source-limited ODE and exact-anchor replay for ATC161, an AUTOTAC alpha-synuclein aggregate degrader. The runtime preserves reported Supplementary Figure 1 PK AUC/half-life anchors, article text DC50 and mouse dosing endpoints, and a normalized first-order PK to aggregate-degradation ODE probe. It is not a published PopPK or fitted QSP reconstruction.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
