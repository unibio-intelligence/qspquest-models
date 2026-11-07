# Shemesh 2019 Atezolizumab Pediatric and Young Adult PopPK/Safety Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore atezolizumab exposure and safety summaries in younger populations.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.1.

This is an alternate version. [Open the default version](../0.2.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_shemesh_2019_atezolizumab_pediatric_poppk_safety/0.1.1/model.omex',
    expected_sha256='c32211635cafec31b6dd90bd20d16302925abc7aaa29b068e1d92febe697ad88',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

<details>
<summary>Browse all 16 runnable experiments</summary>

| Archived experiment ID | Purpose | Time range | Rows |
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

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `C_central_ug_mL` | Atezolizumab concentration | `1` |
| `AUC_ug_day_mL` | Accumulated central drug exposure | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 9 outputs and 4 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `adolescent-ge45kg-15mgkg-q3w-source-limited` starter has **1429 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `C_central_ug_mL` | 0 | 0 (0 d, post) | 481.978 (189.021 d, pre) | 129.189 |
| `AUC_ug_day_mL` | 0 | 0 (0 d, post) | 45739.8 (210 d, pre) | 45739.8 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
