# Lee 2024 SB12/eculizumab healthy-subject PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore SB12/eculizumab PK/PD experiments in healthy subjects.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Independent healthy-subject fit, 35-minute infusion, measured baseline TCA at reference 87.75%. Typical subject, no population intervals.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_lee_2024_sb12_eculizumab_healthy_poppkpd', version='0.1.0')
result = model.run('healthy-82-4kg')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `healthy-70-0kg` | Independent healthy-subject fit, 35-minute infusion, measured baseline TCA at reference 87.75%. Typical subject, no population intervals. | 0–1512 h | 130 |
| `healthy-82-4kg` | Independent healthy-subject fit, 35-minute infusion, measured baseline TCA at reference 87.75%. Typical subject, no population intervals. | 0–1512 h | 130 |
| `healthy-94-3kg` | Independent healthy-subject fit, 35-minute infusion, measured baseline TCA at reference 87.75%. Typical subject, no population intervals. | 0–1512 h | 130 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_ug_ml` | Eculizumab or SB12 concentration | `1` |
| `terminal_complement_activity_pct` | Terminal complement activity | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_lee_2024_sb12_eculizumab_healthy_poppkpd --model-version 0.1.0 --scenario healthy-82-4kg --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 26 outputs and 4 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `baseline_ic50_exponent` | `1` |
| `baseline_tca_pct` | `1` |
| `baseline_tca_ref_pct` | `1` |
| `body_weight_kg` | `1` |
| `central_conc_ug_ml` | `1` |
| `cl_l_h` | `1` |
| `effective_ic50_ug_ml` | `1` |
| `pd_e0_healthy_pct` | `1` |
| `pd_e0_pct` | `1` |
| `pd_hill` | `1` |
| `pd_ic50_ug_ml` | `1` |
| `pd_imax_fraction` | `1` |
| `pd_imax_healthy_fraction` | `1` |
| `peripheral_conc_ug_ml` | `1` |
| `pk_cl_l_h` | `1` |
| `pk_cl_weight_exponent` | `1` |
| `pk_q_l_h` | `1` |
| `pk_vc_healthy_l` | `1` |
| `pk_vc_weight_exponent` | `1` |
| `pk_vp_l` | `1` |
| `pk_weight_ref_kg` | `1` |
| `terminal_beta_h` | `1` |
| `terminal_complement_activity_pct` | `1` |
| `terminal_half_life_h` | `1` |
| `vc_l` | `1` |
| `weight_ratio` | `1` |
| `state__auc_ug_h_ml` | `ug*h/mL` |
| `state__central_mg` | `mg` |
| `state__elapsed_h` | `h` |
| `state__peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `healthy-82-4kg` starter has **130 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_ug_ml` | 0 | 0 (0 h, post) | 85.4914 (0.583333 h, pre) | 0.166291 |
| `terminal_complement_activity_pct` | 86.2 | 7.64919 (0.583333 h, pre) | 86.2 (0 h, post) | 86.2 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
