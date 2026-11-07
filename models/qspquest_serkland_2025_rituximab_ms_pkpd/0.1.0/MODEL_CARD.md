# Rituximab exposure–CD19+ B-cell dynamics

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare typical and individualized rituximab exposure and B-cell depletion/recovery.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.3.2/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_serkland_2025_rituximab_ms_pkpd/0.1.0/model.omex',
    expected_sha256='bcc2ff5beffbc678359fc3bd8799d3174320290d8cb408a4806bf504d82d3efd',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Archived experiment ID | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-monolix-archive-anchor` | No-dose replay of final model 3 population estimates, likelihood criteria, and subject-1 exported prediction endpoints. | 0–0.001 d | 2 |
| `population-typical-1000mg-full-ode` | Explore rituximab persistence, CD19+ B-cell depletion, and gradual repopulation over 200 days using the typical parameter set. | 0–200 d | 201 |
| `subject1-saem-full-ode-overlay` | Explore how an individualized PK/PD parameter set changes rituximab exposure, CD19+ B-cell depletion, and recovery relative to the typical configuration. | 0–186.05 d | 192 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `rituximab_concentration_mg_l` | Rituximab concentration | `1` |
| `cd19_cells_mm3` | CD19-positive B-cell count during depletion and recovery | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 7 outputs and 3 states</summary>

| Technical column | Unit |
| --- | --- |
| `bcell_production_cells_mm3_day` | `1` |
| `cd19_cells_mm3` | `1` |
| `elapsed_days` | `1` |
| `initial_concentration_mg_l` | `1` |
| `linear_clearance_component_mg_l_day` | `1` |
| `rituximab_concentration_mg_l` | `1` |
| `tmdd_clearance_component_mg_l_day` | `1` |
| `state__C` | `mg/L` |
| `state__L` | `cell/millimeter^3` |
| `state__elapsed_day` | `day` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `population-typical-1000mg-full-ode` starter has **201 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `rituximab_concentration_mg_l` | 350.816 | 0.0562336 (200 d, pre) | 350.816 (0 d, post) | 0.0562336 |
| `cd19_cells_mm3` | 199.57 | 0.355817 (23 d, post) | 199.57 (0 d, post) | 8.70521 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

- Interpret this as a deterministic typical-parameter trajectory, not a population distribution.
- The starting administration is encoded as C(0) = dose/V; repeat-dose events are not represented in this released setup.
- Do not use the simulated CD19+ trajectory as a clinical dosing recommendation.
- This configuration demonstrates individual-parameter behavior; it is not a prospective patient-specific dosing workflow.
- Do not infer clinical benefit or an optimal redosing time from CD19+ cell count alone.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
