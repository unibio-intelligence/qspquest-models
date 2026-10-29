# Caimi 2024 loncastuximab CD19 QSP dynamic reconstruction

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore reduced loncastuximab trafficking and tumor response; some experiments are unavailable.

**Source replay available; dynamic simulation unavailable · 4 unavailable.** Version 0.1.0.

## Run an experiment

Exact replay of public Caimi main-text counts, regimen values, threshold statements, and SI Table 3 QSP parameters.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_caimi_2024_loncastuximab_cd19_qsp', version='0.1.0')
result = model.run('caimi-2024-exact-article-si-anchors')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `caimi-2024-exact-article-si-anchors` | Exact replay of public Caimi main-text counts, regimen values, threshold statements, and SI Table 3 QSP parameters. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `tumor_total_cells` | Total tumor cells in the retained source replay | `1` |
| `tumor_volume_l` | Tumor volume in the retained source replay | `1` |

**This starter is a source replay.** Its retained values are constant or short source checks.
No qualified dynamic simulation is available in this version. Zero drug states do not demonstrate a treatment response.

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_caimi_2024_loncastuximab_cd19_qsp --model-version 0.1.0 --scenario caimi-2024-exact-article-si-anchors --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 74 outputs and 22 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `ACSINS_score` | `1` |
| `CD21Factor` | `1` |
| `DAR` | `1` |
| `FcRn_Conc_high_uM` | `1` |
| `FcRn_Conc_low_uM` | `1` |
| `K_D_uM` | `1` |
| `PBD_IC50_low_uM` | `1` |
| `PBD_IC50_pos_uM` | `1` |
| `R0_max` | `1` |
| `R0_min` | `1` |
| `Rn0_max` | `1` |
| `Rn0_min` | `1` |
| `body_weight_kg` | `1` |
| `cd19_exp_tum` | `1` |
| `cd19_low_density_per_cell` | `1` |
| `cd19_surface_density_per_cell` | `1` |
| `cell_radius_um` | `1` |
| `central_uM` | `1` |
| `cl_l_day` | `1` |
| `initial_total_tumor_cells` | `1` |
| `k_death_day` | `1` |
| `k_death_h` | `1` |
| `k_deg_day` | `1` |
| `k_deg_h` | `1` |
| `k_e_day` | `1` |
| `k_e_h` | `1` |
| `k_el_payload_day` | `1` |
| `k_el_payload_h` | `1` |
| `k_in_day` | `1` |
| `k_in_h` | `1` |
| `k_off21_day` | `1` |
| `k_off21_h` | `1` |
| `k_off_day` | `1` |
| `k_on21_day` | `1` |
| `k_on21_per_cell_h` | `1` |
| `k_on_day` | `1` |
| `k_on_per_uM_h` | `1` |
| `k_out_day` | `1` |
| `k_out_h` | `1` |
| `k_trans_day` | `1` |
| `k_trans_h` | `1` |
| `kill_low_day` | `1` |
| `kill_pos_day` | `1` |
| `low_hscore_response_n` | `1` |
| `low_hscore_response_pct` | `1` |
| `low_hscore_total_n` | `1` |
| `molecular_weight_mg_per_nmol` | `1` |
| `mu_fast_h` | `1` |
| `mu_h` | `1` |
| `mu_low_day` | `1` |
| `mu_low_h` | `1` |
| `mu_pos_day` | `1` |
| `nmol_per_mg` | `1` |
| `payload_release_uM_day` | `1` |
| `q_l_day` | `1` |
| `reported_oci_ly3_cd19_copy_number` | `1` |
| `reported_oci_ly3_cd19_positive_pct` | `1` |
| `reported_response_threshold_cd19` | `1` |
| `reported_virtual_patients` | `1` |
| `response_auc_ratio` | `1` |
| `response_flag` | `1` |
| `response_score` | `1` |
| `tumor_adc_uM` | `1` |
| `tumor_cell_volume_l` | `1` |
| `tumor_cellularity` | `1` |
| `tumor_partition_fraction` | `1` |
| `tumor_total_cells` | `1` |
| `tumor_volume_l` | `1` |
| `validation_run_nonce` | `1` |
| `vc_l` | `1` |
| `very_low_hscore_response_n` | `1` |
| `very_low_hscore_response_pct` | `1` |
| `very_low_hscore_total_n` | `1` |
| `vp_l` | `1` |
| `state__CRR21_low` | `#/cell` |
| `state__CRR21_pos` | `#/cell` |
| `state__C_low` | `#/cell` |
| `state__C_pos` | `#/cell` |
| `state__De_low` | `#/cell` |
| `state__De_pos` | `#/cell` |
| `state__Dm_uM` | `uM` |
| `state__I_low` | `#/cell` |
| `state__I_pos` | `#/cell` |
| `state__N_low` | `cells` |
| `state__N_pos` | `cells` |
| `state__Nd_low` | `cells` |
| `state__Nd_pos` | `cells` |
| `state__R21_low` | `#/cell` |
| `state__R21_pos` | `#/cell` |
| `state__R_low` | `#/cell` |
| `state__R_pos` | `#/cell` |
| `state__central_nmol` | `nmol` |
| `state__elapsed_day` | `day` |
| `state__peripheral_nmol` | `nmol` |
| `state__stable_auc_cells_day` | `cells*day` |
| `state__tumor_auc_cells_day` | `cells*day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `caimi-2024-exact-article-si-anchors` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `tumor_total_cells` | 1e+09 | 1e+09 (0 h, post) | 1.16883e+09 (1 h, pre) | 1.16883e+09 |
| `tumor_volume_l` | 0.00266667 | 0.00266667 (0 h, post) | 0.00311687 (1 h, pre) | 0.00311687 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**4 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
