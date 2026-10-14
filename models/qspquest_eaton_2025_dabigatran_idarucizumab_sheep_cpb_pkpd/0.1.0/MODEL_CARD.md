# Eaton 2025 dabigatran-idarucizumab sheep CPB PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore dabigatran reversal by idarucizumab in a sheep bypass model.

**Runnable · 2 experiments.** Version 0.1.0.

## Run an experiment

Full fixed-effect ODE protocol from Methods with a primed CPB circuit and post-CPB idarucizumab reversal.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_eaton_2025_dabigatran_idarucizumab_sheep_cpb_pkpd', version='0.1.0')
result = model.run('cpb-idarucizumab-reversal-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `cpb-idarucizumab-reversal-overlay` | Full fixed-effect ODE protocol from Methods with a primed CPB circuit and post-CPB idarucizumab reversal. | 0–1440 h | 1443 |
| `exact-source-anchor` | No-protocol exact replay of public parameter, method, and source constants. | 0–0.001 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `dabigatran_conc_mg_l` | Dabigatran concentration | `1` |
| `idarucizumab_conc_mg_l` | Idarucizumab concentration | `1` |
| `r_time_min` | Coagulation reaction time in the reversal model | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_eaton_2025_dabigatran_idarucizumab_sheep_cpb_pkpd --model-version 0.1.0 --scenario cpb-idarucizumab-reversal-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 10 outputs and 7 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `cpb_mean_dabigatran_mg_l` | `1` |
| `cpb_prime_amount_mg` | `1` |
| `dabigatran_conc_mg_l` | `1` |
| `dabigatran_loading_total_mg` | `1` |
| `dabigatran_peripheral_conc_mg_l` | `1` |
| `idarucizumab_conc_mg_l` | `1` |
| `idarucizumab_total_protocol_mg` | `1` |
| `pump_conc_mg_l` | `1` |
| `r_time_min` | `1` |
| `target_r_time_at_5mg_l_no_ida_min` | `1` |
| `state__cpb_auc_mg_min_l` | `mg*min/L` |
| `state__cpb_elapsed_min` | `min` |
| `state__dab_central_mg` | `mg` |
| `state__dab_peripheral_mg` | `mg` |
| `state__effect_conc_mg_l` | `mg/L` |
| `state__idarucizumab_mg` | `mg` |
| `state__pump_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `cpb-idarucizumab-reversal-overlay` starter has **1443 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `dabigatran_conc_mg_l` | 0 | 0 (0 h, post) | 4.84688 (1 h, pre) | 0.0304997 |
| `idarucizumab_conc_mg_l` | 0 | 0 (0 h, post) | 307.292 (180.5 h, pre) | 0.143403 |
| `r_time_min` | 0.584 | 0.584 (0 h, post) | 19.55 (1 h, pre) | 0.717822 |

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
Evidence identity: `sha256:df66111021cf1ce22b72bf136427397baac922562d9e6fd3daa0784db14d7fdb`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Fixed-effect reconstruction of the public NM-TRAN ADVAN13 model for dabigatran PK, CPB pump exchange, effect-site R-time response, and idarucizumab antagonism.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
