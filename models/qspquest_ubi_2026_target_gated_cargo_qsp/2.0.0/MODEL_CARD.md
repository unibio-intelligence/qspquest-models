# Target-Gated Cargo QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare tumor and systemic receptor occupancy under synthetic gating assumptions.

**Runnable · 6 experiments.** Version 2.0.0.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_ubi_2026_target_gated_cargo_qsp', version='2.0.0')
result = model.run('balanced_gate_30nmol_iv')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `attenuated_cargo_receptor_30nmol_iv` | Attenuated cargo receptor 30nmol iv | 0–336 h | 57 |
| `balanced_gate_30nmol_iv` | Balanced gate 30nmol iv | 0–336 h | 57 |
| `leaky_systemic_gate_30nmol_iv` | Leaky systemic gate 30nmol iv | 0–336 h | 57 |
| `no_dose_homeostasis` | No dose homeostasis | 0–24 h | 25 |
| `no_tumor_gate_30nmol_iv` | No tumor gate 30nmol iv | 0–336 h | 57 |
| `tight_systemic_gate_30nmol_iv` | Tight systemic gate 30nmol iv | 0–336 h | 57 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `tumor_receptor_occupancy_percent` | Percentage of tumor receptors occupied | `1` |
| `central_receptor_occupancy_percent` | Percentage of systemic receptors occupied | `1` |
| `total_construct_nmol` | Total remaining construct amount | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_ubi_2026_target_gated_cargo_qsp --model-version 2.0.0 --scenario balanced_gate_30nmol_iv --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 19 outputs and 11 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `background_open_equilibrium_ratio` | `1` |
| `cargo_receptor_effective_Kd_nM` | `1` |
| `central_accessible_cargo_percent` | `1` |
| `central_receptor_occupancy_fraction` | `1` |
| `central_receptor_occupancy_percent` | `1` |
| `central_total_construct_nM` | `1` |
| `central_total_construct_nmol` | `1` |
| `gate_bound_open_equilibrium_ratio` | `1` |
| `gate_closed_effective_Kd_nM` | `1` |
| `gate_open_effective_Kd_nM` | `1` |
| `instantaneous_tumor_to_systemic_ro_ratio` | `1` |
| `total_construct_nmol` | `1` |
| `tumor_accessible_cargo_percent` | `1` |
| `tumor_gate_occupancy_fraction` | `1` |
| `tumor_gate_occupancy_percent` | `1` |
| `tumor_receptor_occupancy_fraction` | `1` |
| `tumor_receptor_occupancy_percent` | `1` |
| `tumor_total_construct_nM` | `1` |
| `tumor_total_construct_nmol` | `1` |
| `state__closed_central` | `nmol` |
| `state__closed_peripheral` | `nmol` |
| `state__closed_tumor` | `nmol` |
| `state__gate_bound_closed_tumor` | `nmol` |
| `state__gate_bound_open_tumor` | `nmol` |
| `state__gate_receptor_bound_open_tumor` | `nmol` |
| `state__open_central` | `nmol` |
| `state__open_peripheral` | `nmol` |
| `state__open_tumor` | `nmol` |
| `state__receptor_bound_central` | `nmol` |
| `state__receptor_bound_open_tumor` | `nmol` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `balanced_gate_30nmol_iv` starter has **57 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `tumor_receptor_occupancy_percent` | 0 | 0 (0 h, post) | 69.9314 (174 h, post) | 62.3724 |
| `central_receptor_occupancy_percent` | 0 | 0 (0 h, post) | 13.5125 (18 h, post) | 4.46119 |
| `total_construct_nmol` | 30 | 22.4046 (336 h, pre) | 30 (0 h, post) | 22.4046 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

No paper-specific model. Independently authored 11-state gated-cargo mechanism with synthetic parameters and six curated controls.

Outside this version’s scope:

- Kahn 2026 equations/parameters/figures
- named target/cargo efficacy
- immune signaling/tumor killing/toxicity

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
