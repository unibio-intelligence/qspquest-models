# Garrett 2019 Inotuzumab Ozogamicin PopPK Model

Paper-derived fixed-effect implementation of the Garrett et al. 2019 inotuzumab ozogamicin population PK model in relapsed/refractory B-cell ALL and NHL. The runtime implements the two-compartment structural PK model with linear plus exponentially declining time-dependent clearance, BBSA/BLSTPB/disease/rituximab covariate equations, and exact scalar checks from Table 1, Table 2, the supplement NONMEM control stream, and simulation text. It does not reproduce NONMEM M3 censored-data likelihood, interindividual effects, covariance, BLQ handling, or VPC envelopes.

Source scientific documents and source terms are included in this OMEX archive. Ubi contributions are Apache-2.0; attributed source content retains CC BY 4.0.

11 of 11 source presets are independently matched with the current engine and exposed for standalone simulation. Others remain source-only with explicit holds. This is not population-fitting or clinical qualification.

DOIs: 10.1007/s10928-018-9614-9

## Changes from source

UniBio Intelligence authored the QSPQuest representation, explicit native
execution requests, OMEX packaging, scenario selection and runnable/held status
from the cited scientific source. These additions preserve the declared source
numerical values in the source-coordinate execution profile. They do not
establish physical-unit, population-fitting or complete paper reproduction.
The archive identifies the retained source terms and per-scenario limitations.
