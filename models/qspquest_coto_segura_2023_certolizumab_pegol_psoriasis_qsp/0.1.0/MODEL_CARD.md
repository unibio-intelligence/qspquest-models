# Coto-Segura 2023 certolizumab pegol psoriasis QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore certolizumab exposure and psoriasis-response mechanisms.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Approved EU-style loading regimen: 400 mg at weeks 0, 2, 4 then 200 mg Q2W, simulated with the public PBPK ODE.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_coto_segura_2023_certolizumab_pegol_psoriasis_qsp', version='0.1.0')
result = model.run('label-loading-200mg-q2w-pbpk-endpoint-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-anchor` | No-dose exact replay of article and supplement source values. | 0–0.001 h | 2 |
| `label-loading-200mg-q2w-pbpk-endpoint-overlay` | Approved EU-style loading regimen: 400 mg at weeks 0, 2, 4 then 200 mg Q2W, simulated with the public PBPK ODE. | 0–112 h | 225 |
| `single-400mg-pbpk-ode-endpoint-overlay` | Standard-patient SC two-compartment PBPK ODE matched to Supplementary Table F 400 mg Cmax/Tmax endpoints. | 0–14.125 h | 73 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `blood_concentration_mg_l` | Certolizumab concentration in blood | `1` |
| `auc_mg_day_l` | Accumulated drug exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_coto_segura_2023_certolizumab_pegol_psoriasis_qsp --model-version 0.1.0 --scenario label-loading-200mg-q2w-pbpk-endpoint-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 63 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `auc_mg_day_l` | `1` |
| `blood_concentration_mg_l` | `1` |
| `blood_concentration_ug_ml` | `1` |
| `derived_half_life_h` | `1` |
| `derived_ka_from_literature_tmax_1_day` | `1` |
| `derived_kel_from_literature_half_life_1_day` | `1` |
| `derived_single_200_cmax_mg_l` | `1` |
| `derived_single_400_cmax_mg_l` | `1` |
| `derived_tmax_h` | `1` |
| `elapsed_day` | `1` |
| `source__age_mean_year` | `1` |
| `source__age_sd_year` | `1` |
| `source__bmi_mean_kg_m2` | `1` |
| `source__bmi_sd_kg_m2` | `1` |
| `source__certolizumab_bioavailability_pct` | `1` |
| `source__certolizumab_half_life_h` | `1` |
| `source__certolizumab_pasi75_high_pct` | `1` |
| `source__certolizumab_pasi75_low_pct` | `1` |
| `source__certolizumab_tmax_h` | `1` |
| `source__certolizumab_tpms_accuracy` | `1` |
| `source__characterized_drugs` | `1` |
| `source__clinical_condition_key_proteins` | `1` |
| `source__clinical_conditions` | `1` |
| `source__cluster12_distance` | `1` |
| `source__cluster13_distance` | `1` |
| `source__cluster1_differential_rows` | `1` |
| `source__cluster1_enrichment_rows` | `1` |
| `source__cluster23_distance` | `1` |
| `source__cluster2_differential_rows` | `1` |
| `source__cluster2_enrichment_rows` | `1` |
| `source__cluster3_differential_rows` | `1` |
| `source__cluster3_enrichment_rows` | `1` |
| `source__comorbidity_any_pct` | `1` |
| `source__considered_interactions` | `1` |
| `source__considered_proteins` | `1` |
| `source__curated_drug_indication_positive` | `1` |
| `source__curated_drug_indication_restrictions` | `1` |
| `source__disease_protein_rows` | `1` |
| `source__disease_unique_genes` | `1` |
| `source__drug_adr_positive` | `1` |
| `source__drug_adr_restrictions` | `1` |
| `source__drug_indication_adr_protein_correlations` | `1` |
| `source__drug_targets` | `1` |
| `source__female_pct` | `1` |
| `source__height_mean_cm` | `1` |
| `source__height_sd_cm` | `1` |
| `source__literature_cmax_mg_l` | `1` |
| `source__literature_cmaxss_mg_l` | `1` |
| `source__literature_half_life_h` | `1` |
| `source__literature_tmax_h` | `1` |
| `source__pasi75_optimized_rows` | `1` |
| `source__pasi75_optimized_unique_genes` | `1` |
| `source__pbpk_cmax_mg_l` | `1` |
| `source__pbpk_cmaxss_mg_l` | `1` |
| `source__pbpk_half_life_h` | `1` |
| `source__pbpk_r2_min` | `1` |
| `source__pbpk_tmax_h` | `1` |
| `source__reference_population_n` | `1` |
| `source__tpms_accuracy_pct` | `1` |
| `source__tsignal_pasi75_r` | `1` |
| `source__virtual_population_n` | `1` |
| `source__weight_mean_kg` | `1` |
| `source__weight_sd_kg` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__blood_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `label-loading-200mg-q2w-pbpk-endpoint-overlay` starter has **225 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `blood_concentration_mg_l` | 0 | 0 (0 h, post) | 103.386 (32 h, post) | 13.8442 |
| `auc_mg_day_l` | 0 | 0 (0 h, post) | 6307.92 (112 h, pre) | 6307.92 |

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
Evidence identity: `sha256:8d5dfb56a0cd16ae31fa470b016bd885d1b7abb3b13a3659fb0e1d7a7a3d5885`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Public-source reconstruction of the certolizumab pegol two-compartment SC PBPK ODE from Coto-Segura et al. 2023, with exact replay anchors for the published QSP/TPMS source tables. The proprietary TPMS interaction network and patient-level SimBiology project are not public.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
