# Chang 2025 Positively Charged Trastuzumab-vc-MMAE ADC Mouse PK/PD

Reduced empirical ODE and exact endpoint replay model for Chang et al. 2025, which compared wild-type trastuzumab-vc-MMAE ADC with a +5 positively charged variant in mouse plasma, NCI-N87 and MCF-7 tumors, liver, spleen, and N87 efficacy studies. The article reports WinNonlin NCA summaries rather than a mechanistic structural PK/PD ODE; this implementation preserves every public Table 1-6 scalar as exact anchors and provides first-order exposure ODE scenarios calibrated to reported Cmax/AUC endpoints for paper-overlay validation.

Source scientific documents and source terms are included in this OMEX archive. Ubi contributions are Apache-2.0; attributed source content retains CC BY 4.0.

37 of 37 source presets are independently matched with the current engine and exposed for standalone simulation. Others remain source-only with explicit holds. This is not population-fitting or clinical qualification.

DOIs: 10.3390/pharmaceutics17030377

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish physical-unit, population-fitting or complete paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.
