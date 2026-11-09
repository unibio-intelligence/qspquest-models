# Prybylski 2026 dazukibart IFN-beta dermatomyositis ER

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore dazukibart exposure-response endpoints in dermatomyositis.

**Runnable · 4 experiments.** Version 0.2.0.

## Run an experiment

Full ODE simulation of the Stage 1/3 600 mg q4w regimen through crossover week 12.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_prybylski_2026_dazukibart_ifnb_dm_er', version='0.2.0')
result = model.run('stage1-600mg-q4w-cdasi-tis')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

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

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `state__central_mg` | Dazukibart amount in the central compartment | `mg` |
| `state__ifn_total_pg_ml` | Total interferon concentration | `pg/mL` |
| `state__end_cdasi_a` | Skin disease activity endpoint in the source response model | `score` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_prybylski_2026_dazukibart_ifnb_dm_er --model-version 0.2.0 --scenario stage1-600mg-q4w-cdasi-tis --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 15 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `stage1-600mg-q4w-cdasi-tis` starter has **52 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 0 | 0 (0 h, post) | 772.916 (8.05 h, pre) | 225.315 |
| `state__ifn_total_pg_ml` | 0.45885 | 0.45885 (0 h, post) | 122.732 (8.5 h, post) | 119.953 |
| `state__end_cdasi_a` | 24 | 10.7518 (12 h, pre) | 24 (0 h, post) | 10.7518 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
