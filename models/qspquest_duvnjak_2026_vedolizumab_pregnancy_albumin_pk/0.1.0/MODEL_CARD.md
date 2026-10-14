# Duvnjak 2026 vedolizumab pregnancy albumin/PK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect the relationship between albumin and vedolizumab exposure during pregnancy.

**Source replay available; dynamic simulation unavailable · 4 unavailable.** Version 0.1.0.

## Run an experiment

No-dose exact replay of paper parameter estimates, public NONMEM constants, and reported pregnancy effects.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_duvnjak_2026_vedolizumab_pregnancy_albumin_pk', version='0.1.0')
result = model.run('exact-table-code-and-text-anchor')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-table-code-and-text-anchor` | No-dose exact replay of paper parameter estimates, public NONMEM constants, and reported pregnancy effects. | 0–40 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `source__albumin_c` | Retained baseline albumin coefficient, constant source value | `g/L` |
| `source__cl_cd_l_day` | Retained reference Crohn disease clearance, constant source value | `L/day` |

**This starter is a source replay.** Its retained values are constant or short source checks.
No qualified dynamic simulation is available in this version. Zero drug states do not demonstrate a treatment response.

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_duvnjak_2026_vedolizumab_pregnancy_albumin_pk --model-version 0.1.0 --scenario exact-table-code-and-text-anchor --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__auc_mg_week_l` | `mg*week/L` |
| `state__central_mg` | `mg` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `exact-table-code-and-text-anchor` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `source__albumin_c` | 40.7 | 40.7 (0 h, post) | 40.7 (0 h, post) | 40.7 |
| `source__cl_cd_l_day` | 0.155 | 0.155 (0 h, post) | 0.155 (0 h, post) | 0.155 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**4 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

<details>
<summary>Availability and qualification</summary>

Execution: `source_replay`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:8a650b58f6699ac7894e17467e8b062213504e6d5c87cd2fd6731eb22ea4c2b4`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Full deterministic ODE reconstruction of the Duvnjak et al. 2026 vedolizumab pregnancy PopPK model: albumin polynomial, two-compartment disposition, linear plus Michaelis-Menten clearance, albumin-mediated pregnancy effects on CL/Vc, and third-trimester gestational-age clearance effect.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
