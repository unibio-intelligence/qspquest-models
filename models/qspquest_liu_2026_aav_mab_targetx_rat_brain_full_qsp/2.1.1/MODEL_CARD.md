# Whole-body AAV–anti-TargetX rat brain QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare AAV delivery routes, antibody distribution and brain target engagement in a rat model.

**Runnable · 13 experiments.** Version 2.1.1.

This is an alternate version. [Open the default version](../2.1.2/MODEL_CARD.md) for the standard quickstart.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import load_archive

model = load_archive(
    'models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.1.1/model.omex',
    expected_sha256='fdd64ce17b2e6c3e69e2c0c0ca50e6c166a36e39857ac5acbba6aa13e11be5c5',
)
result = model.run('figure3_mab_iv_100mgkg')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 13 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `figure3_mab_iv_100mgkg` | Figure3 mab iv 100mgkg | -1000–504 h | 253 |
| `figure3_mab_iv_10mgkg` | Figure3 mab iv 10mgkg | -1000–504 h | 253 |
| `figure3_mab_iv_30mgkg` | Figure3 mab iv 30mgkg | -1000–504 h | 253 |
| `figure3_mab_iv_3mgkg` | Figure3 mab iv 3mgkg | -1000–504 h | 253 |
| `figure3a_exogenous_targetx_shape` | Figure3a exogenous targetx shape | 0–6 h | 61 |
| `figure3b_targetx_steady_state` | Figure3b targetx steady state | -504–0 h | 85 |
| `icm_1e12_aav9` | Icm 1e12 aav9 | -1000–1344 h | 101 |
| `icm_5e11_aav9` | Icm 5e11 aav9 | -1000–1344 h | 101 |
| `icm_5e12_aav5` | Icm 5e12 aav5 | -1000–1344 h | 101 |
| `icm_5e12_aav9` | Icm 5e12 aav9 | -1000–1344 h | 101 |
| `ist_2_5e11_aav9` | Ist 2 5e11 aav9 | -1000–1344 h | 101 |
| `iv_5e12_aav9` | Iv 5e12 aav9 | -1000–1344 h | 101 |
| `source_structure_no_dose_smoke` | Source structure no dose smoke | 0–0.01 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `mab_plasma_ug_mL` | Antibody concentration in plasma | `1` |
| `mab_isf_nM` | Antibody concentration in brain interstitial fluid | `1` |
| `target_isf_pct_baseline` | Brain interstitial target as a percentage of baseline | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

Use the checksum-pinned Python archive command above for this version. The library CLI selects the current default archive.

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 27 outputs and 725 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `aav_blood_Vg_mL` | `1` |
| `aav_brain_Vg_mL` | `1` |
| `aav_heart_Vg_mL` | `1` |
| `aav_liver_Vg_mL` | `1` |
| `aav_lung_Vg_mL` | `1` |
| `blood_aav_Vg_uL` | `1` |
| `central_plasma_volume_mL` | `1` |
| `mab_brain_nM` | `1` |
| `mab_csf_nM` | `1` |
| `mab_csf_ug_mL` | `1` |
| `mab_heart_nM` | `1` |
| `mab_isf_nM` | `1` |
| `mab_isf_ug_mL` | `1` |
| `mab_liver_nM` | `1` |
| `mab_lung_nM` | `1` |
| `mab_plasma_nM` | `1` |
| `mab_plasma_ug_mL` | `1` |
| `state_count_anchor` | `1` |
| `supplement_equation_count_anchor` | `1` |
| `target_csf_pM` | `1` |
| `target_csf_pct_baseline` | `1` |
| `target_isf_pM` | `1` |
| `target_isf_pct_baseline` | `1` |
| `target_lv_pM` | `1` |
| `target_lv_pct_reported_baseline` | `1` |
| `target_plasma_pM` | `1` |
| `target_plasma_pct_baseline` | `1` |
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
| `state__aav_brain_bbb_aav` | `1/L` |
| `state__aav_brain_bbb_cmal_r` | `1/L` |
| `state__aav_brain_bbb_cmal_rc` | `1/L` |
| `state__aav_brain_bbb_cml_r` | `1/L` |
| `state__aav_brain_bbb_cml_rc` | `1/L` |
| `state__aav_brain_bbb_n` | `1/L` |
| `state__aav_brain_bbb_r` | `1/L` |
| `state__aav_brain_bbb_rc` | `1/L` |
| `state__aav_brain_bcsfb_aav` | `1/L` |
| `state__aav_brain_bcsfb_cmal_r` | `1/L` |
| `state__aav_brain_bcsfb_cmal_rc` | `1/L` |
| `state__aav_brain_bcsfb_cml_r` | `1/L` |
| `state__aav_brain_bcsfb_cml_rc` | `1/L` |
| `state__aav_brain_bcsfb_n` | `1/L` |
| `state__aav_brain_bcsfb_r` | `1/L` |
| `state__aav_brain_bcsfb_rc` | `1/L` |
| `state__aav_brain_cm` | `1/L` |
| `state__aav_brain_i` | `1/L` |
| `state__aav_brain_lv` | `1/L` |
| `state__aav_brain_p_aav` | `1/L` |
| `state__aav_brain_p_cm_r` | `1/L` |
| `state__aav_brain_p_cm_rc` | `1/L` |
| `state__aav_brain_p_n` | `1/L` |
| `state__aav_brain_p_r` | `1/L` |
| `state__aav_brain_p_rc` | `1/L` |
| `state__aav_brain_pv_art` | `1/L` |
| `state__aav_brain_pv_ven` | `1/L` |
| `state__aav_brain_sas` | `1/L` |
| `state__aav_brain_tfv` | `1/L` |
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
| `state__aav_men_cm_aav` | `1/L` |
| `state__aav_men_cm_cm_r` | `1/L` |
| `state__aav_men_cm_cm_rc` | `1/L` |
| `state__aav_men_cm_n` | `1/L` |
| `state__aav_men_cm_r` | `1/L` |
| `state__aav_men_cm_rc` | `1/L` |
| `state__aav_men_sas_aav` | `1/L` |
| `state__aav_men_sas_cm_r` | `1/L` |
| `state__aav_men_sas_cm_rc` | `1/L` |
| `state__aav_men_sas_n` | `1/L` |
| `state__aav_men_sas_r` | `1/L` |
| `state__aav_men_sas_rc` | `1/L` |
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
| `state__complex_adipose_e_b` | `M` |
| `state__complex_adipose_e_ub` | `M` |
| `state__complex_adipose_i` | `M` |
| `state__complex_adipose_v` | `M` |
| `state__complex_bone_e_b` | `M` |
| `state__complex_bone_e_ub` | `M` |
| `state__complex_bone_i` | `M` |
| `state__complex_bone_v` | `M` |
| `state__complex_brain_bbb_e_b` | `M` |
| `state__complex_brain_bbb_e_ub` | `M` |
| `state__complex_brain_bcsfb_e_b` | `M` |
| `state__complex_brain_bcsfb_e_ub` | `M` |
| `state__complex_brain_cm` | `M` |
| `state__complex_brain_i` | `M` |
| `state__complex_brain_lv` | `M` |
| `state__complex_brain_p_endo` | `M` |
| `state__complex_brain_pv_art` | `M` |
| `state__complex_brain_pv_ven` | `M` |
| `state__complex_brain_sas` | `M` |
| `state__complex_brain_tfv` | `M` |
| `state__complex_brain_v` | `M` |
| `state__complex_heart_e_b` | `M` |
| `state__complex_heart_e_ub` | `M` |
| `state__complex_heart_i` | `M` |
| `state__complex_heart_v` | `M` |
| `state__complex_kidney_e_b` | `M` |
| `state__complex_kidney_e_ub` | `M` |
| `state__complex_kidney_i` | `M` |
| `state__complex_kidney_v` | `M` |
| `state__complex_large_intestine_e_b` | `M` |
| `state__complex_large_intestine_e_ub` | `M` |
| `state__complex_large_intestine_i` | `M` |
| `state__complex_large_intestine_v` | `M` |
| `state__complex_liver_e_b` | `M` |
| `state__complex_liver_e_ub` | `M` |
| `state__complex_liver_i` | `M` |
| `state__complex_liver_v` | `M` |
| `state__complex_lung_e_b` | `M` |
| `state__complex_lung_e_ub` | `M` |
| `state__complex_lung_i` | `M` |
| `state__complex_lung_v` | `M` |
| `state__complex_lymph` | `M` |
| `state__complex_muscle_e_b` | `M` |
| `state__complex_muscle_e_ub` | `M` |
| `state__complex_muscle_i` | `M` |
| `state__complex_muscle_v` | `M` |
| `state__complex_other_e_b` | `M` |
| `state__complex_other_e_ub` | `M` |
| `state__complex_other_i` | `M` |
| `state__complex_other_v` | `M` |
| `state__complex_pancreas_e_b` | `M` |
| `state__complex_pancreas_e_ub` | `M` |
| `state__complex_pancreas_i` | `M` |
| `state__complex_pancreas_v` | `M` |
| `state__complex_plasma` | `M` |
| `state__complex_skin_e_b` | `M` |
| `state__complex_skin_e_ub` | `M` |
| `state__complex_skin_i` | `M` |
| `state__complex_skin_v` | `M` |
| `state__complex_small_intestine_e_b` | `M` |
| `state__complex_small_intestine_e_ub` | `M` |
| `state__complex_small_intestine_i` | `M` |
| `state__complex_small_intestine_v` | `M` |
| `state__complex_spleen_e_b` | `M` |
| `state__complex_spleen_e_ub` | `M` |
| `state__complex_spleen_i` | `M` |
| `state__complex_spleen_v` | `M` |
| `state__complex_thymus_e_b` | `M` |
| `state__complex_thymus_e_ub` | `M` |
| `state__complex_thymus_i` | `M` |
| `state__complex_thymus_v` | `M` |
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
| `state__mab_brain_p_endo` | `M` |
| `state__mab_brain_pv_art` | `M` |
| `state__mab_brain_pv_ven` | `M` |
| `state__mab_brain_sas` | `M` |
| `state__mab_brain_tfv` | `M` |
| `state__mab_brain_v` | `M` |
| `state__mab_heart_e_b` | `M` |
| `state__mab_heart_e_ub` | `M` |
| `state__mab_heart_i` | `M` |
| `state__mab_heart_v` | `M` |
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
| `state__target_adipose_e_b` | `M` |
| `state__target_adipose_e_ub` | `M` |
| `state__target_adipose_i` | `M` |
| `state__target_adipose_v` | `M` |
| `state__target_bone_e_b` | `M` |
| `state__target_bone_e_ub` | `M` |
| `state__target_bone_i` | `M` |
| `state__target_bone_v` | `M` |
| `state__target_brain_bbb_e_b` | `M` |
| `state__target_brain_bbb_e_ub` | `M` |
| `state__target_brain_bcsfb_e_b` | `M` |
| `state__target_brain_bcsfb_e_ub` | `M` |
| `state__target_brain_cm` | `M` |
| `state__target_brain_i` | `M` |
| `state__target_brain_lv` | `M` |
| `state__target_brain_p_endo` | `M` |
| `state__target_brain_pv_art` | `M` |
| `state__target_brain_pv_ven` | `M` |
| `state__target_brain_sas` | `M` |
| `state__target_brain_tfv` | `M` |
| `state__target_brain_v` | `M` |
| `state__target_heart_e_b` | `M` |
| `state__target_heart_e_ub` | `M` |
| `state__target_heart_i` | `M` |
| `state__target_heart_v` | `M` |
| `state__target_kidney_e_b` | `M` |
| `state__target_kidney_e_ub` | `M` |
| `state__target_kidney_i` | `M` |
| `state__target_kidney_v` | `M` |
| `state__target_large_intestine_e_b` | `M` |
| `state__target_large_intestine_e_ub` | `M` |
| `state__target_large_intestine_i` | `M` |
| `state__target_large_intestine_v` | `M` |
| `state__target_liver_e_b` | `M` |
| `state__target_liver_e_ub` | `M` |
| `state__target_liver_i` | `M` |
| `state__target_liver_v` | `M` |
| `state__target_lung_e_b` | `M` |
| `state__target_lung_e_ub` | `M` |
| `state__target_lung_i` | `M` |
| `state__target_lung_v` | `M` |
| `state__target_lymph` | `M` |
| `state__target_muscle_e_b` | `M` |
| `state__target_muscle_e_ub` | `M` |
| `state__target_muscle_i` | `M` |
| `state__target_muscle_v` | `M` |
| `state__target_other_e_b` | `M` |
| `state__target_other_e_ub` | `M` |
| `state__target_other_i` | `M` |
| `state__target_other_v` | `M` |
| `state__target_pancreas_e_b` | `M` |
| `state__target_pancreas_e_ub` | `M` |
| `state__target_pancreas_i` | `M` |
| `state__target_pancreas_v` | `M` |
| `state__target_plasma` | `M` |
| `state__target_skin_e_b` | `M` |
| `state__target_skin_e_ub` | `M` |
| `state__target_skin_i` | `M` |
| `state__target_skin_v` | `M` |
| `state__target_small_intestine_e_b` | `M` |
| `state__target_small_intestine_e_ub` | `M` |
| `state__target_small_intestine_i` | `M` |
| `state__target_small_intestine_v` | `M` |
| `state__target_spleen_e_b` | `M` |
| `state__target_spleen_e_ub` | `M` |
| `state__target_spleen_i` | `M` |
| `state__target_spleen_v` | `M` |
| `state__target_thymus_e_b` | `M` |
| `state__target_thymus_e_ub` | `M` |
| `state__target_thymus_i` | `M` |
| `state__target_thymus_v` | `M` |
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
| `state__tx_brain_bbb_1` | `M` |
| `state__tx_brain_bbb_2` | `M` |
| `state__tx_brain_bbb_3` | `M` |
| `state__tx_brain_bbb_mab` | `M` |
| `state__tx_brain_bcsfb_1` | `M` |
| `state__tx_brain_bcsfb_2` | `M` |
| `state__tx_brain_bcsfb_3` | `M` |
| `state__tx_brain_bcsfb_mab` | `M` |
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
| `state__tx_men_cm_1` | `M` |
| `state__tx_men_cm_2` | `M` |
| `state__tx_men_cm_3` | `M` |
| `state__tx_men_cm_mab` | `M` |
| `state__tx_men_sas_1` | `M` |
| `state__tx_men_sas_2` | `M` |
| `state__tx_men_sas_3` | `M` |
| `state__tx_men_sas_mab` | `M` |
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

The `figure3_mab_iv_100mgkg` starter has **253 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `mab_plasma_ug_mL` | 0 | -1.01558e-27 (-160 h, post) | 2680.44 (2 h, post) | 49.9467 |
| `mab_isf_nM` | 0 | -1.21368e-29 (-154 h, post) | 21.6721 (32 h, post) | 0.762937 |
| `target_isf_pct_baseline` | 0 | 0 (-1000 h, post) | 99.5489 (-742 h, post) | 90.1056 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

Generalized source equation templates expanded into 725 ODE states, disclosed fixed/final parameters and route/serotype mechanisms.

Outside this version’s scope:

- sponsor Ubiquity control stream
- animal-level fits
- residual model/covariance
- bit-for-bit sponsor predictions

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:28f144300edd88b3321dc300056e7310cd5448e842790c3861701b3ea7dd250d`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Mechanistic rat QSP linking IV, intracisterna-magna, or intrastriatal AAV delivery to whole-body vector disposition, transgene-derived anti-TargetX antibody, FcRn-aware protein distribution, and free TargetX in plasma, brain ISF, and CSF.

## Serotype initialization

The AAV5 preset couples its declared receptor-total parameters with all 65 nonzero free receptor starting coordinates. The retained -1000 h equilibration precedes the bolus at 0 h. Blood-cell and tissue receptor coordinates use their respective declared totals.

Receptor-total parameters are initialization inputs and do not occur in the derivative equations. Changing one parameter alone in a research request does not reinitialize its receptor states. Use a named serotype preset or explicitly update the coupled initial states.

Source numerical coordinates; physical-unit qualification and author-control-stream reproduction are not established.

## Source equation interpretations

Archive SHA-256: `fdd64ce17b2e6c3e69e2c0c0ca50e6c166a36e39857ac5acbba6aa13e11be5c5`. Coverage: selected disclosed choices; complete source qualification remains open.

DOI 10.1007/s10928-026-10051-w; supplementary equations 134-136, printed page 32.

The printed equations use plasma concentrations while declaring Y as Plasma or Lymph. This implementation evaluates association and dissociation with concentrations in the named local compartment. This is a disclosed locality interpretation; the author control stream has not been checked.

Printed coordinates: `mab_plasma`, `target_plasma`, `complex_plasma`.
Adopted coordinates: `mab_lymph`, `target_lymph`, `complex_lymph`.

The binding contribution cancels in antibody plus complex and target plus complex for either convention. That stoichiometric cancellation does not certify whole-body conservation, physical dimensions or positivity. A plasma-driven lymph reaction can consume local species without local reactant availability.

A literal printed-plasma reconstruction and a local-lymph reconstruction represent distinct source conventions. Neither is rejected as scientifically incorrect solely for this choice. Complete author-code, dimensional and whole-body conservation qualification remain open.

## Barrier inputs

BBB and BCSFB reflection inputs are separate for AAV vector and proteins. sigma_vector_bbb and sigma_vector_bcsfb affect AAV equations; sigma_protein_bbb and sigma_protein_bcsfb affect mAb, TargetX and their complex together. A protein-only perturbation leaves all vector equation coefficients unchanged. A shared perturbation must explicitly set both vector and protein inputs and therefore affects AAV, mAb, TargetX and complex.

Liu 2026, DOI 10.1007/s10928-026-10051-w, Table 1 page 11. The table prints separate modality superscripts with common BBB 0.9975 and BCSFB 0.9973 values.

All four coefficients use unit 1, values from 0 through 1 and the retained source numerical scale. The protein profile deliberately groups mAb, TargetX and complex at their disclosed common barrier defaults; a TargetX-only perturbation is not represented. Other organ reflection, interstitial/CSF reflection, diffusion, receptor and transgene coordinates are unchanged. Complete source, author-code, physical-unit and whole-body conservation qualification remain open.

Version 2.1.0 uses four explicit modality names. The ambiguous sigma_bbb and sigma_bcsfb inputs and their prior native source_symbol_872/source_symbol_873 names are unavailable. To reproduce a shared barrier perturbation, set both sigma_vector_bbb and sigma_protein_bbb, and both sigma_vector_bcsfb and sigma_protein_bcsfb. For a historical calculation use its exact pinned archive and request.

<details>
<summary>Output identities</summary>

Analyte and compartment identities of the archived source readout expressions. Aggregate labels describe only the states included by those expressions. CSF aliases denote cisterna magna, not all CSF compartments.

Returned native units remain 1. Friendly name suffixes and semantic identities do not establish physical units, conserved mass or complete source reproduction.

Liu 2026, DOI 10.1007/s10928-026-10051-w, Figure 2 and Table 1, pages 5–10.

| Readout | Analyte identifier | Compartment identifier | Returned native unit | Archive source label |
| --- | --- | --- | --- | --- |
| `aav_blood_Vg_mL` | `aav_vector` | `central_blood` | `1` | `1` |
| `aav_brain_Vg_mL` | `aav_vector` | `brain_tissue_aggregate` | `1` | `1` |
| `aav_heart_Vg_mL` | `aav_vector` | `heart_tissue_aggregate` | `1` | `1` |
| `aav_liver_Vg_mL` | `aav_vector` | `liver_tissue_aggregate` | `1` | `1` |
| `aav_lung_Vg_mL` | `aav_vector` | `lung_tissue_aggregate` | `1` | `1` |
| `blood_aav_Vg_uL` | `aav_vector` | `central_blood` | `1` | `1` |
| `mab_brain_nM` | `anti_targetx_mab` | `brain_tissue_aggregate` | `1` | `1` |
| `mab_csf_nM` | `anti_targetx_mab` | `cisterna_magna_csf` | `1` | `1` |
| `mab_csf_ug_mL` | `anti_targetx_mab` | `cisterna_magna_csf` | `1` | `1` |
| `mab_heart_nM` | `anti_targetx_mab` | `heart_tissue_aggregate` | `1` | `1` |
| `mab_isf_nM` | `anti_targetx_mab` | `brain_interstitial_fluid` | `1` | `1` |
| `mab_isf_ug_mL` | `anti_targetx_mab` | `brain_interstitial_fluid` | `1` | `1` |
| `mab_liver_nM` | `anti_targetx_mab` | `liver_tissue_aggregate` | `1` | `1` |
| `mab_lung_nM` | `anti_targetx_mab` | `lung_tissue_aggregate` | `1` | `1` |
| `mab_plasma_nM` | `anti_targetx_mab` | `central_plasma` | `1` | `1` |
| `mab_plasma_ug_mL` | `anti_targetx_mab` | `central_plasma` | `1` | `1` |
| `target_csf_pM` | `targetx` | `cisterna_magna_csf` | `1` | `1` |
| `target_csf_pct_baseline` | `targetx` | `cisterna_magna_csf` | `1` | `1` |
| `target_isf_pM` | `targetx` | `brain_interstitial_fluid` | `1` | `1` |
| `target_isf_pct_baseline` | `targetx` | `brain_interstitial_fluid` | `1` | `1` |
| `target_lv_pM` | `targetx` | `brain_lateral_ventricle_csf` | `1` | `1` |
| `target_lv_pct_reported_baseline` | `targetx` | `brain_lateral_ventricle_csf` | `1` | `1` |
| `target_plasma_pM` | `targetx` | `central_plasma` | `1` | `1` |
| `target_plasma_pct_baseline` | `targetx` | `central_plasma` | `1` | `1` |

Inspect the same declarations using `model.output_semantics`. An undeclared identity is `None`; it is not inferred from the readout name.

</details>

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)

## Initialization and percentage denominators

The ICM AAV scenarios initialize literal source states at −1000 h and integrate
before the first administration at 0 h. This interval does not by itself assert
equilibrium or convergence. Starting parameter overrides apply from −1000 h;
timed changes apply after their stated boundary. Receptor-total parameters alone
do not recompute literal free-receptor initial values. Use the coupled scenario
or supply the intended initial states explicitly. Other archived protocols have
their own initialization clocks, including no-dose scenarios.

[PROTOCOL_INITIALIZATION.json](PROTOCOL_INITIALIZATION.json) pins the archive,
native model and all thirteen scenarios, and declares the exact numerator state
and baseline input for the four percentage readouts. Each uses a declared
reference input; an explicit override changes that denominator. Neither a
transport perturbation nor a new trajectory automatically establishes a
condition-specific baseline. Use `model.protocol_initialization` in the Python
SDK to inspect the verified declaration. Source coordinates and native unit `1`
remain unqualified as physical dimensions.
