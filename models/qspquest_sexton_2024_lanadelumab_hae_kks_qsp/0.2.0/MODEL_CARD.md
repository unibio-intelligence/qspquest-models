# Sexton 2024 Lanadelumab HAE Plasma Kallikrein-Kinin QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore lanadelumab effects on the kallikrein-kinin system.

**Runnable · 1 experiment.** Version 0.2.0.

## Run an experiment

Replay of the public SI author-code smoke run for the first sampled virtual patient. The internal model clock starts at 0 h; reported paper/author time is internal time minus 3016 h.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_sexton_2024_lanadelumab_hae_kks_qsp', version='0.2.0')
result = model.run('first-virtual-patient-150mg-q2w-author-replay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `first-virtual-patient-150mg-q2w-author-replay` | Replay of the public SI author-code smoke run for the first sampled virtual patient. The internal model clock starts at 0 h; reported paper/author time is internal time minus 3016 h. | 0–9400 h | 147 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `PK_Conc_Central_in_nM` | Lanadelumab concentration in the central compartment | `nmol/L` |
| `CS_RO_BDKRB2` | Bradykinin B2 receptor occupancy | `1` |
| `CS_prct_HK2Chain` | Percentage of two-chain high-molecular-weight kininogen | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_sexton_2024_lanadelumab_hae_kks_qsp --model-version 0.2.0 --scenario first-virtual-patient-150mg-q2w-author-replay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 14 outputs and 61 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AA_Fold_profile` | `1` |
| `CS_FXII_in_plasma_ngml` | `1` |
| `CS_FXIIa_in_plasma_ngml` | `1` |
| `CS_RO_BDKRB2` | `1` |
| `CS_Total_HMWK_in_plasma` | `1` |
| `CS_Total_preKAL_in_plasma` | `1` |
| `CS_prct_HK2Chain` | `1` |
| `CS_prct_HK2Chain_normalized` | `1` |
| `CS_preKAL_prct_free` | `1` |
| `PK_Amount_SC` | `mg` |
| `PK_Conc_Central_in_nM` | `nmol/L` |
| `PK_Conc_Central_in_ugml` | `ug/mL` |
| `reported_time_h` | `1` |
| `validation_run_nonce_echo` | `1` |
| `state__CS_BDKRB2` | `1` |
| `state__CS_BDKRB2_degraded` | `1` |
| `state__CS_BK` | `1` |
| `state__CS_BK_BDKRB2` | `1` |
| `state__CS_BK_BDKRB2_degraded` | `1` |
| `state__CS_BK_degraded` | `1` |
| `state__CS_BK_in_plasma` | `1` |
| `state__CS_C1Inh` | `1` |
| `state__CS_C1Inh_FXIIa` | `1` |
| `state__CS_C1Inh_FXIIa_degraded` | `1` |
| `state__CS_C1Inh_FXIIa_gC1qR` | `1` |
| `state__CS_C1Inh_FXIIa_gC1qR_degraded` | `1` |
| `state__CS_C1Inh_FXIIa_in_plasma` | `1` |
| `state__CS_C1Inh_KAL_HMWK` | `1` |
| `state__CS_C1Inh_KAL_HMWK_degraded` | `1` |
| `state__CS_C1Inh_KAL_HMWK_gC1qR` | `1` |
| `state__CS_C1Inh_KAL_HMWK_gC1qR_degraded` | `1` |
| `state__CS_C1Inh_KAL_HMWK_in_plasma` | `1` |
| `state__CS_C1Inh_KAL_degraded` | `1` |
| `state__CS_C1Inh_KAL_in_plasma` | `1` |
| `state__CS_C1Inh_degraded` | `1` |
| `state__CS_C1Inh_in_plasma` | `1` |
| `state__CS_FXII` | `1` |
| `state__CS_FXII_degraded` | `1` |
| `state__CS_FXII_gC1qR` | `1` |
| `state__CS_FXII_gC1qR_degraded` | `1` |
| `state__CS_FXII_in_plasma` | `1` |
| `state__CS_FXIIa` | `1` |
| `state__CS_FXIIa_degraded` | `1` |
| `state__CS_FXIIa_gC1qR` | `1` |
| `state__CS_FXIIa_gC1qR_degraded` | `1` |
| `state__CS_FXIIa_in_plasma` | `1` |
| `state__CS_HK2Chain_degraded` | `1` |
| `state__CS_HK2Chain_in_plasma` | `1` |
| `state__CS_HMWK_degraded` | `1` |
| `state__CS_HMWK_in_plasma` | `1` |
| `state__CS_KAL_HK2Chain` | `1` |
| `state__CS_KAL_HK2Chain_gC1qR` | `1` |
| `state__CS_KAL_HK2Chain_gC1qR_degraded` | `1` |
| `state__CS_KAL_HK2Chain_in_plasma` | `1` |
| `state__CS_KAL_HMWK` | `1` |
| `state__CS_KAL_HMWK_gC1qR` | `1` |
| `state__CS_KAL_HMWK_gC1qR_degraded` | `1` |
| `state__CS_KAL_HMWK_in_plasma` | `1` |
| `state__CS_KAL_degraded` | `1` |
| `state__CS_KAL_in_plasma` | `1` |
| `state__CS_Lanadelumab_KAL_HMWK` | `1` |
| `state__CS_Lanadelumab_KAL_HMWK_gC1qR` | `1` |
| `state__CS_Lanadelumab_KAL_HMWK_gC1qR_degraded` | `1` |
| `state__CS_Lanadelumab_KAL_HMWK_in_plasma` | `1` |
| `state__CS_Lanadelumab_KAL_in_plasma` | `1` |
| `state__CS_gC1qR` | `1` |
| `state__CS_gC1qR_degraded` | `1` |
| `state__CS_preKAL_HMWK` | `1` |
| `state__CS_preKAL_HMWK_gC1qR` | `1` |
| `state__CS_preKAL_HMWK_gC1qR_degraded` | `1` |
| `state__CS_preKAL_HMWK_in_plasma` | `1` |
| `state__CS_preKAL_degraded` | `1` |
| `state__CS_preKAL_in_plasma` | `1` |
| `state__PK_Amount_SC` | `mg` |
| `state__PK_Conc_Central_in_ugml` | `ug/mL` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `first-virtual-patient-150mg-q2w-author-replay` starter has **147 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `PK_Conc_Central_in_nM` | 0 | -7.60785e-18 (2856 h, post) | 118.656 (5452.4 h, pre) | 1.47639 |
| `CS_RO_BDKRB2` | 0 | 0 (0 h, post) | 68.4571 (2530.4 h, pre) | 48.888 |
| `CS_prct_HK2Chain` | 0 | 0 (0 h, post) | 82.2145 (2530.4 h, pre) | 73.0344 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Only the PK dose and concentration coordinates described above carry explicit physical units. Other coordinates and complete model dimensions remain unqualified.

<details>
<summary>Availability and qualification</summary>

Execution: `dynamic`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect, run_preset, exploratory_simulation.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:83fd13ea949eaae58ee806789ab754f72f700eb4ade14b5b5bcce57d65151a0a`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Full runtime translation of the Sexton 2024 hereditary angioedema plasma kallikrein-kinin system model for lanadelumab. The model uses the public supplementary R/C source code: 61 states, 82 base biochemical parameters, sampled virtual-patient PK and acute-attack forcing, and SC 150 mg q2w dosing.

<details>
<summary>Output identities</summary>

Lanadelumab depot amount and central plasma mass and molar concentrations.

Depot amount uses mg; central mass concentration uses ug/mL (numerically mg/L); the molar output uses nmol/L (nM) and the source molecular mass. Other contact-system coordinates retain unqualified source numerical values.

Retained source PK amount, central concentration and molecular-mass definitions.

| Readout | Analyte identifier | Compartment identifier | Returned native unit | Archive source label |
| --- | --- | --- | --- | --- |
| `PK_Amount_SC` | `lanadelumab` | `subcutaneous_depot` | `mg` | `mg` |
| `PK_Conc_Central_in_nM` | `lanadelumab` | `central_plasma` | `nmol/L` | `nmol/L` |
| `PK_Conc_Central_in_ugml` | `lanadelumab` | `central_plasma` | `ug/mL` | `ug/mL` |

Inspect the same declarations using `model.output_semantics`. An undeclared identity is `None`; it is not inferred from the readout name.

</details>

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
