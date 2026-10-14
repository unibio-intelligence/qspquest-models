# Prybylski 2026 dazukibart IFN-beta dermatomyositis ER

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore dazukibart exposure-response endpoints in dermatomyositis.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Full ODE simulation of the Stage 1/3 600 mg q4w regimen through crossover week 12.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_prybylski_2026_dazukibart_ifnb_dm_er', version='0.1.0')
result = model.run('stage1-600mg-q4w-cdasi-tis')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-si-model-anchor` | Exact replay of PK/PD SI parameter estimates, ER Supplementary Table S1 values, study design constants, and runtime state count. | 0–0.01 h | 2 |
| `placebo-week12-endpoint-turnover` | No-dose endpoint turnover scenario for placebo comparator overlays. | 0–12 h | 49 |
| `stage1-600mg-q4w-cdasi-tis` | Full ODE simulation of the Stage 1/3 600 mg q4w regimen through crossover week 12. | 0–12 h | 52 |
| `stage2-150mg-q4w-cdasi` | Full ODE simulation of the Stage 2 150 mg q4w regimen through crossover week 12. | 0–12 h | 52 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__central_mg` | Dazukibart amount in the central compartment | `mg` |
| `state__ifn_total_pg_ml` | Total interferon concentration | `pg/mL` |
| `state__end_cdasi_a` | Skin disease activity endpoint in the source response model | `score` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_prybylski_2026_dazukibart_ifnb_dm_er --model-version 0.1.0 --scenario stage1-600mg-q4w-cdasi-tis --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 15 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__central_mg` | `mg` |
| `state__depot_mg` | `mg` |
| `state__end_cdasi_a` | `score` |
| `state__end_cdasi_d` | `score` |
| `state__end_enzyme` | `score` |
| `state__end_exga` | `score` |
| `state__end_haq` | `score` |
| `state__end_mmt8` | `score` |
| `state__end_phga` | `score` |
| `state__end_ptga` | `score` |
| `state__end_sf36_mcs` | `score` |
| `state__end_sf36_pfd` | `score` |
| `state__end_tis_phga` | `score` |
| `state__ifn_total_pg_ml` | `pg/mL` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `stage1-600mg-q4w-cdasi-tis` starter has **52 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 0 | 0 (0 h, post) | 772.916 (8.05 h, pre) | 225.315 |
| `state__ifn_total_pg_ml` | 0.45885 | 0.45885 (0 h, post) | 122.732 (8.5 h, post) | 119.953 |
| `state__end_cdasi_a` | 24 | 10.7518 (12 h, pre) | 24 (0 h, post) | 10.7518 |

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
Evidence identity: `sha256:bf3395767f89c9f5aecc9a22a2121fbfe42946453777be0c159b6ffef6929bce`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Public ODE reconstruction of the dazukibart dermatomyositis PK/PD and exposure-response model: two-compartment mAb PK, IFN-beta QSS turnover, and endpoint indirect-response ODEs from the NONMEM control stream and supplementary tables.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
