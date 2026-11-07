# Drug-stimulated biomarker turnover

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore how repeated exposure changes biomarker turnover in a small benchmark.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.3.0.

This is an alternate version. [Open the default version](../0.3.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_diffdose_2026_idr_benchmark/0.3.0/model.omex',
    expected_sha256='34dd0d01af9ef951fa84969ce4d008c860ac7abe55ae701b0866b80a8be426c0',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Archived experiment ID | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `higher_exposure` | Higher exposure | 0–42 d | 421 |
| `lower_exposure` | Lower exposure | 0–42 d | 421 |
| `untreated` | Untreated | 0–42 d | 421 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `drug_exposure` | Drug exposure driving the biomarker effect | `1` |
| `biomarker` | Biomarker level under indirect turnover | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 3 outputs and 2 states</summary>

| Technical column | Unit |
| --- | --- |
| `C` | `1` |
| `biomarker` | `1` |
| `drug_exposure` | `1` |
| `state__A` | `dimensionless` |
| `state__B` | `dimensionless` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `lower_exposure` starter has **421 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `drug_exposure` | 0 | 0 (0 d, post) | 0.839754 (41.1 d, pre) | 0.540291 |
| `biomarker` | 46 | 9.82515 (41.8 d, post) | 46 (0 d, post) | 9.82737 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

Normalized benchmark coordinates; V is a benchmark volume ratio and doses must not be called mg.

Forward turnover equations in equivalent amount coordinates A=V*C, with source-duration infusions and three exploratory regimens.

Outside this version’s scope:

- paper optimal regimens
- clinical doses
- population fitting

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
