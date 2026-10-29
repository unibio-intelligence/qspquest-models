# Markovic 2024 Vedolizumab Clearance/Remission PopPK

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore vedolizumab clearance and remission relationships.

**Runnable · 9 experiments.** Version 0.1.0.

## Run an experiment

Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_markovic_2024_vedolizumab_clearance_remission_poppk', version='0.1.0')
result = model.run('induction-q8w-no-prior-anti-tnf')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `induction-10w-q4w-no-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–630 d | 654 |
| `induction-10w-q4w-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–630 d | 654 |
| `induction-10w-q8w-no-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–1190 d | 1214 |
| `induction-10w-q8w-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–1190 d | 1214 |
| `induction-14w-q6w-no-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–938 d | 962 |
| `induction-14w-q6w-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–938 d | 962 |
| `induction-q8w-no-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–1162 d | 1185 |
| `induction-q8w-prior-anti-tnf` | Paper dosing-regimen scenario using the Table 2 fixed-effect ODE. Table 3 paper medians and intervals are included as endpoint overlays; exact CI parity is source-limited because population simulation draws and covariance are not public. | 0–1162 d | 1185 |
| `table2-table4-exact-anchors` | Short exact-anchor scenario exposing final fixed effects, variability/residual error anchors, and Table 4 CL threshold/AUROC values. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `C_central_ug_mL` | Vedolizumab concentration | `1` |
| `AUC_central_ug_day_mL` | Accumulated central exposure | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_markovic_2024_vedolizumab_clearance_remission_poppk --model-version 0.1.0 --scenario induction-q8w-no-prior-anti-tnf --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 10 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_central_ug_day_mL` | `1` |
| `CL_effective_L_day_out` | `1` |
| `C_central_ug_mL` | `1` |
| `table2_ATNF_effect_out` | `1` |
| `table2_CL_L_day_out` | `1` |
| `table2_IIV_CL_pct_out` | `1` |
| `table2_residual_error_out` | `1` |
| `table4_cl_clinical_auroc_pct_out` | `1` |
| `table4_cl_endoscopic_auroc_pct_out` | `1` |
| `table4_cl_threshold_L_day_out` | `1` |
| `state__AUC_central_mg_day_L` | `mg*day/L` |
| `state__A_central_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `induction-q8w-no-prior-anti-tnf` starter has **1185 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `C_central_ug_mL` | 0 | 0 (0 d, post) | 129.86 (14.0208 d, pre) | 11.2747 |
| `AUC_central_ug_day_mL` | 0 | 0 (0 d, post) | 41095.5 (1162 d, pre) | 41095.5 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
