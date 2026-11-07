# Inspect and edit version-bound native inputs

Purpose: select an exact model version, inspect its input names and native units,
edit one parameter and one starting state, and save a reproducible research copy.
It uses the synthetic target-gated cargo model and its `balanced_gate_30nmol_iv`
experiment. No experimental data is needed.

Prerequisites: CPython 3.10+ and the library checkout. Complete the
[setup commands](../README.md#setup) for a simulation, including the standalone
QSPQuest engine. Keep that environment active and run from the library root:

```sh
python tutorials/input_bindings.py --library-dir .
```

The script uses `QSPQUEST_EXECUTABLE` or the installed engine. To select a CLI
explicitly, pass `--engine-cli` with its absolute path. It writes to
`research-output/input-bindings/`. Existing outputs are never overwritten, so pass
a new `--output-dir` for repeat runs.

For inspection without an engine, install only the library and run:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python tutorials/input_bindings.py --library-dir . --inspect-only \
  --output-dir research-output/inspected-bindings
```

The [runnable script](input_bindings.py) loads version `2.0.0`, reads
`model.input_bindings` and keeps `context.input_binding_hash`. Each input lists its
native name and unit, its source label, and either its default, fixed flag and
bounds (parameters) or its starting expression (states). Some inputs also have a
description or a more descriptive alias. Computed readouts cannot be set as starting
states.

The script changes `source_symbol_15` (the closing rate while the construct is
gate-bound) from `0.03` to `0.06`, in unit `1`. It looks up the alias
`closed_peripheral` (native state `source_symbol_1`) and sets its starting value
to `2`. It then checks that the dose and other starting values are unchanged;
changing a parameter does not recompute linked starting states.

Expected output begins with:

```text
2.0.0 source_symbol_15 0.03 -> 0.06; closed_peripheral -> source_symbol_1 = 2; native unit 1
Saved four input files; stale context refused
```

A simulation then reports `57 rows` and confirms the peripheral starting
value `2`. Inspection mode instead reports that no simulation was performed.
Saved inputs contain `model.json`, `request.json`, `input-bindings.json` and
`provenance.json`. The simulation also writes `trajectory.csv` and its
`.manifest.json`, which records units and the inputs used.

Use `Library.load(model_id, version='...')` to select an exact version. A missing
version raises `InputBindingError` with code `model_version_unavailable` instead of
picking another. The input-binding hash identifies exactly what you inspected.
Pass it to `resolve_input_alias()` and `research_copy()` so they stop if the model
has changed since. An unknown alias gives `input_alias_unknown`; a changed model
gives `input_bindings_changed` with action `inspect_current_bindings`. In that
case, inspect the inputs again and create a new research copy. The Python hash and
the MCP inspection hash are different and not interchangeable.

Edits use the input's **actual native unit**; nothing is converted from source
labels. In this model that unit is `1`, even where a name mentions a physical
unit. Output columns likewise report their actual unit, with the source label in
`declared_source_unit`. Parameter edits reject fixed inputs, non-finite values and
values outside bounds. Starting expressions are shown as written, not evaluated.
If the solver fails, check your edited inputs.

This exercise checks that edits are applied and recorded correctly. It does not
validate the model's units, science or clinical use.
