# Zeng 2026 atezolizumab PopPK software-comparison simulation

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Compare atezolizumab fixed-input PK simulation scenarios.

**Runnable · 40 experiments.** Version 0.1.0.

## Run an experiment

Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_zeng_2026_atezolizumab_software_poppk_simulation', version='0.1.0')
result = model.run('standard-1200-q3w')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 40 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `cycle1-figure-control-1680-q4w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–28 h | 59 |
| `cycle1-figure-control-840-q2w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–14 h | 31 |
| `cycle1-loading-1200-q3w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–21 h | 45 |
| `cycle1-loading-1680-q4w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–28 h | 59 |
| `cycle1-loading-840-q2w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–14 h | 31 |
| `cycle1-standard-1200-q3w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–21 h | 45 |
| `figure-control-1680-q4w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–196 h | 407 |
| `figure-control-1680-q4w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–196 h | 407 |
| `figure-control-1680-q4w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–196 h | 400 |
| `figure-control-1680-q4w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–196 h | 407 |
| `figure-control-840-q2w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–98 h | 211 |
| `figure-control-840-q2w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–98 h | 211 |
| `figure-control-840-q2w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–98 h | 204 |
| `figure-control-840-q2w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–98 h | 211 |
| `loading-1200-q3w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–273 h | 561 |
| `loading-1200-q3w-then-840-q6w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–273 h | 561 |
| `loading-1200-q3w-then-840-q6w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–273 h | 554 |
| `loading-1200-q3w-then-840-q6w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–273 h | 561 |
| `loading-1680-q4w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–280 h | 575 |
| `loading-1680-q4w-then-840-q6w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–280 h | 575 |
| `loading-1680-q4w-then-840-q6w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–280 h | 568 |
| `loading-1680-q4w-then-840-q6w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–280 h | 575 |
| `loading-840-q2w-then-840-q6w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–266 h | 547 |
| `loading-840-q2w-then-840-q6w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–266 h | 547 |
| `loading-840-q2w-then-840-q6w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–266 h | 540 |
| `loading-840-q2w-then-840-q6w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–266 h | 547 |
| `standard-1200-q3w` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-60min-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-ada-positive` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-bolus-sensitivity` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 302 |
| `standard-1200-q3w-eta-cl-plus-sd` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-eta-imax-plus-sd` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-eta-vc-plus-sd` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-eta-vp-plus-sd` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-female` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-female-ada-positive` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-high-tumor` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-low-albumin` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-low-weight` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |
| `standard-1200-q3w-pumas-fixed-effect-variant` | Individual latent-concentration simulation. A typical subject is not the paper population geometric mean. Infusion duration is an explicit approximation; bolus is a sensitivity matching the nlmixr2 vignette. | 0–147 h | 309 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__central_mg` | Atezolizumab amount in the central compartment | `mg` |
| `state__auc_ug_day_ml` | Accumulated central atezolizumab exposure | `ug*day/mL` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_zeng_2026_atezolizumab_software_poppk_simulation --model-version 0.1.0 --scenario standard-1200-q3w --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__auc_ug_day_ml` | `ug*day/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_day` | `day` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `standard-1200-q3w` starter has **309 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__central_mg` | 0 | 0 (0 h, post) | 1796.03 (126.021 h, pre) | 618.475 |
| `state__auc_ug_day_ml` | 0 | 0 (0 h, post) | 34598.6 (147 h, pre) | 34598.6 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
