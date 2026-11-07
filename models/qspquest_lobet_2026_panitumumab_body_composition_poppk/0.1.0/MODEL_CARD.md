# Lobet 2026 panitumumab body-composition PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore panitumumab exposure with body-composition covariates.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.1.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_lobet_2026_panitumumab_body_composition_poppk/0.1.0/model.omex',
    expected_sha256='a2d56b907079b5574035d2a2519814835d97295b261fbf54591436023a79800d',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Archived experiment ID | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-source-anchor` | No-dose exact replay of Table 1, Table 2, Supplement Table S1, and Results scalar values. | 0–0.001 h | 2 |
| `ffcd0904-typical-3mgkg-q2w-ode-overlay` | Deterministic typical-subject ODE using median 62 kg body weight and Table 2 fixed effects; paper AUC0-14 median/range is carried as comparator data. | 0–70 h | 281 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `central_conc_mg_l` | Panitumumab concentration | `1` |
| `auc_mg_day_l` | Accumulated panitumumab exposure | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 9 outputs and 4 states</summary>

| Technical column | Unit |
| --- | --- |
| `auc_mg_day_l` | `1` |
| `central_conc_mg_l` | `1` |
| `dose_mg` | `1` |
| `linear_elimination_mg_day` | `1` |
| `michaelis_menten_elimination_mg_day` | `1` |
| `paper_auc0_14_median_mg_day_l` | `1` |
| `paper_auc0_14_p05_mg_day_l` | `1` |
| `paper_auc0_14_p95_mg_day_l` | `1` |
| `peripheral_conc_mg_l` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `ffcd0904-typical-3mgkg-q2w-ode-overlay` starter has **281 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_l` | 74.1036 | 0.0547415 (14 h, pre) | 74.1036 (0 h, post) | 1.91396 |
| `auc_mg_day_l` | 0 | 0 (0 h, post) | 1462.26 (70 h, pre) | 1462.26 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
