# Vu 2017 Erenumab QSS TMDD and CIDBF PK/PD Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore erenumab disposition and capsaicin-induced dermal blood-flow response.

**Retained alternate archive · source and stored-evidence inspection.** Version 0.1.0.

This is an alternate version. [Open the default version](../0.1.1/MODEL_CARD.md) for the standard quickstart.

## Inspect a retained archive

This version is retained for source and stored-evidence inspection. Use the linked current version for the supported simulation quickstart.

Complete [setup](../../../README.md#setup), then run this Python code from any working directory:

```python
from qspquest_models import Library, load_archive

model = load_archive(
    Library().root / 'models/qspquest_vu_2017_erenumab_cidbf_pkpd_tmdd/0.1.0/model.omex',
    expected_sha256='d82b41ccfaf1747814251d3d79dec10533683744c5b040d04b048f47f677a4d7',
)
print(model.model_id, model.index['model_version'])
print(model.scenario_ids)
```

### Archived experiments

A preset is a named experiment with fixed inputs. Summary and table replays return stored
values; they are not new fits and may not change over time.

<details>
<summary>Browse all 13 runnable experiments</summary>

| Archived experiment ID | Purpose | Time range | Rows |
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

The archived primary table contains `time`, `side` and the readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Unit |
| --- | --- | --- |
| `total_concentration_ug_mL` | Total erenumab concentration | `1` |
| `cidbf_inhibition_pct` | Inhibition of capsaicin-induced dermal blood flow | `1` |

The table describes archived primary readouts. Use the current-version guide for supported simulation and CSV or R data-frame export.

<details>
<summary>Technical inventory: 65 outputs and 6 states</summary>

| Technical column | Unit |
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

Column names follow the source paper. A unit of `1` means the engine uses the source's number
as-is, without a physical unit or conversion; do not infer a unit from the column name.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Stored reference result

The `sc-70mg-q4w-75kg-dynamic` starter has **85 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `total_concentration_ug_mL` | 0 | 0 (0 h, post) | 10.0224 (61 h, post) | 5.54912 |
| `cidbf_inhibition_pct` | 0 | 0 (0 h, post) | 89.2983 (61 h, post) | 89.2833 |

These rounded values help you recognize the expected result; they are not pass/fail tolerances.
The [full starter reference](starter-preview.json) contains simulated values produced by running this archive.
The original stored CSV may omit states.
[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Units have not been independently checked for this version.

## Reference

[Source and reuse terms](SOURCE_REFERENCE.md) · [Archive format](../../../tutorials/model-format.md)
