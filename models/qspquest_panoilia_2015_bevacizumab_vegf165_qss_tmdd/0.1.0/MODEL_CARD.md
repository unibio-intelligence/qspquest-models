# Panoilia 2015 Bevacizumab VEGF165 QSS TMDD PopPK Binding Model

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Explore bevacizumab binding to VEGF165 and target-mediated disposition.

**Runnable · 14 experiments.** Version 0.1.0.

## Run an experiment

Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation.

Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:

```python
from qspquest_models import Library

model = Library('.').load('qspquest_panoilia_2015_bevacizumab_vegf165_qss_tmdd', version='0.1.0')
result = model.run('fig3-5mgkg-q2w-70kg-dynamic')
model.write_csv(result, 'model-example-python.csv')
print(len(result['times']), 'rows')
```

### Choose an experiment

A preset is a named experiment with fixed inputs. Summary/table replays expose retained
values; they are not new parameter fits or necessarily a changing biological trajectory.

<details>
<summary>Browse all 14 runnable experiments</summary>

| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |
| --- | --- | --- | ---: |
| `fig3-5mgkg-q2w-70kg-dynamic` | Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation. | 0–126 d | 136 |
| `fig3-7p5mgkg-q3w-70kg-dynamic` | Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation. | 0–126 d | 133 |
| `fig3-text-and-source-status-checks` | Exact Fig. 3 text values for free VEGF165 decline after 5 mg/kg q2w and 7.5 mg/kg q3w regimens, plus source-packet availability flags. | 0–1 d | 2 |
| `methods-covariate-and-evaluation-checks` | Exact methods and model-evaluation scalar checks: software versions, OFV thresholds, randomization-test size, allometry exponents, two-compartment model improvement, VPC simulations, shrinkage, and Kss genotype randomization-test thresholds. | 0–1 d | 2 |
| `source-review-10mgkg-q2w` | Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation. | 0–126 d | 136 |
| `source-review-5mgkg-q2w-50kg` | Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation. | 0–126 d | 136 |
| `source-review-5mgkg-q2w-90-then-30min` | Typical fixed effects; no original patients, variability or observation noise. First infusion 90 min, subsequent 30 min; conditional Methods schedule, not known patient histories. | 0–126 d | 136 |
| `source-review-5mgkg-q2w-90-then-60min` | Typical fixed effects; no original patients, variability or observation noise. First infusion 90 min, subsequent 60 min; conditional Methods schedule, not known patient histories. | 0–126 d | 136 |
| `source-review-5mgkg-q2w-94kg` | Typical fixed effects; no original patients, variability or observation noise. 85-minute Table 1 median infusion is an explicit Figure 3 approximation. | 0–126 d | 136 |
| `source-review-doubled-baseline-vegf` | Synthetic twofold baseline perturbation verifies the baseline input, initialization and target production. Not a reported patient or paper figure. | 0–126 d | 136 |
| `source-review-untreated-baseline` | Structural equilibrium check; no infusion and no paper patient comparison. | 0–126 d | 127 |
| `table1-patient-study-characteristics` | Exact Table 1 patient/study, dose, infusion, concentration, sampling, and genotype scalar values. | 0–1 d | 2 |
| `table2-in-vitro-free-vegf-assay` | Exact Table 2 average free VEGF165 concentrations after adding bevacizumab at specified molar ratios. | 0–1 d | 2 |
| `table3-pk-and-tmdd-parameter-estimates` | Exact Table 3 population parameter estimates, inter-individual variability, and residual-error values for both PK-only and TMDD models. | 0–1 d | 2 |

</details>

## Inputs and outputs

Each experiment supplies the parameters, initial state, dosing schedule and sampling times.
[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.

`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes
samples before (`pre`) and after (`post`) a dosing or other discrete event.
State columns use `state__`; retained constant source values use `source__`.

| Primary column | Meaning | Archive unit label |
| --- | --- | --- |
| `total_bevacizumab_mg_L` | Total bevacizumab concentration | `1` |
| `free_vegf165_ng_L` | Unbound VEGF165 target concentration | `1` |
| `complex_nM` | Drug-target complex concentration | `1` |

Python exports this small table by default. To export every output and biological state:

```python
model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)
```

The CLI uses the same selection (`--all-readouts` exports the complete table):

```sh
python -m qspquest_models --library . --model qspquest_panoilia_2015_bevacizumab_vegf165_qss_tmdd --model-version 0.1.0 --scenario fig3-5mgkg-q2w-70kg-dynamic --csv model-example-cli.csv
```

In R, `qspquest_data_frame(result)` returns the same primary columns.
Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.
[R setup and examples](../../../tutorials/r-quickstart.md).

<details>
<summary>Technical inventory: 96 outputs and 5 states</summary>

| Technical column | Archive unit label |
| --- | --- |
| `AUC_total_mg_day_L` | `1` |
| `BM0_nM` | `1` |
| `BM0_ng_L` | `1` |
| `CLRC_equals_CL_flag` | `1` |
| `CL_L_day` | `1` |
| `Kss_nM` | `1` |
| `Q_L_day` | `1` |
| `V1_L` | `1` |
| `V2_L` | `1` |
| `backward_deletion_delta_ofv` | `1` |
| `berkeley_madonna_version` | `1` |
| `bev_observations_n` | `1` |
| `central_volume_L` | `1` |
| `clearance_L_day` | `1` |
| `complex_clearance_L_day` | `1` |
| `complex_nM` | `1` |
| `complex_vegf165_ng_L` | `1` |
| `dose_10_mg_kg` | `1` |
| `dose_5_mg_kg` | `1` |
| `dose_5mgkg_at_70kg_mg` | `1` |
| `dose_7p5_mg_kg` | `1` |
| `dose_7p5mgkg_at_70kg_mg` | `1` |
| `epsilon_shrinkage_percent` | `1` |
| `eta_shrinkage_cl_bm0_upper_percent` | `1` |
| `eta_shrinkage_v1_percent` | `1` |
| `figure_images_available` | `1` |
| `figure_level_digitization_available` | `1` |
| `figure_validation_score` | `1` |
| `first_dose_free_vegf_drop_5mgkg_percent` | `1` |
| `first_dose_free_vegf_drop_7p5mgkg_percent` | `1` |
| `forward_inclusion_delta_ofv` | `1` |
| `free_bevacizumab_mg_L` | `1` |
| `free_bevacizumab_nM` | `1` |
| `free_vegf165_nM` | `1` |
| `free_vegf165_ng_L` | `1` |
| `full_text_available` | `1` |
| `half_life_free_vegf_day` | `1` |
| `infusion_duration_min_median` | `1` |
| `intercompartmental_clearance_L_day` | `1` |
| `kin_nM_day` | `1` |
| `kin_ng_L_day` | `1` |
| `kout_1_day` | `1` |
| `median_samples_per_patient_n` | `1` |
| `pdf_available` | `1` |
| `peripheral_volume_L` | `1` |
| `pk_only_CL_L_day` | `1` |
| `pk_only_Q_L_day` | `1` |
| `pk_only_V1_L` | `1` |
| `pk_only_V2_L` | `1` |
| `pk_only_iiv_CL_cv_percent` | `1` |
| `pk_only_iiv_V1_cv_percent` | `1` |
| `pk_only_prop_error_bev_percent` | `1` |
| `pk_two_comp_delta_ofv` | `1` |
| `psn_version` | `1` |
| `randomization_test_datasets_n` | `1` |
| `source_completeness_score` | `1` |
| `source_engine_version` | `1` |
| `study_patients_n` | `1` |
| `subsequent_free_vegf_decline_5mgkg_percent` | `1` |
| `subsequent_free_vegf_decline_7p5mgkg_percent` | `1` |
| `supplement_available` | `1` |
| `table1_age_median_year` | `1` |
| `table1_female_n` | `1` |
| `table1_male_n` | `1` |
| `table1_post_bev_mg_L_median` | `1` |
| `table1_post_free_vegf_ng_L_median` | `1` |
| `table1_pre_bev_mg_L_median` | `1` |
| `table1_pre_free_vegf_ng_L_median` | `1` |
| `table1_weight_max_kg` | `1` |
| `table1_weight_median_kg` | `1` |
| `table1_weight_min_kg` | `1` |
| `table2_1000_ratio_1_0_ng_L` | `1` |
| `table2_1000_ratio_1_0p1_ng_L` | `1` |
| `table2_1000_ratio_1_1000_ng_L` | `1` |
| `table2_1000_ratio_1_1_ng_L` | `1` |
| `table2_250_ratio_1_0_ng_L` | `1` |
| `table2_250_ratio_1_0p1_ng_L` | `1` |
| `table2_250_ratio_1_1000_ng_L` | `1` |
| `table2_250_ratio_1_1_ng_L` | `1` |
| `theta_cl_weight` | `1` |
| `theta_v_weight` | `1` |
| `tmdd_iiv_BM0_cv_percent` | `1` |
| `tmdd_iiv_CL_cv_percent` | `1` |
| `tmdd_iiv_V1_cv_percent` | `1` |
| `tmdd_prop_error_bev_percent` | `1` |
| `tmdd_prop_error_vegf_percent` | `1` |
| `total_bevacizumab_mg_L` | `1` |
| `total_bevacizumab_nM` | `1` |
| `total_vegf165_nM` | `1` |
| `total_vegf165_ng_L` | `1` |
| `validation_run_nonce` | `1` |
| `vegf2578_required_ofv_drop` | `1` |
| `vegf634_required_ofv_drop` | `1` |
| `vegf_observations_n` | `1` |
| `vpc_simulated_datasets_n` | `1` |
| `xpose_version` | `1` |
| `state__AUC_total_mg_day_L` | `mg*day/L` |
| `state__A_peripheral_free_mg` | `mg` |
| `state__A_total_central_mg` | `mg` |
| `state__R_total_relative_to_baseline` | `dimensionless` |
| `state__elapsed_time_day` | `day` |

</details>

The names retain the source conventions. A unit label of `1` means this execution profile
uses numerical source values; a unit-looking column name alone does not establish physical units.
[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.

### Check your result

The `fig3-5mgkg-q2w-70kg-dynamic` starter has **136 rows**. Reference checkpoints:

| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |
| --- | ---: | --- | --- | ---: |
| `total_bevacizumab_mg_L` | 0 | 0 (0 d, post) | 211.87 (112.059 d, pre) | 106.813 |
| `free_vegf165_ng_L` | 212 | 58.1236 (0.0590278 d, pre) | 212 (0 d, post) | 164.412 |
| `complex_nM` | 0 | 0 (0 d, post) | 0.0126649 (112.059 d, pre) | 0.0110355 |

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
Evidence identity: `sha256:0f7cd6ded4ba932595626de118481f4f875e6bb3ac31e74e72fb4c5935d6aad2`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Typical-subject bevacizumab and serum VEGF165 binding model from Panoilia 2015, Eqs 5-10 and Table 3. Stable algebra implements the same QSS root. Independently fitted PK-only model is provided separately. No source population fit or pcVPC reproduction is implied.

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
