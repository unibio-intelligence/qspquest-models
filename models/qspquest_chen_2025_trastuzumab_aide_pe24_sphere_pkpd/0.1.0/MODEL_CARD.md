# Chen 2025 trastuzumab-PE24 AIDE sphere PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore a trastuzumab-PE24 distribution model; some experiments are unavailable.

**Source replay available; dynamic simulation unavailable · 4 unavailable.** Version 0.1.0.

## Run an experiment

Exact replay of source identity, recovered supplement, parameter, and paper endpoint values.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_chen_2025_trastuzumab_aide_pe24_sphere_pkpd', version='0.1.0')
result = model.run('exact-source-anchor')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-anchor` | Exact replay of source identity, recovered supplement, parameter, and paper endpoint values. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `total_tumor_mm3` | Total tumor volume in the retained source replay | `1` |

**This starter is a source replay.** Its retained values are constant or short source checks.
No qualified dynamic simulation is available in this version. Zero drug states do not demonstrate a treatment response.

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_chen_2025_trastuzumab_aide_pe24_sphere_pkpd --model-version 0.1.0 --scenario exact-source-anchor --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 41 outputs and 92 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `Ag0` | `1` |
| `Ag0_receptors_per_cell` | `1` |
| `CL1` | `1` |
| `Cld` | `1` |
| `TN50` | `1` |
| `V1` | `1` |
| `V2` | `1` |
| `article_figures_n` | `1` |
| `central_aide_nM` | `1` |
| `central_pe24_nM` | `1` |
| `citation_rank` | `1` |
| `dose_0p15_mgkg_nM` | `1` |
| `dose_0p35_mgkg_nM` | `1` |
| `elapsed_day` | `1` |
| `kdeg` | `1` |
| `kint` | `1` |
| `kkill` | `1` |
| `koffA` | `1` |
| `konA` | `1` |
| `lg1_survival_p_value` | `1` |
| `observed_auc_infinity_difference_pct` | `1` |
| `observed_terminal_slope_reduction_pct` | `1` |
| `onehe_survival_p_value` | `1` |
| `optimal_koff_high_h` | `1` |
| `optimal_koff_low_h` | `1` |
| `pe24_1he_median_survival_day` | `1` |
| `pe24_alone_median_survival_day` | `1` |
| `pe24_koff_scan_dose_mg_kg` | `1` |
| `pe24_lg1_median_survival_day` | `1` |
| `pe24_single_dose_mg_kg` | `1` |
| `pe_cell_death_threshold_molecules` | `1` |
| `pmcid_numeric` | `1` |
| `pmid_numeric` | `1` |
| `predicted_tumor_auc_0_240_reduction_pct` | `1` |
| `publication_year` | `1` |
| `queue_cited_by_count` | `1` |
| `real_dependency_supplements_n` | `1` |
| `region_E_internalized_molecules_per_cell` | `1` |
| `region_E_occupancy_pct` | `1` |
| `total_tumor_mm3` | `1` |
| `whole_tumor_bound_nM` | `1` |
| `state__A1` | `mm3` |
| `state__A2` | `mm3` |
| `state__A3` | `mm3` |
| `state__A4` | `mm3` |
| `state__B1` | `mm3` |
| `state__B2` | `mm3` |
| `state__B3` | `mm3` |
| `state__B4` | `mm3` |
| `state__C1` | `mm3` |
| `state__C2` | `mm3` |
| `state__C3` | `mm3` |
| `state__C4` | `mm3` |
| `state__CP1` | `nM` |
| `state__CP2` | `nM` |
| `state__CP3` | `nM` |
| `state__CP4` | `nM` |
| `state__CP5` | `nM` |
| `state__CT1` | `nM` |
| `state__CT2` | `nM` |
| `state__CT3` | `nM` |
| `state__CT4` | `nM` |
| `state__CT5` | `nM` |
| `state__CTA1` | `nM` |
| `state__CTA10` | `nM` |
| `state__CTA11` | `nM` |
| `state__CTA12` | `nM` |
| `state__CTA2` | `nM` |
| `state__CTA3` | `nM` |
| `state__CTA4` | `nM` |
| `state__CTA5` | `nM` |
| `state__CTA6` | `nM` |
| `state__CTA7` | `nM` |
| `state__CTA8` | `nM` |
| `state__CTA9` | `nM` |
| `state__CTB1` | `nM` |
| `state__CTB10` | `nM` |
| `state__CTB11` | `nM` |
| `state__CTB12` | `nM` |
| `state__CTB2` | `nM` |
| `state__CTB3` | `nM` |
| `state__CTB4` | `nM` |
| `state__CTB5` | `nM` |
| `state__CTB6` | `nM` |
| `state__CTB7` | `nM` |
| `state__CTB8` | `nM` |
| `state__CTB9` | `nM` |
| `state__CTC1` | `nM` |
| `state__CTC10` | `nM` |
| `state__CTC11` | `nM` |
| `state__CTC12` | `nM` |
| `state__CTC2` | `nM` |
| `state__CTC3` | `nM` |
| `state__CTC4` | `nM` |
| `state__CTC5` | `nM` |
| `state__CTC6` | `nM` |
| `state__CTC7` | `nM` |
| `state__CTC8` | `nM` |
| `state__CTC9` | `nM` |
| `state__CTD1` | `nM` |
| `state__CTD10` | `nM` |
| `state__CTD11` | `nM` |
| `state__CTD12` | `nM` |
| `state__CTD2` | `nM` |
| `state__CTD3` | `nM` |
| `state__CTD4` | `nM` |
| `state__CTD5` | `nM` |
| `state__CTD6` | `nM` |
| `state__CTD7` | `nM` |
| `state__CTD8` | `nM` |
| `state__CTD9` | `nM` |
| `state__CTE1` | `nM` |
| `state__CTE10` | `nM` |
| `state__CTE11` | `nM` |
| `state__CTE12` | `nM` |
| `state__CTE2` | `nM` |
| `state__CTE3` | `nM` |
| `state__CTE4` | `nM` |
| `state__CTE5` | `nM` |
| `state__CTE6` | `nM` |
| `state__CTE7` | `nM` |
| `state__CTE8` | `nM` |
| `state__CTE9` | `nM` |
| `state__D1` | `mm3` |
| `state__D2` | `mm3` |
| `state__D3` | `mm3` |
| `state__D4` | `mm3` |
| `state__E1` | `mm3` |
| `state__E2` | `mm3` |
| `state__E3` | `mm3` |
| `state__E4` | `mm3` |
| `state__elapsed_h` | `h` |
| `state__source_anchor` | `unitless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `exact-source-anchor` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `total_tumor_mm3` | 100 | 100 (0 h, post) | 102.942 (1 h, pre) | 102.942 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**4 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

<details>
<summary>Availability and qualification</summary>

Execution: `source_replay`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:9021509dd68e75a9c890d4b4cb977b82501f037c9bc78fd8e237d8d5e8baaa86`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Public-source ODE reconstruction of the Chen 2025 trastuzumab-PE24 anti-idiotypic distribution-enhancer model, using the recovered 2022 sphere PK/PD equations and 2025 PE24 endpoints.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
