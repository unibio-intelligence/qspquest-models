# CD3×5T4 In Vitro Activation and Cytotoxicity QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore bispecific-driven T-cell activation and tumor-cell killing in vitro.

**Runnable · 11 experiments.** Version 2.0.1.

## Run an experiment

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.1')
result = model.run('mda_mb_468_duobody_6_86nm_et4')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `bxpc_3_duobody_6_86nm_et4` | Bxpc 3 duobody 6 86nm et4 | 0–72 h | 73 |
| `eplc_272h_duobody_6_86nm_et4` | Eplc 272h duobody 6 86nm et4 | 0–72 h | 73 |
| `mda_mb_231_duobody_6_86nm_et4` | Mda mb 231 duobody 6 86nm et4 | 0–72 h | 73 |
| `mda_mb_231_high_affinity_6_86nm_et8` | Mda mb 231 high affinity 6 86nm et8 | 0–72 h | 73 |
| `mda_mb_468_duobody_6_86nm_et1` | Mda mb 468 duobody 6 86nm et1 | 0–72 h | 73 |
| `mda_mb_468_duobody_6_86nm_et2` | Mda mb 468 duobody 6 86nm et2 | 0–72 h | 73 |
| `mda_mb_468_duobody_6_86nm_et4` | Mda mb 468 duobody 6 86nm et4 | 0–72 h | 73 |
| `mda_mb_468_duobody_6_86nm_et8` | Mda mb 468 duobody 6 86nm et8 | 0–72 h | 73 |
| `mda_mb_468_high_affinity_6_86nm_et8` | Mda mb 468 high affinity 6 86nm et8 | 0–72 h | 73 |
| `mda_mb_468_untreated_et4` | Mda mb 468 untreated et4 | 0–72 h | 73 |
| `sk_gt_4_duobody_6_86nm_et4` | Sk gt 4 duobody 6 86nm et4 | 0–72 h | 73 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `tcell_activation_percent` | Percentage of activated T cells | `1` |
| `tumor_killing_percent` | Percentage tumor-cell killing | `1` |
| `viable_tumor_cells` | Remaining viable tumor cells | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_yuan_2026_cd3x5t4_in_vitro_qsp --model-version 2.0.1 --scenario mda_mb_468_duobody_6_86nm_et4 --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 18 outputs and 17 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `KD_CD3_2D_molecules_per_cell` | `1` |
| `activated_tcells` | `1` |
| `aggregate_trimer_load` | `1` |
| `dead_tumor_cells` | `1` |
| `effector_tcells` | `1` |
| `effector_to_target_ratio` | `1` |
| `f_Tcell` | `1` |
| `f_tumor` | `1` |
| `kprolif_Ta_per_hr` | `1` |
| `kprolif_tumor_per_hr` | `1` |
| `per_effector_kill_rate` | `1` |
| `resting_tcells` | `1` |
| `tcell_activation_percent` | `1` |
| `total_tcells` | `1` |
| `total_tumor_cells` | `1` |
| `trimer_per_tcell` | `1` |
| `tumor_killing_percent` | `1` |
| `viable_tumor_cells` | `1` |
| `state__BsAb` | `nM` |
| `state__CD3` | `molecule/cell` |
| `state__CD3_BsAb` | `molecule/cell` |
| `state__TAA` | `molecule/cell` |
| `state__TAA_BsAb` | `molecule/cell` |
| `state__Ta` | `cell` |
| `state__Ta_generation_counter` | `dimensionless` |
| `state__Te` | `cell` |
| `state__Te_generation_counter` | `dimensionless` |
| `state__Tr` | `cell` |
| `state__apoT1` | `cell` |
| `state__apoT2` | `cell` |
| `state__apoT3` | `cell` |
| `state__dead_tumor` | `cell` |
| `state__trimer` | `molecule/cell` |
| `state__tumor_cell` | `cell` |
| `state__tumor_without_drug` | `cell` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `mda_mb_468_duobody_6_86nm_et4` starter has **73 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `tcell_activation_percent` | 0 | 0 (0 h, post) | 40.1075 (58 h, post) | 39.3303 |
| `tumor_killing_percent` | 0 | 0 (0 h, post) | 99.7935 (72 h, pre) | 99.7935 |
| `viable_tumor_cells` | 16000 | 104.005 (72 h, pre) | 19085.4 (13 h, post) | 104.005 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

Final 17-state in-vitro ODE system, disclosed population parameter profile and source-aligned mechanistic scenarios; no systemic PK.

Outside this version’s scope:

- historical base/intermediate executable models
- Monolix project
- individual culture/donor effects
- S7–S8 residual diagnostics
- donor-weighted pooled population replay

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:5f5bc66430a82d7cea07d98b478e372826dfa03de77ae380e76eb164ad6cb1f3`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Links per-cell CD3×5T4 trimer formation to resting-to-activated-to-effector T-cell dynamics and three-stage apoptotic tumor-cell loss across drug affinity, concentration, antigen density, and effector-to-target ratio.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)

## Source precision profiles

Eight complete parameter conventions cover the eleven curated conditions.
Inspect `model.precision_profiles` and follow the
[source precision tutorial](../../../tutorials/precision-profiles.md) to select
a convention and retain its complete receipt. The default matches archived
scalar inputs. Source rounding conventions and native unit labels do not
establish physical dimensional or biological qualification.
