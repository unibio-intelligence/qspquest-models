# Eaton 2025 dabigatran-idarucizumab sheep CPB PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore dabigatran reversal by idarucizumab in a sheep bypass model.

**Runnable · 2 experiments.** Version 0.2.0.

## Run an experiment

Full fixed-effect ODE protocol from Methods with a primed CPB circuit and post-CPB idarucizumab reversal.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_eaton_2025_dabigatran_idarucizumab_sheep_cpb_pkpd', version='0.2.0')
result = model.run('cpb-idarucizumab-reversal-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

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

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `dabigatran_conc_mg_l` | Dabigatran concentration | `1` |
| `idarucizumab_conc_mg_l` | Idarucizumab concentration | `1` |
| `r_time_min` | Coagulation reaction time in the reversal model | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_eaton_2025_dabigatran_idarucizumab_sheep_cpb_pkpd --model-version 0.2.0 --scenario cpb-idarucizumab-reversal-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 10 outputs and 7 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `cpb-idarucizumab-reversal-overlay` starter has **1443 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `dabigatran_conc_mg_l` | 0 | 0 (0 h, post) | 4.84688 (1 h, pre) | 0.0304997 |
| `idarucizumab_conc_mg_l` | 0 | 0 (0 h, post) | 307.292 (180.5 h, pre) | 0.143403 |
| `r_time_min` | 0.584 | 0.584 (0 h, post) | 19.55 (1 h, pre) | 0.717822 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
