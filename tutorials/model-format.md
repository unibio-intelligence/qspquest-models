# Versions, archive format and reproducibility

[Start here](../README.md) · [Choose a model](../MODEL_CATALOG.md) · [Understand results](understand-results.md)

Use this reference when selecting an exact version, inspecting equations or
checking a saved run. For everyday use, start with a model guide and the
[Python](python-quickstart.md) or [R](r-quickstart.md) quickstart.

## Select a version

`Library.load(model_id)` loads the default version listed in `catalog.json`.
Pass `version='...'` for an exact catalog selection. An unavailable version raises
`InputBindingError` with code `model_version_unavailable`, without choosing a
replacement. Inspect the selected version with:

```python
from qspquest_models import Library

library = Library('.')
model = library.load('qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.2')
print(model.index['model_version'])  # 2.0.2
```

The shared CLI uses the same exact catalog selection. This command lists the
selected version's experiments without starting the engine:

```sh
python -m qspquest_models --library . --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.1
```

`qspquest-library` accepts the same option. An unavailable `--model-version`
exits with status 2 and code `model_version_unavailable`; JSON errors list
`requested_version`, `available_versions` and how to fix it in `details`. The CLI
never falls back to another version.
The R helpers accept the same selection with `version = '0.3.1'` in scenario
inspection and named runs; the tutorial bridge also supports it in `inputs()`.
Use `NULL` only when selecting the current catalog default is intended.

To load another distributed version, use its archive and the checksum in the
adjacent evidence record. This example explicitly selects version 0.1.0:

```python
from pathlib import Path
import json
from qspquest_models import load_archive

folder = Path('models/qspquest_yuan_2026_cd3x5t4_in_vitro_qsp/0.1.0')
evidence = json.loads((folder / 'evidence.json').read_text())
model = load_archive(folder / 'model.omex', expected_sha256=evidence['omex_sha256'])
print(model.index['model_version'])
print(model.scenario_ids)  # () — this alternate version is inspection-only
```

Read that version's [model guide](../models/qspquest_yuan_2026_cd3x5t4_in_vitro_qsp/0.1.0/MODEL_CARD.md)
for its inspection-only scope. Use the default 2.0.2 version for runnable experiments.
Save the version and checksum with your analysis
if you need to repeat it exactly. A matching checksum confirms the file is
unchanged; it does not validate the science.

## Inspect equations and experiment inputs

OMEX is a ZIP container for a model and its experiments. An SBML file describes
the mathematical model; a SED-ML file describes an experiment. Python can inspect
the already verified archive without extracting files:

```python
from xml.etree import ElementTree as ET

print(sorted(model.members))
if 'model.xml' in model.members:
    sbml = ET.fromstring(model.members['model.xml'])
    ns = {'s': 'http://www.sbml.org/sbml/level3/version2/core'}
    for species in sbml.findall('.//s:species', ns):
        print(species.attrib['id'], species.attrib.get('name', ''))
print([name for name in model.members if name.endswith('.sedml')])
```

`manifest.xml` lists members. `index.json` records member checksums and the
`native_execution` paths for the model and requests that QSPQuest runs.
The loader uses those prepared inputs; it does not translate arbitrary SBML
or interpret general SED-ML at runtime. Some inspection-only archives contain
JSON source material without an executable model.

## Research copies

Follow [Change an input](change-inputs.md) for a complete dose-change example.
Keep edited requests in a separate research directory and save their resulting
trajectories. The engine's [model guide](https://github.com/unibio-intelligence/qspquest/blob/main/docs/PYTHON-USER-GUIDE.md)
explains native model and request syntax.

A research copy with edited native JSON does not automatically update its SBML
representation. A proposed library release needs both representations regenerated
and scientific checks for its new conditions. The original archive's stored
comparisons apply only to its original named experiments.

The supported `research_copy()` helper handles scheduled doses and biological
initial states through Python, CLI and R. For advanced edits, `copy.request` holds
the native request dictionary; edit it using the engine's request schema, then call
`copy.run()` and `copy.save(new_directory)`. Raw parameter names are native engine
symbols. Changing model equations requires regenerating the execution projection,
SBML and evidence rather than editing a preset request.

`all_readouts=True` exports every original output and state; the full JSON result
also retains both arrays. `include_states=True` remains a compatibility alias for
the complete CSV. The default primary-readout selection applies only to the exact
archive; a modified archive exports all readouts.

## Check the library snapshot

```sh
python scripts/verify_library.py
```

The verifier checks archive and file checksums, source snapshots and stored
trajectories. The library contains 81 archive versions of 72 models and 647
stored trajectories; the default versions offer 644 presets. Archives without a
stored reference result are marked unqualified. Some archives use native JSON
rather than SBML/SED-ML. Results use lossless `.csv.gz` compression with
compressed and uncompressed checksums. [Read a stored result](understand-results.md#read-a-stored-result)
without installing the engine.

Model guides describe the available experiments and source reuse terms.
`evidence.json` links stored results to their archive;
`SOURCE_REPRODUCTION.json` lists what the version can run and which experiments are unavailable.

## Machine-readable discovery

```sh
python -m qspquest_models --library . --format json
python -m qspquest_models --library . --search rituximab --runnable --format json
```

Discovery defaults to readable text. Add `--format json` for structured records;
simulation JSON contains all outputs, states and primary-readout metadata.
Python's `Library.list_models()` returns the complete structured records.

`catalog.json` selects default runtime models. `source-catalog.json` and
`source-omex-catalog.json` describe scientific sources, which use hyphenated IDs
and may select a different version. Prefer the model ID shown in the user catalog
for normal simulation. The source-specific Python methods are
`list_source_models()`, `load_source_model(source_id)` and
`load_source_execution(source_id)`.

`list_source_executions()` reports the source snapshot's `version` separately
from the archive's `execution_version`, `model_id` and `archive_sha256`.
`available_scenario_ids` lists runnable presets; `qualified_scenario_ids` lists
only those with stored reference results for that archive. Runnable presets
without a reference are marked `fixed_presets_unqualified`.


[Independent validation](https://github.com/unibio-intelligence/qspquest-validation)
reports simulation and fitting comparisons and what they cover. Passing the
archive check means the files are intact; it does not show that a model reproduces
its paper, that its units are correct or that it is fit for clinical use.

## Availability and qualification

`qspquest_models/availability.json` records what each model version can do. The
catalog, model guides, and Python and MCP discovery all read it. `dynamic`
(simulates), `source_replay` (replays published results) and `inspection_only`
describe what runs; publication review, units, fitting support and fit readiness
are recorded separately. `current_engine_qualification=not_assessed` means the
stored results have not been checked against the engine you are running.

From the library checkout, inspect the record and generated counts without an engine:

```python
from qspquest_models import Library

library = Library('.')
print(library.availability_counts)
row = next(r for r in library.list_models() if r['id'] == 'qspquest_serkland_2025_rituximab_ms_pkpd')
print(row['availability'])
```

The default versions cover 72 models and 644 presets; the archive holds 81
versions. The record lists supported operations and blockers. `run_preset` runs a
stored experiment as is; `exploratory_simulation` allows research copies, whose
results need their own assessment. Source replays reproduce stored values and
cannot show a treatment response over time. Two models support synthetic fitting
workflows.

Check archive integrity with `python scripts/verify_library.py`; it needs only
Python's standard library. It checks checksums, declarations, observations,
recorded convergence and recovery limits, and reports
`fitting_native_identity=not_assessed`. With the matching QSPQuest Python binding
installed, `python scripts/verify_library.py --native-fitting` also checks the
fitting records against the engine; the fitting APIs always run this check.
Neither command reruns simulations or fits. Use
`python scripts/verify_library.py --for-publication` to also require a completed
publication review for every archived version; it exits with code 2 if any review
is pending or missing.

## Declared source families

`catalog.json` contains the optional `qspquest.source-families/v1` registry,
identified by `source_family_schema`. Each `source_families` entry has exactly
`family_id`, `paper_id`, `canonical_model` and `members`. A canonical reference
contains `model_id` and `version`. Each member contains `model_id`, `version`,
`archive_sha256` and `model_fidelity`. Fidelity is `full`, `reduced`, `synthetic`
or `unrecorded`; these are declared representation labels.

Members must point to distinct default archives with matching versions and
checksums, and the canonical reference must be one runnable `full` member. A model
belongs to at most one family, and a family has at most 32 members. A new version
or archive needs a reviewed update to the family record.

`python scripts/build_model_guides.py` generates each model's `source_family`
declaration (`family_id`, `paper_id` and `canonical_model`), fidelity labels and
guide links from this registry. `Library` and `scripts/verify_library.py` reject
stale or contradictory family records. Models outside a family have no
declaration. See the [complete family inspection example](python-quickstart.md#compare-declared-representations-of-a-source).

## Source equation interpretations

Some models include `source_interpretations` (schema `qspquest.source-interpretations/v1`), which documents where the model deliberately differs from the printed source equations. Each entry gives the printed and adopted coordinates, source locator, source/native definition names, rationale, conservation implications and qualification limits. `Library.load()` checks that the record matches the archive; `model.source_interpretations` returns it, or `None` when there is none. It covers selected choices, not a full check against the paper, author code or units. See the [runnable lymph interpretation example](rat-aav-brain-model.md#inspect-the-rat-models-source-interpretation-before-running).

## Research parameter inputs

`copy.parameters` lists editable inputs with their values and units.
`copy.set_parameter(name, value)` keeps the unit and rejects non-finite or
out-of-bounds values; fixed inputs cannot be edited. Changing a parameter that
sets starting values does not recompute linked starting states.
See the complete [protein-only barrier workflow](rat-aav-brain-model.md#change-protein-barriers-without-changing-vector-barriers)
for named vector/protein inputs, explicit shared perturbations and migration guidance.
`model.parameter_effects` lists what each input affects, where declared.

## Native input bindings

`model.input_bindings` lists each native input and its aliases with unit,
default, fixed flag, bounds or starting expression, and the source's display unit.
Edits use the native unit; nothing is converted from a source label. A native
unit of `1` keeps the source's number unchanged: the source label only describes
it, and a physical unit such as `1/h` is refused for that input.

Keep `context.input_binding_hash` after inspection and pass it to
`resolve_input_alias(group, name, expected_input_binding_hash=hash)` or
`research_copy(scenario, expected_input_binding_hash=hash)`. Groups are
`parameters` and `initial_states`. If the model changes after you inspect it,
research copies stop working and `InputBindingError.diagnostic` says what to do.
See the complete
[input inspection and edit tutorial](input-bindings.md).

## Focused tutorials

- [Save and verify table bundles](table-bundles.md): units, inputs and provenance with CSV data.
- [Inspect version-bound inputs](input-bindings.md): aliases and native units for reproducible edits.
- [Source precision profiles](precision-profiles.md): reproduce complete rounding conventions.
- [Protocol initialization](protocol-initialization.md): pre-dose clocks and percentage denominators.
- [Synthetic parameter recovery](library-fitting.md): prerequisites, exact workflows and fitting limits.
- [Explore the rat AAV brain model](rat-aav-brain-model.md): serotype presets, barrier inputs and output identities.

## Command diagnostics

Command failures write a problem, cause and fix to stderr without a traceback.
Exit status 2 means invalid arguments or unknown model/experiment IDs; status 1
means a library, archive, engine or output failure. An unavailable exact version
also exits with status 2; its JSON error includes `details`. Use `--json-errors` to receive
one JSON object with schema `qspquest.library-error/v1` and fields `code`,
`problem`, `cause` and `fix`. Result and discovery JSON remain on stdout.

This command deliberately selects a nonexistent experiment and exits with status 2:

```sh
python -m qspquest_models --library . --json-errors \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --scenario missing-experiment
```

Its `code` is `unknown_scenario`; the fix tells you to list the exact experiment
IDs. The codes below are stable within this error schema:

| Code | Meaning |
| --- | --- |
| `invalid_arguments` | Unsupported arguments or option combinations |
| `unknown_model`, `unknown_scenario` | An exact runnable identity was not selected |
| `model_version_unavailable` | The exact catalog version is unavailable; inspect the migration details |
| `library_unavailable`, `discovery_failed` | Catalog or search metadata could not be read or validated |
| `archive_invalid` | The selected archive is missing, corrupt or does not match its checksum |
| `invalid_inputs` | The research copy or an input edit is unavailable or invalid |
| `engine_unavailable`, `engine_timeout`, `execution_failed` | The engine cannot start, exceeded its limit or rejected the experiment |
| `output_unavailable` | A CSV, JSON or research-copy destination cannot be written |
| `loader_unavailable` | `qspquest-library` needs the companion loader from the matching release |


`qspquest-library`, installed with the QSPQuest Python binding, accepts the same
options as `python -m qspquest_models`. Both locate the library using `--library`,
then `QSPQUEST_LIBRARY_DIR`, then the loader's package checkout. The Python
`Library(root)` API takes an explicit root or uses the package checkout.

For example, from the library checkout:

```sh
export QSPQUEST_LIBRARY_DIR="$(pwd)"
python -m qspquest_models --search 'B-cell recovery' --format json
```

This includes `qspquest_li_2024_rituximab_bcell_repletion_kpd_nephrotic` with its
availability record. Source replay models can run only their stored presets, not
new simulations.

If R cannot find Python, set `QSPQUEST_PYTHON` to the Python executable in your
activated environment, then recreate `models`; see the [R guide](r-quickstart.md).
