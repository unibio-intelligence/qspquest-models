# Eaton 2025 idarucizumab/dabigatran sheep PK-PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore sheep idarucizumab/dabigatran scenarios and published PK/PD endpoints.

**Runnable · 33 experiments.** Version 0.1.0.

## Run an experiment

Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_eaton_2025_idarucizumab_dabigatran_sheep_pkpd', version='0.1.0')
result = model.run('actual-administration-duration-sensitivity')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 33 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `actual-administration-duration-sensitivity` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 316 |
| `dabigatran-4mgkg-sheep-pkpd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-ce50-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-ce50-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-cl-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-cl-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-e0-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-e0-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-k-ida-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-k-ida-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-q-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-q-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-v1-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-v1-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-v2-minus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `eta-v2-plus-one-approx-sd` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `figure4-label-150min-maintenance-sensitivity` | Loading and two-step infusion from Figure4; circuit settings unavailable. Not an exact Figure4 reproduction. | 0–150 h | 301 |
| `figure4-one-min-loading-sensitivity` | Loading and two-step infusion from Figure4; circuit settings unavailable. Not an exact Figure4 reproduction. | 0–150 h | 301 |
| `sheep-1-with-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-1-without-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-2-with-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-2-without-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-3-with-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-3-without-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-4-with-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-4-without-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-5-with-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `sheep-5-without-idarucizumab` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `study-sequence-mean-weight` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `target-infusion-90min-figure4` | Loading and two-step infusion from Figure4; circuit settings unavailable. Not an exact Figure4 reproduction. | 0–150 h | 301 |
| `upstream-half-time-allometry-28-7` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `upstream-half-time-allometry-34-42` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |
| `upstream-half-time-allometry-41-8` | Sheep source-dose sequence; zero individual effects unless explicitly overridden. One reversal unit denotes the studied15mg/kg, not an arbitrary mass conversion. | 0–1560 h | 317 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__central_mg` | Dabigatran amount in the central compartment | `mg` |
| `state__effect_conc_mg_l` | Effect-compartment dabigatran concentration | `mg/L` |
| `state__idarucizumab_effect_unit` | Idarucizumab effect in the source numerical scale | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_eaton_2025_idarucizumab_dabigatran_sheep_pkpd --model-version 0.1.0 --scenario actual-administration-duration-sensitivity --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__auc_mg_min_l` | `mg*min/L` |
| `state__central_mg` | `mg` |
| `state__cpb_circuit_mg` | `mg` |
| `state__effect_conc_mg_l` | `mg/L` |
| `state__idarucizumab_effect_unit` | `1` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `actual-administration-duration-sensitivity` starter has **316 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 0 | 0 (0 h, post) | 129.358 (1 h, pre) | 0.0569042 |
| `state__effect_conc_mg_l` | 0 | 0 (0 h, post) | 61.8218 (5 h, pre) | 0.039597 |
| `state__idarucizumab_effect_unit` | 0 | 0 (0 h, post) | 0.99457 (120.5 h, pre) | 2.33915e-14 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:3246a44821897597b21a06b5a2c9a06fbd3e2ccfeb6ccd773e9655aad03aa1f2`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Dabigatran disposition and delayed coagulation response in sheep, with separately dosed empirical idarucizumab reversal. Source-model assumptions and population reproduction remain incomplete.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
