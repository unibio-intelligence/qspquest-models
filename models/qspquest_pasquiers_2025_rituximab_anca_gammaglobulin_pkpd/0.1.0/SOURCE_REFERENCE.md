# Pasquiers 2025 rituximab ANCA/gammaglobulin PK/PD

Source-complete fixed-effect ODE reconstruction of the Pasquiers et al. 2025 real-world rituximab PK/PD model in ANCA-associated vasculitis. Runtime includes two-compartment rituximab PK, indirect gammaglobulin turnover inhibited by rituximab, and the Bensalem/Friberg ANCA production-blood feedback model. Exact API anchors replay the public article and supplement tables; dynamic regimen scenarios attach paper final-model simulation endpoints as overlays. Exact 1000-virtual-patient Monolix parity is source-limited because random-effect draws, patient data, and source simulation outputs are not public.

Source scientific documents and source terms are included in this OMEX archive. Ubi contributions are Apache-2.0; attributed source content retains CC BY 4.0.

5 of 5 source presets are independently matched with the current engine and exposed for standalone simulation. Others remain source-only with explicit holds. This is not population-fitting or clinical qualification.

DOIs: 10.1016/j.ebiom.2025.105989

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish physical-unit, population-fitting or complete paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.
