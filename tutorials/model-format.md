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
model = library.load('qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.1')
print(model.index['model_version'])  # 2.0.1
```

The shared CLI uses the same exact catalog selection. This command lists the
selected version's experiments without starting the engine:

```sh
python -m qspquest_models --library . --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.0
```

`qspquest-library` accepts the same option. An unavailable `--model-version`
exits with status 2 and code `model_version_unavailable`; JSON errors retain
`requested_version`, `available_versions` and the migration instruction in
`details`. The CLI does not choose an alternate archive or replace the pin.
The R helpers accept the same selection with `version = '0.3.0'` in scenario
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
for its inspection-only scope. Use the default 2.0.1 version for runnable experiments.
Save the version and checksum with an analysis
when an exact repeat is needed. A matching checksum verifies bytes against the
selected record; it is not an independent scientific validation.

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
the complete CSV. Curated presentation metadata applies only to the exact pinned
archive. An archive with different bytes falls back to the complete readout set.

## Check the library snapshot

```sh
python scripts/verify_library.py
```

The verifier checks archive/member hashes, scientific-source snapshots and stored
trajectories. The library contains 81 archive versions for 72 model identities and 647
stored trajectories. Selected versions expose 644 preset requests. Archives
without a numerical reference retain an explicit unqualified execution status.
Some archives use native JSON profiles rather than SBML/SED-ML. Results use lossless `.csv.gz` compression with
compressed and uncompressed checksums. [Read a stored result](understand-results.md#read-a-stored-result)
without installing the engine.

Model guides describe the available experiments and source reuse terms.
`evidence.json` binds stored results to their exact archive;
`SOURCE_REPRODUCTION.json` records the execution scope and unavailable experiments.

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

`list_source_executions()` distinguishes the scientific source snapshot's
`version` from the selected archive's `execution_version`, `model_id` and
`archive_sha256`. `available_scenario_ids` describes executable presets;
`qualified_scenario_ids` describes only presets with stored evidence bound to
that exact archive. Available presets without a numerical reference are marked
`fixed_presets_unqualified`. Both discovery and source-route loading reject
stale qualified-preset claims or changed evidence. Stored evidence does not
qualify the current engine, physical units or source reconstruction.


[Independent validation](https://github.com/unibio-intelligence/qspquest-validation)
reports simulation and fitting comparisons with their tested scope. A successful
archive check establishes file consistency; it does not establish full publication
reproduction, physical-unit correctness or clinical applicability.

## Availability and qualification

`qspquest_models/availability.json` is the versioned availability registry.
Catalog selection, model guides, Python discovery and MCP discovery use this
record. It binds a model version to its archive SHA-256 and stored-evidence
identity. `dynamic`, `source_replay` and `inspection_only` describe execution;
publication review, physical units, fitting support and fit readiness are separate.
`current_engine_qualification=not_assessed` means that this archive record cannot
establish qualification for the engine you are running.

From the library checkout, inspect the record and generated counts without an engine:

```python
from qspquest_models import Library

library = Library('.')
print(library.availability_counts)
row = next(r for r in library.list_models() if r['id'] == 'qspquest_serkland_2025_rituximab_ms_pkpd')
print(row['availability'])
```

The selected cohort contains 72 identities and 644 preset requests; the archive
inventory contains 81 versions. The record lists supported operations and blockers.
`run_preset` permits the exact stored request. `exploratory_simulation` supports
research copies; modified requests require their own scientific assessment.
Source replays support retained checks and cannot establish a dynamic treatment response.
Two selected models declare passed synthetic fitting workflows. Their archived
recovery records do not establish physical qualification or qualify another engine.

Verify archive integrity with `python scripts/verify_library.py`; it needs only
Python's standard library. This checks archive/member digests, declaration fields,
observations, recorded convergence and recovery limits. Its report states
`fitting_native_identity=not_assessed`: it does not verify native serde/JCS
identity normalization. With the matching QSPQuest Python binding installed, run
`python scripts/verify_library.py --native-fitting` to additionally verify those
identities. The fitting APIs always require this full native verification;
archive inspection does not bypass it. Neither check performs new numerical
qualification. Use
`python scripts/verify_library.py --for-publication` to also require resolved
publication review for every archived version. Pending or missing review states
produce an actionable error and exit code 2. A verified historical review is scoped
to its exact candidate; changing a label is not a review receipt.

## Declared source families

`catalog.json` contains the optional `qspquest.source-families/v1` registry,
identified by `source_family_schema`. Each `source_families` entry has exactly
`family_id`, `paper_id`, `canonical_model` and `members`. A canonical reference
contains `model_id` and `version`. Each member contains `model_id`, `version`,
`archive_sha256` and `model_fidelity`. Fidelity is `full`, `reduced`, `synthetic`
or `unrecorded`; these are declared representation labels.

Members must resolve to distinct selected archives with their exact versions and
hashes. The canonical reference must resolve to one executable `full` member.
One selected model can belong to only one declared family. A changed version or
archive needs a reviewed update to its pin; qualification is not transferred.
Families are limited to 32 members, matching the complete discovery inventory.

`python scripts/build_model_guides.py` generates per-model `source_family`
declarations, fidelity labels, source-catalog fields and guide links from the
registry. The generated declaration contains only `family_id`, `paper_id` and
`canonical_model`. `Library` and `scripts/verify_library.py` reject stale fields,
missing members, contradictory canonical references and archive-pin drift.
Unrelated models retain no family declaration. Archive contents, scientific
requests, stored evidence, unit status and publication review remain separate.
See the [complete family inspection example](python-quickstart.md#compare-declared-representations-of-a-source).

## Source equation interpretations

Selected records may include `source_interpretations` with schema `qspquest.source-interpretations/v1`, exact model/version, archive SHA-256 and native-model SHA-256. Each entry gives the printed and adopted coordinates, source locator, source/native definition names, rationale, conservation implications and qualification limits. `Library.load()` checks this binding before execution; `model.source_interpretations` returns the validated record or `None` when unrecorded. A selected interpretation is not complete paper, author-code or unit qualification. See the [runnable lymph interpretation example](change-inputs.md#inspect-the-rat-models-source-interpretation-before-running).

## Research parameter inputs

`copy.parameters` lists mutable native input names with effective values and archived
units. `copy.set_parameter(name, value)` retains that unit and checks finite values
and declared bounds before changing the request. Fixed inputs are unavailable.
Changing an initialization parameter does not recompute coupled initial states.
See the complete [protein-only barrier workflow](change-inputs.md#change-protein-barriers-without-changing-vector-barriers)
for named vector/protein inputs, explicit shared perturbations and migration guidance.
`model.parameter_effects` exposes any archive-declared modality effects. These
declarations do not establish scientific qualification.

## Native input bindings

`model.input_bindings` describes canonical native inputs and declared aliases with
actual units, defaults, fixed flags, bounds and initial expressions. Source display
units and archive request coordinates are separate fields. Numeric edits use the
actual native unit; no conversion is inferred from a source label.

Retain `context.input_binding_hash` after inspection and pass it to
`resolve_input_alias(group, name, expected_input_binding_hash=hash)` or
`research_copy(scenario, expected_input_binding_hash=hash)`. Groups are
`parameters` and `initial_states`. Research copies retain their creation context
and refuse edits, execution and saving after changes to that context.
`InputBindingError.diagnostic` supplies model/version and an explicit migration
action for changed contexts or unknown aliases. See the complete
[input inspection and edit tutorial](input-bindings.md).

## Focused tutorials

- [Save and verify table bundles](table-bundles.md): units, inputs and provenance with CSV data.
- [Inspect version-bound inputs](input-bindings.md): aliases and native units for reproducible edits.
- [Source precision profiles](precision-profiles.md): reproduce complete rounding conventions.
- [Protocol initialization](protocol-initialization.md): pre-dose clocks and percentage denominators.
- [Synthetic parameter recovery](library-fitting.md): prerequisites, exact workflows and fitting limits.

## Command diagnostics

Command failures write a problem, cause and fix to stderr without a traceback.
Exit status 2 means invalid arguments or unknown model/experiment IDs; status 1
means a library, archive, engine or output failure. An unavailable exact version
also exits with status 2 and includes bounded migration `details` in JSON errors. Use `--json-errors` to receive
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
availability record. Source replays permit named retained-source presets;
they do not establish exploratory dynamic simulation.

If R cannot find Python, set `QSPQUEST_PYTHON` to the Python executable in your
activated environment, then recreate `models`; see the [R guide](r-quickstart.md).
