# Drug injury and delayed tumor loss

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore how drug injury propagates through delayed tumor-cell loss.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_diffdose_2026_tgi_benchmark', version='0.1.0')
result = model.run('lower_exposure')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `higher_exposure` | Higher exposure | 0–30 d | 301 |
| `lower_exposure` | Lower exposure | 0–30 d | 301 |
| `untreated` | Untreated | 0–30 d | 301 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `drug_exposure` | Drug exposure driving tumor injury | `1` |
| `tumor_total` | Total tumor burden across proliferating and injured cells | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_diffdose_2026_tgi_benchmark --model-version 0.1.0 --scenario lower_exposure --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 3 outputs and 6 states</summary>

| Technical column | Unit |
| --- | --- |
| `drug_exposure` | `1` |
| `proliferating_tumor` | `1` |
| `tumor_total` | `1` |
| `state__Abs` | `dimensionless` |
| `state__C` | `dimensionless` |
| `state__D1` | `dimensionless` |
| `state__D2` | `dimensionless` |
| `state__D3` | `dimensionless` |
| `state__P` | `dimensionless` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `lower_exposure` starter has **301 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `drug_exposure` | 0 | 0 (0 d, post) | 2.08468 (28.3 d, post) | 0.0564925 |
| `tumor_total` | 0.0098 | 0.0098 (0 d, post) | 3.26495 (30 d, pre) | 3.26495 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

Normalized benchmark coordinates.

Forward PK/tumor-damage example with three damage transits and rational viable/total-tumor growth; three exploratory regimens.

Outside this version’s scope:

- paper optimal regimens
- clinical doses
- population fitting

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
