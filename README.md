# QSPQuest models

Run pharmacology model experiments in Python or R, plot trajectories, and compare
fixed experimental conditions. To run QSPQuest without installing anything, use
the hosted service at [biologics.unibiointelligence.com](https://biologics.unibiointelligence.com/).

**[Choose a model](MODEL_CATALOG.md)** · **[Run the example below](#run-a-rituximab-model)** ·
**[Preview a stored result](tutorials/understand-results.md#read-a-stored-result)**

The library contains 62 simulation models. Together they provide 631 preset experiments.
Examples use fixed parameters, their units have not been independently checked,
and they are not intended for clinical dose selection.

## Setup

Use CPython 3.10 or newer. From the root of this model-library checkout,
create a virtual environment and install the library with its matching
simulation engine:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
```

On Windows PowerShell, create the environment with `py -m venv .venv` and
activate it with `.\.venv\Scripts\Activate.ps1` before the same install command.
The installed library bundles its catalog and model archives. Supported engine
wheels run without a Rust compiler or a separate engine executable.
See the [installation and Python guide](PACKAGE_README.md) for supported platforms,
a complete Python example and troubleshooting.

After installation, run the examples below from any working directory.
Use `--library .` from the checkout root to select its archives directly.
The extended tutorials use the checkout for their accompanying files.

## Run a rituximab model

This example simulates circulating rituximab and CD19+ B cells over 200 days with a fixed typical
parameter set. The 1000 mg dose is a bolus into the circulating concentration at day 0;
add further doses to study a regimen.

```sh
python -m qspquest_models \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.5.0 \
  --scenario population-typical-1000mg-full-ode --csv rituximab-cli.csv
python -m qspquest_models --verify-table rituximab-cli.csv
```

Keep `rituximab-cli.csv` and `rituximab-cli.csv.manifest.json` together. The CSV
contains **201 data rows** with time, event side, rituximab concentration and
B-cell readouts. Simulated CD19+ B cells start at **199.57** and end near **8.70521**.
Choose a new filename when rerunning: exports never replace existing files.

Outputs are in `mg/L` and `[cell]/mm3`; these units have not yet been independently
checked. If you see `unknown_unit`, install the matching `qspquest==0.1.1` engine. Read the
[model guide](models/qspquest_serkland_2025_rituximab_ms_pkpd/0.5.0/MODEL_CARD.md)
and [output interpretation](tutorials/understand-results.md) before using values
quantitatively.

## Next steps

| Task | Guide |
| --- | --- |
| Plot a result | [Python quickstart](tutorials/python-quickstart.md) or [R quickstart](tutorials/r-quickstart.md) |
| Find a different drug or mechanism | [Model catalog](MODEL_CATALOG.md), grouped by topic |
| Compare tumor and systemic occupancy | [Target-gated cargo walkthrough](tutorials/qsp-gated-cargo.md) |
| Change a dose or another input | [Experiment guide](tutorials/change-inputs.md) |
| Inspect units, versions, fitting or saved data | [Technical reference](tutorials/model-format.md) |

Search and list a model's exact experiment IDs from the terminal:

```sh
python -m qspquest_models --search rituximab --runnable
python -m qspquest_models --model qspquest_serkland_2025_rituximab_ms_pkpd
```

Use `--model-version VERSION` to pin a catalog version; omitting it chooses the
current default. `--format json` returns structured discovery records. Search
also matches catalog descriptions, such as `B-cell recovery`. CSV exports use a
small set of explained primary readouts; `--all-readouts` includes every output
and biological state.

## Troubleshooting

| Problem | Next step |
| --- | --- |
| Loader cannot be imported | Activate the environment used to install `qspquest-models`. |
| Engine cannot be found | Reinstall `qspquest-models==0.1.0` in the active environment and run `python -m pip check`. |
| Catalog cannot be found | Remove an obsolete `QSPQUEST_LIBRARY_DIR` setting to use the bundled library. |
| Unknown model, version or experiment | Search the catalog and list the exact experiment IDs before running. |
| An output file already exists | Choose a new filename; keep each CSV with its manifest. |

See [command diagnostics](tutorials/model-format.md#command-diagnostics) for exit
codes, JSON errors and R environment selection.

## Contribute

Contributions are welcome: open an issue first, then follow the
[contributing guide](CONTRIBUTING.md).

## Sources and reuse

Ubi-owned contributions use [Apache-2.0](LICENSE). Published sources keep their own
terms; see [source notices](SOURCE_NOTICE.md), [NOTICE](NOTICE) and each model's notice.
[Independent validation](https://github.com/unibio-intelligence/qspquest-validation)
shows how results from a tested QSPQuest build compare with reference engines.

## Acknowledgements

We gratefully acknowledge support from Anthropic's AI for Science rare disease
research grants.
