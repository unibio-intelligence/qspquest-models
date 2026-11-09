# Lee 2023 ATC161 AUTOTAC alpha-synuclein source-limited PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect ATC161 degradation endpoints and an exploratory reduced PK/PD model.

**Runnable · 2 experiments.** Version 0.3.0.

## Run an experiment

Source-limited ODE initialized from AUC*kel for the reported 20 mg/kg PO ATC161 AUC and half-life, linked to normalized aggregate degradation through the reported DC50.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_lee_2023_atc161_autotac_alpha_syn_pkpd', version='0.3.0')
result = model.run('po20mgkg-first-order-pk-degradation-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `atc161-pk-pd-anchor-exact-replay` | Reported PK, DC50, dosing, and text endpoint anchors from the article and Supplementary Figure 1. | 0–0.01 h | 2 |
| `po20mgkg-first-order-pk-degradation-probe` | Source-limited ODE initialized from AUC*kel for the reported 20 mg/kg PO ATC161 AUC and half-life, linked to normalized aggregate degradation through the reported DC50. | 0–24 h | 241 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `plasma_atc161_ng_mL` | ATC161 plasma concentration | `1` |
| `aggregate_fraction` | Remaining alpha-synuclein aggregate fraction | `1` |
| `degradation_effect_fraction` | Drug-driven degradation effect | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_lee_2023_atc161_autotac_alpha_syn_pkpd --model-version 0.3.0 --scenario po20mgkg-first-order-pk-degradation-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 42 outputs and 4 states</summary>

| Technical column | Unit |
| --- | --- |
| `aggregate_fraction` | `1` |
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
| `ip_auc_infinity_from_c0_h_ng_mL` | `1` |
| `ip_half_life_replayed_h` | `1` |
| `ip_initial_concentration_ng_mL` | `1` |
| `ip_kel_h` | `1` |
| `pff_injection_mass_ug` | `1` |
| `pff_mouse_post_surgery_wait_max_weeks` | `1` |
| `pff_mouse_post_surgery_wait_min_weeks` | `1` |
| `plasma_atc161_ng_mL` | `1` |
| `po_auc_infinity_from_c0_h_ng_mL` | `1` |
| `po_half_life_replayed_h` | `1` |
| `po_initial_concentration_ng_mL` | `1` |
| `po_kel_h` | `1` |
| `rotarod_improvement_percent` | `1` |
| `summary_marker` | `1` |
| `state__aggregate_fraction` | `fraction of baseline` |
| `state__auc_atc161_h_ng_mL` | `h*ng/mL` |
| `state__plasma_atc161_ng_mL` | `ng/mL` |
| `state__summary_marker` | `dimensionless` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `po20mgkg-first-order-pk-degradation-probe` starter has **241 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `plasma_atc161_ng_mL` | 618.081 | 6.89322 (24 h, pre) | 618.081 (0 h, post) | 6.89322 |
| `aggregate_fraction` | 1 | 0.619692 (24 h, pre) | 1 (0 h, post) | 0.619692 |
| `degradation_effect_fraction` | 0.908264 | 0.0994396 (24 h, pre) | 0.908264 (0 h, post) | 0.0994396 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
