# Pernice 2023 GreatNector Alemtuzumab MS Petri Net ODE

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect alemtuzumab and multiple-sclerosis immune dynamics; simulation is unavailable.

**Inspection only · simulation unavailable.** Version 0.1.0.

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**5 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

<details>
<summary>Availability and qualification</summary>

Execution: `inspection_only`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:83f5609eae9a1ea9a60420c6837a2db11fc99a1017def1db8b4d380c1b3ae98f`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Full public-source deterministic ODE expansion of the Pernice et al. 2023 GreatNector multiple-sclerosis alemtuzumab Petri Net. The runtime reconstructs the GreatMod Petri Net places, colored Th1/Th17 transitions, generated C++ rate functions, parameter sets, alemtuzumab pulse events, and source RData trace overlays.

No experiments in this version can currently run through the library loader.
The source files are available for inspection, but a simulation command would fail.

[Choose a runnable model](../../../MODEL_CATALOG.md) or inspect the
[unavailable experiment details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
