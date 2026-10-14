# Liu 2026 reduced AAV-mediated anti-TargetX rat brain QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore reduced AAV-driven antibody expression and brain target dynamics.

**Runnable · 7 experiments.** Version 0.1.0.

## Run an experiment

Reduced Figure 7 reproduction for ICM 1e+12 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp', version='0.1.0')
result = model.run('icm-1e12-aav9')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-parameter-anchor` | Short no-dose run exposing exact paper constants and exact paper-derived values as API outputs. | 0–0.01 h | 2 |
| `icm-1e12-aav9` | Reduced Figure 7 reproduction for ICM 1e+12 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |
| `icm-5e11-aav9` | Reduced Figure 7 reproduction for ICM 5e+11 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |
| `icm-5e12-aav5` | Reduced Figure 7 reproduction for ICM 5e+12 Vg AAV5. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |
| `icm-5e12-aav9` | Reduced Figure 7 reproduction for ICM 5e+12 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |
| `ist-2-5e11-aav9` | Reduced Figure 7 reproduction for IST 2.5e+11 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |
| `iv-5e12-aav9` | Reduced Figure 7 reproduction for IV 5e+12 Vg AAV9. Effective transduced burdens are source-limited calibration quantities, not measured vector copy counts. | 0–1344 h | 57 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `mab_plasma_nM` | Antibody concentration in plasma | `1` |
| `mab_isf_nM` | Antibody concentration in brain interstitial fluid | `1` |
| `target_isf_pct_baseline` | Brain interstitial target as a percentage of baseline | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp --model-version 0.1.0 --scenario icm-1e12-aav9 --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 58 outputs and 18 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `aav5_kd_copy_L` | `1` |
| `aav5_kdeg_h` | `1` |
| `aav5_kint_h` | `1` |
| `aav5_knuc_h` | `1` |
| `aav5_kon_L_copy_h` | `1` |
| `aav5_krec_h` | `1` |
| `aav5_ktrans_h` | `1` |
| `aav9_kd_copy_L` | `1` |
| `aav9_kdeg_h` | `1` |
| `aav9_kint_h` | `1` |
| `aav9_knuc_h` | `1` |
| `aav9_koff_h` | `1` |
| `aav9_kon_L_copy_h` | `1` |
| `aav9_krec_h` | `1` |
| `aav9_ktrans_h` | `1` |
| `complex_csf_nM` | `1` |
| `complex_isf_nM` | `1` |
| `complex_plasma_nM` | `1` |
| `free_target_csf_nM` | `1` |
| `free_target_isf_nM` | `1` |
| `free_target_plasma_nM` | `1` |
| `mab_csf_nM` | `1` |
| `mab_isf_nM` | `1` |
| `mab_kprod_mouse_high_mol_vg_h` | `1` |
| `mab_kprod_mouse_other_mol_vg_h` | `1` |
| `mab_ksec_h` | `1` |
| `mab_plasma_nM` | `1` |
| `protein_clup_L_h_L` | `1` |
| `protein_kdeg_h` | `1` |
| `ps_aav_brain_L_h` | `1` |
| `ps_complex_brain_L_h` | `1` |
| `ps_mab_brain_L_h` | `1` |
| `ps_target_brain_L_h` | `1` |
| `q_csf_L_h` | `1` |
| `q_csf_osc_L_h` | `1` |
| `q_isf_L_h` | `1` |
| `q_perivascular_L_h` | `1` |
| `rat_mouse_kprod_scale` | `1` |
| `rtot_blood_cells_copy_L` | `1` |
| `rtot_meningeal_cells_copy_L` | `1` |
| `target_baseline_csf_nM` | `1` |
| `target_baseline_isf_nM` | `1` |
| `target_baseline_plasma_nM` | `1` |
| `target_csf_pct_baseline` | `1` |
| `target_half_life_h` | `1` |
| `target_isf_pct_baseline` | `1` |
| `target_kd_nM` | `1` |
| `target_kdeg_h` | `1` |
| `target_koff_h` | `1` |
| `target_kon_per_nM_h` | `1` |
| `target_plasma_pct_baseline` | `1` |
| `v_brain_endothelial_L` | `1` |
| `v_cisterna_magna_L` | `1` |
| `v_lateral_ventricle_L` | `1` |
| `v_meningeal_cells_L` | `1` |
| `v_perivascular_total_L` | `1` |
| `v_sas_L` | `1` |
| `v_third_fourth_ventricle_L` | `1` |
| `state__AAV_fast_csf` | `1` |
| `state__AAV_fast_isf` | `1` |
| `state__AAV_fast_plasma` | `1` |
| `state__AAV_nuclear_csf` | `1` |
| `state__AAV_nuclear_isf` | `1` |
| `state__AAV_nuclear_plasma` | `1` |
| `state__complex_csf` | `nM` |
| `state__complex_isf` | `nM` |
| `state__complex_plasma` | `nM` |
| `state__mAb_csf` | `nM` |
| `state__mAb_isf` | `nM` |
| `state__mAb_plasma` | `nM` |
| `state__target_csf` | `nM` |
| `state__target_isf` | `nM` |
| `state__target_plasma` | `nM` |
| `state__transgene_csf` | `1` |
| `state__transgene_isf` | `1` |
| `state__transgene_plasma` | `1` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `icm-1e12-aav9` starter has **57 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `mab_plasma_nM` | 0 | 0 (0 h, post) | 5.94651 (1344 h, pre) | 5.94651 |
| `mab_isf_nM` | 0 | 0 (0 h, post) | 39.7369 (1344 h, pre) | 39.7369 |
| `target_isf_pct_baseline` | 100 | 46.751 (1344 h, pre) | 100 (0 h, post) | 46.751 |

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
Evidence identity: `sha256:34f6bbbb648eac0479252818812a214f190efcad71d83c4859e2912855df039b`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## Related representations

Declared representation: `reduced`. Source family: `liu-2026-aav-mab-targetx-rat-brain`; paper: `10.1007/s10928-026-10051-w`.
Canonical full representation: [qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp](../../../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.1.2/MODEL_CARD.md), version `2.1.2`.
Related representations: [qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp](../../../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.1.2/MODEL_CARD.md) (`full`, `2.1.2`), [qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp](../../../models/qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp/0.1.0/MODEL_CARD.md) (`reduced`, `0.1.0`).
This relationship does not establish physical units, publication reproduction or current-engine qualification.

## What you can explore

Source-limited 18-state reduced QSP reconstruction of Liu et al. 2026. It links effective transient/durable AAV transduction, delayed anti-TargetX mAb expression, and the published TargetX binding and turnover constants in plasma, brain ISF, and CSF. It is not the authors' full 136-equation, 14-tissue PBPK/QSP model.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
