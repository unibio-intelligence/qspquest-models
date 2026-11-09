# Rituximab exposure–CD19+ B-cell dynamics

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare typical and individualized rituximab exposure and B-cell depletion/recovery.

**Runnable · 3 experiments.** Version 0.5.0.

## Run an experiment

Explore rituximab persistence, CD19+ B-cell depletion, and gradual repopulation over 200 days using the typical parameter set.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_serkland_2025_rituximab_ms_pkpd', version='0.5.0')
result = model.run('population-typical-1000mg-full-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-monolix-archive-anchor` | Replay to day 0.001 after the starting 1000 mg dose of final model 3 population estimates, likelihood criteria, and subject-1 exported prediction endpoints. | 0–0.001 d | 2 |
| `population-typical-1000mg-full-ode` | Explore rituximab persistence, CD19+ B-cell depletion, and gradual repopulation over 200 days using the typical parameter set. | 0–200 d | 201 |
| `subject1-saem-full-ode-overlay` | Explore how an individualized PK/PD parameter set changes rituximab exposure, CD19+ B-cell depletion, and recovery relative to the typical configuration. | 0–186.05 d | 192 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `rituximab_concentration_mg_l` | Rituximab concentration | `mg/L` |
| `cd19_cells_mm3` | CD19-positive B-cell count during depletion and recovery | `[cell]/mm3` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.5.0 --scenario population-typical-1000mg-full-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 6 outputs and 3 states</summary>

| Technical column | Unit |
| --- | --- |
| `bcell_production_cells_mm3_day` | `[cell]/(mm3.d)` |
| `cd19_cells_mm3` | `[cell]/mm3` |
| `elapsed_days` | `d` |
| `linear_clearance_component_mg_l_day` | `mg/(L.d)` |
| `rituximab_concentration_mg_l` | `mg/L` |
| `tmdd_clearance_component_mg_l_day` | `mg/(L.d)` |
| `state__C` | `mg/L` |
| `state__L` | `[cell]/mm3` |
| `state__elapsed_day` | `d` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

No reference result is stored for this version.

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Only the PK dose and concentrations above declare physical units; no units have been independently checked.

- Interpret this as a deterministic typical-parameter trajectory, not a population distribution.
- The starting 1000 mg administration is a bolus into C at day 0, which approximates the source's 4-hour infusion as dose/V; further doses or infusions can be added to the regimen.
- Do not use the simulated CD19+ trajectory as a clinical dosing recommendation.
- This configuration demonstrates individual-parameter behavior; it is not a prospective patient-specific dosing workflow.
- Do not infer clinical benefit or an optimal redosing time from CD19+ cell count alone.

Source-backed output identities. Returned native units and source display labels remain distinct; an undeclared compartment is not inferred.

## Archived synthetic fitting contract

This archive declares 3 synthetic parameter-recovery workflows. Archived fit readiness does not establish compatibility with the installed engine.

Use the [fitting guide](../../../tutorials/library-fitting.md#prerequisites-and-discovery) to list compatible workflows and current engine holds before fitting. Preset simulation does not require fitting compatibility.

These fixtures do not establish source-population reproduction, uncertainty or clinical use.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
