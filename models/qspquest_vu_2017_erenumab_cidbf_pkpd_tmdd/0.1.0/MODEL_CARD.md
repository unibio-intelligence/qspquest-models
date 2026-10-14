# Vu 2017 Erenumab QSS TMDD and CIDBF PK/PD Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore erenumab disposition and capsaicin-induced dermal blood-flow response.

**Runnable · 13 experiments.** Version 0.1.0.

## Run an experiment

Monthly 70 mg SC dose-selection simulation at the phase 1 median body weight; paper reports all subjects were expected to exceed mean IC99 within the first dose.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_vu_2017_erenumab_cidbf_pkpd_tmdd', version='0.1.0')
result = model.run('sc-70mg-q4w-75kg-dynamic')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 13 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `iv-140mg-single-infusion-dynamic` | IV infusion path exercising the paper's Atot(0)=DoseIV branch using an input rate into the central total amount. This is a runtime smoke scenario, not a reproduced figure. | 0–84 h | 86 |
| `paper-population-and-threshold-checks` | Exact paper and supplement text values for data size, ADA counts, IC99, nonlinear clearance, body-weight percentiles, and selected dose-regimen statements. | 0–1 h | 2 |
| `sc-21mg-q4w-68kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 68 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-21mg-q4w-75kg-dynamic` | Monthly 21 mg SC dose-selection simulation at the phase 1 median body weight; paper reports this regimen placed more than 50% of subjects above IC99 after the second dose in stochastic simulations. | 0–84 h | 85 |
| `sc-21mg-q4w-75kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 75 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-21mg-q4w-84kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 84 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-70mg-q4w-68kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 68 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-70mg-q4w-75kg-dynamic` | Monthly 70 mg SC dose-selection simulation at the phase 1 median body weight; paper reports all subjects were expected to exceed mean IC99 within the first dose. | 0–84 h | 85 |
| `sc-70mg-q4w-75kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 75 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-70mg-q4w-84kg-s8-dynamic` | Deterministic Supplementary Figure S8 simulation for three monthly SC doses at 84 kg, extended to 24.5 weeks so the published PK and DBF-inhibition terminal decline can be compared. | 0–175 h | 176 |
| `sc-7mg-q4w-75kg-dynamic` | The 7 mg SC monthly dose selected to demonstrate a non-effective dose in phase 2 dose selection; deterministic median-weight simulation without population variability. | 0–84 h | 85 |
| `table3-pk-parameter-estimates` | Exact rounded Table III population PK parameter estimates and random-effect/residual-error summaries. | 0–1 h | 2 |
| `table4-pd-parameter-estimates` | Exact rounded Table IV capsaicin-induced dermal blood-flow PD parameter estimates and variability summaries. | 0–1 h | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `total_concentration_ug_mL` | Total erenumab concentration | `1` |
| `cidbf_inhibition_pct` | Inhibition of capsaicin-induced dermal blood flow | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_vu_2017_erenumab_cidbf_pkpd_tmdd --model-version 0.1.0 --scenario sc-70mg-q4w-75kg-dynamic --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 65 outputs and 6 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `CL_ref_L_day` | `1` |
| `F_bioavailability` | `1` |
| `IC50_ng_mL` | `1` |
| `Imax_fraction` | `1` |
| `Kss_ng_mL` | `1` |
| `Q_L_day` | `1` |
| `Vc_ref_L` | `1` |
| `Vp_L` | `1` |
| `baseline_dbf_PU` | `1` |
| `bound_complex_ng_mL` | `1` |
| `central_volume_L` | `1` |
| `cidbf_delta_dbf_PU` | `1` |
| `cidbf_inhibition_pct` | `1` |
| `cidbf_inhibition_percent_of_imax` | `1` |
| `hill_coefficient` | `1` |
| `ic99_calculated_ng_mL` | `1` |
| `ka_1_day` | `1` |
| `ka_half_life_calculated_day` | `1` |
| `kc0_1_day` | `1` |
| `kcp_1_day` | `1` |
| `kdeg_1_day` | `1` |
| `kint_1_day` | `1` |
| `kpc_1_day` | `1` |
| `ksyn_ng_mL_day` | `1` |
| `linear_clearance_L_day` | `1` |
| `max_nonlinear_clearance_calculated_L_day` | `1` |
| `nonlinear_clearance_L_day` | `1` |
| `reported_21mg_above_ic99_subject_fraction_pct` | `1` |
| `reported_70mg_first_dose_ic99_fold` | `1` |
| `reported_70mg_third_dose_ic99_fold` | `1` |
| `reported_binding_ada_subjects` | `1` |
| `reported_bql_pk_excluded` | `1` |
| `reported_dbf_measurements` | `1` |
| `reported_dbf_subjects` | `1` |
| `reported_ic99_ng_mL` | `1` |
| `reported_mad_subjects` | `1` |
| `reported_max_nonlinear_clearance_L_day` | `1` |
| `reported_neutralizing_ada_subjects` | `1` |
| `reported_pk_concentrations` | `1` |
| `reported_pk_subjects` | `1` |
| `reported_sad_subjects` | `1` |
| `reported_sc_absorption_complete_approx_day` | `1` |
| `reported_sc_absorption_half_life_day` | `1` |
| `reported_total_pkpd_subjects` | `1` |
| `reported_weight_25th_kg` | `1` |
| `reported_weight_50th_kg` | `1` |
| `reported_weight_75th_kg` | `1` |
| `table3_bsv_cl_cv_pct` | `1` |
| `table3_bsv_ka_cv_pct` | `1` |
| `table3_bsv_kint_cv_pct` | `1` |
| `table3_bsv_vc_cv_pct` | `1` |
| `table3_eta_cl_ka_cov` | `1` |
| `table3_eta_cl_kint_cov` | `1` |
| `table3_pk_residual_cv_pct` | `1` |
| `table4_bsv_baseline_dbf_cv_pct` | `1` |
| `table4_bsv_ic50_cv_pct` | `1` |
| `table4_residual_error_cv_pct` | `1` |
| `table4_residual_variability_PU` | `1` |
| `table4_residual_variability_cv_pct` | `1` |
| `total_auc_ug_day_mL` | `1` |
| `total_clearance_L_day` | `1` |
| `total_concentration_ng_mL` | `1` |
| `total_concentration_ug_mL` | `1` |
| `unbound_concentration_ng_mL` | `1` |
| `unbound_concentration_ug_mL` | `1` |
| `state__AUC_total` | `ug*day/mL` |
| `state__A_depot` | `mg` |
| `state__A_peripheral` | `mg` |
| `state__A_total_central` | `mg` |
| `state__R_total` | `ng/mL` |
| `state__elapsed_time` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `sc-70mg-q4w-75kg-dynamic` starter has **85 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `total_concentration_ug_mL` | 0 | 0 (0 h, post) | 10.0224 (61 h, post) | 5.54912 |
| `cidbf_inhibition_pct` | 0 | 0 (0 h, post) | 89.2983 (61 h, post) | 89.2833 |

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
Evidence identity: `sha256:6eb5d26f99c532983e37ad2c0510d1163e00f770dad515d4ecce9d19f61839d1`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Paper-derived erenumab population PK/PD model from Vu et al. 2017. The runtime implements the two-compartment quasi-steady-state target-mediated drug-disposition model with first-order SC absorption, IV infusion input, body-weight allometry on CL and Vc, receptor turnover, nonlinear target-mediated clearance, and the direct inhibitory Emax-Hill capsaicin-induced dermal blood-flow pharmacodynamic model.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
