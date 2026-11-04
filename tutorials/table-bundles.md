# Save and validate a table bundle

Purpose: save a simulation table with what you need to understand it later, and
detect changed data before you reuse it. Prerequisites: complete the
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
The CSV is an ordinary table: `time`, `side` and the primary readouts. The
manifest records column names, units and meanings; the model and version; the
engine; and the exact inputs used for this edited run. Expect unit status
`source_scale_unqualified`: units such as `1` have not been independently checked.
The saved inputs let you rerun with the same model and engine; results on another
platform may differ.

An edited run keeps its original `scenario_id` and the full edited inputs.
`qualification.qualified` is always false and `status` is `not_assessed`.
`recorded_availability` and `recorded_dimensional_qualification` copy the original
model's status for reference only. If you assemble a result by hand, missing
fields are `null`; use a result from `model.run()` or a research copy instead.

## Validate without running an engine

```sh
python -m qspquest_models --verify-table table-example/dose15.csv
```

This prints the validated manifest. Add `--format json` to return both the
manifest and the validated numerical rows. It needs neither the engine nor the
library.
Use `--json-errors` to receive a structured `table_invalid` error on stderr;
failures exit 1. Invalid argument combinations exit 2.

The reader checks the CSV against its recorded checksum, headers and row count,
rejects non-finite values, and checks that times never decrease. Two equal-time rows must be exactly `pre` followed by `post`;
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

`qspquest_read_table` uses the same Python validator, attaches the manifest and
keeps column names unchanged.
Set `QSPQUEST_PYTHON` to the installed loader environment's Python when R uses
another environment. To export directly during an R run, pass `csv='new.csv'`
to `models$run(...)`; both files come from that same run.

## Failure recovery and limits

- Keep both files together and keep the CSV basename recorded in the manifest.
  Copying the pair to another directory preserves validation; renaming only
  the CSV fails the filename check.
- Export never replaces either existing file. Choose a new basename for another
  run. If a write fails, partial files are removed; a crash may leave an
  incomplete pair, which validation rejects, so rerun with a fresh name.
- Do not use `write.csv` or a spreadsheet save operation to replace the validated
  CSV: they may change bytes, columns or event rows. Keep any derived table under
  a different name and retain this bundle as its source.
- Version 1 supports at most 256 MiB of CSV bytes, 16 MiB of manifest bytes and
  2,000,000 data rows. These are local read/write limits, not promises that a
  model or engine can execute that workload.
- Checksums catch corruption and accidental edits, not deliberate changes:
  someone who replaces both files can change anything. Validation does not prove
  who made the files or that the science is right.
- Stored `.csv.gz` results shipped with the library do not have this manifest.
  Read them with the [stored-result instructions](understand-results.md#read-a-stored-result).

Tables saved from MCP simulations can also include an `initialization_receipt`:
the actual start time, starting states before dosing, input timing and declared
percentage denominators. The reader checks it. See
[protocol initialization](protocol-initialization.md) to inspect the source
protocol.

They can also include a `scheduled_boundary_receipt`, which records when
scheduled switches and doses take effect and which sample sides were requested.
The reader checks it against the CSV's actual times and sides. A predicate's exact
time value can differ from its pre-boundary integration phase; observation side
controls state updates and does not change a comparison operator. Inspect the
receipt before interpreting a dose-time value. Requested solver tolerances are
retained; `achieved_error_estimate` is null because native execution does not
provide that estimate.

Some models include a scientific assessment that reports numerical agreement, source fidelity, conservation, author-code agreement, clinical validation and units as separate findings. Inspect `bundle["manifest"]["scientific_assessment"]` when present, or `Library(...).load(model_id).scientific_assessments` (`None` if there is none). A passed assessment applies to the original model, not to your engine or edits.
