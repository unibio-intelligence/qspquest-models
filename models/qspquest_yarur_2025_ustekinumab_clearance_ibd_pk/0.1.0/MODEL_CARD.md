# Yarur 2025 ustekinumab clearance/disease-control PK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect ustekinumab clearance and IBD disease-control relationships.

**Source replay available; dynamic simulation unavailable · 3 unavailable.** Version 0.1.0.

## Run an experiment

No-dose replay of public PK priors, cohort summaries, and reported p-value/cutoff anchors.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yarur_2025_ustekinumab_clearance_ibd_pk', version='0.1.0')
result = model.run('exact-article-table-anchor')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-article-table-anchor` | No-dose replay of public PK priors, cohort summaries, and reported p-value/cutoff anchors. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `source__cl_pop_l_day` | Retained population clearance prior, constant source value | `L/day` |
| `source__beta_albumin_on_cl` | Retained albumin effect on clearance, constant source value | `power` |
| `source__bioavailability` | Retained subcutaneous bioavailability prior, constant source value | `fraction` |

**This starter is a source replay.** Its values are stored constants or short checks from the source.
This version cannot simulate over time. Zero drug states do not show a treatment response.

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_yarur_2025_ustekinumab_clearance_ibd_pk --model-version 0.1.0 --scenario exact-article-table-anchor --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 4 states</summary>

| Technical column | Unit |
| --- | --- |
| `state__auc_ug_day_ml` | `ug*day/mL` |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__peripheral_mg` | `mg` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `exact-article-table-anchor` starter has **2 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `source__cl_pop_l_day` | 0.161 | 0.161 (0 d, post) | 0.161 (0 d, post) | 0.161 |
| `source__beta_albumin_on_cl` | -0.887 | -0.887 (0 d, post) | -0.887 (0 d, post) | -0.887 |
| `source__bioavailability` | 0.735 | 0.735 (0 d, post) | 0.735 (0 d, post) | 0.735 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) was produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

**3 experiments cannot be simulated.** See [why they are unavailable](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
