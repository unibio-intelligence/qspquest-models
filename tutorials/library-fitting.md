# Inspect and execute an archived fitting workflow

Use this workflow to check that a fit recovers known parameters from synthetic
data stored with the model. Two archive versions declare fitting contracts: the
turnover benchmark at version `0.3.1` and the rituximab PK/PD model at version
`0.3.2`. Archived readiness is separate from compatibility with the installed
engine.

With the published `qspquest==0.1.0` engine, both workflows are compatible and
the turnover workflow below passes its recovery checks. The superseded rituximab
version `0.3.1` records a native-request fingerprint that differs from the
engine's, so fitting that version is held; its preset simulations remain
available. Version `0.3.2` reran the same synthetic fits with the engine's
fingerprint. The integrity check is preserved; changing archived evidence is not
a way to clear a hold.

## Prerequisites and discovery

Complete the [library setup](../README.md#setup) and activate that environment.
Installing `qspquest-models==0.1.0` installs the matching Python engine required
for fitting. The Python API blocks below work from any working directory.

The optional helper-script commands use the complete source distribution.
Download and extract that same public package, then run from its root:

```sh
python -m pip download --no-deps --no-binary=qspquest-models qspquest-models==0.1.0
python -m tarfile -e qspquest_models-0.1.0.tar.gz .
cd qspquest_models-0.1.0
python tutorials/fitting_workflow.py --library .
```

The last command lists fitting workflows and checks them against the installed
binding; it does not run a fit. No engine checkout or native build is needed.

It prints compatible contracts under `fit_ready_models` and any engine-identity
holds under `unavailable_fitting_models`. For the engine above, expect the
turnover benchmark and rituximab in the first list and an empty second list. Each compatible
entry gives the model version, workflow ID, operation, parameter units, bounds,
starting values, true values and allowed error. Discovery checks compatibility;
it does not run or qualify every fit. An empty compatible list does not mean
preset simulation is unavailable.

Inspect a verified declaration without running a fit:

```sh
python - <<'PY'
import json
from qspquest_models import Library
model = Library().load('qspquest_diffdose_2026_idr_benchmark', version='0.3.1')
print(json.dumps(model.fitting_contract, indent=2))
print(model.fitting_workflows)
PY
```

Each model has three workflows that use the backward differentiation formula (BDF) solver, with different starting points. Without the Python binding, `fitting_contract` and
`fitting_workflows` fail with an installation message. A model without fitting
support returns `{}` and `[]`, and `fit_workflow` fails before fitting.

## Execute one exact passed fixture

Run the turnover benchmark's first BDF fixture. Its observations and complete
native request are included in the archive; no external dataset is needed.

```sh
export MODEL_ID=qspquest_diffdose_2026_idr_benchmark
export MODEL_VERSION=0.3.1
export WORKFLOW_ID=diffsol_bdf-start-1
python tutorials/fitting_workflow.py --library . \
  --model "$MODEL_ID" --version "$MODEL_VERSION" \
  --workflow "$WORKFLOW_ID" --out synthetic-fitting-result.json
```

The equivalent Python call is:

```python
import os
from qspquest_models import Library
model = Library().load(os.environ['MODEL_ID'], version=os.environ['MODEL_VERSION'])
result = model.fit_workflow(os.environ['WORKFLOW_ID'])
print(result['checks'])
```

The command saves the full result, the inputs used and the recovery checks. It
exits with code zero only if the fit converged and every check passed. A fit that
did not converge is still saved and exits with code one. If the model is rejected
or fails to compile, the error is reported and no result is written. Choose a new
output filename each time; existing results are never overwritten.

## Interpret the result

Read `native_result` for objective values, evaluations, iterations and execution
identity. Scalar fits store these at the top level of that native object;
individual fits store them under `native_result.fit`, including the projected
gradient norm. `checks.parameters` compares each estimate with its synthetic
truth using the original absolute limit. Individual fitting also requires its
projected gradient to meet its tolerance. `checks.passed` reports this attempt
only; `current_engine_qualification` stays `not_assessed`.

The model fixes everything in the fit: data, normal residual errors, units,
initial conditions, regimen, solver, bounds, starting points and optimizer
budgets. You choose a workflow by ID; you cannot edit its data or settings here.

Recovering synthetic parameters does not validate units, clinical predictions,
uncertainty or the source paper's population fit. Do not relabel unit `1` with a
physical unit, or treat a recovered parameter as population evidence. Stored
results apply to the engine that produced them.
