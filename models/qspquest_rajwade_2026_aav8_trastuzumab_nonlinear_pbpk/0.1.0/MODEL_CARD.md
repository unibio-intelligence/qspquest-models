# Whole-body AAV8 gene-delivery and transgene-antibody PBPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore mouse AAV8 delivery, trastuzumab expression and whole-body antibody distribution.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_rajwade_2026_aav8_trastuzumab_nonlinear_pbpk', version='0.1.0')
result = model.run('figure3_5_iv_aav8_1e11_vg_mouse')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `figure3_5_iv_aav8_1e11_vg_mouse` | Figure3 5 iv aav8 1e11 vg mouse | 0–504 h | 87 |
| `figure3_5_iv_aav8_2e10_vg_mouse` | Figure3 5 iv aav8 2e10 vg mouse | 0–504 h | 87 |
| `figure3_5_iv_aav8_2e11_vg_mouse` | Figure3 5 iv aav8 2e11 vg mouse | 0–504 h | 87 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `aav_blood_vg_per_uL` | Vector genomes in blood | `1` |
| `mab_plasma_ug_mL` | Expressed antibody concentration in plasma | `1` |
| `mab_brain_interstitial_nM` | Antibody concentration in brain interstitial fluid | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_rajwade_2026_aav8_trastuzumab_nonlinear_pbpk --model-version 0.1.0 --scenario figure3_5_iv_aav8_1e11_vg_mouse --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 6 outputs and 545 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `aav_blood_vg_per_uL` | `1` |
| `liver_vector_genomes_per_ng_dna` | `1` |
| `mab_brain_interstitial_nM` | `1` |
| `mab_immune_loss_h` | `1` |
| `mab_plasma_nM` | `1` |
| `mab_plasma_ug_mL` | `1` |
| `state__aav_adipose_e_aav` | `1/L` |
| `state__aav_adipose_e_cmal_r` | `1/L` |
| `state__aav_adipose_e_cmal_rc` | `1/L` |
| `state__aav_adipose_e_cml_r` | `1/L` |
| `state__aav_adipose_e_cml_rc` | `1/L` |
| `state__aav_adipose_e_n` | `1/L` |
| `state__aav_adipose_e_r` | `1/L` |
| `state__aav_adipose_e_rc` | `1/L` |
| `state__aav_adipose_i` | `1/L` |
| `state__aav_adipose_p_aav` | `1/L` |
| `state__aav_adipose_p_cm_r` | `1/L` |
| `state__aav_adipose_p_cm_rc` | `1/L` |
| `state__aav_adipose_p_n` | `1/L` |
| `state__aav_adipose_p_r` | `1/L` |
| `state__aav_adipose_p_rc` | `1/L` |
| `state__aav_adipose_v` | `1/L` |
| `state__aav_bc_adipose_aav` | `1/L` |
| `state__aav_bc_adipose_cm_r` | `1/L` |
| `state__aav_bc_adipose_cm_rc` | `1/L` |
| `state__aav_bc_adipose_n` | `1/L` |
| `state__aav_bc_adipose_r` | `1/L` |
| `state__aav_bc_adipose_rc` | `1/L` |
| `state__aav_bc_bone_aav` | `1/L` |
| `state__aav_bc_bone_cm_r` | `1/L` |
| `state__aav_bc_bone_cm_rc` | `1/L` |
| `state__aav_bc_bone_n` | `1/L` |
| `state__aav_bc_bone_r` | `1/L` |
| `state__aav_bc_bone_rc` | `1/L` |
| `state__aav_bc_brain_aav` | `1/L` |
| `state__aav_bc_brain_cm_r` | `1/L` |
| `state__aav_bc_brain_cm_rc` | `1/L` |
| `state__aav_bc_brain_n` | `1/L` |
| `state__aav_bc_brain_r` | `1/L` |
| `state__aav_bc_brain_rc` | `1/L` |
| `state__aav_bc_central_aav` | `1/L` |
| `state__aav_bc_central_cm_r` | `1/L` |
| `state__aav_bc_central_cm_rc` | `1/L` |
| `state__aav_bc_central_n` | `1/L` |
| `state__aav_bc_central_r` | `1/L` |
| `state__aav_bc_central_rc` | `1/L` |
| `state__aav_bc_heart_aav` | `1/L` |
| `state__aav_bc_heart_cm_r` | `1/L` |
| `state__aav_bc_heart_cm_rc` | `1/L` |
| `state__aav_bc_heart_n` | `1/L` |
| `state__aav_bc_heart_r` | `1/L` |
| `state__aav_bc_heart_rc` | `1/L` |
| `state__aav_bc_kidney_aav` | `1/L` |
| `state__aav_bc_kidney_cm_r` | `1/L` |
| `state__aav_bc_kidney_cm_rc` | `1/L` |
| `state__aav_bc_kidney_n` | `1/L` |
| `state__aav_bc_kidney_r` | `1/L` |
| `state__aav_bc_kidney_rc` | `1/L` |
| `state__aav_bc_large_intestine_aav` | `1/L` |
| `state__aav_bc_large_intestine_cm_r` | `1/L` |
| `state__aav_bc_large_intestine_cm_rc` | `1/L` |
| `state__aav_bc_large_intestine_n` | `1/L` |
| `state__aav_bc_large_intestine_r` | `1/L` |
| `state__aav_bc_large_intestine_rc` | `1/L` |
| `state__aav_bc_liver_aav` | `1/L` |
| `state__aav_bc_liver_cm_r` | `1/L` |
| `state__aav_bc_liver_cm_rc` | `1/L` |
| `state__aav_bc_liver_n` | `1/L` |
| `state__aav_bc_liver_r` | `1/L` |
| `state__aav_bc_liver_rc` | `1/L` |
| `state__aav_bc_lung_aav` | `1/L` |
| `state__aav_bc_lung_cm_r` | `1/L` |
| `state__aav_bc_lung_cm_rc` | `1/L` |
| `state__aav_bc_lung_n` | `1/L` |
| `state__aav_bc_lung_r` | `1/L` |
| `state__aav_bc_lung_rc` | `1/L` |
| `state__aav_bc_muscle_aav` | `1/L` |
| `state__aav_bc_muscle_cm_r` | `1/L` |
| `state__aav_bc_muscle_cm_rc` | `1/L` |
| `state__aav_bc_muscle_n` | `1/L` |
| `state__aav_bc_muscle_r` | `1/L` |
| `state__aav_bc_muscle_rc` | `1/L` |
| `state__aav_bc_other_aav` | `1/L` |
| `state__aav_bc_other_cm_r` | `1/L` |
| `state__aav_bc_other_cm_rc` | `1/L` |
| `state__aav_bc_other_n` | `1/L` |
| `state__aav_bc_other_r` | `1/L` |
| `state__aav_bc_other_rc` | `1/L` |
| `state__aav_bc_pancreas_aav` | `1/L` |
| `state__aav_bc_pancreas_cm_r` | `1/L` |
| `state__aav_bc_pancreas_cm_rc` | `1/L` |
| `state__aav_bc_pancreas_n` | `1/L` |
| `state__aav_bc_pancreas_r` | `1/L` |
| `state__aav_bc_pancreas_rc` | `1/L` |
| `state__aav_bc_skin_aav` | `1/L` |
| `state__aav_bc_skin_cm_r` | `1/L` |
| `state__aav_bc_skin_cm_rc` | `1/L` |
| `state__aav_bc_skin_n` | `1/L` |
| `state__aav_bc_skin_r` | `1/L` |
| `state__aav_bc_skin_rc` | `1/L` |
| `state__aav_bc_small_intestine_aav` | `1/L` |
| `state__aav_bc_small_intestine_cm_r` | `1/L` |
| `state__aav_bc_small_intestine_cm_rc` | `1/L` |
| `state__aav_bc_small_intestine_n` | `1/L` |
| `state__aav_bc_small_intestine_r` | `1/L` |
| `state__aav_bc_small_intestine_rc` | `1/L` |
| `state__aav_bc_spleen_aav` | `1/L` |
| `state__aav_bc_spleen_cm_r` | `1/L` |
| `state__aav_bc_spleen_cm_rc` | `1/L` |
| `state__aav_bc_spleen_n` | `1/L` |
| `state__aav_bc_spleen_r` | `1/L` |
| `state__aav_bc_spleen_rc` | `1/L` |
| `state__aav_bc_thymus_aav` | `1/L` |
| `state__aav_bc_thymus_cm_r` | `1/L` |
| `state__aav_bc_thymus_cm_rc` | `1/L` |
| `state__aav_bc_thymus_n` | `1/L` |
| `state__aav_bc_thymus_r` | `1/L` |
| `state__aav_bc_thymus_rc` | `1/L` |
| `state__aav_bone_e_aav` | `1/L` |
| `state__aav_bone_e_cmal_r` | `1/L` |
| `state__aav_bone_e_cmal_rc` | `1/L` |
| `state__aav_bone_e_cml_r` | `1/L` |
| `state__aav_bone_e_cml_rc` | `1/L` |
| `state__aav_bone_e_n` | `1/L` |
| `state__aav_bone_e_r` | `1/L` |
| `state__aav_bone_e_rc` | `1/L` |
| `state__aav_bone_i` | `1/L` |
| `state__aav_bone_p_aav` | `1/L` |
| `state__aav_bone_p_cm_r` | `1/L` |
| `state__aav_bone_p_cm_rc` | `1/L` |
| `state__aav_bone_p_n` | `1/L` |
| `state__aav_bone_p_r` | `1/L` |
| `state__aav_bone_p_rc` | `1/L` |
| `state__aav_bone_v` | `1/L` |
| `state__aav_brain_e_aav` | `1/L` |
| `state__aav_brain_e_cmal_r` | `1/L` |
| `state__aav_brain_e_cmal_rc` | `1/L` |
| `state__aav_brain_e_cml_r` | `1/L` |
| `state__aav_brain_e_cml_rc` | `1/L` |
| `state__aav_brain_e_n` | `1/L` |
| `state__aav_brain_e_r` | `1/L` |
| `state__aav_brain_e_rc` | `1/L` |
| `state__aav_brain_i` | `1/L` |
| `state__aav_brain_p_aav` | `1/L` |
| `state__aav_brain_p_cm_r` | `1/L` |
| `state__aav_brain_p_cm_rc` | `1/L` |
| `state__aav_brain_p_n` | `1/L` |
| `state__aav_brain_p_r` | `1/L` |
| `state__aav_brain_p_rc` | `1/L` |
| `state__aav_brain_v` | `1/L` |
| `state__aav_heart_e_aav` | `1/L` |
| `state__aav_heart_e_cmal_r` | `1/L` |
| `state__aav_heart_e_cmal_rc` | `1/L` |
| `state__aav_heart_e_cml_r` | `1/L` |
| `state__aav_heart_e_cml_rc` | `1/L` |
| `state__aav_heart_e_n` | `1/L` |
| `state__aav_heart_e_r` | `1/L` |
| `state__aav_heart_e_rc` | `1/L` |
| `state__aav_heart_i` | `1/L` |
| `state__aav_heart_p_aav` | `1/L` |
| `state__aav_heart_p_cm_r` | `1/L` |
| `state__aav_heart_p_cm_rc` | `1/L` |
| `state__aav_heart_p_n` | `1/L` |
| `state__aav_heart_p_r` | `1/L` |
| `state__aav_heart_p_rc` | `1/L` |
| `state__aav_heart_v` | `1/L` |
| `state__aav_kidney_e_aav` | `1/L` |
| `state__aav_kidney_e_cmal_r` | `1/L` |
| `state__aav_kidney_e_cmal_rc` | `1/L` |
| `state__aav_kidney_e_cml_r` | `1/L` |
| `state__aav_kidney_e_cml_rc` | `1/L` |
| `state__aav_kidney_e_n` | `1/L` |
| `state__aav_kidney_e_r` | `1/L` |
| `state__aav_kidney_e_rc` | `1/L` |
| `state__aav_kidney_i` | `1/L` |
| `state__aav_kidney_p_aav` | `1/L` |
| `state__aav_kidney_p_cm_r` | `1/L` |
| `state__aav_kidney_p_cm_rc` | `1/L` |
| `state__aav_kidney_p_n` | `1/L` |
| `state__aav_kidney_p_r` | `1/L` |
| `state__aav_kidney_p_rc` | `1/L` |
| `state__aav_kidney_v` | `1/L` |
| `state__aav_large_intestine_e_aav` | `1/L` |
| `state__aav_large_intestine_e_cmal_r` | `1/L` |
| `state__aav_large_intestine_e_cmal_rc` | `1/L` |
| `state__aav_large_intestine_e_cml_r` | `1/L` |
| `state__aav_large_intestine_e_cml_rc` | `1/L` |
| `state__aav_large_intestine_e_n` | `1/L` |
| `state__aav_large_intestine_e_r` | `1/L` |
| `state__aav_large_intestine_e_rc` | `1/L` |
| `state__aav_large_intestine_i` | `1/L` |
| `state__aav_large_intestine_p_aav` | `1/L` |
| `state__aav_large_intestine_p_cm_r` | `1/L` |
| `state__aav_large_intestine_p_cm_rc` | `1/L` |
| `state__aav_large_intestine_p_n` | `1/L` |
| `state__aav_large_intestine_p_r` | `1/L` |
| `state__aav_large_intestine_p_rc` | `1/L` |
| `state__aav_large_intestine_v` | `1/L` |
| `state__aav_liver_e_aav` | `1/L` |
| `state__aav_liver_e_cmal_r` | `1/L` |
| `state__aav_liver_e_cmal_rc` | `1/L` |
| `state__aav_liver_e_cml_r` | `1/L` |
| `state__aav_liver_e_cml_rc` | `1/L` |
| `state__aav_liver_e_n` | `1/L` |
| `state__aav_liver_e_r` | `1/L` |
| `state__aav_liver_e_rc` | `1/L` |
| `state__aav_liver_i` | `1/L` |
| `state__aav_liver_p_aav` | `1/L` |
| `state__aav_liver_p_cm_r` | `1/L` |
| `state__aav_liver_p_cm_rc` | `1/L` |
| `state__aav_liver_p_n` | `1/L` |
| `state__aav_liver_p_r` | `1/L` |
| `state__aav_liver_p_rc` | `1/L` |
| `state__aav_liver_v` | `1/L` |
| `state__aav_lung_e_aav` | `1/L` |
| `state__aav_lung_e_cmal_r` | `1/L` |
| `state__aav_lung_e_cmal_rc` | `1/L` |
| `state__aav_lung_e_cml_r` | `1/L` |
| `state__aav_lung_e_cml_rc` | `1/L` |
| `state__aav_lung_e_n` | `1/L` |
| `state__aav_lung_e_r` | `1/L` |
| `state__aav_lung_e_rc` | `1/L` |
| `state__aav_lung_i` | `1/L` |
| `state__aav_lung_p_aav` | `1/L` |
| `state__aav_lung_p_cm_r` | `1/L` |
| `state__aav_lung_p_cm_rc` | `1/L` |
| `state__aav_lung_p_n` | `1/L` |
| `state__aav_lung_p_r` | `1/L` |
| `state__aav_lung_p_rc` | `1/L` |
| `state__aav_lung_v` | `1/L` |
| `state__aav_lymph` | `1/L` |
| `state__aav_muscle_e_aav` | `1/L` |
| `state__aav_muscle_e_cmal_r` | `1/L` |
| `state__aav_muscle_e_cmal_rc` | `1/L` |
| `state__aav_muscle_e_cml_r` | `1/L` |
| `state__aav_muscle_e_cml_rc` | `1/L` |
| `state__aav_muscle_e_n` | `1/L` |
| `state__aav_muscle_e_r` | `1/L` |
| `state__aav_muscle_e_rc` | `1/L` |
| `state__aav_muscle_i` | `1/L` |
| `state__aav_muscle_p_aav` | `1/L` |
| `state__aav_muscle_p_cm_r` | `1/L` |
| `state__aav_muscle_p_cm_rc` | `1/L` |
| `state__aav_muscle_p_n` | `1/L` |
| `state__aav_muscle_p_r` | `1/L` |
| `state__aav_muscle_p_rc` | `1/L` |
| `state__aav_muscle_v` | `1/L` |
| `state__aav_other_e_aav` | `1/L` |
| `state__aav_other_e_cmal_r` | `1/L` |
| `state__aav_other_e_cmal_rc` | `1/L` |
| `state__aav_other_e_cml_r` | `1/L` |
| `state__aav_other_e_cml_rc` | `1/L` |
| `state__aav_other_e_n` | `1/L` |
| `state__aav_other_e_r` | `1/L` |
| `state__aav_other_e_rc` | `1/L` |
| `state__aav_other_i` | `1/L` |
| `state__aav_other_p_aav` | `1/L` |
| `state__aav_other_p_cm_r` | `1/L` |
| `state__aav_other_p_cm_rc` | `1/L` |
| `state__aav_other_p_n` | `1/L` |
| `state__aav_other_p_r` | `1/L` |
| `state__aav_other_p_rc` | `1/L` |
| `state__aav_other_v` | `1/L` |
| `state__aav_pancreas_e_aav` | `1/L` |
| `state__aav_pancreas_e_cmal_r` | `1/L` |
| `state__aav_pancreas_e_cmal_rc` | `1/L` |
| `state__aav_pancreas_e_cml_r` | `1/L` |
| `state__aav_pancreas_e_cml_rc` | `1/L` |
| `state__aav_pancreas_e_n` | `1/L` |
| `state__aav_pancreas_e_r` | `1/L` |
| `state__aav_pancreas_e_rc` | `1/L` |
| `state__aav_pancreas_i` | `1/L` |
| `state__aav_pancreas_p_aav` | `1/L` |
| `state__aav_pancreas_p_cm_r` | `1/L` |
| `state__aav_pancreas_p_cm_rc` | `1/L` |
| `state__aav_pancreas_p_n` | `1/L` |
| `state__aav_pancreas_p_r` | `1/L` |
| `state__aav_pancreas_p_rc` | `1/L` |
| `state__aav_pancreas_v` | `1/L` |
| `state__aav_plasma` | `1/L` |
| `state__aav_skin_e_aav` | `1/L` |
| `state__aav_skin_e_cmal_r` | `1/L` |
| `state__aav_skin_e_cmal_rc` | `1/L` |
| `state__aav_skin_e_cml_r` | `1/L` |
| `state__aav_skin_e_cml_rc` | `1/L` |
| `state__aav_skin_e_n` | `1/L` |
| `state__aav_skin_e_r` | `1/L` |
| `state__aav_skin_e_rc` | `1/L` |
| `state__aav_skin_i` | `1/L` |
| `state__aav_skin_p_aav` | `1/L` |
| `state__aav_skin_p_cm_r` | `1/L` |
| `state__aav_skin_p_cm_rc` | `1/L` |
| `state__aav_skin_p_n` | `1/L` |
| `state__aav_skin_p_r` | `1/L` |
| `state__aav_skin_p_rc` | `1/L` |
| `state__aav_skin_v` | `1/L` |
| `state__aav_small_intestine_e_aav` | `1/L` |
| `state__aav_small_intestine_e_cmal_r` | `1/L` |
| `state__aav_small_intestine_e_cmal_rc` | `1/L` |
| `state__aav_small_intestine_e_cml_r` | `1/L` |
| `state__aav_small_intestine_e_cml_rc` | `1/L` |
| `state__aav_small_intestine_e_n` | `1/L` |
| `state__aav_small_intestine_e_r` | `1/L` |
| `state__aav_small_intestine_e_rc` | `1/L` |
| `state__aav_small_intestine_i` | `1/L` |
| `state__aav_small_intestine_p_aav` | `1/L` |
| `state__aav_small_intestine_p_cm_r` | `1/L` |
| `state__aav_small_intestine_p_cm_rc` | `1/L` |
| `state__aav_small_intestine_p_n` | `1/L` |
| `state__aav_small_intestine_p_r` | `1/L` |
| `state__aav_small_intestine_p_rc` | `1/L` |
| `state__aav_small_intestine_v` | `1/L` |
| `state__aav_spleen_e_aav` | `1/L` |
| `state__aav_spleen_e_cmal_r` | `1/L` |
| `state__aav_spleen_e_cmal_rc` | `1/L` |
| `state__aav_spleen_e_cml_r` | `1/L` |
| `state__aav_spleen_e_cml_rc` | `1/L` |
| `state__aav_spleen_e_n` | `1/L` |
| `state__aav_spleen_e_r` | `1/L` |
| `state__aav_spleen_e_rc` | `1/L` |
| `state__aav_spleen_i` | `1/L` |
| `state__aav_spleen_p_aav` | `1/L` |
| `state__aav_spleen_p_cm_r` | `1/L` |
| `state__aav_spleen_p_cm_rc` | `1/L` |
| `state__aav_spleen_p_n` | `1/L` |
| `state__aav_spleen_p_r` | `1/L` |
| `state__aav_spleen_p_rc` | `1/L` |
| `state__aav_spleen_v` | `1/L` |
| `state__aav_thymus_e_aav` | `1/L` |
| `state__aav_thymus_e_cmal_r` | `1/L` |
| `state__aav_thymus_e_cmal_rc` | `1/L` |
| `state__aav_thymus_e_cml_r` | `1/L` |
| `state__aav_thymus_e_cml_rc` | `1/L` |
| `state__aav_thymus_e_n` | `1/L` |
| `state__aav_thymus_e_r` | `1/L` |
| `state__aav_thymus_e_rc` | `1/L` |
| `state__aav_thymus_i` | `1/L` |
| `state__aav_thymus_p_aav` | `1/L` |
| `state__aav_thymus_p_cm_r` | `1/L` |
| `state__aav_thymus_p_cm_rc` | `1/L` |
| `state__aav_thymus_p_n` | `1/L` |
| `state__aav_thymus_p_r` | `1/L` |
| `state__aav_thymus_p_rc` | `1/L` |
| `state__aav_thymus_v` | `1/L` |
| `state__fcrn_adipose` | `M` |
| `state__fcrn_bone` | `M` |
| `state__fcrn_brain_bbb` | `M` |
| `state__fcrn_brain_bcsfb` | `M` |
| `state__fcrn_heart` | `M` |
| `state__fcrn_kidney` | `M` |
| `state__fcrn_large_intestine` | `M` |
| `state__fcrn_liver` | `M` |
| `state__fcrn_lung` | `M` |
| `state__fcrn_muscle` | `M` |
| `state__fcrn_other` | `M` |
| `state__fcrn_pancreas` | `M` |
| `state__fcrn_skin` | `M` |
| `state__fcrn_small_intestine` | `M` |
| `state__fcrn_spleen` | `M` |
| `state__fcrn_thymus` | `M` |
| `state__mab_adipose_e_b` | `M` |
| `state__mab_adipose_e_ub` | `M` |
| `state__mab_adipose_i` | `M` |
| `state__mab_adipose_v` | `M` |
| `state__mab_bone_e_b` | `M` |
| `state__mab_bone_e_ub` | `M` |
| `state__mab_bone_i` | `M` |
| `state__mab_bone_v` | `M` |
| `state__mab_brain_bbb_e_b` | `M` |
| `state__mab_brain_bbb_e_ub` | `M` |
| `state__mab_brain_bcsfb_e_b` | `M` |
| `state__mab_brain_bcsfb_e_ub` | `M` |
| `state__mab_brain_cm` | `M` |
| `state__mab_brain_i` | `M` |
| `state__mab_brain_lv` | `M` |
| `state__mab_brain_sas` | `M` |
| `state__mab_brain_tfv` | `M` |
| `state__mab_brain_v` | `M` |
| `state__mab_heart_e_b` | `M` |
| `state__mab_heart_e_ub` | `M` |
| `state__mab_heart_i` | `M` |
| `state__mab_heart_v` | `M` |
| `state__mab_immune_k1` | `1/h` |
| `state__mab_immune_k2` | `1/h` |
| `state__mab_immune_k3` | `1/h` |
| `state__mab_kidney_e_b` | `M` |
| `state__mab_kidney_e_ub` | `M` |
| `state__mab_kidney_i` | `M` |
| `state__mab_kidney_v` | `M` |
| `state__mab_large_intestine_e_b` | `M` |
| `state__mab_large_intestine_e_ub` | `M` |
| `state__mab_large_intestine_i` | `M` |
| `state__mab_large_intestine_v` | `M` |
| `state__mab_liver_e_b` | `M` |
| `state__mab_liver_e_ub` | `M` |
| `state__mab_liver_i` | `M` |
| `state__mab_liver_v` | `M` |
| `state__mab_lung_e_b` | `M` |
| `state__mab_lung_e_ub` | `M` |
| `state__mab_lung_i` | `M` |
| `state__mab_lung_v` | `M` |
| `state__mab_lymph` | `M` |
| `state__mab_muscle_e_b` | `M` |
| `state__mab_muscle_e_ub` | `M` |
| `state__mab_muscle_i` | `M` |
| `state__mab_muscle_v` | `M` |
| `state__mab_other_e_b` | `M` |
| `state__mab_other_e_ub` | `M` |
| `state__mab_other_i` | `M` |
| `state__mab_other_v` | `M` |
| `state__mab_pancreas_e_b` | `M` |
| `state__mab_pancreas_e_ub` | `M` |
| `state__mab_pancreas_i` | `M` |
| `state__mab_pancreas_v` | `M` |
| `state__mab_plasma` | `M` |
| `state__mab_skin_e_b` | `M` |
| `state__mab_skin_e_ub` | `M` |
| `state__mab_skin_i` | `M` |
| `state__mab_skin_v` | `M` |
| `state__mab_small_intestine_e_b` | `M` |
| `state__mab_small_intestine_e_ub` | `M` |
| `state__mab_small_intestine_i` | `M` |
| `state__mab_small_intestine_v` | `M` |
| `state__mab_spleen_e_b` | `M` |
| `state__mab_spleen_e_ub` | `M` |
| `state__mab_spleen_i` | `M` |
| `state__mab_spleen_v` | `M` |
| `state__mab_thymus_e_b` | `M` |
| `state__mab_thymus_e_ub` | `M` |
| `state__mab_thymus_i` | `M` |
| `state__mab_thymus_v` | `M` |
| `state__tx_adipose_e1` | `M` |
| `state__tx_adipose_e2` | `M` |
| `state__tx_adipose_e3` | `M` |
| `state__tx_adipose_e_mab` | `M` |
| `state__tx_adipose_p1` | `M` |
| `state__tx_adipose_p2` | `M` |
| `state__tx_adipose_p3` | `M` |
| `state__tx_adipose_p_mab` | `M` |
| `state__tx_bone_e1` | `M` |
| `state__tx_bone_e2` | `M` |
| `state__tx_bone_e3` | `M` |
| `state__tx_bone_e_mab` | `M` |
| `state__tx_bone_p1` | `M` |
| `state__tx_bone_p2` | `M` |
| `state__tx_bone_p3` | `M` |
| `state__tx_bone_p_mab` | `M` |
| `state__tx_brain_e1` | `M` |
| `state__tx_brain_e2` | `M` |
| `state__tx_brain_e3` | `M` |
| `state__tx_brain_e_mab` | `M` |
| `state__tx_brain_p1` | `M` |
| `state__tx_brain_p2` | `M` |
| `state__tx_brain_p3` | `M` |
| `state__tx_brain_p_mab` | `M` |
| `state__tx_heart_e1` | `M` |
| `state__tx_heart_e2` | `M` |
| `state__tx_heart_e3` | `M` |
| `state__tx_heart_e_mab` | `M` |
| `state__tx_heart_p1` | `M` |
| `state__tx_heart_p2` | `M` |
| `state__tx_heart_p3` | `M` |
| `state__tx_heart_p_mab` | `M` |
| `state__tx_kidney_e1` | `M` |
| `state__tx_kidney_e2` | `M` |
| `state__tx_kidney_e3` | `M` |
| `state__tx_kidney_e_mab` | `M` |
| `state__tx_kidney_p1` | `M` |
| `state__tx_kidney_p2` | `M` |
| `state__tx_kidney_p3` | `M` |
| `state__tx_kidney_p_mab` | `M` |
| `state__tx_large_intestine_e1` | `M` |
| `state__tx_large_intestine_e2` | `M` |
| `state__tx_large_intestine_e3` | `M` |
| `state__tx_large_intestine_e_mab` | `M` |
| `state__tx_large_intestine_p1` | `M` |
| `state__tx_large_intestine_p2` | `M` |
| `state__tx_large_intestine_p3` | `M` |
| `state__tx_large_intestine_p_mab` | `M` |
| `state__tx_liver_e1` | `M` |
| `state__tx_liver_e2` | `M` |
| `state__tx_liver_e3` | `M` |
| `state__tx_liver_e_mab` | `M` |
| `state__tx_liver_p1` | `M` |
| `state__tx_liver_p2` | `M` |
| `state__tx_liver_p3` | `M` |
| `state__tx_liver_p_mab` | `M` |
| `state__tx_lung_e1` | `M` |
| `state__tx_lung_e2` | `M` |
| `state__tx_lung_e3` | `M` |
| `state__tx_lung_e_mab` | `M` |
| `state__tx_lung_p1` | `M` |
| `state__tx_lung_p2` | `M` |
| `state__tx_lung_p3` | `M` |
| `state__tx_lung_p_mab` | `M` |
| `state__tx_muscle_e1` | `M` |
| `state__tx_muscle_e2` | `M` |
| `state__tx_muscle_e3` | `M` |
| `state__tx_muscle_e_mab` | `M` |
| `state__tx_muscle_p1` | `M` |
| `state__tx_muscle_p2` | `M` |
| `state__tx_muscle_p3` | `M` |
| `state__tx_muscle_p_mab` | `M` |
| `state__tx_other_e1` | `M` |
| `state__tx_other_e2` | `M` |
| `state__tx_other_e3` | `M` |
| `state__tx_other_e_mab` | `M` |
| `state__tx_other_p1` | `M` |
| `state__tx_other_p2` | `M` |
| `state__tx_other_p3` | `M` |
| `state__tx_other_p_mab` | `M` |
| `state__tx_pancreas_e1` | `M` |
| `state__tx_pancreas_e2` | `M` |
| `state__tx_pancreas_e3` | `M` |
| `state__tx_pancreas_e_mab` | `M` |
| `state__tx_pancreas_p1` | `M` |
| `state__tx_pancreas_p2` | `M` |
| `state__tx_pancreas_p3` | `M` |
| `state__tx_pancreas_p_mab` | `M` |
| `state__tx_skin_e1` | `M` |
| `state__tx_skin_e2` | `M` |
| `state__tx_skin_e3` | `M` |
| `state__tx_skin_e_mab` | `M` |
| `state__tx_skin_p1` | `M` |
| `state__tx_skin_p2` | `M` |
| `state__tx_skin_p3` | `M` |
| `state__tx_skin_p_mab` | `M` |
| `state__tx_small_intestine_e1` | `M` |
| `state__tx_small_intestine_e2` | `M` |
| `state__tx_small_intestine_e3` | `M` |
| `state__tx_small_intestine_e_mab` | `M` |
| `state__tx_small_intestine_p1` | `M` |
| `state__tx_small_intestine_p2` | `M` |
| `state__tx_small_intestine_p3` | `M` |
| `state__tx_small_intestine_p_mab` | `M` |
| `state__tx_spleen_e1` | `M` |
| `state__tx_spleen_e2` | `M` |
| `state__tx_spleen_e3` | `M` |
| `state__tx_spleen_e_mab` | `M` |
| `state__tx_spleen_p1` | `M` |
| `state__tx_spleen_p2` | `M` |
| `state__tx_spleen_p3` | `M` |
| `state__tx_spleen_p_mab` | `M` |
| `state__tx_thymus_e1` | `M` |
| `state__tx_thymus_e2` | `M` |
| `state__tx_thymus_e3` | `M` |
| `state__tx_thymus_e_mab` | `M` |
| `state__tx_thymus_p1` | `M` |
| `state__tx_thymus_p2` | `M` |
| `state__tx_thymus_p3` | `M` |
| `state__tx_thymus_p_mab` | `M` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `figure3_5_iv_aav8_1e11_vg_mouse` starter has **87 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `aav_blood_vg_per_uL` | 5.82411e+07 | 408.356 (504 h, pre) | 5.82411e+07 (0 h, post) | 408.356 |
| `mab_plasma_ug_mL` | 0 | 0 (0 h, post) | 166.492 (258 h, post) | 80.3328 |
| `mab_brain_interstitial_nM` | 0 | 0 (0 h, post) | 2.79443 (270 h, post) | 1.66335 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

545-state AAV expression and nonlinear antibody PBPK topology, disclosed source parameter anchors and curated source-reconstruction readouts.

Outside this version’s scope:

- sponsor control stream
- animal-level observations/fitting
- error model/covariance
- clinical dose selection

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
