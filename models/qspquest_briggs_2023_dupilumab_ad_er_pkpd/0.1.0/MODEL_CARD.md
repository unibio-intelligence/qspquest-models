# Briggs 2023 dupilumab AD exposure-response PK/PD

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore dupilumab exposure-response relationships in atopic dermatitis.

**Runnable · 3 experiments.** Version 0.1.0.

## Run an experiment

Fixed-effect adult scenario approximating Figure 4/5 adult reference simulations.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_briggs_2023_dupilumab_ad_er_pkpd', version='0.1.0')
result = model.run('adult-severe-300mg-q2w-16weeks')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `adult-severe-300mg-q2w-16weeks` | Fixed-effect adult scenario approximating Figure 4/5 adult reference simulations. | 0–112 d | 17 |
| `child-severe-200mg-q2w-16weeks` | Fixed-effect child scenario using Supplement Table S1 child PK and Figure 4 child comparator points. | 0–112 d | 17 |
| `source-table-parameter-checks` | Exact replay of article Table II/III and Supplement Table S1/S3 scalar anchors. | 0–1 d | 2 |

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `central_conc_mg_l` | Dupilumab concentration in the central compartment | `1` |
| `easi_score` | Eczema severity score | `1` |
| `easi_change_from_baseline_pct` | Percentage change in eczema severity from baseline | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_briggs_2023_dupilumab_ad_er_pkpd --model-version 0.1.0 --scenario adult-severe-300mg-q2w-16weeks --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 128 outputs and 11 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `ada_positive` | `1` |
| `adult_cl_l_day_exact` | `1` |
| `adult_q_l_day_exact` | `1` |
| `adult_v3_l_exact` | `1` |
| `age_delta_decade` | `1` |
| `age_year` | `1` |
| `albumin_g_l` | `1` |
| `albumin_ratio` | `1` |
| `asian_race` | `1` |
| `baseline_easi_score` | `1` |
| `baseline_eos_10e9_l` | `1` |
| `baseline_tarc_pg_ml` | `1` |
| `bmi_kg_m2` | `1` |
| `bmi_ratio` | `1` |
| `body_weight_kg` | `1` |
| `cavg_mg_l` | `1` |
| `central_conc_mg_l` | `1` |
| `cl_l_day` | `1` |
| `easi75_response_approx` | `1` |
| `easi90_response_approx` | `1` |
| `easi_age_baseline` | `1` |
| `easi_asian_drug` | `1` |
| `easi_base_tukey` | `1` |
| `easi_base_tukey_source` | `1` |
| `easi_baseline_score_exact` | `1` |
| `easi_change_from_baseline_pct` | `1` |
| `easi_effect_half_life_day` | `1` |
| `easi_et50_day` | `1` |
| `easi_ic50_mg_l` | `1` |
| `easi_imax` | `1` |
| `easi_imax_cov` | `1` |
| `easi_kin_tukey_day` | `1` |
| `easi_kout_day` | `1` |
| `easi_lambda` | `1` |
| `easi_log_eos_baseline` | `1` |
| `easi_log_eos_drug` | `1` |
| `easi_log_tarc_baseline` | `1` |
| `easi_placebo_tukey` | `1` |
| `easi_pmax` | `1` |
| `easi_pmax_cov` | `1` |
| `easi_prior_baseline` | `1` |
| `easi_prior_pmax` | `1` |
| `easi_ratio` | `1` |
| `easi_score` | `1` |
| `easi_tcs_baseline` | `1` |
| `easi_tcs_pmax` | `1` |
| `easi_transformed` | `1` |
| `easi_weight_drug` | `1` |
| `eos_ratio` | `1` |
| `f_sc` | `1` |
| `iga_0_1_prob_approx` | `1` |
| `iga_age_pmax` | `1` |
| `iga_asian_drug` | `1` |
| `iga_base_le3` | `1` |
| `iga_base_q3` | `1` |
| `iga_beta_le0` | `1` |
| `iga_beta_le1` | `1` |
| `iga_beta_le2` | `1` |
| `iga_dslp` | `1` |
| `iga_dslp_cov` | `1` |
| `iga_effect_half_life_day` | `1` |
| `iga_et50_day` | `1` |
| `iga_ic50_mg_l` | `1` |
| `iga_kout_day` | `1` |
| `iga_latent_le1` | `1` |
| `iga_log_eos_drug` | `1` |
| `iga_log_tarc_drug` | `1` |
| `iga_moderate_baseline_shift` | `1` |
| `iga_moderate_pmax` | `1` |
| `iga_placebo` | `1` |
| `iga_pmax` | `1` |
| `iga_pmax_cov` | `1` |
| `iga_prior_pmax` | `1` |
| `iga_q0` | `1` |
| `iga_q1` | `1` |
| `iga_q2` | `1` |
| `iga_tcs_pmax` | `1` |
| `iga_weight_drug` | `1` |
| `k23_day` | `1` |
| `k32_day` | `1` |
| `ka_day` | `1` |
| `ke_ada_effect` | `1` |
| `ke_bmi_power` | `1` |
| `ke_day` | `1` |
| `ke_easi_power` | `1` |
| `ke_ind_day` | `1` |
| `ke_white_effect` | `1` |
| `km_mg_l` | `1` |
| `ktr_day` | `1` |
| `linear_elim_mg_day` | `1` |
| `moderate_iga_flag` | `1` |
| `mtt_day` | `1` |
| `nonlinear_elim_mg_day` | `1` |
| `peripheral_conc_mg_l` | `1` |
| `prior_immunotherapy_flag` | `1` |
| `q_l_day` | `1` |
| `reference_age_year` | `1` |
| `reference_albumin_g_l` | `1` |
| `reference_bmi_kg_m2` | `1` |
| `reference_body_weight_kg` | `1` |
| `reference_easi_score` | `1` |
| `reference_eos_10e9_l` | `1` |
| `reference_tarc_pg_ml` | `1` |
| `source_adolescents_n` | `1` |
| `source_adults_n` | `1` |
| `source_article_pdf_fetched_flag` | `1` |
| `source_children_n` | `1` |
| `source_citation_rank` | `1` |
| `source_cited_by_count` | `1` |
| `source_easi_observations_n` | `1` |
| `source_iga_observations_n` | `1` |
| `source_nonmem_public_flag` | `1` |
| `source_preprint_found_flag` | `1` |
| `source_publication_year` | `1` |
| `source_si_docx_fetched_flag` | `1` |
| `source_total_patients_n` | `1` |
| `tarc_ratio` | `1` |
| `tcs_flag` | `1` |
| `v2_albumin_power` | `1` |
| `v2_ind_l` | `1` |
| `v2_l` | `1` |
| `v2_weight_power` | `1` |
| `validation_nonce_echo` | `1` |
| `validation_run_nonce` | `1` |
| `vm_mg_l_day` | `1` |
| `vp_ind_l` | `1` |
| `weight_ratio` | `1` |
| `white_race` | `1` |
| `state__auc_mg_day_l` | `mg*day/L` |
| `state__central_mg` | `mg` |
| `state__easi_response_tukey` | `Tukey(EASI)` |
| `state__elapsed_day` | `day` |
| `state__iga_response` | `latent` |
| `state__peripheral_mg` | `mg` |
| `state__sc_depot_mg` | `mg` |
| `state__summary_marker` | `dimensionless` |
| `state__transit1_mg` | `mg` |
| `state__transit2_mg` | `mg` |
| `state__transit3_mg` | `mg` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `adult-severe-300mg-q2w-16weeks` starter has **17 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `central_conc_mg_l` | 0 | 0 (0 d, post) | 84.7063 (105 d, post) | 66.8288 |
| `easi_score` | 32.6 | 6.48988 (112 d, pre) | 32.6 (0 d, post) | 6.48988 |
| `easi_change_from_baseline_pct` | 0 | -80.0924 (112 d, pre) | 0 (0 d, post) | -80.0924 |

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
Evidence identity: `sha256:cfaeecf329d4f513d9c59076aa2fb224b7dc985e484640a5c002936e70fcadc2`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Fixed-effect ODE reconstruction of the Briggs et al. 2023 dupilumab atopic dermatitis population exposure-response model, including SC transit/two-compartment nonlinear PK, EASI indirect response, and IGA latent indirect-response components. Exact table anchors and source-limited paper figure overlays are provided.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
