# Cai 2024 ustekinumab pediatric IBD PBPK reduced FcRn/lymphatic ODE

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore pediatric ustekinumab distribution with a reduced physiological model.

**Runnable · 8 experiments.** Version 0.1.0.

## Run an experiment

Exploratory calibrated ODE induction plus repeated subcutaneous maintenance simulation. Effective Vc and clearance are calibrated from the induction Cmax and half-life targets; SC absorption, distribution, and FcRn terms are unvalidated effective assumptions. It cannot reproduce native PK-Sim organ/FcRn population ribbons without the project and virtual populations.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_cai_2024_ustekinumab_pediatric_ibd_pbpk_reduced', version='0.1.0')
result = model.run('pediatric-130mg-iv-90mg-sc-q8w-reduced')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `adult-390mg-iv-90mg-sc-q8w-reduced` | Exploratory calibrated ODE induction plus repeated subcutaneous maintenance simulation. Effective Vc and clearance are calibrated from the induction Cmax and half-life targets; SC absorption, distribution, and FcRn terms are unvalidated effective assumptions. It cannot reproduce native PK-Sim organ/FcRn population ribbons without the project and virtual populations. | 0–9000 h | 751 |
| `adult-390mg-iv-induction-adedokun2018` | Exploratory reduced ODE induction probe. Effective Vc and linear clearance are algebraically calibrated from the same paper-predicted Cmax and terminal half-life shown as comparator points, so endpoint agreement is calibration-target replay rather than independent validation. This is not the native 15-organ PK-Sim model. | 0–808.8 h | 41 |
| `exact-main-and-supplement-table-anchor` | Short exact replay of curated public model constants, regimens, virtual-population descriptors, ontogeny factors, dose recommendations, predicted/observed PK endpoints, and sensitivity coefficients. This proves extraction and API field integrity, not independent dynamic prediction. | 0–0.01 h | 2 |
| `pediatric-130mg-iv-90mg-sc-q8w-reduced` | Exploratory calibrated ODE induction plus repeated subcutaneous maintenance simulation. Effective Vc and clearance are calibrated from the induction Cmax and half-life targets; SC absorption, distribution, and FcRn terms are unvalidated effective assumptions. It cannot reproduce native PK-Sim organ/FcRn population ribbons without the project and virtual populations. | 0–9000 h | 751 |
| `pediatric-130mg-iv-induction-rosh2021` | Exploratory reduced ODE induction probe. Effective Vc and linear clearance are algebraically calibrated from the same paper-predicted Cmax and terminal half-life shown as comparator points, so endpoint agreement is calibration-target replay rather than independent validation. This is not the native 15-organ PK-Sim model. | 0–534.24 h | 41 |
| `pediatric-390mg-iv-90mg-sc-q8w-reduced` | Exploratory calibrated ODE induction plus repeated subcutaneous maintenance simulation. Effective Vc and clearance are calibrated from the induction Cmax and half-life targets; SC absorption, distribution, and FcRn terms are unvalidated effective assumptions. It cannot reproduce native PK-Sim organ/FcRn population ribbons without the project and virtual populations. | 0–9000 h | 751 |
| `pediatric-390mg-iv-induction-rosh2021` | Exploratory reduced ODE induction probe. Effective Vc and linear clearance are algebraically calibrated from the same paper-predicted Cmax and terminal half-life shown as comparator points, so endpoint agreement is calibration-target replay rather than independent validation. This is not the native 15-organ PK-Sim model. | 0–547.68 h | 41 |
| `pediatric-9mgkg-iv-induction-rosh2021` | Exploratory reduced ODE induction probe. Effective Vc and linear clearance are algebraically calibrated from the same paper-predicted Cmax and terminal half-life shown as comparator points, so endpoint agreement is calibration-target replay rather than independent validation. This is not the native 15-organ PK-Sim model. | 0–614.4 h | 41 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__A_central_mg` | Ustekinumab amount in the central compartment | `mg` |
| `state__A_fcrn_bound_mg` | Drug amount bound to the recycling receptor FcRn | `mg` |
| `state__AUC_central_mg_h_L` | Accumulated central drug exposure | `mg*h/L` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_cai_2024_ustekinumab_pediatric_ibd_pbpk_reduced --model-version 0.1.0 --scenario pediatric-130mg-iv-90mg-sc-q8w-reduced --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 7 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__AUC_central_mg_h_L` | `mg*h/L` |
| `state__A_central_mg` | `mg` |
| `state__A_endosomal_mg` | `mg` |
| `state__A_fcrn_bound_mg` | `mg` |
| `state__A_peripheral_mg` | `mg` |
| `state__A_sc_depot_mg` | `mg` |
| `state__elapsed_time_h` | `h` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `pediatric-130mg-iv-90mg-sc-q8w-reduced` starter has **751 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__A_central_mg` | 130 | 9.88048 (1344 h, pre) | 130 (0 h, post) | 16.9616 |
| `state__A_fcrn_bound_mg` | 0 | 0 (0 h, post) | 0.292843 (72 h, post) | 0.0637179 |
| `state__AUC_central_mg_h_L` | 0 | 0 (0 h, post) | 92318.1 (9000 h, pre) | 92318.1 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
