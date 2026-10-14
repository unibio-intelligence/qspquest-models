# Sule 2025/2026 bevacizumab pediatric minimal PBPK bridge

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore a reduced physiological model for pediatric bevacizumab exposure.

**Runnable · 13 experiments.** Version 0.1.0.

## Run an experiment

Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_sule_2025_bevacizumab_minimal_pbpk_pediatric_bridge', version='0.1.0')
result = model.run('female-6-12y-10mgkg-q2w-ode-endpoint-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 13 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `adult-female-ge18-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `adult-male-ge18-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `female-0p5-2y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `female-12-18y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `female-2-6y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `female-6-12y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `figure2-pbpk-poppk-ratio-digitized` | Overlay-only scenario exposing raster-digitized PBPK/popPK ratio markers from Sule 2025/2026 Figure 2. This is a source-limited display anchor, not a native Simcyp/popPK rerun. | 0–1 h | 2 |
| `figure4-pediatric-pk-digitized` | Overlay-only scenario exposing raster-digitized pediatric observed concentrations from Sule 2025 Figure 4. It is not a native Simcyp replay scenario. | 0–120 h | 121 |
| `male-0p5-2y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `male-12-18y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `male-2-6y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `male-6-12y-10mgkg-q2w-ode-endpoint-overlay` | Dose-driven reduced ODE probe for the public Sule exposure endpoints. The native Simcyp physiology/project is unavailable, so this scenario is validated as a source-limited table-endpoint overlay rather than strict Simcyp parity. | 0–3024 h | 766 |
| `source-tables-exact-replay` | No-dose exact replay of Table I, Table II, and Supplementary Tables S1-S3 public numeric anchors. | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__central_mg` | Bevacizumab amount in the central compartment | `mg` |
| `state__peripheral_mg` | Bevacizumab amount in the peripheral compartment | `mg` |
| `state__auc_mg_h_l` | Accumulated central drug exposure | `mg*h/L` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_sule_2025_bevacizumab_minimal_pbpk_pediatric_bridge --model-version 0.1.0 --scenario female-6-12y-10mgkg-q2w-ode-endpoint-overlay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__auc_mg_h_l` | `mg*h/L` |
| `state__central_mg` | `mg` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `female-6-12y-10mgkg-q2w-ode-endpoint-overlay` starter has **766 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 0 | 0 (0 h, post) | 366.15 (2689 h, pre) | 20.6017 |
| `state__peripheral_mg` | 0 | 0 (0 h, post) | 102.357 (2744 h, post) | 23.8565 |
| `state__auc_mg_h_l` | 0 | 0 (0 h, post) | 153133 (3024 h, pre) | 153133 |

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
Evidence identity: `sha256:56294f7a3fdb2d59a1268be34695aa288e7d91cd0cfbe194b1b007d212b61d0e`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Reduced public-parameter ODE reconstruction of Sule et al.'s Simcyp V22 minimal PBPK bevacizumab adult-to-pediatric bridge. The runtime carries the paper's published physicochemical/FcRn/distribution/clearance parameters and dose-driven central/peripheral drug amounts, while exact validation replays the public Table I, Table II, and SI Table S1-S3 exposure anchors.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
