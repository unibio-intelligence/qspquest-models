# Shemesh 2019 Atezolizumab Pediatric and Young Adult PopPK/Safety Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore atezolizumab exposure and safety summaries in younger populations.

**Runnable · 16 experiments.** Version 0.1.1.

This is an alternate version. [Open the default version](../0.2.1/MODEL_CARD.md) for the standard quickstart.

## Run an experiment

Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import load_archive

model = load_archive(
    'models/qspquest_shemesh_2019_atezolizumab_pediatric_poppk_safety/0.1.1/model.omex',
    expected_sha256='c32211635cafec31b6dd90bd20d16302925abc7aaa29b068e1d92febe697ad88',
)
result = model.run('adolescent-ge45kg-15mgkg-q3w-source-limited')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 16 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `adolescent-ge45kg-15mgkg-q3w-source-limited` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `child-lt30kg-15mgkg-q3w-source-limited` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `infant-lt2-15mgkg-q3w-figure2-source-limited` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-at-cap` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-below-cap` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-child-ada-positive` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-high-albumin` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-high-tumor-burden` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-high-weight-pediatric` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-high-weight-young-adult` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-infant-low-weight` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-low-albumin` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-low-tumor-burden` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-reference-covariates` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `source-review-young-adult-ada-positive` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |
| `young-adult-57to65kg-1200mg-q3w-source-limited` | Fixed-effect projection using published coefficients. Covariate combinations are diagnostic subjects, not reconstructed patients or cohort medians. Dose amounts are fixed in this scenario: recompute the regimen when editing weight. Pediatric dose=min(15 mg/kg,1200 mg); age>=18 dose=1200 mg. No age effect in the final PK equations. | 0–210 d | 1429 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `C_central_ug_mL` | Atezolizumab concentration | `1` |
| `AUC_ug_day_mL` | Accumulated central drug exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

Use the checksum-pinned Python archive command above for this version. The library CLI selects the current default archive.

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 9 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_ug_day_mL` | `1` |
| `CL_L_day` | `1` |
| `C_central_ug_mL` | `1` |
| `V1_L` | `1` |
| `V2_L` | `1` |
| `central_to_peripheral_mg_day` | `1` |
| `elimination_mg_day` | `1` |
| `instantaneous_above_target_flag` | `1` |
| `peripheral_to_central_mg_day` | `1` |
| `state__AUC_ug_day_mL` | `ug*day/mL` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__elapsed_time_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `adolescent-ge45kg-15mgkg-q3w-source-limited` starter has **1429 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `C_central_ug_mL` | 0 | 0 (0 d, post) | 481.978 (189.021 d, pre) | 129.189 |
| `AUC_ug_day_mL` | 0 | 0 (0 d, post) | 45739.8 (210 d, pre) | 45739.8 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
