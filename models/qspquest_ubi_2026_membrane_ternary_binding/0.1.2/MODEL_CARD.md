# Membrane Ternary Binding

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore membrane binding, ternary bridging and loss of bridging at high ligand concentrations.

**Runnable · 5 experiments.** Version 0.1.2.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_ubi_2026_membrane_ternary_binding', version='0.1.2')
result = model.run('intermediate_ligand')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `high_left_site_density` | High left site density | 0–24 h | 97 |
| `high_ligand_hook` | High ligand hook | 0–24 h | 97 |
| `intermediate_ligand` | Intermediate ligand | 0–24 h | 97 |
| `low_ligand` | Low ligand | 0–24 h | 97 |
| `zero_ligand_control` | Zero ligand control | 0–12 h | 49 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `ternary_bridge_nM` | Ternary bridges linking the two membrane sites | `1` |
| `left_site_ternary_percent` | Percentage of left membrane sites in ternary bridges | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_ubi_2026_membrane_ternary_binding --model-version 0.1.2 --scenario intermediate_ligand --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 9 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `binary_complex_total_nM` | `1` |
| `left_binary_Kd_nM` | `1` |
| `left_site_ledger_nM` | `1` |
| `left_site_ternary_percent` | `1` |
| `right_binary_Kd_nM` | `1` |
| `right_site_ledger_nM` | `1` |
| `right_site_ternary_percent` | `1` |
| `ternary_bridge_copies` | `1` |
| `ternary_bridge_nM` | `1` |
| `state__left_binary` | `nM` |
| `state__left_site_free` | `nM` |
| `state__right_binary` | `nM` |
| `state__right_site_free` | `nM` |
| `state__ternary_bridge` | `nM` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `intermediate_ligand` starter has **97 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `ternary_bridge_nM` | 0 | 0 (0 h, post) | 30.9726 (23.5 h, post) | 30.9726 |
| `left_site_ternary_percent` | 0 | 0 (0 h, post) | 77.4316 (23.5 h, post) | 77.4316 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

No paper-specific model. Independently authored five-state binding kinetics with synthetic parameters and conserved site ledgers.

Outside this version’s scope:

- Bellout 2026 equilibrium model
- paper geometry/parameters/figures
- named molecules or cell lines

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
