# Haid 2023 PROTAC mechanistic pharmacodynamic framework

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore a mechanistic framework for PROTAC pharmacodynamics.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

ODE form of Eq. 14 at C = steady-state DCmax, using t1/2,P = 45 h and steady-state Table 1 hook parameters to reproduce the reported 6 h, 24 h, and steady-state Dmax endpoints.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_haid_2023_protac_mechanistic_pd_framework', version='0.1.0')
result = model.run('mares-ripk2-hook-timecourse')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `exact-article-si-source-checks` | One-hour exact replay of all public table/source anchors carried as derived outputs. | 0–1 h | 2 |
| `mares-ripk2-hook-timecourse` | ODE form of Eq. 14 at C = steady-state DCmax, using t1/2,P = 45 h and steady-state Table 1 hook parameters to reproduce the reported 6 h, 24 h, and steady-state Dmax endpoints. | 0–96 h | 97 |
| `ramos-cpd-i-mechanistic-te-ode` | Illustrative Eq. 8 mechanistic target-engagement ODE using Supplement Table S1 Cpd I and Supplement Table S2 Ramos parameters. kcat is user-overridable because the public paper does not report a fitted kcat for this exact combination. | 0–48 h | 49 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `mechanistic_degradation` | Target degradation predicted by the mechanistic model | `1` |
| `pd_response` | Pharmacodynamic response in the source scale | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_haid_2023_protac_mechanistic_pd_framework --model-version 0.1.0 --scenario mares-ripk2-hook-timecourse --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 85 outputs and 3 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `alpha` | `1` |
| `e0_nm` | `1` |
| `ec50_nm` | `1` |
| `emax` | `1` |
| `emax_degradation` | `1` |
| `hill_n` | `1` |
| `hook_closed_form_degradation` | `1` |
| `hook_closed_form_degradation_pct` | `1` |
| `hook_dc50_nm` | `1` |
| `hook_dcmax_nm` | `1` |
| `hook_degradation` | `1` |
| `hook_degradation_pct` | `1` |
| `hook_dmax_ss` | `1` |
| `hook_dss` | `1` |
| `hook_dss_den` | `1` |
| `hook_dss_num` | `1` |
| `hook_p_ss` | `1` |
| `hook_rate_h` | `1` |
| `ic50_nm` | `1` |
| `inhibition_fraction` | `1` |
| `kcat_h` | `1` |
| `kd_e_nm` | `1` |
| `kd_p_nm` | `1` |
| `kdeg_p_h` | `1` |
| `mechanistic_degradation` | `1` |
| `p0_nm` | `1` |
| `p50` | `1` |
| `pd_min` | `1` |
| `pd_response` | `1` |
| `protac_conc_nm` | `1` |
| `source_article_pdf_fetched_flag` | `1` |
| `source_cited_by_count_queue` | `1` |
| `source_mdpi_direct_blocked_flag` | `1` |
| `source_pmc_html_fetched_flag` | `1` |
| `source_publication_year` | `1` |
| `source_supplement_zip_fetched_flag` | `1` |
| `t_half_p_h` | `1` |
| `table1_24h_dc50_nm` | `1` |
| `table1_24h_dcmax_nm` | `1` |
| `table1_24h_dmax_pct` | `1` |
| `table1_6h_dc50_nm` | `1` |
| `table1_6h_dcmax_nm` | `1` |
| `table1_6h_dmax_pct` | `1` |
| `table1_steady_state_dc50_nm` | `1` |
| `table1_steady_state_dcmax_nm` | `1` |
| `table1_steady_state_dmax_pct` | `1` |
| `table_s1_cpd_a_alpha` | `1` |
| `table_s1_cpd_a_kd_e_nm` | `1` |
| `table_s1_cpd_a_kd_p_nm` | `1` |
| `table_s1_cpd_b_alpha` | `1` |
| `table_s1_cpd_b_kd_e_nm` | `1` |
| `table_s1_cpd_b_kd_p_nm` | `1` |
| `table_s1_cpd_c_alpha` | `1` |
| `table_s1_cpd_c_kd_e_nm` | `1` |
| `table_s1_cpd_c_kd_p_nm` | `1` |
| `table_s1_cpd_d_alpha` | `1` |
| `table_s1_cpd_d_kd_e_nm` | `1` |
| `table_s1_cpd_d_kd_p_nm` | `1` |
| `table_s1_cpd_e_alpha` | `1` |
| `table_s1_cpd_e_kd_e_nm` | `1` |
| `table_s1_cpd_e_kd_p_nm` | `1` |
| `table_s1_cpd_f_alpha` | `1` |
| `table_s1_cpd_f_kd_e_nm` | `1` |
| `table_s1_cpd_f_kd_p_nm` | `1` |
| `table_s1_cpd_g_alpha` | `1` |
| `table_s1_cpd_g_kd_e_nm` | `1` |
| `table_s1_cpd_g_kd_p_nm` | `1` |
| `table_s1_cpd_h_alpha` | `1` |
| `table_s1_cpd_h_kd_e_nm` | `1` |
| `table_s1_cpd_h_kd_p_nm` | `1` |
| `table_s1_cpd_i_alpha` | `1` |
| `table_s1_cpd_i_kd_e_nm` | `1` |
| `table_s1_cpd_i_kd_p_nm` | `1` |
| `table_s2_ramos_e0_nm` | `1` |
| `table_s2_ramos_p0_nm` | `1` |
| `table_s2_ramos_t_half_h` | `1` |
| `table_s2_ratsplenocytes_e0_nm` | `1` |
| `table_s2_ratsplenocytes_p0_nm` | `1` |
| `table_s2_ratsplenocytes_t_half_h` | `1` |
| `table_s2_thp1_e0_nm` | `1` |
| `table_s2_thp1_p0_nm` | `1` |
| `table_s2_thp1_t_half_h` | `1` |
| `target_modulation` | `1` |
| `te_simplified` | `1` |
| `validation_run_nonce` | `1` |
| `state__elapsed_h` | `h` |
| `state__p_hook_rel` | `fraction of baseline` |
| `state__p_mech_rel` | `fraction of baseline` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `mares-ripk2-hook-timecourse` starter has **97 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `mechanistic_degradation` | 0 | 0 (0 h, post) | 0.445796 (96 h, pre) | 0.445796 |
| `pd_response` | 0.666989 | 0.369648 (96 h, pre) | 0.666989 (0 h, post) | 0.369648 |

These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.
[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.
The original stored CSV may omit states; the starter reference includes the primary readouts above.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
