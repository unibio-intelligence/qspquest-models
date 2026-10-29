# Bispecific exposure and ternary binding

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare bispecific exposure and binary versus ternary complex formation.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_diffdose_2026_bite_benchmark', version='0.1.0')
result = model.run('lower_exposure')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `higher_exposure` | Higher exposure | 0–140 d | 564 |
| `lower_exposure` | Lower exposure | 0–140 d | 564 |
| `untreated` | Untreated | 0–140 d | 561 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `drug_exposure` | Drug exposure driving binding | `1` |
| `binary_complexes` | Total binary complexes | `1` |
| `ternary_complex` | Ternary complexes linking both receptors | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_diffdose_2026_bite_benchmark --model-version 0.1.0 --scenario lower_exposure --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 5 outputs and 8 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `binary_complexes` | `1` |
| `drug_exposure` | `1` |
| `receptor_a_total` | `1` |
| `receptor_b_total` | `1` |
| `ternary_complex` | `1` |
| `state__AP` | `dimensionless` |
| `state__Abs` | `dimensionless` |
| `state__C` | `dimensionless` |
| `state__RA` | `dimensionless` |
| `state__RB` | `dimensionless` |
| `state__RCA` | `dimensionless` |
| `state__RCAB` | `dimensionless` |
| `state__RCB` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `lower_exposure` starter has **564 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `drug_exposure` | 0 | 0 (0 d, post) | 0.0480558 (98 d, post) | 5.32502e-06 |
| `binary_complexes` | 0 | 0 (0 d, post) | 8.25015 (103.75 d, post) | 0.000217359 |
| `ternary_complex` | 0 | 0 (0 d, post) | 9.98669 (103.75 d, post) | 0.975948 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

Normalized benchmark coordinates; no clinical mass/concentration conversion is established.

Forward BiTE example equations and explicit infusion timing from separately BSD-licensed DiffDose code; three Ubi-selected exploratory regimens.

Outside this version’s scope:

- paper optimal regimens
- clinical doses
- population fitting

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
