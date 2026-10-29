# Rituximab exposure–CD19+ B-cell dynamics

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare typical and individualized rituximab exposure and B-cell depletion/recovery.

**Runnable · 3 experiments.** Version 0.3.0.

## Run an experiment

Explore rituximab persistence, CD19+ B-cell depletion, and gradual repopulation over 200 days using the typical parameter set.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_serkland_2025_rituximab_ms_pkpd', version='0.3.0')
result = model.run('population-typical-1000mg-full-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-monolix-archive-anchor` | No-dose replay of final model 3 population estimates, likelihood criteria, and subject-1 exported prediction endpoints. | 0–0.001 d | 2 |
| `population-typical-1000mg-full-ode` | Explore rituximab persistence, CD19+ B-cell depletion, and gradual repopulation over 200 days using the typical parameter set. | 0–200 d | 201 |
| `subject1-saem-full-ode-overlay` | Explore how an individualized PK/PD parameter set changes rituximab exposure, CD19+ B-cell depletion, and recovery relative to the typical configuration. | 0–186.05 d | 192 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `rituximab_concentration_mg_l` | Rituximab concentration | `mg/L` |
| `cd19_cells_mm3` | CD19-positive B-cell count during depletion and recovery | `[cell]/mm3` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.0 --scenario population-typical-1000mg-full-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 7 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `bcell_production_cells_mm3_day` | `[cell]/(mm3.d)` |
| `cd19_cells_mm3` | `[cell]/mm3` |
| `elapsed_days` | `d` |
| `initial_concentration_mg_l` | `mg/L` |
| `linear_clearance_component_mg_l_day` | `mg/(L.d)` |
| `rituximab_concentration_mg_l` | `mg/L` |
| `tmdd_clearance_component_mg_l_day` | `mg/(L.d)` |
| `state__C` | `mg/L` |
| `state__L` | `[cell]/mm3` |
| `state__elapsed_day` | `d` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

This version has no independent numerical reference.

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

- Interpret this as a deterministic typical-parameter trajectory, not a population distribution.
- The starting administration is encoded as C(0) = dose/V; repeat-dose events are not represented in this released setup.
- Do not use the simulated CD19+ trajectory as a clinical dosing recommendation.
- This configuration demonstrates individual-parameter behavior; it is not a prospective patient-specific dosing workflow.
- Do not infer clinical benefit or an optimal redosing time from CD19+ cell count alone.

Source-backed output identities. Returned native units and source display labels remain distinct; an undeclared compartment is not inferred.

## Synthetic parameter recovery

Complete the [fitting prerequisites](../../../tutorials/library-fitting.md#prerequisites-and-discovery) with the matching QSPQuest Python binding. The archive fixes synthetic observations, residual errors, parameter bounds, solver and convergence controls for each workflow.

```python
from qspquest_models import Library
model = Library('.').load('qspquest_serkland_2025_rituximab_ms_pkpd', version='0.3.0')
print([(w['id'], w['operation']) for w in model.fitting_workflows])
fit = model.fit_workflow('diffsol_bdf-start-1')
assert fit['checks']['passed'], fit['checks']
print(fit['checks']['parameters'])
```

A successful fixture reports converged parameter recovery within its declared absolute limits. Retain the complete native result and diagnostics. A budget-limited or nonconverged result has failed checks; inspect those diagnostics before interpreting estimates.

The six workflows cover three parameter starters under BDF and Rodas5P. Their scope is the exact archived synthetic recovery case. Source population reproduction, uncertainty coverage and clinical qualification require separate evidence.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
