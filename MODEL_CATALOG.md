# Choose a model

[Start here](README.md) · [Python](tutorials/python-quickstart.md) · [R](tutorials/r-quickstart.md) · [Understand results](tutorials/understand-results.md)

Browse 72 selected model identities below, grouped by topic. Use your browser’s Find command to search for a drug,
disease or mechanism. Each model guide lists its experiments, outputs and runnable status.
62 selected identities offer dynamic starters; 5 offer source replays; 5 are inspection only.
The archive inventory contains 81 versions; selected versions provide 644 preset requests and 2 fit-ready models.

## Good places to start

| Your question | Start with |
| --- | --- |
| How do I run and plot a published PK/PD model? | [Rituximab and B-cell dynamics](models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.0/MODEL_CARD.md) |
| How does local gating affect tumor versus systemic occupancy? | [Target-gated cargo walkthrough](tutorials/qsp-gated-cargo.md) |
| How does exposure change biomarker turnover? | [Small turnover benchmark](models/qspquest_diffdose_2026_idr_benchmark/0.1.0/MODEL_CARD.md) |

PK describes drug exposure, PD describes drug effects, PBPK describes distribution through
physiological compartments, and QSP describes interacting biological mechanisms.
PopPK in a model name describes its source; these library examples run fixed parameters, not population fits.

## Browse by topic

- [Antibody–drug conjugates and immunotoxins](#antibodydrug-conjugates-and-immunotoxins)
- [Gene delivery and antibody distribution](#gene-delivery-and-antibody-distribution)
- [Inflammation, skin and bowel disease](#inflammation-skin-and-bowel-disease)
- [Learning and synthetic mechanisms](#learning-and-synthetic-mechanisms)
- [Neurology and immune-cell dynamics](#neurology-and-immune-cell-dynamics)
- [Oncology, binding and immune mechanisms](#oncology-binding-and-immune-mechanisms)
- [Other pharmacology and protein distribution](#other-pharmacology-and-protein-distribution)

## Antibody–drug conjugates and immunotoxins

| Model | What it describes | Availability |
| --- | --- | --- |
| [Asiimwe 2025 ADC MBMA/CUI PopPK](models/qspquest_asiimwe_2025_adc_mbma_cui_poppk/0.1.0/MODEL_CARD.md) | Explore fixed-effect T-DM1 and T-DXd exposure; inspect static utility endpoints. | Runnable · 15 experiments |
| [Caimi 2024 loncastuximab CD19 QSP dynamic reconstruction](models/qspquest_caimi_2024_loncastuximab_cd19_qsp/0.1.0/MODEL_CARD.md) | Explore reduced loncastuximab trafficking and tumor response; some experiments are unavailable. | Source replay available; dynamic simulation unavailable · 4 unavailable |
| [Chang 2025 Positively Charged Trastuzumab-vc-MMAE ADC Mouse PK/PD](models/qspquest_chang_2025_charged_trastuzumab_adc_mice_pkpd/0.1.0/MODEL_CARD.md) | Compare charged and wild-type trastuzumab ADC exposure and mouse study endpoints. | Runnable · 37 experiments |
| [Chen 2025 trastuzumab-PE24 AIDE sphere PK/PD](models/qspquest_chen_2025_trastuzumab_aide_pe24_sphere_pkpd/0.1.0/MODEL_CARD.md) | Explore a trastuzumab-PE24 distribution model; some experiments are unavailable. | Source replay available; dynamic simulation unavailable · 4 unavailable |
| [Cheng 2022 SKB264 TROP2 ADC Preclinical PK/PD Table-Replay Model](models/qspquest_cheng_2022_skb264_trop2_adc_preclinical_pkpd/0.1.0/MODEL_CARD.md) | Inspect SKB264 preclinical endpoints and exploratory tumor-growth curves. | Runnable · 47 experiments |
| [Enfortumab vedotin ADC–payload exposure: exploratory reduced model](models/qspquest_choules_2024_enfortumab_vedotin_adc_pbpk_ddi/0.1.0/MODEL_CARD.md) | Explore reduced ADC and payload exposure; this is not the original full PBPK mechanism. | Runnable · 8 experiments |
| [Garrett 2019 Inotuzumab Ozogamicin PopPK Model](models/qspquest_garrett_2019_inotuzumab_ozogamicin_poppk/0.1.0/MODEL_CARD.md) | Explore fixed inotuzumab exposure with time-dependent clearance and covariates. | Runnable · 11 experiments |
| [Op t Hoog 2025 enfortumab vedotin PopPK dosing](models/qspquest_op_t_hoog_2025_enfortumab_vedotin_poppk_dosing/0.1.0/MODEL_CARD.md) | Inspect enfortumab dosing and exposure scenarios; simulation is unavailable. | Inspection only · simulation unavailable |
| [Stathis 2018 IMGN529 NCA Replay and Exploratory Dose-Level PK Surrogate](models/qspquest_stathis_2018_imgn529_cd37_adc_phase1_nca/0.1.0/MODEL_CARD.md) | Inspect IMGN529 NCA endpoints and exploratory exposure curves. | Runnable · 17 experiments |

## Gene delivery and antibody distribution

| Model | What it describes | Availability |
| --- | --- | --- |
| [Liu 2026 reduced AAV-mediated anti-TargetX rat brain QSP](models/qspquest_liu_2026_aav_mab_targetx_rat_brain_reduced_qsp/0.1.0/MODEL_CARD.md) | Explore reduced AAV-driven antibody expression and brain target dynamics. | Runnable · 7 experiments |
| [Whole-body AAV8 gene-delivery and transgene-antibody PBPK](models/qspquest_rajwade_2026_aav8_trastuzumab_nonlinear_pbpk/0.1.0/MODEL_CARD.md) | Explore mouse AAV8 delivery, trastuzumab expression and whole-body antibody distribution. | Runnable · 3 experiments |
| [Whole-body AAV–anti-TargetX rat brain QSP](models/qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp/2.1.2/MODEL_CARD.md) | Compare AAV delivery routes, antibody distribution and brain target engagement in a rat model. | Runnable · 13 experiments |

## Inflammation, skin and bowel disease

| Model | What it describes | Availability |
| --- | --- | --- |
| [Aguilo-Lafarga 2026 Adalimumab IBD PopPK External Validation](models/qspquest_aguilo_lafarga_2026_adalimumab_ibd_poppk_external_validation/0.1.0/MODEL_CARD.md) | Compare fixed adalimumab regimens and inspect published IBD model-validation summaries. | Runnable · 13 experiments |
| [Brekkan 2024 certolizumab ADA bivariate hidden-Markov model](models/qspquest_brekkan_2024_certolizumab_ada_hidden_markov/0.1.0/MODEL_CARD.md) | Inspect certolizumab exposure and anti-drug-antibody state dynamics. | Runnable · 3 experiments |
| [Briggs 2023 dupilumab AD exposure-response PK/PD](models/qspquest_briggs_2023_dupilumab_ad_er_pkpd/0.1.0/MODEL_CARD.md) | Explore dupilumab exposure-response relationships in atopic dermatitis. | Runnable · 3 experiments |
| [Cai 2024 ustekinumab pediatric IBD PBPK reduced FcRn/lymphatic ODE](models/qspquest_cai_2024_ustekinumab_pediatric_ibd_pbpk_reduced/0.1.0/MODEL_CARD.md) | Explore pediatric ustekinumab distribution with a reduced physiological model. | Runnable · 8 experiments |
| [Coto-Segura 2023 certolizumab pegol psoriasis QSP](models/qspquest_coto_segura_2023_certolizumab_pegol_psoriasis_qsp/0.1.0/MODEL_CARD.md) | Explore certolizumab exposure and psoriasis-response mechanisms. | Runnable · 3 experiments |
| [Duvnjak 2026 vedolizumab pregnancy albumin/PK](models/qspquest_duvnjak_2026_vedolizumab_pregnancy_albumin_pk/0.1.0/MODEL_CARD.md) | Inspect the relationship between albumin and vedolizumab exposure during pregnancy. | Source replay available; dynamic simulation unavailable · 4 unavailable |
| [Hemperly 2025 infliximab pediatric IBD PK/ER](models/qspquest_hemperly_2025_infliximab_pediatric_ibd_poc_pk_er/0.1.0/MODEL_CARD.md) | Explore pediatric infliximab exposure and IBD response summaries. | Runnable · 4 experiments |
| [Hyams 2022 Vedolizumab Pediatric HUBBLE PK/NCA/Exposure-Response Intake](models/qspquest_hyams_2022_vedolizumab_pediatric_hubble_pk_nca_er/0.1.0/MODEL_CARD.md) | Inspect pediatric vedolizumab exposure, NCA and response endpoints. | Runnable · 11 experiments |
| [Markovic 2024 Vedolizumab Clearance/Remission PopPK](models/qspquest_markovic_2024_vedolizumab_clearance_remission_poppk/0.1.0/MODEL_CARD.md) | Explore vedolizumab clearance and remission relationships. | Runnable · 9 experiments |
| [Prybylski 2026 dazukibart IFN-beta dermatomyositis ER](models/qspquest_prybylski_2026_dazukibart_ifnb_dm_er/0.1.0/MODEL_CARD.md) | Explore dazukibart exposure-response endpoints in dermatomyositis. | Runnable · 4 experiments |
| [Rodriguez-Fernandez 2024 Secukinumab MIPD Psoriasis PK/PD](models/qspquest_rodriguez_fernandez_2024_secukinumab_psoriasis_mipd/0.1.0/MODEL_CARD.md) | Explore fixed secukinumab exposure and psoriasis-response scenarios. | Runnable · 26 experiments |
| [Rodriguez-Fernandez 2024 Ustekinumab MIPD Psoriasis PK/PD](models/qspquest_rodriguez_fernandez_2024_ustekinumab_mipd_psoriasis/0.1.0/MODEL_CARD.md) | Explore fixed ustekinumab exposure and psoriasis-response scenarios. | Runnable · 3 experiments · 1 unavailable |
| [Thomas 2025 risankizumab precision-dosing dashboard](models/qspquest_thomas_2025_risankizumab_precision_dosing_dashboard/0.1.0/MODEL_CARD.md) | Inspect fixed risankizumab exposure; this is not a clinical dosing service. | Source replay available; dynamic simulation unavailable · 2 unavailable |
| [Waterhouse 2024 Vedolizumab allo-HSCT GvHD prophylaxis PopPK](models/qspquest_waterhouse_2024_vedolizumab_gvhd_allohsct_poppk/0.1.0/MODEL_CARD.md) | Explore fixed vedolizumab exposure in transplant prophylaxis scenarios. | Runnable · 37 experiments |
| [Yarur 2025 ustekinumab clearance/disease-control PK](models/qspquest_yarur_2025_ustekinumab_clearance_ibd_pk/0.1.0/MODEL_CARD.md) | Inspect ustekinumab clearance and IBD disease-control relationships. | Source replay available; dynamic simulation unavailable · 3 unavailable |

## Learning and synthetic mechanisms

| Model | What it describes | Availability |
| --- | --- | --- |
| [Bispecific exposure and ternary binding](models/qspquest_diffdose_2026_bite_benchmark/0.1.0/MODEL_CARD.md) | Compare bispecific exposure and binary versus ternary complex formation. | Runnable · 3 experiments |
| [Drug injury and delayed tumor loss](models/qspquest_diffdose_2026_tgi_benchmark/0.1.0/MODEL_CARD.md) | Explore how drug injury propagates through delayed tumor-cell loss. | Runnable · 3 experiments |
| [Drug-stimulated biomarker turnover](models/qspquest_diffdose_2026_idr_benchmark/0.3.0/MODEL_CARD.md) | Explore how repeated exposure changes biomarker turnover in a small benchmark. | Runnable · 3 experiments |
| [Membrane Ternary Binding](models/qspquest_ubi_2026_membrane_ternary_binding/0.1.2/MODEL_CARD.md) | Explore membrane binding, ternary bridging and loss of bridging at high ligand concentrations. | Runnable · 5 experiments |
| [Target-Gated Cargo QSP](models/qspquest_ubi_2026_target_gated_cargo_qsp/2.0.0/MODEL_CARD.md) | Compare tumor and systemic receptor occupancy under synthetic gating assumptions. | Runnable · 6 experiments |

## Neurology and immune-cell dynamics

| Model | What it describes | Availability |
| --- | --- | --- |
| [Gupta 2025 erenumab rat immune-tolerance PK/PD](models/qspquest_gupta_2025_erenumab_immune_tolerance_pkpd/0.1.0/MODEL_CARD.md) | Inspect a rat erenumab immune-tolerance model; simulation is unavailable. | Inspection only · simulation unavailable |
| [Lee 2023 ATC161 AUTOTAC alpha-synuclein source-limited PK/PD](models/qspquest_lee_2023_atc161_autotac_alpha_syn_pkpd/0.1.0/MODEL_CARD.md) | Inspect ATC161 degradation endpoints and an exploratory reduced PK/PD model. | Runnable · 3 experiments |
| [Li 2024 rituximab pediatric INS B-cell repletion K-PD](models/qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic/0.1.0/MODEL_CARD.md) | Explore B-cell recovery after rituximab in pediatric nephrotic syndrome. | Runnable · 24 experiments |
| [Monteleone 2021 Eculizumab gMG PK/PD](models/qspquest_monteleone_2021_eculizumab_gmg_pkpd/0.1.0/MODEL_CARD.md) | Explore reduced eculizumab exposure and free-C5 response in generalized myasthenia gravis. | Runnable · 7 experiments |
| [Ortiz 2024 ravulizumab NMOSD PK/PD](models/qspquest_ortiz_2024_ravulizumab_nmosd_pkpd/0.1.0/MODEL_CARD.md) | Explore endpoint-constrained ravulizumab exposure and free-C5 response. | Runnable · 4 experiments |
| [Pasquiers 2025 rituximab ANCA/gammaglobulin PK/PD](models/qspquest_pasquiers_2025_rituximab_anca_gammaglobulin_pkpd/0.1.0/MODEL_CARD.md) | Explore rituximab exposure, ANCA and gammaglobulin dynamics. | Runnable · 5 experiments |
| [Pernice 2023 GreatNector Alemtuzumab MS Petri Net ODE](models/qspquest_pernice_2023_greatnector_alemtuzumab_ms_petrinet_ode/0.1.0/MODEL_CARD.md) | Inspect alemtuzumab and multiple-sclerosis immune dynamics; simulation is unavailable. | Inspection only · simulation unavailable |
| [Rituximab exposure–CD19+ B-cell dynamics](models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.0/MODEL_CARD.md) | Compare typical and individualized rituximab exposure and B-cell depletion/recovery. | Runnable · 3 experiments |
| [Vu 2017 Erenumab QSS TMDD and CIDBF PK/PD Model](models/qspquest_vu_2017_erenumab_cidbf_pkpd_tmdd/0.1.0/MODEL_CARD.md) | Explore erenumab disposition and capsaicin-induced dermal blood-flow response. | Runnable · 13 experiments |
| [Yoshida 2020 crenezumab Abeta TMDD PK/PD model](models/qspquest_yoshida_2020_crenezumab_abeta_tmdd_pkpd/0.1.0/MODEL_CARD.md) | Explore crenezumab binding and amyloid-beta PK/PD dynamics. | Runnable · 4 experiments |

## Oncology, binding and immune mechanisms

| Model | What it describes | Availability |
| --- | --- | --- |
| [Besbassi 2026 CRS QSP locked cytokine network](models/qspquest_besbassi_2026_crs_qsp_locked_cytokine_network/0.1.1/MODEL_CARD.md) | Explore drug exposure, immune activation and cytokine dynamics in a CRS model. | Runnable · 5 experiments |
| [CD3×5T4 In Vitro Activation and Cytotoxicity QSP](models/qspquest_yuan_2026_cd3x5t4_in_vitro_qsp/2.0.1/MODEL_CARD.md) | Explore bispecific-driven T-cell activation and tumor-cell killing in vitro. | Runnable · 11 experiments |
| [Cui 2024 Envafolimab SC PD-L1 PopPK/MIDD](models/qspquest_cui_2024_envafolimab_sc_pdl1_midd/0.1.0/MODEL_CARD.md) | Explore subcutaneous envafolimab exposure and published development summaries. | Runnable · 4 experiments |
| [Haid 2023 PROTAC mechanistic pharmacodynamic framework](models/qspquest_haid_2023_protac_mechanistic_pd_framework/0.1.0/MODEL_CARD.md) | Explore a mechanistic framework for PROTAC pharmacodynamics. | Runnable · 3 experiments |
| [Han 2026 Sim2Real-PK Daratumumab Public TMDD ODE](models/qspquest_han_2026_sim2real_pk_daratumumab_tmdd/0.1.0/MODEL_CARD.md) | Explore daratumumab target-mediated drug disposition. | Runnable · 4 experiments |
| [Hurkmans 2019 Nivolumab Real-World PopPK Clearance-Response](models/qspquest_hurkmans_2019_nivolumab_real_world_poppk_cl_response/0.1.0/MODEL_CARD.md) | Explore nivolumab clearance and response relationships with fixed inputs. | Runnable · 8 experiments |
| [Jafarnejad 2019 Neoadjuvant Nivolumab NSCLC QSP](models/qspquest_jafarnejad_2019_nivolumab_neoadjuvant_pd1_nsclc_qsp/0.1.0/MODEL_CARD.md) | Explore nivolumab and immune mechanisms in neoadjuvant lung-cancer scenarios. | Runnable · 2 experiments |
| [Lobet 2026 panitumumab body-composition PopPK](models/qspquest_lobet_2026_panitumumab_body_composition_poppk/0.1.0/MODEL_CARD.md) | Explore panitumumab exposure with body-composition covariates. | Runnable · 2 experiments |
| [Panoilia 2015 Bevacizumab VEGF165 QSS TMDD PopPK Binding Model](models/qspquest_panoilia_2015_bevacizumab_vegf165_qss_tmdd/0.1.0/MODEL_CARD.md) | Explore bevacizumab binding to VEGF165 and target-mediated disposition. | Runnable · 14 experiments |
| [Poels 2025 elranatamab RRMM QSP](models/qspquest_poels_2025_elranatamab_mm_qsp/0.1.0/MODEL_CARD.md) | Inspect an elranatamab multiple-myeloma QSP model; simulation is unavailable. | Inspection only · simulation unavailable |
| [Prunella 2025 Ramucirumab/Paclitaxel Digital-Twin PK-PD QSP](models/qspquest_prunella_2025_ramucirumab_paclitaxel_digital_twin/0.1.0/MODEL_CARD.md) | Inspect ramucirumab/paclitaxel PK/PD scenarios; simulation is unavailable. | Inspection only · simulation unavailable |
| [Quartino 2017 Pertuzumab Neoadjuvant PK/Exposure-Response Model](models/qspquest_quartino_2017_pertuzumab_neoadjuvant_pk_er/0.1.0/MODEL_CARD.md) | Explore pertuzumab exposure and neoadjuvant response summaries. | Runnable · 7 experiments |
| [Shemesh 2019 Atezolizumab Pediatric and Young Adult PopPK/Safety Model](models/qspquest_shemesh_2019_atezolizumab_pediatric_poppk_safety/0.2.1/MODEL_CARD.md) | Explore atezolizumab exposure and safety summaries in younger populations. | Runnable · 16 experiments |
| [Sule 2025/2026 bevacizumab pediatric minimal PBPK bridge](models/qspquest_sule_2025_bevacizumab_minimal_pbpk_pediatric_bridge/0.1.0/MODEL_CARD.md) | Explore a reduced physiological model for pediatric bevacizumab exposure. | Runnable · 13 experiments |
| [Yagishita 2024 Atezolizumab J-TAIL Real-World PopPK Validation](models/qspquest_yagishita_2024_atezolizumab_jtail_real_world_pk/0.1.0/MODEL_CARD.md) | Explore atezolizumab exposure against real-world study summaries. | Runnable · 4 experiments |
| [Yang 2021 Cemiplimab Advanced-Malignancy PopPK Model](models/qspquest_yang_2021_cemiplimab_advanced_malignancies_poppk/0.1.0/MODEL_CARD.md) | Explore fixed cemiplimab exposure in advanced malignancy scenarios. | Runnable · 33 experiments |
| [Zeng 2026 atezolizumab PopPK software-comparison simulation](models/qspquest_zeng_2026_atezolizumab_software_poppk_simulation/0.1.0/MODEL_CARD.md) | Compare atezolizumab fixed-input PK simulation scenarios. | Runnable · 40 experiments |
| [de Vries Schultink 2018 MCLA-128/Zenocutuzumab Translational PK-PD](models/qspquest_de_vries_2018_mcla128_zenocutuzumab_pkpd/0.1.0/MODEL_CARD.md) | Explore translational zenocutuzumab exposure and pharmacodynamic scenarios. | Runnable · 10 experiments · 5 unavailable |

## Other pharmacology and protein distribution

| Model | What it describes | Availability |
| --- | --- | --- |
| [Choi 2025 Denosumab SB16 Biosimilarity PopPK/PD](models/qspquest_choi_2025_denosumab_sb16_biosimilarity_poppkpd/0.1.0/MODEL_CARD.md) | Compare fixed denosumab/SB16 exposure and pharmacodynamic experiments. | Runnable · 11 experiments |
| [Clegg 2024 AZD7442 serum PK](models/qspquest_clegg_2024_azd7442_tixagevimab_cilgavimab_poppk/0.1.0/MODEL_CARD.md) | Explore fixed tixagevimab/cilgavimab exposure scenarios. | Runnable · 20 experiments |
| [Eaton 2025 dabigatran-idarucizumab sheep CPB PK/PD](models/qspquest_eaton_2025_dabigatran_idarucizumab_sheep_cpb_pkpd/0.1.0/MODEL_CARD.md) | Explore dabigatran reversal by idarucizumab in a sheep bypass model. | Runnable · 2 experiments |
| [Eaton 2025 idarucizumab/dabigatran sheep PK-PD](models/qspquest_eaton_2025_idarucizumab_dabigatran_sheep_pkpd/0.1.0/MODEL_CARD.md) | Explore sheep idarucizumab/dabigatran scenarios and published PK/PD endpoints. | Runnable · 33 experiments |
| [Efalizumab PASI time course: source-partial model](models/qspquest_chetty_2014_efalizumab_fcrn_pbpk_pd/0.1.0/MODEL_CARD.md) | Inspect efalizumab FcRn distribution and pharmacodynamic evidence replays. | Runnable · 4 experiments |
| [Efalizumab-driven CD11a turnover](models/qspquest_chetty_2014_efalizumab_cd11a_turnover/0.1.0/MODEL_CARD.md) | Explore how efalizumab changes CD11a turnover. | Runnable · 6 experiments |
| [Frank 2023 sutimlimab CAD PK/PD](models/qspquest_frank_2023_sutimlimab_cad_pkpd/0.1.0/MODEL_CARD.md) | Explore sutimlimab exposure and pharmacodynamics in cold agglutinin disease. | Runnable · 4 experiments |
| [Gu 2017 BAY 1093884 TFPI QSS-TMDD and Exploratory SC/Human PK/PD](models/qspquest_gu_2017_bay1093884_tfpi_qss_tmdd/0.1.0/MODEL_CARD.md) | Explore TFPI binding, target-mediated disposition and exploratory BAY 1093884 exposure. | Runnable · 6 experiments |
| [Lee 2024 SB12/eculizumab biosimilar PopPK/PD/efficacy](models/qspquest_lee_2024_sb12_eculizumab_biosimilar_poppkpd/0.1.0/MODEL_CARD.md) | Explore fixed SB12/eculizumab exposure and pharmacodynamic comparisons. | Runnable · 5 experiments |
| [Lee 2024 SB12/eculizumab healthy-subject PK/PD](models/qspquest_lee_2024_sb12_eculizumab_healthy_poppkpd/0.1.0/MODEL_CARD.md) | Explore SB12/eculizumab PK/PD experiments in healthy subjects. | Runnable · 3 experiments |
| [Pan/Basu 2020 Pediatric Therapeutic Protein PBPK Reduced Validation Model](models/qspquest_pan_2020_pediatric_tp_pbpk_pk_sim/0.1.0/MODEL_CARD.md) | Explore reduced pediatric therapeutic-protein distribution scenarios. | Runnable · 3 experiments |
| [Sexton 2024 Lanadelumab HAE Plasma Kallikrein-Kinin QSP](models/qspquest_sexton_2024_lanadelumab_hae_kks_qsp/0.2.0/MODEL_CARD.md) | Explore lanadelumab effects on the kallikrein-kinin system. | Runnable · 1 experiment |

## Search from the terminal

```sh
python -m qspquest_models --library . --search rituximab --runnable
```

Use `--format json` for machine-readable discovery. [Technical reference](tutorials/model-format.md)
covers version selection and the underlying archive catalogs.
