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

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-table-code-and-text-anchor` | No-dose exact replay of paper parameter estimates, public NONMEM constants, and reported pregnancy effects. | 0–40 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `source__albumin_c` | Retained baseline albumin coefficient, constant source value | `g/L` |
| `source__cl_cd_l_day` | Retained reference Crohn disease clearance, constant source value | `L/day` |

**This starter is a source replay.** Its values are stored constants or short checks from the source.
This version cannot simulate over time. Zero drug states do not show a treatment response.

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

| Technical column | Unit |
| --- | --- |
| `state__auc_mg_week_l` | `mg*week/L` |
| `state__central_mg` | `mg` |
| `state__peripheral_mg` | `mg` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `exact-table-code-and-text-anchor` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `source__albumin_c` | 40.7 | 40.7 (0 h, post) | 40.7 (0 h, post) | 40.7 |
| `source__cl_cd_l_day` | 0.155 | 0.155 (0 h, post) | 0.155 (0 h, post) | 0.155 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) was produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

**4 experiments cannot be simulated.** See [why they are unavailable](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
