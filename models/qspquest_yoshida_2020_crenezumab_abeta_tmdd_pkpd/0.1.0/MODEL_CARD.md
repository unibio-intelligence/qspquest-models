# Yoshida 2020 crenezumab Abeta TMDD PK/PD model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore crenezumab binding and amyloid-beta PK/PD dynamics.

**Runnable · 4 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect q4w IV simulation at the Fig. 7 reference dose and one of the Fig. 8 dose levels.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yoshida_2020_crenezumab_abeta_tmdd_pkpd', version='0.1.0')
result = model.run('fig8-60mgkg-q4w-iv-source-limited')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `fig8-120mgkg-q4w-iv-source-limited` | Fixed-effect high-dose q4w IV simulation using Table 2 parameters. | 0–168 h | 169 |
| `fig8-15mgkg-q4w-iv-source-limited` | Fixed-effect q4w IV simulation using Table 2 parameters. Paper Fig. 8 dose-color raster curves are digitized as source-limited comparators; author simulation coordinates and line-style-separated curves are unavailable. | 0–168 h | 169 |
| `fig8-60mgkg-q4w-iv-source-limited` | Fixed-effect q4w IV simulation at the Fig. 7 reference dose and one of the Fig. 8 dose levels. | 0–168 h | 169 |
| `table1-table2-exact-anchor` | Exact replay of study design, population sizes, and Table 2 fixed-effect parameter values. | 0–1 h | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `Ccren_nM` | Crenezumab concentration | `1` |
| `free_abeta40_pM` | Unbound amyloid-beta 40 concentration | `1` |
| `free_abeta42_pM` | Unbound amyloid-beta 42 concentration | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_yoshida_2020_crenezumab_abeta_tmdd_pkpd --model-version 0.1.0 --scenario fig8-60mgkg-q4w-iv-source-limited --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 61 outputs and 9 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_crenezumab_nM_day` | `1` |
| `AUC_free_abeta40_pM_day` | `1` |
| `AUC_free_abeta42_pM_day` | `1` |
| `BWT_on_CLel` | `1` |
| `BWT_on_CLint` | `1` |
| `BWT_on_Vcent` | `1` |
| `CLel_L_day` | `1` |
| `CLint_L_day` | `1` |
| `Ccren_nM` | `1` |
| `Cperiph_nM` | `1` |
| `Fsc_fraction` | `1` |
| `Ka_1_day` | `1` |
| `Kd_abeta40_nM` | `1` |
| `Kd_abeta42_nM` | `1` |
| `Q_L_day` | `1` |
| `T_abeta40_pM` | `1` |
| `T_abeta42_pM` | `1` |
| `Vcent_L` | `1` |
| `Vperiph_L` | `1` |
| `abby_patients_n` | `1` |
| `abeta40_Q_L_day` | `1` |
| `abeta40_Vperiph_L` | `1` |
| `abeta40_age_on_baseline` | `1` |
| `abeta40_baseline_pM` | `1` |
| `abeta40_gfr_on_baseline` | `1` |
| `abeta40_kdeg_1_day` | `1` |
| `abeta40_kdeg_complex_1_day_text` | `1` |
| `abeta42_Q_L_day` | `1` |
| `abeta42_Vperiph_L` | `1` |
| `abeta42_baseline_pM` | `1` |
| `abeta42_gfr_on_baseline` | `1` |
| `abeta42_kdeg_1_day` | `1` |
| `abeta42_kdeg_complex_1_day_text` | `1` |
| `blaze_patients_n` | `1` |
| `central_half_life_day` | `1` |
| `complex40_pM` | `1` |
| `complex42_pM` | `1` |
| `complex_half_life_day` | `1` |
| `csf_pkpd_patients_n` | `1` |
| `csf_serum_ratio_pct` | `1` |
| `dose_120mgkg_nmol` | `1` |
| `dose_15mgkg_nmol` | `1` |
| `dose_60mgkg_nmol` | `1` |
| `figure7_dose_mg_kg` | `1` |
| `free_abeta40_fraction` | `1` |
| `free_abeta40_pM` | `1` |
| `free_abeta42_fraction` | `1` |
| `free_abeta42_pM` | `1` |
| `kel_1_day` | `1` |
| `kint_complex_1_day` | `1` |
| `paper_half_life_day` | `1` |
| `phase_ib_patients_n` | `1` |
| `reference_age_year` | `1` |
| `reference_gfr_mL_min_1_73m2` | `1` |
| `reference_weight_kg` | `1` |
| `sc_300mg_nmol` | `1` |
| `sc_bioavailability_pct` | `1` |
| `serum_pk_patients_n` | `1` |
| `sex_male_on_kdeg` | `1` |
| `total_abeta40_fold` | `1` |
| `total_abeta42_fold` | `1` |
| `state__AUC_crenezumab_nM_day` | `nM*day` |
| `state__AUC_free_abeta40_pM_day` | `pM*day` |
| `state__AUC_free_abeta42_pM_day` | `pM*day` |
| `state__A_central_nmol` | `nmol` |
| `state__A_depot_nmol` | `nmol` |
| `state__A_peripheral_nmol` | `nmol` |
| `state__T_abeta40_pM` | `pM` |
| `state__T_abeta42_pM` | `pM` |
| `state__elapsed_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `fig8-60mgkg-q4w-iv-source-limited` starter has **169 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `Ccren_nM` | 10352 | 1876.55 (28 h, pre) | 12564.9 (141 h, post) | 3360 |
| `free_abeta40_pM` | 0.164415 | 0.164415 (0 h, post) | 98.1791 (28 h, pre) | 78.2216 |
| `free_abeta42_pM` | 0.00540784 | 0.00540784 (0 h, post) | 4.88561 (28 h, pre) | 4.24637 |

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
Evidence identity: `sha256:dc9ea73a9359963aadf34480d12cfbfb98ce27614093674a4eef434a12492555`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Reduced fixed-effect implementation of Yoshida et al. 2020 for crenezumab two-compartment PK and plasma Abeta(1-40)/(1-42) target-mediated drug-disposition pharmacodynamics.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
