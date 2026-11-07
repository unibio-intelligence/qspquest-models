# Asiimwe 2025 ADC MBMA/CUI PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed-effect T-DM1 and T-DXd exposure; inspect static utility endpoints.

**Runnable · 15 experiments.** Version 0.1.0.

## Run an experiment

Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_asiimwe_2025_adc_mbma_cui_poppk', version='0.1.0')
result = model.run('tdm1-3p6mgkg-cycle1-fixed-effect-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

<details>
<summary>Browse all 15 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-table1-cui-source-anchor` | No-dose exact replay of Table 1 structural model parameters, reported median weights, dosing, and key CUI dose-selection endpoints. | 0–1 h | 2 |
| `tdm1-0p3mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-0p6mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-1p2mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-1p8mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-2p4mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-3p6mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdm1-4p8mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-0p8mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-1p6mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-3p2mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-5p4mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-6p4mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-7p4mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |
| `tdxd-8p0mgkg-cycle1-fixed-effect-ode` | Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script. | 0–21 h | 842 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `central_conc_ng_ml` | T-DM1 concentration in the central compartment | `1` |
| `auc_ng_day_ml` | Accumulated central drug exposure | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_asiimwe_2025_adc_mbma_cui_poppk --model-version 0.1.0 --scenario tdm1-3p6mgkg-cycle1-fixed-effect-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 6 outputs and 4 states</summary>

| Technical column | Unit |
| --- | --- |
| `auc_ng_day_ml` | `1` |
| `central_conc_mg_l` | `1` |
| `central_conc_ng_ml` | `1` |
| `dose_mg` | `1` |
| `elapsed_day` | `1` |
| `peripheral_conc_mg_l` | `1` |
| `state__auc_ng_day_ml` | `ng*day/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `tdm1-3p6mgkg-cycle1-fixed-effect-ode` starter has **842 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ng_ml` | 0 | 0 (0 h, post) | 74745 (0.0625 h, pre) | 974.653 |
| `auc_ng_day_ml` | 0 | 0 (0 h, post) | 303834 (21 h, pre) | 303834 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
