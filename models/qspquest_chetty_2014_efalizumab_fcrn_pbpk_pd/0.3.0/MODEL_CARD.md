# Efalizumab PASI time course: source-partial model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect efalizumab FcRn distribution and pharmacodynamic evidence replays.

**Runnable · 4 experiments.** Version 0.3.0.

## Run an experiment

Reduced first-order progression from Gordon baseline PASI toward Chetty source Yss. This is not a Simcyp virtual-population reproduction.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_chetty_2014_efalizumab_fcrn_pbpk_pd', version='0.3.0')
result = model.run('gordon-1mgkg-pasi-progression-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exploratory-calibrated-gordon-digitized-pasi-probe` | Exploratory calibrated reduced PASI ODE fit to digitized Chetty Figure 4 points. This is not the paper fixed-effect Simcyp/FcRn model. | 0–2016 h | 85 |
| `exploratory-calibrated-gottlieb-digitized-pasi-probe` | Exploratory calibrated reduced PASI ODE fit to digitized Chetty Figure 4 points. This is not the paper fixed-effect Simcyp/FcRn model. | 0–1344 h | 57 |
| `gordon-1mgkg-pasi-progression-probe` | Reduced first-order progression from Gordon baseline PASI toward Chetty source Yss. This is not a Simcyp virtual-population reproduction. | 0–2016 h | 85 |
| `gottlieb-escalating-pasi-progression-probe` | Reduced first-order progression from Gottlieb baseline PASI toward Chetty source Yss. This is not a Simcyp virtual-population reproduction. | 0–1344 h | 57 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `PASI_current` | Psoriasis severity score in the progression probe | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_chetty_2014_efalizumab_fcrn_pbpk_pd --model-version 0.3.0 --scenario gordon-1mgkg-pasi-progression-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 75 outputs and 2 states</summary>

| Technical column | Unit |
| --- | --- |
| `CLiv_CV_pct` | `1` |
| `CLiv_L_h` | `1` |
| `MM_Km_uM` | `1` |
| `PASI_current` | `1` |
| `Tp_h` | `1` |
| `Yss_current_PASI` | `1` |
| `cd11a_Kdeg_CV_pct` | `1` |
| `cd11a_Kdeg_h` | `1` |
| `cd11a_Ksyn_from_Rmax_Kdeg_uM_h` | `1` |
| `cd11a_Ksyn_uM_h` | `1` |
| `cd11a_Rmax_uM` | `1` |
| `cd11a_mw_Da` | `1` |
| `cd11a_typical_suppressed_pct_baseline` | `1` |
| `complex_Kint_L_h` | `1` |
| `dose_10_mg_kg` | `1` |
| `dose_1_mg_kg` | `1` |
| `dose_3_mg_kg` | `1` |
| `efalizumab_mw_g_mol` | `1` |
| `elapsed_h` | `1` |
| `escalation_week1_mg_kg` | `1` |
| `escalation_week2_mg_kg` | `1` |
| `escalation_week3_mg_kg` | `1` |
| `escalation_week4_to_7_mg_kg` | `1` |
| `fcrn_KD_uM` | `1` |
| `gordon_PASI_reduction_to_Yss_pct` | `1` |
| `gordon_Yss_PASI` | `1` |
| `gordon_baseline_PASI` | `1` |
| `gordon_expected_PASI_reduction_high_pct` | `1` |
| `gordon_expected_PASI_reduction_low_pct` | `1` |
| `gottlieb_PASI_reduction_to_Yss_pct` | `1` |
| `gottlieb_Yss_PASI` | `1` |
| `gottlieb_Yss_PASI_CV_pct` | `1` |
| `gottlieb_baseline_PASI` | `1` |
| `gottlieb_baseline_PASI_CV_pct` | `1` |
| `infusion_duration_h` | `1` |
| `maintenance_weeks_after_week3` | `1` |
| `ng_weekly_dose_mg_kg` | `1` |
| `observed_CL_10_mgkg_mL_day_kg` | `1` |
| `observed_CL_10_mgkg_single_subject_flag` | `1` |
| `observed_CL_1_mgkg_high_mL_day_kg` | `1` |
| `observed_CL_1_mgkg_low_mL_day_kg` | `1` |
| `observed_CL_1_mgkg_mL_day_kg` | `1` |
| `observed_CL_3_mgkg_high_mL_day_kg` | `1` |
| `observed_CL_3_mgkg_low_mL_day_kg` | `1` |
| `observed_CL_3_mgkg_mL_day_kg` | `1` |
| `pasi_progression_rate_h` | `1` |
| `predicted_CL_TMDD_10_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_TMDD_10_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_TMDD_10_mgkg_mL_day_kg` | `1` |
| `predicted_CL_TMDD_1_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_TMDD_1_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_TMDD_1_mgkg_mL_day_kg` | `1` |
| `predicted_CL_TMDD_3_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_TMDD_3_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_TMDD_3_mgkg_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_10_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_10_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_10_mgkg_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_1_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_1_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_1_mgkg_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_3_mgkg_high_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_3_mgkg_low_mL_day_kg` | `1` |
| `predicted_CL_no_TMDD_3_mgkg_mL_day_kg` | `1` |
| `prediction_interval_high_pct` | `1` |
| `prediction_interval_low_pct` | `1` |
| `published_year` | `1` |
| `simulation_trials_n` | `1` |
| `table2_tmdd_clearance_increment_10_mgkg` | `1` |
| `table2_tmdd_clearance_increment_1_mgkg` | `1` |
| `table2_tmdd_clearance_increment_3_mgkg` | `1` |
| `total_virtual_subjects_n` | `1` |
| `virtual_age_max_year` | `1` |
| `virtual_age_min_year` | `1` |
| `virtual_subjects_per_trial_n` | `1` |
| `state__PASI_score` | `score` |
| `state__elapsed_h` | `h` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `gordon-1mgkg-pasi-progression-probe` starter has **85 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `PASI_current` | 19 | 9.78123 (2016 h, pre) | 19 (0 h, post) | 9.78123 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
