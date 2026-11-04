# Understand your results

[Start here](../README.md) · [Choose a model](../MODEL_CATALOG.md) · [Change an input](change-inputs.md)

A library experiment produces a trajectory at specified sampling times. Start with
the model guide: it identifies the scientific question, the fixed experiment inputs,
available outputs and what the model can support.

## Read the output table

| Field | Meaning |
| --- | --- |
| `time` | Sampling time, in the time unit reported by the result. |
| `side` | `pre` means before a discrete event; `post` means after it. Two rows at the same time may represent different event sides. |
| Named output columns | Readouts defined by the model, such as concentration, cell count or receptor occupancy. |
| `state__…` columns | Biological states selected as primary readouts, such as cytokine concentration or cell count. |
| `source__…` columns | Source parameters in summary-only models; these are constants, not simulated responses. |

In Python, `result['outputs']` holds named columns with `values` and `unit`.
`result['states']` holds internal states, and `result['time_unit']` supplies the time label.
`result_columns(result)` selects the primary readouts, including key states.
Python CSV and R data frames use that selection by default. For all outputs and
states, use `model.write_csv(result, path, all_readouts=True)` or
`qspquest_data_frame(result, all_readouts = TRUE)`. The CLI option is `--all-readouts`.
Every export also writes `<filename>.csv.manifest.json`, which records column
units and meanings, the model version and the inputs used. Keep and share both
files together. Exports never overwrite a file, so choose a new name each time.
[Validate and reimport a saved table](table-bundles.md) before using it in analysis.

Some outputs report constants or published table values. A flat line may be a
summary replay rather than a changing biological response. Check the experiment's
purpose before selecting a column to plot.

## Interpret the numerical scale

Values are reported as the source model computes them; nothing is converted.
Each column's `unit` is the unit the engine used. The JSON field
`declared_source_unit` keeps the source's own label, which may differ; a different
label does not mean a conversion was applied. Stored result files and source
replay values keep the source's units.

Many units are `1` even when names contain `mg_l`, `cells_mm3` or `percent`. A
unit of `1` means the engine uses the source's number as-is, without a physical
unit or conversion. The names follow the source paper; do not infer a unit or
conversion from a column name.

For the rituximab example, the typical experiment has 201 rows from day 0 to day 200.
The `cd19_cells_mm3` readout begins at 199.57 and ends near 8.70521. This is a
fixed-parameter model trajectory. It does not represent population variability,
a new fit to patients, or an optimal redosing schedule.

For the synthetic target-gated cargo example, compare tumor occupancy and central
occupancy side by side. The [walkthrough](qsp-gated-cargo.md) explains how the gate
and background opening assumptions produce the differences.

## Read a stored result

You can inspect the distributed results with Python's standard library, without
building QSPQuest. From the library checkout:

```python
from pathlib import Path
import csv
import gzip

path = Path('models/qspquest_serkland_2025_rituximab_ms_pkpd/0.1.0/results/'
            'population-typical-1000mg-full-ode/qspquest.csv.gz')
with gzip.open(path, 'rt', newline='') as stream:
    rows = list(csv.DictReader(stream))
print(len(rows), 'rows')
print('First B-cell value:', rows[0]['cd19_cells_mm3'])
print('Last B-cell value:', rows[-1]['cd19_cells_mm3'])
```

Expect 201 rows, with first and last B-cell values of 199.57 and approximately
8.70521. This is the stored 0.1.0 trajectory, not a check of version 0.3.1.

Each version's `evidence.json` lists its stored files under
`results/<experiment-id>/`. Reading them does not run a new simulation. Some
versions have no stored results even when their experiments can run. Some stored
CSVs omit states; a `starter-preview.json`, when present, gives checkpoints for
the primary readouts. The model guide says what each version provides.

## Decide what to do next

- To see the trajectory: [plot it in Python](python-quickstart.md) or [R](r-quickstart.md).
- To ask a different question: choose another experiment in the model guide.
- To change an assumption: follow the [input-change example](change-inputs.md).
- To reproduce or audit a run: use the [technical reference](model-format.md).

Each stored trajectory records the engine and inputs that produced it. This shows how it was made; it does not validate a different engine build, the biology or the units.
