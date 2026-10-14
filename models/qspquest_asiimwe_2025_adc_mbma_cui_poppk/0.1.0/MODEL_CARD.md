# Asiimwe 2025 ADC MBMA/CUI PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore fixed-effect T-DM1 and T-DXd exposure; inspect static utility endpoints.

**Runnable · 15 experiments.** Version 0.1.0.

## Run an experiment

Deterministic two-compartment IV-infusion scenario using Table 1 fixed effects and the paper GitHub median body weight. Paper PK metric summaries are overlaid by the dynamic validation script.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_asiimwe_2025_adc_mbma_cui_poppk', version='0.1.0')
result = model.run('tdm1-3p6mgkg-cycle1-fixed-effect-ode')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

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

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ng_ml` | T-DM1 concentration in the central compartment | `1` |
| `auc_ng_day_ml` | Accumulated central drug exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_asiimwe_2025_adc_mbma_cui_poppk --model-version 0.1.0 --scenario tdm1-3p6mgkg-cycle1-fixed-effect-ode --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 6 outputs and 4 states</summary>

| Technical column | Archive unit label |
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

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `tdm1-3p6mgkg-cycle1-fixed-effect-ode` starter has **842 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ng_ml` | 0 | 0 (0 h, post) | 74745 (0.0625 h, pre) | 974.653 |
| `auc_ng_day_ml` | 0 | 0 (0 h, post) | 303834 (21 h, pre) | 303834 |

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
Evidence identity: `sha256:0a7071b276b54d95c7babf3dddf4657adb92796e6895e5486bcb21888e9d68a8`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Fixed-effect two-compartment IV ADC PK reconstruction for T-DM1 and T-DXd from Asiimwe et al. 2025. Published CUI endpoints are replayed as static source anchors; dose selection is not executed.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
