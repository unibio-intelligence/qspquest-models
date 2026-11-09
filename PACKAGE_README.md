# QSPQuest models

Install a curated pharmacology model library, find an experiment and run it
locally. The package includes the catalog, model archives, model guides and
source notices. It installs the matching QSPQuest simulation engine automatically.

## Install

Use CPython 3.10 or newer in a virtual environment. Run these commands from
the root of the model-library checkout. On macOS or Linux:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
```

Published engine wheels support Linux x86-64/ARM64, macOS Intel/Apple Silicon
and Windows x86-64. On these platforms, a matching wheel needs no Rust compiler.
Other platforms may require building the engine from source.
After installation you can run the library from any working directory.

## Find and run a model

Search for a drug, then list the selected model's experiments and local guide:

```sh
python -m qspquest_models --search rituximab --runnable
python -m qspquest_models --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.5.0
```

Run the typical-parameter rituximab example and check its saved table:

```sh
python -m qspquest_models --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.5.0 --scenario population-typical-1000mg-full-ode --csv rituximab.csv
python -m qspquest_models --verify-table rituximab.csv
```

Keep `rituximab.csv` and `rituximab.csv.manifest.json` together. The table has
201 rows from day 0 to day 200, with rituximab concentration in `mg/L` and CD19+
B-cell density in `[cell]/mm3`. Simulated B cells start at 199.57 and end near 8.70521.
The 1000 mg dose is a bolus into the circulating concentration at day 0. This
example has one dose and no patient-to-patient variability.

## Use Python

Save this complete example as `run_model.py`, then run `python run_model.py`:

```python
from qspquest_models import Library

library = Library()
model = library.load("qspquest_serkland_2025_rituximab_ms_pkpd", version="0.5.0")
result = model.run("population-typical-1000mg-full-ode")
assert len(result["times"]) == 201
cells = next(output for output in result["outputs"] if output["name"] == "cd19_cells_mm3")
print("CD19+ B cells:", cells["values"][0], "to", cells["values"][-1])
model.write_csv(result, "rituximab-python.csv")
```

Expect the same trajectory as the command-line example and a second CSV/manifest
pair. `Library()` uses the bundled catalog; pass a directory only when selecting
another extracted library. The model-list command reports the installed catalog
path, and the experiment-list command reports the selected model guide path.

## Common problems and scope

- If import fails, activate the environment used for installation and run
  `python -m pip check`.
- If an output file already exists, choose a new filename. CSV exports never
  overwrite a table or its manifest.
- If a model, version or experiment is unavailable, use `--search` and the exact
  experiment IDs printed by `--model`. Inspection-only versions cannot simulate.
- If a previously configured library or executable is selected, remove
  `QSPQUEST_LIBRARY_DIR` and `QSPQUEST_EXECUTABLE` from that terminal's environment
  to use the installed defaults.

This research library uses fixed parameter examples. Running successfully does
not establish scientific validation; source-scale units have not been
independently checked. Read each model guide and source terms before reuse.
