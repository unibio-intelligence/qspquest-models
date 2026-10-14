# Inspect and edit version-bound native inputs

Purpose: select an exact model version, inspect its input names and native units,
edit one parameter and one starting state, and save a reproducible research copy.
This uses the distributed synthetic target-gated cargo model and its complete
`balanced_gate_30nmol_iv` input request. No experimental data is needed.

Prerequisites: CPython 3.10+ and the library checkout. Complete the
[setup commands](../README.md#setup) for a simulation, including the standalone
QSPQuest engine. Keep that environment active and run from the library root:

```sh
python tutorials/input_bindings.py --library-dir .
```

The script uses `QSPQUEST_EXECUTABLE` or the installed engine. To select a CLI
explicitly, pass `--engine-cli` with its absolute path. It writes into the new
directory `research-output/input-bindings/`; choose another directory with
`--output-dir` for repeat runs. Existing input directories or CSV pairs are refused.

For inspection without an engine, install only the library and run:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python tutorials/input_bindings.py --library-dir . --inspect-only \
  --output-dir research-output/inspected-bindings
```

The complete [runnable script](input_bindings.py) loads version `2.0.0`, reads
`model.input_bindings`, and retains `context.input_binding_hash`. Each binding
provides its canonical native name, actual native unit, source display unit,
archive request unit, and parameter default/fixed/bounds or state initial
expression. Native descriptions are included when declared. Canonical names
always remain available; only archive-declared aliases are added. Computed
readouts are unavailable as starting-state inputs.

The script changes `source_symbol_15` from `0.03` to `0.06` in native unit `1`.
Its native description identifies the effective closing rate while the construct
remains gate-bound. It resolves `closed_peripheral` to native state
`source_symbol_1` and sets that starting coordinate to `2`, also in unit `1`.
It checks that the scheduled dose and other retained starting values are unchanged.
Changing a parameter does not reevaluate coupled starting states.

Expected output begins with:

```text
2.0.0 source_symbol_15 0.03 -> 0.06; closed_peripheral -> source_symbol_1 = 2; native unit 1
Saved four input files; stale context refused
```

A simulation then reports `57 rows` and confirms the peripheral starting
value `2`. Inspection mode instead reports that no simulation was performed.
Saved inputs contain `model.json`, `request.json`, `input-bindings.json` and
`provenance.json`; both binding and provenance files retain the binding hash.
The simulation writes `trajectory.csv` and its `.manifest.json`, containing native
units, the effective request and run identity. The script rereads the pair and
checks its input provenance.

Use `Library.load(model_id, version='...')` to select a catalog version explicitly.
An unavailable version raises `InputBindingError` with diagnostic code
`model_version_unavailable`; it never silently selects a replacement. The hash
binds the archive, native model, alias declarations and archived base scenarios.
Pass it to `resolve_input_alias()` and `research_copy()` after inspection.
Research copies also retain their creation hash and refuse editing, execution
or saving if the underlying binding context changes. An unknown alias gives
`input_alias_unknown`; a changed context gives `input_bindings_changed` with
current/expected hashes and migration action `inspect_current_bindings`.
Inspect current bindings, review names, units and defaults, and explicitly
create a new research copy. The Python input-binding hash and MCP inspection
hash describe different contexts and cannot be substituted for one another.

Numeric edits use the **actual native unit**, without conversion from source
labels. For this model, `1` represents source numerical coordinates. A name
containing a physical unit does not turn those coordinates into a qualified
physical quantity. Native simulation columns likewise return their actual unit;
`declared_source_unit` preserves a separate display label. Parameter edits reject
fixed inputs, nonfinite values and values outside declared bounds. Initial
expressions are reported without evaluating derived values. Solver failures
remain failures and require investigating the edited request.

This exercise verifies input selection, execution and provenance for a synthetic
research experiment. It does not grant physical, scientific or clinical
qualification to the model or edited experiment.
