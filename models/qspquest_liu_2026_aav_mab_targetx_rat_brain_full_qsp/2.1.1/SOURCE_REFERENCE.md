# qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp

Version 2.1.1.

Generalized source equation templates expanded into 725 ODE states, disclosed fixed/final parameters and route/serotype mechanisms.

Source card reports Figure 7: 522 digitized trajectory points, RMSE 1.65 and MAE 0.84 percentage points; six day-56 regimens within five percentage points. Figures 3–6: 5,209 evaluable raster-derived points of 5,220, log10 RMSE 0.497; source-limited diagnostics.

Read [source details](SOURCE_REPRODUCTION.json) for provenance, modifications and omitted experiments. The [model guide](MODEL_CARD.md) lists runnable scenarios and the steps to run them with QSPQuest. Native execution preserves source numeric coordinates; physical dimensions are not independently certified. Fitting, population inference and clinical use are not qualified.

Ubi contributions: Apache-2.0. Source material retains its original terms. See root NOTICE and any LICENSE.source. The [evidence record](evidence.json) identifies the stored preset trajectories, their checksums and the engine used to produce them. These records do not qualify a new engine build or a changed request. No separate benchmark download is needed to inspect the distributed evidence.

## Source attribution

QSP model for AAV-mediated antibody delivery in rat brain DOI: https://doi.org/10.1007/s10928-026-10051-w

Source attribution and original terms are recorded in SOURCE_REPRODUCTION.json.

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish physical-unit, population-fitting or complete paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.

## Serotype initialization

The AAV5 preset couples its declared receptor-total parameters with all 65 nonzero free receptor starting coordinates. The retained -1000 h equilibration precedes the bolus at 0 h. Blood-cell and tissue receptor coordinates use their respective declared totals.

Receptor-total parameters are initialization inputs and do not occur in the derivative equations. Changing one parameter alone in a research request does not reinitialize its receptor states. Use a named serotype preset or explicitly update the coupled initial states.

## Lymph binding interpretation

DOI 10.1007/s10928-026-10051-w; supplementary equations 134-136, printed page 32.

The printed equations use plasma concentrations while declaring Y as Plasma or Lymph. This implementation evaluates association and dissociation with concentrations in the named local compartment. This is a disclosed locality interpretation; the author control stream has not been checked.

The binding contribution cancels in antibody plus complex and target plus complex for either convention. That stoichiometric cancellation does not certify whole-body conservation, physical dimensions or positivity. A plasma-driven lymph reaction can consume local species without local reactant availability.

A literal printed-plasma reconstruction and a local-lymph reconstruction represent distinct source conventions. Neither is rejected as scientifically incorrect solely for this choice. Complete author-code, dimensional and whole-body conservation qualification remain open.

## Barrier inputs

BBB and BCSFB reflection inputs are separate for AAV vector and proteins. sigma_vector_bbb and sigma_vector_bcsfb affect AAV equations; sigma_protein_bbb and sigma_protein_bcsfb affect mAb, TargetX and their complex together. A protein-only perturbation leaves all vector equation coefficients unchanged. A shared perturbation must explicitly set both vector and protein inputs and therefore affects AAV, mAb, TargetX and complex.

Liu 2026, DOI 10.1007/s10928-026-10051-w, Table 1 page 11. The table prints separate modality superscripts with common BBB 0.9975 and BCSFB 0.9973 values.

All four coefficients use unit 1, values from 0 through 1 and the retained source numerical scale. The protein profile deliberately groups mAb, TargetX and complex at their disclosed common barrier defaults; a TargetX-only perturbation is not represented. Other organ reflection, interstitial/CSF reflection, diffusion, receptor and transgene coordinates are unchanged. Complete source, author-code, physical-unit and whole-body conservation qualification remain open.

Version 2.1.0 uses four explicit modality names. The ambiguous sigma_bbb and sigma_bcsfb inputs and their prior native source_symbol_872/source_symbol_873 names are unavailable. To reproduce a shared barrier perturbation, set both sigma_vector_bbb and sigma_protein_bbb, and both sigma_vector_bcsfb and sigma_protein_bcsfb. For a historical calculation use its exact pinned archive and request.

## Output identities

Declared analyte and compartment identities describe the exact source expressions. Cisterna magna and lateral-ventricle CSF readouts are separate. Tissue aggregate labels cover only the states present in the archived expression.

Returned native units remain 1. These labels do not establish physical units, source reproduction or current-engine qualification.
