# Lee 2024 SB12/eculizumab biosimilar PopPK/PD/efficacy

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed SB12/eculizumab exposure and pharmacodynamic comparisons.

**Runnable · 5 experiments.** Version 0.1.0.

## Run an experiment

Full regimen through week 50, observed through week 52. Bolus approximation: PNH infusion duration is not specified in this paper; do not qualify peak concentrations.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_lee_2024_sb12_eculizumab_biosimilar_poppkpd', version='0.1.0')
result = model.run('pnh-labeled-regimen-dynamic-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-table-anchor` | No-dose replay exposing Article Tables 3-5, Supplement Tables A1-A2, cohort/dosing counts, and discussion threshold values. | 0–0.001 h | 2 |
| `healthy-300mg-iv-single-dose-dynamic-overlay` | Typical-subject 35-minute infusion; 0.58 h in Table 1 is rounded. Healthy LDH is outside the patient-only efficacy model. | 0–1512 h | 130 |
| `healthy-82-4kg-phase1` | Typical-subject 35-minute infusion; 0.58 h in Table 1 is rounded. Healthy LDH is outside the patient-only efficacy model. | 0–1512 h | 130 |
| `pnh-63kg-phase3` | Full regimen through week 50, observed through week 52. Bolus approximation: PNH infusion duration is not specified in this paper; do not qualify peak concentrations. | 0–8736 h | 729 |
| `pnh-labeled-regimen-dynamic-overlay` | Full regimen through week 50, observed through week 52. Bolus approximation: PNH infusion duration is not specified in this paper; do not qualify peak concentrations. | 0–8736 h | 729 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ug_ml` | Eculizumab or SB12 concentration | `1` |
| `terminal_complement_activity_pct` | Terminal complement activity | `1` |
| `ldh_u_l` | Lactate dehydrogenase activity | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_lee_2024_sb12_eculizumab_biosimilar_poppkpd --model-version 0.1.0 --scenario pnh-labeled-regimen-dynamic-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 73 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `body_weight_kg` | `1` |
| `central_conc_ug_ml` | `1` |
| `cl_l_h` | `1` |
| `complete_inhibition_high_ug_ml` | `1` |
| `complete_inhibition_low_ug_ml` | `1` |
| `ema_complete_inhibition_ug_ml` | `1` |
| `healthy_single_dose_mg` | `1` |
| `healthy_subjects_n` | `1` |
| `healthy_table_a1_cl_l_h` | `1` |
| `healthy_table_a1_cl_weight_exponent` | `1` |
| `healthy_table_a1_q_l_h` | `1` |
| `healthy_table_a1_vc_l` | `1` |
| `healthy_table_a1_vc_weight_exponent` | `1` |
| `healthy_table_a1_vp_l` | `1` |
| `healthy_table_a2_baseline_effect_on_ic50` | `1` |
| `healthy_table_a2_e0_pct` | `1` |
| `healthy_table_a2_hill` | `1` |
| `healthy_table_a2_ic50_ug_ml` | `1` |
| `healthy_table_a2_imax_fraction` | `1` |
| `ic50_085_multiple_ug_ml` | `1` |
| `ldh_iiv_lgam_pct` | `1` |
| `ldh_iiv_ll0_pct` | `1` |
| `ldh_iiv_lmax_pct` | `1` |
| `ldh_lc50_pct` | `1` |
| `ldh_lgam` | `1` |
| `ldh_ll0_u_l` | `1` |
| `ldh_lmax_u_l` | `1` |
| `ldh_prop_error_pct` | `1` |
| `ldh_u_l` | `1` |
| `pd_e0_healthy_pct` | `1` |
| `pd_e0_pct` | `1` |
| `pd_e0_pnh_pct` | `1` |
| `pd_hill` | `1` |
| `pd_ic50_ug_ml` | `1` |
| `pd_iiv_e0_pct` | `1` |
| `pd_iiv_ic50_pct` | `1` |
| `pd_iiv_imax_pct` | `1` |
| `pd_imax_fraction` | `1` |
| `pd_imax_healthy_fraction` | `1` |
| `pd_imax_pnh_fraction` | `1` |
| `pd_prop_error_pct` | `1` |
| `peripheral_conc_ug_ml` | `1` |
| `pk_cl_l_h` | `1` |
| `pk_cl_weight_exponent` | `1` |
| `pk_corr_cl_vc` | `1` |
| `pk_iiv_cl_pct` | `1` |
| `pk_iiv_vc_pct` | `1` |
| `pk_iiv_vp_pct` | `1` |
| `pk_prop_error_pct` | `1` |
| `pk_q_l_h` | `1` |
| `pk_vc_healthy_l` | `1` |
| `pk_vc_pnh_l` | `1` |
| `pk_vc_weight_exponent` | `1` |
| `pk_vp_l` | `1` |
| `pk_weight_ref_kg` | `1` |
| `pnh_initial_weekly_dose_mg` | `1` |
| `pnh_initial_weekly_doses_n` | `1` |
| `pnh_maintenance_dose_mg` | `1` |
| `pnh_maintenance_interval_h` | `1` |
| `pnh_patient_flag` | `1` |
| `pnh_patients_n` | `1` |
| `pnh_week5_dose_mg` | `1` |
| `publication_year` | `1` |
| `queue_citation_rank` | `1` |
| `queue_cited_by_count` | `1` |
| `queue_refined_rank` | `1` |
| `subjects_total_n` | `1` |
| `terminal_beta_h` | `1` |
| `terminal_complement_activity_pct` | `1` |
| `terminal_half_life_h` | `1` |
| `validation_run_nonce` | `1` |
| `vc_l` | `1` |
| `weight_ratio` | `1` |
| `state__auc_ug_h_ml` | `ug*h/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_h` | `h` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `pnh-labeled-regimen-dynamic-overlay` starter has **729 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ug_ml` | 105.634 | 57.4541 (168 h, pre) | 277.228 (684 h, post) | 93.4174 |
| `terminal_complement_activity_pct` | 12.8219 | 12.1287 (684 h, post) | 22.2007 (168 h, pre) | 13.3421 |
| `ldh_u_l` | 219.942 | 216.997 (684 h, post) | 342.84 (168 h, pre) | 222.516 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

- No original population fit or individual clinical predictions.
- PNH infusion duration is unavailable: conditional bolus simulations cannot qualify Cmax.
- Healthy-volunteer LDH is outside the patient-only efficacy relation.
- Static source anchors are archival observations, not independent numerical simulation validation.

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:78c1c8121f98863a09aa99bb4cacafdc24f82a057b366ba81e71533ca0daa2d4`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

- How does exposure relate to terminal complement inhibition under this fixed-effect regimen?

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
