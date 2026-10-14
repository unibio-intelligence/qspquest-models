# Inspect and execute an archived fitting workflow

Use this workflow to reproduce an explicitly declared synthetic parameter
recovery fixture. Simulation availability does not establish fitting support.
The selected library declares **two fit-ready models**: the turnover benchmark
and rituximab PK/PD model, both at version `0.3.0`. Their recovery evidence is
limited to the synthetic observations and exact workflows in each archive.

## Prerequisites and discovery

Complete the [library setup](../README.md#setup), activate that environment, and
run commands from the library checkout. Browsing models and running presets
through the CLI require no native Python binding. Verifying fitting identities
and executing fits require the matching QSPQuest Python binding. Build and
install it from the engine checkout created during setup:

```sh
python -m pip install ../qspquest
python tutorials/fitting_workflow.py --library .
```

Alternatively, install a matching platform wheel as described in
[engine installation](https://github.com/unibio-intelligence/qspquest/blob/main/docs/installation.md#install-a-wheel).
The discovery command validates the native identities of archived fitting
records; it does not run parameter recovery or qualify your installed engine.

Discovery prints a JSON object containing `fit_ready_models`, with two entries
for this release. An empty array in another library means it declares no passed
synthetic workflow; it does not mean the simulator is unavailable.
Each ready entry includes the exact model version, workflow ID, operation,
parameter units, bounds, starter values, synthetic truths and recovery limits.

Inspect a verified declaration without running a fit:

```sh
python - <<'PY'
import json
from qspquest_models import Library
model = Library('.').load('qspquest_diffdose_2026_idr_benchmark', version='0.3.0')
print(json.dumps(model.fitting_contract, indent=2))
print(model.fitting_workflows)
PY
```

Each model has six declared workflows: three parameter starters under BDF and
Rodas5P. `fitting_contract` and `fitting_workflows` require full native identity
verification; they fail with an installation diagnostic when the binding is
missing. An archive without fitting support returns `{}` and `[]`; calling
`fit_workflow` on it fails before a native fit. A different solver cannot bypass
that hold.

## Execute one exact passed fixture

Run the turnover benchmark's first BDF fixture. Its observations and complete
native request are included in the archive; no external dataset is needed.

```sh
export MODEL_ID=qspquest_diffdose_2026_idr_benchmark
export MODEL_VERSION=0.3.0
export WORKFLOW_ID=diffsol_bdf-start-1
python tutorials/fitting_workflow.py --library . \
  --model "$MODEL_ID" --version "$MODEL_VERSION" \
  --workflow "$WORKFLOW_ID" --out synthetic-fitting-result.json
```

The equivalent Python call is:

```python
import os
from qspquest_models import Library
model = Library('.').load(os.environ['MODEL_ID'], version=os.environ['MODEL_VERSION'])
result = model.fit_workflow(os.environ['WORKFLOW_ID'])
print(result['checks'])
```

The command saves the complete native result, effective request, archive/source
identities, parameter recovery checks and limitations. Exit code zero requires
native convergence and every declared recovery check. A returned nonconverged
fit is saved and exits with code one. Compilation or admission errors report the
native diagnostic and produce no fabricated result. Choose a new output filename
for each attempt; an existing result is never overwritten.

## Interpret the result

Read `native_result` for objective values, evaluations, iterations and execution
identity. Scalar fits store these at the top level of that native object;
individual fits store them under `native_result.fit`, including the projected
gradient norm. `checks.parameters` compares each estimate with its synthetic
truth using the original absolute limit. Individual fitting also requires its
projected gradient to meet the declared tolerance. `checks.passed` is the result
of this attempt, while `current_engine_qualification` remains `not_assessed`.

The archive binds the entire request: data, normal residual errors, units,
initial conditions, regimen, solver, bounds, starters and estimator budgets.
This interface accepts a workflow ID rather than edited observations or controls.
Changed data or parameter roles require a separately qualified workflow.

Synthetic recovery does not establish physical units, clinical prediction,
uncertainty coverage or reproduction of a source population fit. A numeric unit
`1` remains the declared source coordinate. Do not relabel it with a physical
unit or interpret a recovered scalar/individual parameter as population evidence.
Hash-bound evidence describes its recorded engine; a newer installed engine
requires its own qualification. Source replays and inspection-only archives
cannot grant fitting support.
