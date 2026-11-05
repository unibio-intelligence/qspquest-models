# QSPQuest models

Run pharmacology model experiments in Python or R, plot trajectories, and compare
fixed experimental conditions. To run QSPQuest without installing anything, use
the hosted service at [biologics.unibiointelligence.com](https://biologics.unibiointelligence.com/).

**[Choose a model](MODEL_CATALOG.md)** · **[Run the example below](#run-a-rituximab-model)** ·
**[Preview a stored result](tutorials/understand-results.md#read-a-stored-result)**

The library contains 72 models: 62 simulate, 5 replay published results and 5 are for inspection only. Together they offer 644 ready-to-run experiments.
Examples use fixed parameters, their units have not been independently checked,
and they are not for choosing clinical doses.

## Setup

You need CPython 3.10+, Rust 1.98.1 and a native compiler. See
[engine installation](https://github.com/unibio-intelligence/qspquest/blob/main/docs/installation.md)
for build tools and Windows environment activation. Clone the library and engine
into the same directory, then install the loader and build the engine:

```sh
git clone https://github.com/unibio-intelligence/qspquest.git qspquest
git clone https://github.com/unibio-intelligence/qspquest-models.git qspquest-models
cd qspquest-models
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
(cd ../qspquest && cargo build --release --locked -p qspquest-cli)
export QSPQUEST_EXECUTABLE="$(cd ../qspquest && pwd)/target/release/qspquest"
```

The first engine build can take several minutes. Keep this environment active and
run the examples from `qspquest-models/`. The Python distribution also bundles the
catalog and model archives; an installed wheel needs no library checkout and uses
its bundled library when `--library` is omitted.
[Fitting](tutorials/library-fitting.md) also needs the matching QSPQuest Python
binding; simulation does not. With the binding installed, `QSPQUEST_EXECUTABLE`
is optional.

## Run a rituximab model

Explore circulating rituximab and CD19+ B cells over 200 days with a fixed typical
parameter set. The 1000 mg dose is set as a starting concentration (dose/V);
repeat doses are not modeled.

```sh
python -m qspquest_models --library . \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.1 \
  --scenario population-typical-1000mg-full-ode --csv rituximab-cli.csv
python -m qspquest_models --verify-table rituximab-cli.csv
```

Keep `rituximab-cli.csv` and `rituximab-cli.csv.manifest.json` together. The CSV
contains **201 data rows** with time, event side, rituximab concentration and
B-cell readouts. CD19+ B cells start at **199.57** and end near **8.70521**.
Choose a new filename when rerunning: exports never replace existing files.

Outputs are in `mg/L` and `[cell]/mm3`; these units have not yet been independently
checked. If you see `unknown_unit`, build the matching engine. Read the
[model guide](models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.1/MODEL_CARD.md)
and [output interpretation](tutorials/understand-results.md) before using values
quantitatively.

## Continue with your question

| I want to… | Next step |
| --- | --- |
| Plot a result | [Python quickstart](tutorials/python-quickstart.md) or [R quickstart](tutorials/r-quickstart.md) |
| Find a different drug or mechanism | [Model catalog](MODEL_CATALOG.md), grouped by topic |
| Compare tumor and systemic occupancy | [Target-gated cargo walkthrough](tutorials/qsp-gated-cargo.md) |
| Change a dose or another input | [Experiment guide](tutorials/change-inputs.md) |
| Inspect units, versions, fitting or saved data | [Technical reference](tutorials/model-format.md) |

Search and list a model's exact experiment IDs from the terminal:

```sh
python -m qspquest_models --library . --search rituximab --runnable
python -m qspquest_models --library . --model qspquest_serkland_2025_rituximab_ms_pkpd
```

Use `--model-version VERSION` to pin a catalog version; omitting it chooses the
current default. `--format json` returns structured discovery records. Search
also matches catalog descriptions, such as `B-cell recovery`. CSV exports use a
small set of explained primary readouts; `--all-readouts` includes every output
and biological state.

## If something goes wrong

| Problem | Next step |
| --- | --- |
| Loader cannot be imported | Activate the environment where `pip install -e .` ran. |
| Engine cannot be found | Set `QSPQUEST_EXECUTABLE` to the built CLI's absolute path. |
| Catalog cannot be found | Pass `--library /path/to/qspquest-models`. |
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
