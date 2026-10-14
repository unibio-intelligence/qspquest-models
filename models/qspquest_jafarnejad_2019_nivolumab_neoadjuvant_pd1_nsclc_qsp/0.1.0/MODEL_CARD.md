# Jafarnejad 2019 Neoadjuvant Nivolumab NSCLC QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore nivolumab and immune mechanisms in neoadjuvant lung-cancer scenarios.

**Runnable · 2 experiments.** Version 0.1.0.

## Run an experiment

Reduced ODE probe for two 3 mg/kg nivolumab doses before day-40 surgery. Paper overlays expose the published clinical/model endpoint markers; figure-level trajectory validation remains pending digitized Fig. 6-7 patient data.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_jafarnejad_2019_nivolumab_neoadjuvant_pd1_nsclc_qsp', version='0.1.0')
result = model.run('neoadjuvant-two-dose-resection-endpoint')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-inventory-and-trial-design` | Exact replay of model inventory, supplement table values, dosing, and reported clinical/model endpoints. | 0–1 d | 2 |
| `neoadjuvant-two-dose-resection-endpoint` | Reduced ODE probe for two 3 mg/kg nivolumab doses before day-40 surgery. Paper overlays expose the published clinical/model endpoint markers; figure-level trajectory validation remains pending digitized Fig. 6-7 patient data. | 0–40 d | 41 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `pd1_blockade_fraction` | Fraction of PD-1 blocked | `1` |
| `tumor_regression_percent_calc` | Calculated percentage tumor regression | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_jafarnejad_2019_nivolumab_neoadjuvant_pd1_nsclc_qsp --model-version 0.1.0 --scenario neoadjuvant-two-dose-resection-endpoint --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 43 outputs and 8 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `checkpoint_inhibition_fraction` | `1` |
| `paper_clinical_major_pathological_response_pct` | `1` |
| `paper_figure7_wilcoxon_p_value` | `1` |
| `pd1_blockade_fraction` | `1` |
| `runtime_mg_per_kg_per_interval` | `1` |
| `source_checkpoint_half_inhibition_molecule` | `1` |
| `source_checkpoint_hill` | `1` |
| `source_compartment_count` | `1` |
| `source_event_assignment_rows` | `1` |
| `source_fig4_random_traces_shown` | `1` |
| `source_k_c_capacity_cells` | `1` |
| `source_k_c_death_by_t_day` | `1` |
| `source_k_c_death_day` | `1` |
| `source_k_c_growth_day` | `1` |
| `source_main_text_algebraic_equation_count` | `1` |
| `source_main_text_ode_count` | `1` |
| `source_nivolumab_dose_mg_per_kg` | `1` |
| `source_nivolumab_infusion_hour` | `1` |
| `source_nivolumab_interval_day` | `1` |
| `source_nivolumab_kd_nm` | `1` |
| `source_nivolumab_planned_doses` | `1` |
| `source_parameter_count` | `1` |
| `source_pat_weight_kg` | `1` |
| `source_patient_count` | `1` |
| `source_patient_simulations_per_patient` | `1` |
| `source_pd1_pdl_complex_initial` | `1` |
| `source_psa_parameter_count` | `1` |
| `source_psa_simulation_count` | `1` |
| `source_reaction_count` | `1` |
| `source_resection_cancer_cells` | `1` |
| `source_resection_teff_cells` | `1` |
| `source_resection_time_day` | `1` |
| `source_resection_treg_cells` | `1` |
| `source_rule_count` | `1` |
| `source_species_count` | `1` |
| `source_tumor_initial_cells` | `1` |
| `source_tumor_initial_teff_cells` | `1` |
| `source_tumor_initial_treg_cells` | `1` |
| `source_tumor_initial_volume_l` | `1` |
| `source_tumor_max_volume_l` | `1` |
| `teff_killing_fraction` | `1` |
| `tumor_diameter_percent_calc` | `1` |
| `tumor_regression_percent_calc` | `1` |
| `state__checkpoint_complex_molecule` | `molecule` |
| `state__nivolumab_central_mg` | `mg` |
| `state__summary_marker` | `dimensionless` |
| `state__teff_cells` | `cell` |
| `state__treg_cells` | `cell` |
| `state__tumor_cells` | `cell` |
| `state__tumor_diameter_percent` | `percent` |
| `state__tumor_regression_percent` | `percent` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `neoadjuvant-two-dose-resection-endpoint` starter has **41 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `pd1_blockade_fraction` | 0.666667 | 0.666667 (0 d, post) | 0.802524 (15 d, post) | 0.728087 |
| `tumor_regression_percent_calc` | 0 | -11.9483 (40 d, pre) | 0 (0 d, post) | -11.9483 |

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
Evidence identity: `sha256:3e24080a2605234ad10a60971f2fa88d32bcebf1bcc480b762275e9724944e09`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Reduced, source-auditable runtime for Jafarnejad et al. 2019 neoadjuvant anti-PD-1 QSP in resectable NSCLC. The source supplement provides the full SBML model inventory with 55 species, 172 parameters, 92 reactions, 53 rules, and 10 event assignment rows. This platform model preserves exact source anchors and a compact nivolumab/checkpoint/tumor-response ODE; it is not a full import of every SBML reaction or event.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
