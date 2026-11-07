# Drug-stimulated biomarker turnover

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore how repeated exposure changes biomarker turnover in a small benchmark.

**Runnable · 3 experiments.** Version 0.3.1.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_diffdose_2026_idr_benchmark', version='0.3.1')
result = model.run('lower_exposure')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `higher_exposure` | Higher exposure | 0–42 d | 421 |
| `lower_exposure` | Lower exposure | 0–42 d | 421 |
| `untreated` | Untreated | 0–42 d | 421 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `drug_exposure` | Drug exposure driving the biomarker effect | `1` |
| `biomarker` | Biomarker level under indirect turnover | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_diffdose_2026_idr_benchmark --model-version 0.3.1 --scenario lower_exposure --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

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

No reference result is stored for this version.

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

Normalized benchmark coordinates; V is a benchmark volume ratio and doses must not be called mg.

Forward turnover equations in equivalent amount coordinates A=V*C, with source-duration infusions and three exploratory regimens.

Outside this version’s scope:

- paper optimal regimens
- clinical doses
- population fitting

## Archived synthetic fitting contract

This archive declares 3 synthetic parameter-recovery workflows. Archived fit readiness does not establish compatibility with the installed engine.

Use the [fitting guide](../../../tutorials/library-fitting.md#prerequisites-and-discovery) to list compatible workflows and current engine holds before fitting. Preset simulation does not require fitting compatibility.

These fixtures do not establish source-population reproduction, uncertainty or clinical use.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
