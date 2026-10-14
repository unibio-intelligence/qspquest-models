# Rodriguez-Fernandez 2024 Secukinumab MIPD Psoriasis PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed secukinumab exposure and psoriasis-response scenarios.

**Runnable · 26 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation using public individual parameters. Paper comparator contains Figure 5 target band and raster-derived paper scatter; strict individual curve parity is source-limited.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_rodriguez_fernandez_2024_secukinumab_psoriasis_mipd', version='0.1.0')
result = model.run('subject1-300mg-q4w-20cycle-ode-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 26 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `si-subject-1-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-10-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-11-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-13-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-14-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-15-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-16-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-17-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-18-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-2-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-20-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-21-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-22-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-23-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-24-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-3-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-4-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-5-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-6-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-7-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-8-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `si-subject-9-parameter-anchor` | No-dose exact replay of individual conditional-distribution parameter mean and SD rows. | 0–0.001 h | 2 |
| `subject1-300mg-q4w-20cycle-ode-probe` | Full ODE simulation using public individual parameters. Paper comparator contains Figure 5 target band and raster-derived paper scatter; strict individual curve parity is source-limited. | 0–616 h | 89 |
| `subject5-300mg-q4w-20cycle-ode-probe` | Full ODE simulation using public individual parameters. Paper comparator contains Figure 5 target band and raster-derived paper scatter; strict individual curve parity is source-limited. | 0–616 h | 89 |
| `subject8-150mg-q6w-20cycle-ode-probe` | Full ODE simulation using public individual parameters. Paper comparator contains Figure 5 target band and raster-derived paper scatter; strict individual curve parity is source-limited. | 0–616 h | 89 |
| `table2-population-pd-anchor` | No-dose exact replay of Table 2 estimates, cohort counts, MIPD result counts, and Figure 5 target statement. | 0–0.001 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_mg_l` | Secukinumab concentration | `1` |
| `drug_effect_fraction` | Fractional drug effect on psoriasis response | `1` |
| `pasi_target_gap` | Difference from the model psoriasis response target | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_rodriguez_fernandez_2024_secukinumab_psoriasis_mipd --model-version 0.1.0 --scenario subject1-300mg-q4w-20cycle-ode-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 548 outputs and 13 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `bioavailability_fraction` | `1` |
| `central_concentration_mg_l` | `1` |
| `drug_effect_fraction` | `1` |
| `effective_imax` | `1` |
| `kin_pasi_day` | `1` |
| `pasi_target_gap` | `1` |
| `peripheral_concentration_mg_l` | `1` |
| `source_CL_L_day` | `1` |
| `source_F_sc_fraction` | `1` |
| `source_Q_L_day` | `1` |
| `source_V2_L` | `1` |
| `source_V3_L` | `1` |
| `source_bioavailability_pct` | `1` |
| `source_ic50_mg_l` | `1` |
| `source_imax` | `1` |
| `source_ka_1_day` | `1` |
| `source_kout_1_day` | `1` |
| `source_kouttol_1_day` | `1` |
| `source_pasi_baseline` | `1` |
| `source_sd_CL_L_day` | `1` |
| `source_sd_Q_L_day` | `1` |
| `source_sd_V2_L` | `1` |
| `source_sd_V3_L` | `1` |
| `source_sd_imax` | `1` |
| `source_sd_ka_1_day` | `1` |
| `source_sd_kout_1_day` | `1` |
| `source_sd_kouttol_1_day` | `1` |
| `source_sd_pasi_baseline` | `1` |
| `source_subject_10_CL_L_day` | `1` |
| `source_subject_10_F_sc_fraction` | `1` |
| `source_subject_10_Q_L_day` | `1` |
| `source_subject_10_V2_L` | `1` |
| `source_subject_10_V3_L` | `1` |
| `source_subject_10_bioavailability_pct` | `1` |
| `source_subject_10_ic50_mg_l` | `1` |
| `source_subject_10_imax` | `1` |
| `source_subject_10_ka_1_day` | `1` |
| `source_subject_10_kout_1_day` | `1` |
| `source_subject_10_kouttol_1_day` | `1` |
| `source_subject_10_pasi_baseline` | `1` |
| `source_subject_10_sd_CL_L_day` | `1` |
| `source_subject_10_sd_Q_L_day` | `1` |
| `source_subject_10_sd_V2_L` | `1` |
| `source_subject_10_sd_V3_L` | `1` |
| `source_subject_10_sd_imax` | `1` |
| `source_subject_10_sd_ka_1_day` | `1` |
| `source_subject_10_sd_kout_1_day` | `1` |
| `source_subject_10_sd_kouttol_1_day` | `1` |
| `source_subject_10_sd_pasi_baseline` | `1` |
| `source_subject_10_tolerance_enabled` | `1` |
| `source_subject_11_CL_L_day` | `1` |
| `source_subject_11_F_sc_fraction` | `1` |
| `source_subject_11_Q_L_day` | `1` |
| `source_subject_11_V2_L` | `1` |
| `source_subject_11_V3_L` | `1` |
| `source_subject_11_bioavailability_pct` | `1` |
| `source_subject_11_ic50_mg_l` | `1` |
| `source_subject_11_imax` | `1` |
| `source_subject_11_ka_1_day` | `1` |
| `source_subject_11_kout_1_day` | `1` |
| `source_subject_11_kouttol_1_day` | `1` |
| `source_subject_11_pasi_baseline` | `1` |
| `source_subject_11_sd_CL_L_day` | `1` |
| `source_subject_11_sd_Q_L_day` | `1` |
| `source_subject_11_sd_V2_L` | `1` |
| `source_subject_11_sd_V3_L` | `1` |
| `source_subject_11_sd_imax` | `1` |
| `source_subject_11_sd_ka_1_day` | `1` |
| `source_subject_11_sd_kout_1_day` | `1` |
| `source_subject_11_sd_kouttol_1_day` | `1` |
| `source_subject_11_sd_pasi_baseline` | `1` |
| `source_subject_11_tolerance_enabled` | `1` |
| `source_subject_13_CL_L_day` | `1` |
| `source_subject_13_F_sc_fraction` | `1` |
| `source_subject_13_Q_L_day` | `1` |
| `source_subject_13_V2_L` | `1` |
| `source_subject_13_V3_L` | `1` |
| `source_subject_13_bioavailability_pct` | `1` |
| `source_subject_13_ic50_mg_l` | `1` |
| `source_subject_13_imax` | `1` |
| `source_subject_13_ka_1_day` | `1` |
| `source_subject_13_kout_1_day` | `1` |
| `source_subject_13_kouttol_1_day` | `1` |
| `source_subject_13_pasi_baseline` | `1` |
| `source_subject_13_sd_CL_L_day` | `1` |
| `source_subject_13_sd_Q_L_day` | `1` |
| `source_subject_13_sd_V2_L` | `1` |
| `source_subject_13_sd_V3_L` | `1` |
| `source_subject_13_sd_imax` | `1` |
| `source_subject_13_sd_ka_1_day` | `1` |
| `source_subject_13_sd_kout_1_day` | `1` |
| `source_subject_13_sd_kouttol_1_day` | `1` |
| `source_subject_13_sd_pasi_baseline` | `1` |
| `source_subject_13_tolerance_enabled` | `1` |
| `source_subject_14_CL_L_day` | `1` |
| `source_subject_14_F_sc_fraction` | `1` |
| `source_subject_14_Q_L_day` | `1` |
| `source_subject_14_V2_L` | `1` |
| `source_subject_14_V3_L` | `1` |
| `source_subject_14_bioavailability_pct` | `1` |
| `source_subject_14_ic50_mg_l` | `1` |
| `source_subject_14_imax` | `1` |
| `source_subject_14_ka_1_day` | `1` |
| `source_subject_14_kout_1_day` | `1` |
| `source_subject_14_kouttol_1_day` | `1` |
| `source_subject_14_pasi_baseline` | `1` |
| `source_subject_14_sd_CL_L_day` | `1` |
| `source_subject_14_sd_Q_L_day` | `1` |
| `source_subject_14_sd_V2_L` | `1` |
| `source_subject_14_sd_V3_L` | `1` |
| `source_subject_14_sd_imax` | `1` |
| `source_subject_14_sd_ka_1_day` | `1` |
| `source_subject_14_sd_kout_1_day` | `1` |
| `source_subject_14_sd_kouttol_1_day` | `1` |
| `source_subject_14_sd_pasi_baseline` | `1` |
| `source_subject_14_tolerance_enabled` | `1` |
| `source_subject_15_CL_L_day` | `1` |
| `source_subject_15_F_sc_fraction` | `1` |
| `source_subject_15_Q_L_day` | `1` |
| `source_subject_15_V2_L` | `1` |
| `source_subject_15_V3_L` | `1` |
| `source_subject_15_bioavailability_pct` | `1` |
| `source_subject_15_ic50_mg_l` | `1` |
| `source_subject_15_imax` | `1` |
| `source_subject_15_ka_1_day` | `1` |
| `source_subject_15_kout_1_day` | `1` |
| `source_subject_15_kouttol_1_day` | `1` |
| `source_subject_15_pasi_baseline` | `1` |
| `source_subject_15_sd_CL_L_day` | `1` |
| `source_subject_15_sd_Q_L_day` | `1` |
| `source_subject_15_sd_V2_L` | `1` |
| `source_subject_15_sd_V3_L` | `1` |
| `source_subject_15_sd_imax` | `1` |
| `source_subject_15_sd_ka_1_day` | `1` |
| `source_subject_15_sd_kout_1_day` | `1` |
| `source_subject_15_sd_kouttol_1_day` | `1` |
| `source_subject_15_sd_pasi_baseline` | `1` |
| `source_subject_15_tolerance_enabled` | `1` |
| `source_subject_16_CL_L_day` | `1` |
| `source_subject_16_F_sc_fraction` | `1` |
| `source_subject_16_Q_L_day` | `1` |
| `source_subject_16_V2_L` | `1` |
| `source_subject_16_V3_L` | `1` |
| `source_subject_16_bioavailability_pct` | `1` |
| `source_subject_16_ic50_mg_l` | `1` |
| `source_subject_16_imax` | `1` |
| `source_subject_16_ka_1_day` | `1` |
| `source_subject_16_kout_1_day` | `1` |
| `source_subject_16_kouttol_1_day` | `1` |
| `source_subject_16_pasi_baseline` | `1` |
| `source_subject_16_sd_CL_L_day` | `1` |
| `source_subject_16_sd_Q_L_day` | `1` |
| `source_subject_16_sd_V2_L` | `1` |
| `source_subject_16_sd_V3_L` | `1` |
| `source_subject_16_sd_imax` | `1` |
| `source_subject_16_sd_ka_1_day` | `1` |
| `source_subject_16_sd_kout_1_day` | `1` |
| `source_subject_16_sd_kouttol_1_day` | `1` |
| `source_subject_16_sd_pasi_baseline` | `1` |
| `source_subject_16_tolerance_enabled` | `1` |
| `source_subject_17_CL_L_day` | `1` |
| `source_subject_17_F_sc_fraction` | `1` |
| `source_subject_17_Q_L_day` | `1` |
| `source_subject_17_V2_L` | `1` |
| `source_subject_17_V3_L` | `1` |
| `source_subject_17_bioavailability_pct` | `1` |
| `source_subject_17_ic50_mg_l` | `1` |
| `source_subject_17_imax` | `1` |
| `source_subject_17_ka_1_day` | `1` |
| `source_subject_17_kout_1_day` | `1` |
| `source_subject_17_kouttol_1_day` | `1` |
| `source_subject_17_pasi_baseline` | `1` |
| `source_subject_17_sd_CL_L_day` | `1` |
| `source_subject_17_sd_Q_L_day` | `1` |
| `source_subject_17_sd_V2_L` | `1` |
| `source_subject_17_sd_V3_L` | `1` |
| `source_subject_17_sd_imax` | `1` |
| `source_subject_17_sd_ka_1_day` | `1` |
| `source_subject_17_sd_kout_1_day` | `1` |
| `source_subject_17_sd_kouttol_1_day` | `1` |
| `source_subject_17_sd_pasi_baseline` | `1` |
| `source_subject_17_tolerance_enabled` | `1` |
| `source_subject_18_CL_L_day` | `1` |
| `source_subject_18_F_sc_fraction` | `1` |
| `source_subject_18_Q_L_day` | `1` |
| `source_subject_18_V2_L` | `1` |
| `source_subject_18_V3_L` | `1` |
| `source_subject_18_bioavailability_pct` | `1` |
| `source_subject_18_ic50_mg_l` | `1` |
| `source_subject_18_imax` | `1` |
| `source_subject_18_ka_1_day` | `1` |
| `source_subject_18_kout_1_day` | `1` |
| `source_subject_18_kouttol_1_day` | `1` |
| `source_subject_18_pasi_baseline` | `1` |
| `source_subject_18_sd_CL_L_day` | `1` |
| `source_subject_18_sd_Q_L_day` | `1` |
| `source_subject_18_sd_V2_L` | `1` |
| `source_subject_18_sd_V3_L` | `1` |
| `source_subject_18_sd_imax` | `1` |
| `source_subject_18_sd_ka_1_day` | `1` |
| `source_subject_18_sd_kout_1_day` | `1` |
| `source_subject_18_sd_kouttol_1_day` | `1` |
| `source_subject_18_sd_pasi_baseline` | `1` |
| `source_subject_18_tolerance_enabled` | `1` |
| `source_subject_1_CL_L_day` | `1` |
| `source_subject_1_F_sc_fraction` | `1` |
| `source_subject_1_Q_L_day` | `1` |
| `source_subject_1_V2_L` | `1` |
| `source_subject_1_V3_L` | `1` |
| `source_subject_1_bioavailability_pct` | `1` |
| `source_subject_1_ic50_mg_l` | `1` |
| `source_subject_1_imax` | `1` |
| `source_subject_1_ka_1_day` | `1` |
| `source_subject_1_kout_1_day` | `1` |
| `source_subject_1_kouttol_1_day` | `1` |
| `source_subject_1_pasi_baseline` | `1` |
| `source_subject_1_sd_CL_L_day` | `1` |
| `source_subject_1_sd_Q_L_day` | `1` |
| `source_subject_1_sd_V2_L` | `1` |
| `source_subject_1_sd_V3_L` | `1` |
| `source_subject_1_sd_imax` | `1` |
| `source_subject_1_sd_ka_1_day` | `1` |
| `source_subject_1_sd_kout_1_day` | `1` |
| `source_subject_1_sd_kouttol_1_day` | `1` |
| `source_subject_1_sd_pasi_baseline` | `1` |
| `source_subject_1_tolerance_enabled` | `1` |
| `source_subject_20_CL_L_day` | `1` |
| `source_subject_20_F_sc_fraction` | `1` |
| `source_subject_20_Q_L_day` | `1` |
| `source_subject_20_V2_L` | `1` |
| `source_subject_20_V3_L` | `1` |
| `source_subject_20_bioavailability_pct` | `1` |
| `source_subject_20_ic50_mg_l` | `1` |
| `source_subject_20_imax` | `1` |
| `source_subject_20_ka_1_day` | `1` |
| `source_subject_20_kout_1_day` | `1` |
| `source_subject_20_kouttol_1_day` | `1` |
| `source_subject_20_pasi_baseline` | `1` |
| `source_subject_20_sd_CL_L_day` | `1` |
| `source_subject_20_sd_Q_L_day` | `1` |
| `source_subject_20_sd_V2_L` | `1` |
| `source_subject_20_sd_V3_L` | `1` |
| `source_subject_20_sd_imax` | `1` |
| `source_subject_20_sd_ka_1_day` | `1` |
| `source_subject_20_sd_kout_1_day` | `1` |
| `source_subject_20_sd_kouttol_1_day` | `1` |
| `source_subject_20_sd_pasi_baseline` | `1` |
| `source_subject_20_tolerance_enabled` | `1` |
| `source_subject_21_CL_L_day` | `1` |
| `source_subject_21_F_sc_fraction` | `1` |
| `source_subject_21_Q_L_day` | `1` |
| `source_subject_21_V2_L` | `1` |
| `source_subject_21_V3_L` | `1` |
| `source_subject_21_bioavailability_pct` | `1` |
| `source_subject_21_ic50_mg_l` | `1` |
| `source_subject_21_imax` | `1` |
| `source_subject_21_ka_1_day` | `1` |
| `source_subject_21_kout_1_day` | `1` |
| `source_subject_21_kouttol_1_day` | `1` |
| `source_subject_21_pasi_baseline` | `1` |
| `source_subject_21_sd_CL_L_day` | `1` |
| `source_subject_21_sd_Q_L_day` | `1` |
| `source_subject_21_sd_V2_L` | `1` |
| `source_subject_21_sd_V3_L` | `1` |
| `source_subject_21_sd_imax` | `1` |
| `source_subject_21_sd_ka_1_day` | `1` |
| `source_subject_21_sd_kout_1_day` | `1` |
| `source_subject_21_sd_kouttol_1_day` | `1` |
| `source_subject_21_sd_pasi_baseline` | `1` |
| `source_subject_21_tolerance_enabled` | `1` |
| `source_subject_22_CL_L_day` | `1` |
| `source_subject_22_F_sc_fraction` | `1` |
| `source_subject_22_Q_L_day` | `1` |
| `source_subject_22_V2_L` | `1` |
| `source_subject_22_V3_L` | `1` |
| `source_subject_22_bioavailability_pct` | `1` |
| `source_subject_22_ic50_mg_l` | `1` |
| `source_subject_22_imax` | `1` |
| `source_subject_22_ka_1_day` | `1` |
| `source_subject_22_kout_1_day` | `1` |
| `source_subject_22_kouttol_1_day` | `1` |
| `source_subject_22_pasi_baseline` | `1` |
| `source_subject_22_sd_CL_L_day` | `1` |
| `source_subject_22_sd_Q_L_day` | `1` |
| `source_subject_22_sd_V2_L` | `1` |
| `source_subject_22_sd_V3_L` | `1` |
| `source_subject_22_sd_imax` | `1` |
| `source_subject_22_sd_ka_1_day` | `1` |
| `source_subject_22_sd_kout_1_day` | `1` |
| `source_subject_22_sd_kouttol_1_day` | `1` |
| `source_subject_22_sd_pasi_baseline` | `1` |
| `source_subject_22_tolerance_enabled` | `1` |
| `source_subject_23_CL_L_day` | `1` |
| `source_subject_23_F_sc_fraction` | `1` |
| `source_subject_23_Q_L_day` | `1` |
| `source_subject_23_V2_L` | `1` |
| `source_subject_23_V3_L` | `1` |
| `source_subject_23_bioavailability_pct` | `1` |
| `source_subject_23_ic50_mg_l` | `1` |
| `source_subject_23_imax` | `1` |
| `source_subject_23_ka_1_day` | `1` |
| `source_subject_23_kout_1_day` | `1` |
| `source_subject_23_kouttol_1_day` | `1` |
| `source_subject_23_pasi_baseline` | `1` |
| `source_subject_23_sd_CL_L_day` | `1` |
| `source_subject_23_sd_Q_L_day` | `1` |
| `source_subject_23_sd_V2_L` | `1` |
| `source_subject_23_sd_V3_L` | `1` |
| `source_subject_23_sd_imax` | `1` |
| `source_subject_23_sd_ka_1_day` | `1` |
| `source_subject_23_sd_kout_1_day` | `1` |
| `source_subject_23_sd_kouttol_1_day` | `1` |
| `source_subject_23_sd_pasi_baseline` | `1` |
| `source_subject_23_tolerance_enabled` | `1` |
| `source_subject_24_CL_L_day` | `1` |
| `source_subject_24_F_sc_fraction` | `1` |
| `source_subject_24_Q_L_day` | `1` |
| `source_subject_24_V2_L` | `1` |
| `source_subject_24_V3_L` | `1` |
| `source_subject_24_bioavailability_pct` | `1` |
| `source_subject_24_ic50_mg_l` | `1` |
| `source_subject_24_imax` | `1` |
| `source_subject_24_ka_1_day` | `1` |
| `source_subject_24_kout_1_day` | `1` |
| `source_subject_24_kouttol_1_day` | `1` |
| `source_subject_24_pasi_baseline` | `1` |
| `source_subject_24_sd_CL_L_day` | `1` |
| `source_subject_24_sd_Q_L_day` | `1` |
| `source_subject_24_sd_V2_L` | `1` |
| `source_subject_24_sd_V3_L` | `1` |
| `source_subject_24_sd_imax` | `1` |
| `source_subject_24_sd_ka_1_day` | `1` |
| `source_subject_24_sd_kout_1_day` | `1` |
| `source_subject_24_sd_kouttol_1_day` | `1` |
| `source_subject_24_sd_pasi_baseline` | `1` |
| `source_subject_24_tolerance_enabled` | `1` |
| `source_subject_2_CL_L_day` | `1` |
| `source_subject_2_F_sc_fraction` | `1` |
| `source_subject_2_Q_L_day` | `1` |
| `source_subject_2_V2_L` | `1` |
| `source_subject_2_V3_L` | `1` |
| `source_subject_2_bioavailability_pct` | `1` |
| `source_subject_2_ic50_mg_l` | `1` |
| `source_subject_2_imax` | `1` |
| `source_subject_2_ka_1_day` | `1` |
| `source_subject_2_kout_1_day` | `1` |
| `source_subject_2_kouttol_1_day` | `1` |
| `source_subject_2_pasi_baseline` | `1` |
| `source_subject_2_sd_CL_L_day` | `1` |
| `source_subject_2_sd_Q_L_day` | `1` |
| `source_subject_2_sd_V2_L` | `1` |
| `source_subject_2_sd_V3_L` | `1` |
| `source_subject_2_sd_imax` | `1` |
| `source_subject_2_sd_ka_1_day` | `1` |
| `source_subject_2_sd_kout_1_day` | `1` |
| `source_subject_2_sd_kouttol_1_day` | `1` |
| `source_subject_2_sd_pasi_baseline` | `1` |
| `source_subject_2_tolerance_enabled` | `1` |
| `source_subject_3_CL_L_day` | `1` |
| `source_subject_3_F_sc_fraction` | `1` |
| `source_subject_3_Q_L_day` | `1` |
| `source_subject_3_V2_L` | `1` |
| `source_subject_3_V3_L` | `1` |
| `source_subject_3_bioavailability_pct` | `1` |
| `source_subject_3_ic50_mg_l` | `1` |
| `source_subject_3_imax` | `1` |
| `source_subject_3_ka_1_day` | `1` |
| `source_subject_3_kout_1_day` | `1` |
| `source_subject_3_kouttol_1_day` | `1` |
| `source_subject_3_pasi_baseline` | `1` |
| `source_subject_3_sd_CL_L_day` | `1` |
| `source_subject_3_sd_Q_L_day` | `1` |
| `source_subject_3_sd_V2_L` | `1` |
| `source_subject_3_sd_V3_L` | `1` |
| `source_subject_3_sd_imax` | `1` |
| `source_subject_3_sd_ka_1_day` | `1` |
| `source_subject_3_sd_kout_1_day` | `1` |
| `source_subject_3_sd_kouttol_1_day` | `1` |
| `source_subject_3_sd_pasi_baseline` | `1` |
| `source_subject_3_tolerance_enabled` | `1` |
| `source_subject_4_CL_L_day` | `1` |
| `source_subject_4_F_sc_fraction` | `1` |
| `source_subject_4_Q_L_day` | `1` |
| `source_subject_4_V2_L` | `1` |
| `source_subject_4_V3_L` | `1` |
| `source_subject_4_bioavailability_pct` | `1` |
| `source_subject_4_ic50_mg_l` | `1` |
| `source_subject_4_imax` | `1` |
| `source_subject_4_ka_1_day` | `1` |
| `source_subject_4_kout_1_day` | `1` |
| `source_subject_4_kouttol_1_day` | `1` |
| `source_subject_4_pasi_baseline` | `1` |
| `source_subject_4_sd_CL_L_day` | `1` |
| `source_subject_4_sd_Q_L_day` | `1` |
| `source_subject_4_sd_V2_L` | `1` |
| `source_subject_4_sd_V3_L` | `1` |
| `source_subject_4_sd_imax` | `1` |
| `source_subject_4_sd_ka_1_day` | `1` |
| `source_subject_4_sd_kout_1_day` | `1` |
| `source_subject_4_sd_kouttol_1_day` | `1` |
| `source_subject_4_sd_pasi_baseline` | `1` |
| `source_subject_4_tolerance_enabled` | `1` |
| `source_subject_5_CL_L_day` | `1` |
| `source_subject_5_F_sc_fraction` | `1` |
| `source_subject_5_Q_L_day` | `1` |
| `source_subject_5_V2_L` | `1` |
| `source_subject_5_V3_L` | `1` |
| `source_subject_5_bioavailability_pct` | `1` |
| `source_subject_5_ic50_mg_l` | `1` |
| `source_subject_5_imax` | `1` |
| `source_subject_5_ka_1_day` | `1` |
| `source_subject_5_kout_1_day` | `1` |
| `source_subject_5_kouttol_1_day` | `1` |
| `source_subject_5_pasi_baseline` | `1` |
| `source_subject_5_sd_CL_L_day` | `1` |
| `source_subject_5_sd_Q_L_day` | `1` |
| `source_subject_5_sd_V2_L` | `1` |
| `source_subject_5_sd_V3_L` | `1` |
| `source_subject_5_sd_imax` | `1` |
| `source_subject_5_sd_ka_1_day` | `1` |
| `source_subject_5_sd_kout_1_day` | `1` |
| `source_subject_5_sd_kouttol_1_day` | `1` |
| `source_subject_5_sd_pasi_baseline` | `1` |
| `source_subject_5_tolerance_enabled` | `1` |
| `source_subject_6_CL_L_day` | `1` |
| `source_subject_6_F_sc_fraction` | `1` |
| `source_subject_6_Q_L_day` | `1` |
| `source_subject_6_V2_L` | `1` |
| `source_subject_6_V3_L` | `1` |
| `source_subject_6_bioavailability_pct` | `1` |
| `source_subject_6_ic50_mg_l` | `1` |
| `source_subject_6_imax` | `1` |
| `source_subject_6_ka_1_day` | `1` |
| `source_subject_6_kout_1_day` | `1` |
| `source_subject_6_kouttol_1_day` | `1` |
| `source_subject_6_pasi_baseline` | `1` |
| `source_subject_6_sd_CL_L_day` | `1` |
| `source_subject_6_sd_Q_L_day` | `1` |
| `source_subject_6_sd_V2_L` | `1` |
| `source_subject_6_sd_V3_L` | `1` |
| `source_subject_6_sd_imax` | `1` |
| `source_subject_6_sd_ka_1_day` | `1` |
| `source_subject_6_sd_kout_1_day` | `1` |
| `source_subject_6_sd_kouttol_1_day` | `1` |
| `source_subject_6_sd_pasi_baseline` | `1` |
| `source_subject_6_tolerance_enabled` | `1` |
| `source_subject_7_CL_L_day` | `1` |
| `source_subject_7_F_sc_fraction` | `1` |
| `source_subject_7_Q_L_day` | `1` |
| `source_subject_7_V2_L` | `1` |
| `source_subject_7_V3_L` | `1` |
| `source_subject_7_bioavailability_pct` | `1` |
| `source_subject_7_ic50_mg_l` | `1` |
| `source_subject_7_imax` | `1` |
| `source_subject_7_ka_1_day` | `1` |
| `source_subject_7_kout_1_day` | `1` |
| `source_subject_7_kouttol_1_day` | `1` |
| `source_subject_7_pasi_baseline` | `1` |
| `source_subject_7_sd_CL_L_day` | `1` |
| `source_subject_7_sd_Q_L_day` | `1` |
| `source_subject_7_sd_V2_L` | `1` |
| `source_subject_7_sd_V3_L` | `1` |
| `source_subject_7_sd_imax` | `1` |
| `source_subject_7_sd_ka_1_day` | `1` |
| `source_subject_7_sd_kout_1_day` | `1` |
| `source_subject_7_sd_kouttol_1_day` | `1` |
| `source_subject_7_sd_pasi_baseline` | `1` |
| `source_subject_7_tolerance_enabled` | `1` |
| `source_subject_8_CL_L_day` | `1` |
| `source_subject_8_F_sc_fraction` | `1` |
| `source_subject_8_Q_L_day` | `1` |
| `source_subject_8_V2_L` | `1` |
| `source_subject_8_V3_L` | `1` |
| `source_subject_8_bioavailability_pct` | `1` |
| `source_subject_8_ic50_mg_l` | `1` |
| `source_subject_8_imax` | `1` |
| `source_subject_8_ka_1_day` | `1` |
| `source_subject_8_kout_1_day` | `1` |
| `source_subject_8_kouttol_1_day` | `1` |
| `source_subject_8_pasi_baseline` | `1` |
| `source_subject_8_sd_CL_L_day` | `1` |
| `source_subject_8_sd_Q_L_day` | `1` |
| `source_subject_8_sd_V2_L` | `1` |
| `source_subject_8_sd_V3_L` | `1` |
| `source_subject_8_sd_imax` | `1` |
| `source_subject_8_sd_ka_1_day` | `1` |
| `source_subject_8_sd_kout_1_day` | `1` |
| `source_subject_8_sd_kouttol_1_day` | `1` |
| `source_subject_8_sd_pasi_baseline` | `1` |
| `source_subject_8_tolerance_enabled` | `1` |
| `source_subject_9_CL_L_day` | `1` |
| `source_subject_9_F_sc_fraction` | `1` |
| `source_subject_9_Q_L_day` | `1` |
| `source_subject_9_V2_L` | `1` |
| `source_subject_9_V3_L` | `1` |
| `source_subject_9_bioavailability_pct` | `1` |
| `source_subject_9_ic50_mg_l` | `1` |
| `source_subject_9_imax` | `1` |
| `source_subject_9_ka_1_day` | `1` |
| `source_subject_9_kout_1_day` | `1` |
| `source_subject_9_kouttol_1_day` | `1` |
| `source_subject_9_pasi_baseline` | `1` |
| `source_subject_9_sd_CL_L_day` | `1` |
| `source_subject_9_sd_Q_L_day` | `1` |
| `source_subject_9_sd_V2_L` | `1` |
| `source_subject_9_sd_V3_L` | `1` |
| `source_subject_9_sd_imax` | `1` |
| `source_subject_9_sd_ka_1_day` | `1` |
| `source_subject_9_sd_kout_1_day` | `1` |
| `source_subject_9_sd_kouttol_1_day` | `1` |
| `source_subject_9_sd_pasi_baseline` | `1` |
| `source_subject_9_tolerance_enabled` | `1` |
| `source_table2_bioavailability_pct` | `1` |
| `source_table2_ic50_fixed_flag` | `1` |
| `source_table2_ic50_mg_l` | `1` |
| `source_table2_iiv_imax_pct` | `1` |
| `source_table2_iiv_imax_rse_pct` | `1` |
| `source_table2_iiv_kout_pct` | `1` |
| `source_table2_iiv_kout_rse_pct` | `1` |
| `source_table2_iiv_kouttol_pct` | `1` |
| `source_table2_iiv_kouttol_rse_pct` | `1` |
| `source_table2_imax` | `1` |
| `source_table2_imax_rse_pct` | `1` |
| `source_table2_intensified_patient_count` | `1` |
| `source_table2_intensified_patient_pct` | `1` |
| `source_table2_kout_1_day` | `1` |
| `source_table2_kout_rse_pct` | `1` |
| `source_table2_kouttol_1_day` | `1` |
| `source_table2_kouttol_rse_pct` | `1` |
| `source_table2_nonresponder_patient_count` | `1` |
| `source_table2_nonresponder_patient_pct` | `1` |
| `source_table2_optimized_patient_count` | `1` |
| `source_table2_optimized_patient_pct` | `1` |
| `source_table2_pasi_observation_count` | `1` |
| `source_table2_pasi_target_probability_pct` | `1` |
| `source_table2_pasi_target_score` | `1` |
| `source_table2_patient_count` | `1` |
| `source_table2_ruv_error_pct` | `1` |
| `source_table2_ruv_error_rse_pct` | `1` |
| `source_table2_sck_concentration_count` | `1` |
| `source_table2_tolerance_patient_count` | `1` |
| `source_table2_trough_target_high_mg_l` | `1` |
| `source_table2_trough_target_low_mg_l` | `1` |
| `source_table2_unchanged_patient_count` | `1` |
| `source_table2_unchanged_patient_pct` | `1` |
| `source_tolerance_enabled` | `1` |
| `steady_state_trough_target_mid_mg_l` | `1` |
| `tolerance_drive` | `1` |
| `state__AUC_conc_day` | `mg*day/L` |
| `state__A_central_mg` | `mg` |
| `state__A_depot_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_day` | `day` |
| `state__pasi` | `score` |
| `state__pre_pasi1` | `score` |
| `state__pre_pasi2` | `score` |
| `state__pre_pasi3` | `score` |
| `state__pre_pasi4` | `score` |
| `state__tol1` | `dimensionless` |
| `state__tol2` | `dimensionless` |
| `state__tol3` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `subject1-300mg-q4w-20cycle-ode-probe` starter has **89 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_mg_l` | 0 | 0 (0 h, post) | 106.321 (35 h, post) | 39.543 |
| `drug_effect_fraction` | 0 | 0 (0 h, post) | 1.07543 (35 h, post) | 0.946256 |
| `pasi_target_gap` | 6.05 | -1.49535 (42 h, post) | 6.05 (0 h, post) | -0.893571 |

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
Evidence identity: `sha256:8515fce7181cd9be2467882ee46c4d351c21ef9be2a8b2efa2fb05785ba70f7f`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Full public ODE reconstruction of the secukinumab plaque-psoriasis MIPD PK/PD model: SC depot, two-compartment linear PK, four-compartment prePASI indirect response, and source-limited three-compartment tolerance scaffold.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
