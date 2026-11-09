# Sexton 2024 Lanadelumab HAE Plasma Kallikrein-Kinin QSP

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore lanadelumab effects on the kallikrein-kinin system.

**Runnable · 1 experiment.** Version 0.3.0.

## Run an experiment

Replay of the public SI author-code smoke run for the first sampled virtual patient. The internal model clock starts at 0 h; reported paper/author time is internal time minus 3016 h.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library

model = Library().load('qspquest_sexton_2024_lanadelumab_hae_kks_qsp', version='0.3.0')
result = model.run('first-virtual-patient-150mg-q2w-author-replay')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `first-virtual-patient-150mg-q2w-author-replay` | Replay of the public SI author-code smoke run for the first sampled virtual patient. The internal model clock starts at 0 h; reported paper/author time is internal time minus 3016 h. | 0–9400 h | 147 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `PK_Conc_Central_in_nM` | Lanadelumab concentration in the central compartment | `nmol/L` |
| `CS_RO_BDKRB2` | Bradykinin B2 receptor occupancy | `1` |
| `CS_prct_HK2Chain` | Percentage of two-chain high-molecular-weight kininogen | `1` |

Python exports these primary readouts by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --model qspquest_sexton_2024_lanadelumab_hae_kks_qsp --model-version 0.3.0 --scenario first-virtual-patient-150mg-q2w-author-replay --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 13 outputs and 61 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `first-virtual-patient-150mg-q2w-author-replay` starter has **147 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `PK_Conc_Central_in_nM` | 0 | -6.29842e-18 (2121.8 h, pre) | 118.656 (5452.4 h, pre) | 1.47639 |
| `CS_RO_BDKRB2` | 0 | 0 (0 h, post) | 68.4571 (2530.4 h, pre) | 48.888 |
| `CS_prct_HK2Chain` | 0 | 0 (0 h, post) | 82.2145 (2530.4 h, pre) | 73.0344 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Only the PK dose and concentrations above declare physical units; no units have been independently checked.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
