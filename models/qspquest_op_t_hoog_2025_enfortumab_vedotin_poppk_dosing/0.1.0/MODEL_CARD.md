# Op t Hoog 2025 enfortumab vedotin PopPK dosing

[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)

Inspect enfortumab dosing and exposure scenarios; simulation is unavailable.

**Inspection only · simulation unavailable.** Version 0.1.0.

## Interpretation and limits

These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.
Physical units have not been independently checked for this execution profile.

**9 experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

<details>
<summary>Availability and qualification</summary>

Execution: `inspection_only`. Publication review: `pending`.
Units: `source_scale_unqualified`. Current-engine qualification: `not_assessed`.
Supported operations: inspect.
Fitting supported: `false`; fit ready: `false`.
Evidence identity: `sha256:04560546af243181a4b7dc9032c25b0e341f4509d8e325da11c2d6a76ae64446`.

A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.

</details>

## What you can explore

Full three-compartment intact-ADC IV infusion ODE reconstruction of the Op t Hoog et al. 2025 enfortumab vedotin cost-saving dosing simulations, using the published supplementary NONMEM ADVAN13 control stream. Exact scenarios replay the control stream, Table 1 weight-band doses, Table 2 exposure/equivalence endpoints, Figure 1 population AUC summaries, and Table 3 cost results. Dynamic scenarios simulate representative fixed-effect patients and overlay the paper's population geometric mean endpoints.

No experiments in this version can currently run through the library loader.
The source files are available for inspection, but a simulation command would fail.

[Choose a runnable model](../../../MODEL_CATALOG.md) or inspect the
[unavailable experiment details](INTERCHANGE_AND_EXECUTION_HOLDS.json).

## Sources and technical reference

[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)
