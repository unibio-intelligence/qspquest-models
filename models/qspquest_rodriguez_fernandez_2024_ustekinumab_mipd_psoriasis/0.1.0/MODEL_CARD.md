# Rodriguez-Fernandez 2024 Ustekinumab MIPD Psoriasis PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed ustekinumab exposure and psoriasis-response scenarios.

**Runnable · 3 experiments · 1 unavailable.** Version 0.1.0.

## Run an experiment

Source-limited deterministic ODE probe using Supplementary Table S1 patient 18, a high-clearance/low-kout patient, under 90 mg q8w intensified dosing.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_rodriguez_fernandez_2024_ustekinumab_mipd_psoriasis', version='0.1.0')
result = model.run('patient18-90mg-q8w-intensified-probe')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `patient18-90mg-q8w-intensified-probe` | Source-limited deterministic ODE probe using Supplementary Table S1 patient 18, a high-clearance/low-kout patient, under 90 mg q8w intensified dosing. | 0–616 d | 617 |
| `si-patient1-parameter-anchor` | No-dose exact replay of one representative patient's individual parameter means. The validator checks all 23 SI patient rows via overrides. | 0–0.001 d | 2 |
| `table2-population-pd-anchor` | No-dose exact replay of main-text Table 2 PD estimates, cohort counts, MIPD category counts, and the Figure 6 trough/PASI target statement. | 0–0.001 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_concentration_mg_l` | Ustekinumab concentration | `1` |
| `drug_effect_fraction` | Fractional drug effect on psoriasis response | `1` |
| `pasi_target_gap` | Difference from the model psoriasis response target | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_rodriguez_fernandez_2024_ustekinumab_mipd_psoriasis --model-version 0.1.0 --scenario patient18-90mg-q8w-intensified-probe --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 40 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `bioavailability_fraction` | `1` |
| `central_concentration_mg_l` | `1` |
| `drug_effect_fraction` | `1` |
| `intercompartmental_flux_mg_day` | `1` |
| `kin_pasi_day` | `1` |
| `linear_elimination_mg_day` | `1` |
| `pasi_target_gap` | `1` |
| `peripheral_concentration_mg_l` | `1` |
| `source_bioavailability_pct` | `1` |
| `source_cl_l_d` | `1` |
| `source_ic50_mg_l` | `1` |
| `source_imax` | `1` |
| `source_intensified_patient_count` | `1` |
| `source_intensified_patient_pct` | `1` |
| `source_ka_d` | `1` |
| `source_kout_d` | `1` |
| `source_nonresponder_patient_count` | `1` |
| `source_nonresponder_patient_pct` | `1` |
| `source_optimized_patient_count` | `1` |
| `source_optimized_patient_pct` | `1` |
| `source_pasi_baseline` | `1` |
| `source_pasi_observation_count` | `1` |
| `source_pasi_target_probability_pct` | `1` |
| `source_pasi_target_score` | `1` |
| `source_patient_count` | `1` |
| `source_q_l_d` | `1` |
| `source_table2_imax_rse_pct` | `1` |
| `source_table2_kout_iiv_pct` | `1` |
| `source_table2_kout_iiv_rse_pct` | `1` |
| `source_table2_kout_rse_pct` | `1` |
| `source_table2_ruv_error_pct` | `1` |
| `source_table2_ruv_error_rse_pct` | `1` |
| `source_trough_target_high_mg_l` | `1` |
| `source_trough_target_low_mg_l` | `1` |
| `source_unchanged_patient_count` | `1` |
| `source_unchanged_patient_pct` | `1` |
| `source_utk_concentration_count` | `1` |
| `source_v2_l` | `1` |
| `source_v3_l` | `1` |
| `steady_state_trough_target_mid_mg_l` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__pasi` | `score` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `patient18-90mg-q8w-intensified-probe` starter has **617 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_concentration_mg_l` | 0 | 0 (0 d, post) | 7.59224 (35 d, post) | 1.1789 |
| `drug_effect_fraction` | 0 | 0 (0 d, post) | 0.959157 (35 d, post) | 0.913744 |
| `pasi_target_gap` | 17.845 | 0.328356 (606 d, post) | 17.845 (0 d, post) | 0.338366 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**1 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
