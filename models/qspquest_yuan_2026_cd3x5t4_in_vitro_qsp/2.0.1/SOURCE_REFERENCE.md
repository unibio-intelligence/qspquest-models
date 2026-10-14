# qspquest_yuan_2026_cd3x5t4_in_vitro_qsp

Version 2.0.1.

Final 17-state in-vitro ODE system, disclosed population parameter profile and source-aligned mechanistic scenarios; no systemic PK.

Retained report compares 1,762 points: 389 observed-marker and 1,373 sampled published-curve points. Coverage inventory: 27 source items; seven exact tables, 15 digitized figure entries, four qualitative entries, one grouped non-reconstructable S7–S8 entry. Digitization is approximate, with 30 unresolved candidates.

Read [source details](SOURCE_REPRODUCTION.json) for provenance, modifications and omitted experiments. The [model guide](MODEL_CARD.md) lists runnable scenarios and the steps to run them with QSPQuest. Native execution preserves source numeric coordinates; physical dimensions are not independently certified. Fitting, population inference and clinical use are not qualified.

Ubi contributions: Apache-2.0. Source material retains its original terms. See root NOTICE and any LICENSE.source. The [evidence record](evidence.json) identifies the stored preset trajectories, their checksums and the engine used to produce them. These records do not qualify a new engine build or a changed request. No separate benchmark download is needed to inspect the distributed evidence.

The native projection rewrites exact nonnegative Hill fractions to QSPQuest’s stable Hill intrinsic. SBML, parameter values and primal equations are unchanged. At a singular zero-input boundary with exponent below one, the native intrinsic uses its documented bounded state-Jacobian approximation for integration; parameter-sensitivity qualification is not implied.

## Source attribution

Yuan X, Thalhauser CJ, Afzal N, Kemper K, An G, Li T. An In Vitro Quantitative Systems Pharmacology Platform for Characterizing CD3-Bispecific Antibody-Mediated T-Cell Activation and Tumor Cell Cytotoxicity. AAPS J. 2026;28(5):123. DOI: https://doi.org/10.1208/s12248-026-01259-2

Source attribution and original terms are recorded in SOURCE_REPRODUCTION.json.

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish physical-unit, population-fitting or complete paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.
