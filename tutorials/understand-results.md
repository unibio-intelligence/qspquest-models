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
| `source__…` columns | Retained source parameters in summary-only models; these are constant values, not simulated responses. |

In Python, `result['outputs']` holds named columns with `values` and `unit`.
`result['states']` holds internal states, and `result['time_unit']` supplies the time label.
`result_columns(result)` selects the explained primary readouts, including useful states.
Python CSV and R data frames use that selection by default. For all outputs and
states, use `model.write_csv(result, path, all_readouts=True)` or
`qspquest_data_frame(result, all_readouts = TRUE)`. The CLI option is `--all-readouts`.
CSV keeps its ordinary header and numerical rows. Every new export also creates
`<filename>.csv.manifest.json`: keep and share both files together. The manifest
records ordered column units and meanings, archive/version, engine identity,
effective native inputs, modified-run status and explicit qualification scope.
Existing filenames are never replaced; choose a new name for each export.
[Validate and reimport a saved table](table-bundles.md) before using it in analysis.

Some outputs report constants or published table values. A flat line may be a
summary replay rather than a changing biological response. Check the experiment's
purpose before selecting a column to plot.

## Interpret the numerical scale

Native simulation columns in Python, CLI, R and newly written CSV bundles return
the actual native `unit`; their numerical values are unchanged. The JSON field
`declared_source_unit` preserves the archive display label separately. A different
source label does not imply a conversion. Retained source replay constants and
stored trajectory files keep their declared source units.

The library preserves the source numerical values. Many output unit labels are
`1` even when names contain `mg_l`, `cells_mm3` or `percent`. Those names describe
the source convention; the execution profile has not independently established
physical dimensional correctness. Do not infer a physical-unit conversion from
a column name alone.

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
8.70521. This is the retained 0.1.0 trajectory; it does not qualify version 0.3.0.

Versions with numerical evidence list stored files in `evidence.json`, under
`results/<experiment-id>/`. Use the exact recorded filename. Reading these
trajectories does not perform a fresh simulation. Source-preparation-only
versions have no stored numerical reference, even when their presets can run.
Some retained CSVs omit states; versions with a `starter-preview.json` also
provide primary-readout checkpoints and engine identity. See the selected
model guide for that version's available evidence.

## Decide what to do next

- To see the trajectory: [plot it in Python](python-quickstart.md) or [R](r-quickstart.md).
- To ask a different question: choose another experiment in the model guide.
- To change an assumption: follow the [input-change example](change-inputs.md).
- To reproduce or audit a run: use the [technical reference](model-format.md).

Each stored trajectory records the exact compiler version, source fingerprint and request identity that produced it. Those records establish the execution provenance for that archive and request; they do not qualify a different engine build or establish biological or physical-unit validity.
