# Sexton 2024 Lanadelumab HAE Plasma Kallikrein-Kinin QSP

Full runtime translation of the Sexton 2024 hereditary angioedema plasma kallikrein-kinin system model for lanadelumab. The model uses the public supplementary R/C source code: 61 states, 82 base biochemical parameters, sampled virtual-patient PK and acute-attack forcing, and SC 150 mg q2w dosing.

Source scientific documents and source terms are included in this OMEX archive. Ubi contributions are Apache-2.0; attributed source content retains CC BY 4.0.

The stored 150 mg q2w source preset is available for standalone simulation. Selected PK coordinates have independent linear PK checks; contact-system physics, complete publication reproduction and population fitting remain unqualified. Recorded execution evidence applies to its identified engine build.

DOIs: 10.1007/s10928-024-09919-6

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish complete physical-unit, population-fitting or paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.

## PK amount and concentration units

Depot dose and amount use mg; central mass concentration uses ug/mL, numerically equivalent to mg/L. Central molar concentration uses nmol/L (nM) with molecular mass 150000 g/mol. Other native coordinates remain on their source numerical scale.

Independent linear PK checks cover these selected coordinates and the stored dose schedule. They do not establish complete model dimensions, contact-system qualification, population estimation or clinical use.

Inspect `model.dose_contracts` and `model.output_semantics` before editing the dose or interpreting a concentration.
