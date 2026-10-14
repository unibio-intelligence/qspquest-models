# Save and validate a table bundle

Purpose: keep a simulation table interpretable after the Python session or chat
ends, and detect changed data before reimport. Prerequisites: complete the
[README setup](../README.md#setup), activate that Python environment, and run
these commands from the library checkout. R additionally needs the existing
`jsonlite` dependency described in the [R quickstart](r-quickstart.md).

## Run and save in Python

Use a fresh output directory and the library's synthetic target-gated cargo model:

```sh
python - <<'PY'
from pathlib import Path
from qspquest_models import Library, read_table

output = Path('table-example')
output.mkdir()  # choose another name if this directory already exists
model = Library('.').load('qspquest_ubi_2026_target_gated_cargo_qsp')
copy = model.research_copy('balanced_gate_30nmol_iv')
copy.set_dose(0, 15)
result = copy.run()
manifest = model.write_csv(result, output / 'dose15.csv')
bundle = read_table(output / 'dose15.csv')
assert manifest == bundle['manifest']
assert manifest['inputs']['modified'] is True
assert manifest['inputs']['effective_request']['regimen']['administrations'][0]['amount']['value'] == 15
assert manifest['qualification']['qualified'] is False
print(len(bundle['rows']), 'validated rows')
print([(c['name'], c['unit']) for c in manifest['table']['columns']])
print(manifest['qualification']['unit_status'])
PY
```

The directory contains exactly `dose15.csv` and `dose15.csv.manifest.json`.
The CSV remains an ordinary table: `time`, `side` and the explained primary
readouts. The sidecar contains ordered names, units, meanings and native readout
names; model/version/archive digest; actual engine result identity; the native
request used for this edited run; event counts; and evidence scope. This model
retains source numerical coordinates, so expect `source_scale_unqualified`.
A printed unit such as `1` remains the declared numerical unit, not an independently
established physical unit. The captured request is suitable for inspection and
replay with a matching model/engine, not a guarantee of another platform's result.

A modified run retains its base `scenario_id` and the complete edited request.
`qualification.qualified` is always false and `status` is `not_assessed`: an
archive label or a successful simulation does not qualify this engine/request.
`recorded_availability` and `recorded_dimensional_qualification` preserve the
archive's recorded context without transferring its evidence to the new run.
For manually assembled results, missing context is explicitly `null`; obtain a
full `model.run()` or research-copy result to capture replay inputs and identity.

## Validate without running an engine

```sh
python -m qspquest_models --verify-table table-example/dose15.csv
```

This prints the validated manifest. Add `--format json` to return both the
manifest and the validated numerical rows. It needs neither an engine nor a model
library directory. `QSPQUEST_LIBRARY_DIR` does not affect verification.
Use `--json-errors` to receive a structured `table_invalid` error on stderr;
failures exit 1. Invalid argument combinations exit 2.

The reader checks UTF-8 CSV bytes against the SHA-256 and byte count, matches
ordered headers and row counts, rejects nonfinite numerical values, and checks
nondecreasing times. Two equal-time rows must be exactly `pre` followed by `post`;
three equal-time rows or reversed sides are rejected. A single `pre` or `post`
row can occur at a sampling boundary. Keep those two event rows when plotting
or aggregating; averaging them obscures the instantaneous change.

## Reimport in R

```sh
Rscript - <<'R'
source('tutorials/qspquest-models.R')
trajectory <- qspquest_read_table('table-example/dose15.csv')
manifest <- attr(trajectory, 'manifest')
stopifnot(nrow(trajectory) == manifest$table$rows)
stopifnot(isTRUE(manifest$inputs$modified))
print(vapply(manifest$table$columns, function(c) c$name, ''))
print(manifest$qualification$unit_status)
R
```

`qspquest_read_table` builds its data frame from the rows returned by the same
Python validator and attaches the manifest. It preserves column names with
`check.names=FALSE` and does not reopen the CSV after validation.
Set `QSPQUEST_PYTHON` to the installed loader environment's Python when R uses
another environment. To export directly during an R run, pass `csv='new.csv'`
to `models$run(...)`; both files come from that same run.

## Failure recovery and limits

- Keep both files together and keep the CSV basename recorded in the manifest.
  Copying the pair to another directory preserves validation; renaming only
  the CSV fails the filename check.
- Export never replaces either existing file. Choose a new basename for another
  run. Handled write failures remove newly created files; a process crash may
  leave an incomplete pair. Validation rejects it, so rerun with a fresh name.
- Do not use `write.csv` or a spreadsheet save operation to replace the validated
  CSV: they may change bytes, columns or event rows. Keep any derived table under
  a different name and retain this bundle as its source.
- Version 1 supports at most 256 MiB of CSV bytes, 16 MiB of manifest bytes and
  2,000,000 data rows. These are local read/write limits, not promises that a
  model or engine can execute that workload.
- Digests detect corruption and accidental edits. A person who replaces both
  files can change their claims; validation does not authenticate a producer or
  grant scientific qualification. Inspect identities and the explicit scope.
- Historical distributed `.csv.gz` evidence files do not have this manifest.
  Keep their original provenance and use the [stored-result instructions](understand-results.md#read-a-stored-result).

MCP simulation sidecars can also retain an `initialization_receipt`: the actual
integration clock, initial state coordinates before doses, native input phases,
and explicitly declared percentage denominators. The reader checks those phases
and the execution identity. Source declarations describe archived protocols;
they do not establish equilibrium or qualify a modified run. See
[protocol initialization](protocol-initialization.md) for the source inspection
workflow.

MCP simulation bundles can also carry `scheduled_boundary_receipt`. It records
fixed-switch expressions and their evaluated thresholds, original dose-relative
switch declarations, event references, native binding phase indexes and the
complete requested observation sides. The SDK checks the receipt against
native initialization and the CSV's actual times and sides. A predicate's exact
time value can differ from its pre-boundary integration phase; observation side
controls state updates and does not change a comparison operator. Inspect the
receipt before interpreting a dose-time value. Requested solver tolerances are
retained; `achieved_error_estimate` is null because native execution does not
provide that estimate. These receipts do not establish scientific qualification.

Pinned scientific assessments keep numerical parity, source fidelity, conservation, author-code parity, clinical validation and physical dimensions separate. Inspect `bundle["manifest"]["scientific_assessment"]` when present. A discrepancy has an explicit scoped finding; a passed archive assessment does not qualify the current engine or modified request. The reader verifies declaration/model/provenance consistency, not the truth or authenticity of scientific evidence. `Library(...).load(model_id).scientific_assessments` returns the complete pinned archive declaration, or `None` when none is declared.
