# Besbassi 2026 CRS QSP locked cytokine network

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore drug exposure, immune activation and cytokine dynamics in a CRS model.

**Runnable · 5 experiments.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.1.1/MODEL_CARD.md) for the standard quickstart.

## Run an experiment

Full ODE scenario for blinatumomab 28 ug/day continuous infusion through day 28; paper comparator status: source_limited_dynamic_peak_parity_pending_author_code.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import load_archive

model = load_archive(
    'models/qspquest_besbassi_2026_crs_qsp_locked_cytokine_network/0.1.0/model.omex',
    expected_sha256='0333e521e44b500ca959da3999d329d05c2e9e4b37ef4ac4cff38261cf87392f',
)
result = model.run('blinatumomab-28ug-day-28day-full-ode-overlay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `blinatumomab-28ug-day-28day-full-ode-overlay` | Full ODE scenario for blinatumomab 28 ug/day continuous infusion through day 28; paper comparator status: source_limited_dynamic_peak_parity_pending_author_code. | 0–672 h | 337 |
| `okt3-5mg-full-ode-overlay` | Full ODE scenario for OKT3 5 mg IV bolus; paper comparator status: source_limited_dynamic_peak_parity_pending_author_code. | 0–72 h | 289 |
| `source-tables-exact-anchor` | No-dose exact replay of published Table 1/Table 2/Table 3/Table 8/Table 9/Table 10 scalar values. | 0–0.1 h | 2 |
| `tgn1412-0p1mgkg-full-ode-overlay` | Full ODE scenario for TGN1412 0.1 mg/kg IV bolus in 70 kg subject; paper comparator status: source_limited_dynamic_peak_parity_pending_author_code. | 0–72 h | 289 |
| `tgn1412-tocilizumab-6h-rescue-overlay` | Full ODE scenario for TGN1412 with tocilizumab rescue at 6 h; paper comparator status: source_limited_qualitative_rescue_overlay. | 0–72 h | 289 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `state__Cdrug_nM` | Drug concentration driving immune activation | `nM` |
| `state__Tact_cells_ul` | Activated T cells | `cells/uL` |
| `state__IL6_pg_ml` | IL-6 cytokine concentration | `pg/mL` |
| `state__IFNg_pg_ml` | Interferon-gamma cytokine concentration | `pg/mL` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

Use the checksum-pinned Python archive command above for this version. The library CLI selects the current default archive.

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 0 outputs and 11 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `state__AUC_IL6_pg_h_ml` | `pg*h/mL` |
| `state__Cdrug_nM` | `nM` |
| `state__IFNg_pg_ml` | `pg/mL` |
| `state__IL10_pg_ml` | `pg/mL` |
| `state__IL1b_pg_ml` | `pg/mL` |
| `state__IL6_pg_ml` | `pg/mL` |
| `state__TNFa_pg_ml` | `pg/mL` |
| `state__Tact_cells_ul` | `cells/uL` |
| `state__Tcyt_cells_ul` | `cells/uL` |
| `state__Texh_cells_ul` | `cells/uL` |
| `state__Trest_cells_ul` | `cells/uL` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `blinatumomab-28ug-day-28day-full-ode-overlay` starter has **337 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `state__Cdrug_nM` | 0 | 0 (0 h, post) | 0.010269 (34 h, post) | 0.010269 |
| `state__Tact_cells_ul` | 0 | 0 (0 h, post) | 14.1858 (666 h, post) | 14.1856 |
| `state__IL6_pg_ml` | 5 | 0.0891003 (10 h, post) | 111.549 (672 h, pre) | 111.549 |
| `state__IFNg_pg_ml` | 0 | 0 (0 h, post) | 63.1761 (672 h, pre) | 63.1761 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
