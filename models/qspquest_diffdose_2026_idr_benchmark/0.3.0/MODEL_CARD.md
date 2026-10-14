# Drug-stimulated biomarker turnover

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore how repeated exposure changes biomarker turnover in a small benchmark.

**Runnable · 3 experiments.** Version 0.3.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_diffdose_2026_idr_benchmark', version='0.3.0')
result = model.run('lower_exposure')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

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

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `drug_exposure` | Drug exposure driving the biomarker effect | `1` |
| `biomarker` | Biomarker level under indirect turnover | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_diffdose_2026_idr_benchmark --model-version 0.3.0 --scenario lower_exposure --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 3 outputs and 2 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `C` | `1` |
| `biomarker` | `1` |
| `drug_exposure` | `1` |
| `state__A` | `dimensionless` |
| `state__B` | `dimensionless` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `lower_exposure` starter has **421 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `drug_exposure` | 0 | 0 (0 d, post) | 0.839754 (41.1 d, pre) | 0.540291 |
| `biomarker` | 46 | 9.82515 (41.8 d, post) | 46 (0 d, post) | 9.82737 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

Normalized benchmark coordinates; V is a benchmark volume ratio and doses must not be called mg.

Forward turnover equations in equivalent amount coordinates A=V*C, with source-duration infusions and three exploratory regimens.

Outside this version’s scope:

- paper optimal regimens
- clinical doses
- population fitting

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation, fit.
Fitting supported: `true`; fit ready: `true`.
Evidence identity: `sha256:15d79cb03f9116b5270cf2f2563178e8f9b1a5c453873c4cb2201ca152d084c2`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## Synthetic parameter recovery

Complete the [fitting prerequisites](../../../tutorials/library-fitting.md#prerequisites-and-discovery) with the matching QSPQuest Python binding. The archive fixes synthetic observations, residual errors, parameter bounds, solver and convergence controls for each workflow.

```python
from qspquest_models import Library
model = Library('.').load('qspquest_diffdose_2026_idr_benchmark', version='0.3.0')
print([(w['id'], w['operation']) for w in model.fitting_workflows])
fit = model.fit_workflow('diffsol_bdf-start-1')
assert fit['checks']['passed'], fit['checks']
print(fit['checks']['parameters'])
```

A successful fixture reports converged parameter recovery within its declared absolute limits. Retain the complete native result and diagnostics. A budget-limited or nonconverged result has failed checks; inspect those diagnostics before interpreting estimates.

The six workflows cover three parameter starters under BDF and Rodas5P. Their scope is the exact archived synthetic recovery case. Source population reproduction, uncertainty coverage and clinical qualification require separate evidence.

## What you can explore

How does repeated exposure accelerate biomarker removal?

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
