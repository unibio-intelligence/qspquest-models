# QSPQuest models

Run pharmacology model experiments in Python or R, plot trajectories, and compare
fixed experimental conditions.

**[Choose a model](MODEL_CATALOG.md)** · **[Run the example below](#run-a-rituximab-model)** ·
**[Preview a stored result](tutorials/understand-results.md#read-a-stored-result)**

The library contains 72 selected model identities: 62 offer dynamic starters, 5 offer source replays and 5 are inspection only.
Its 81 archived versions provide 644 selected preset requests and 2 fit-ready models.
Counts describe execution availability. Physical units and current-engine scientific qualification
remain separate; these examples use fixed parameters and do not support clinical dose selection.

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
run the examples from `qspquest-models/`. Retain this library checkout: installing
the loader alone does not install its catalog or model archives.
An installed matching QSPQuest Python binding also runs simulations without
`QSPQUEST_EXECUTABLE`. Only [fitting workflows](tutorials/library-fitting.md)
require that binding; browsing archives and CLI simulation do not.

## Run a rituximab model

Explore circulating rituximab and CD19+ B cells over 200 days with a fixed typical
parameter set. The starting administration is represented by an initial
concentration rather than repeat-dose events.

```sh
python -m qspquest_models --library . \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.0 \
  --scenario population-typical-1000mg-full-ode --csv rituximab-cli.csv
python -m qspquest_models --verify-table rituximab-cli.csv
```

Keep `rituximab-cli.csv` and `rituximab-cli.csv.manifest.json` together. The CSV
contains **201 data rows** with time, event side, rituximab concentration and
B-cell readouts. CD19+ B cells start at **199.57** and end near **8.70521**.
Choose a new filename when rerunning: exports never replace existing files.

The selected model returns `mg/L` and `[cell]/mm3`, but its complete dimensional
and numerical qualification remains pending. An `unknown_unit` error indicates
an engine without count-unit support; build the matching engine. Read the
[model guide](models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.0/MODEL_CARD.md)
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

## Sources and reuse

Model guides explain scientific scope and link source attribution and evidence.
[Source notices](SOURCE_NOTICE.md), [NOTICE](NOTICE) and model-specific notices
describe reuse terms. Ubi-owned contributions use [Apache-2.0](LICENSE); additional
scientific sources retain their attributed terms.
[Independent validation](https://github.com/unibio-intelligence/qspquest-validation)
reports comparisons and their tested scope.
