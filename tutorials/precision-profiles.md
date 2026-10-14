# Select a complete source precision profile

Purpose: reproduce one coherent choice of reported Yuan CD3×5T4 constants across
every readout of an experiment, and preserve that choice with the result. This
uses the distributed version `2.0.1` and its complete scenario inputs. No paper
download, experimental files or authoring tools are required.

Prerequisites: CPython 3.10+, the library checkout and the QSPQuest engine.
Complete [setup](../README.md#setup), keep that environment active, and run from
the library root:

```sh
python tutorials/precision_profiles.py --library-dir .
```

The [complete script](precision_profiles.py) compares two conventions for
`mda_mb_468_duobody_6_86nm_et8`, using BDF, 72 hours, eleven post-event time points,
relative integration tolerance `1e-10` and absolute tolerance `1e-12`. It saves
complete native replay inputs and a receipt for each convention, runs both, and
checks that the paired CSV manifests preserve those receipts. To select the CLI
explicitly, pass `--engine-cli /absolute/path/to/qspquest`.

For inspection without an engine, install only the library:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python tutorials/precision_profiles.py --library-dir . --inspect-only \
  --output-dir research-output/inspected-precision
```

Expected output begins with `8 named profiles; 11 scenarios; 33 mutable parameters
per condition`. A simulation reports `2 runs; 11 time points each` and confirms
that CSV manifests retain complete profile receipts. Inspection mode saves the
same inputs without integration. Both modes verify that a later scalar edit is
labelled `modified` and an unknown profile fails before execution.

Outputs are written below `research-output/precision-profiles/`, one directory per
profile. Each `inputs/` contains native model and request JSON, input bindings,
provenance and `precision-profile.json`. Each simulation adds `trajectory.csv`
and `trajectory.csv.manifest.json`. Use a new `--output-dir` for repeat runs;
existing input directories and CSV pairs are refused.

## The named choices

Every profile supplies all 33 mutable scalar parameters for each of the eleven
archived scenarios. The two fixed unit-basis parameters retain their declared
defaults. Profile identifiers combine these three choices:

| Choice | Reported rounded convention | Alternative calculation |
| --- | --- | --- |
| Cell-line parameters | `stratified_s5`: supplementary Table S5 constants | `covariate_table_ii`: exponentiated Table II coefficients, with Table S3 cell-line and Table S4 donor assignments |
| Molecule conversion | `rounded_eq1`: displayed `1.1e-11` | `geometric_eq1`: Eq. 1 calculation with the reported 150 µL medium volume and `6.022e23` molecule/mol |
| Half-life constant | `displayed_0693`: literal `0.693` | `exact_ln2`: natural logarithm of two |

The archive default is `stratified_s5-rounded_eq1-displayed_0693`. Five unchanged
native equations contain `0.693`. To execute the `exact_ln2` choice, the profile
multiplies their runtime durations by `0.693 / ln(2)`. These are computational
inputs to those equations, not claims of changed biological half-lives. The
receipt explains the transformation explicitly. The profile file includes source
DOI and equation/table locators.

## Inspect and select

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.1')
manifest = model.precision_profiles
print(manifest['default_profile_id'])
print([p['id'] for p in manifest['profiles']])

research = model.research_copy(
    'mda_mb_468_duobody_6_86nm_et8',
    precision_profile_id='covariate_table_ii-geometric_eq1-exact_ln2')
print(research.precision_profile['parameters_status'])  # matches_profile
result = research.run()
print(result['precision_profile']['choices'])
```

`model.run(scenario_id, precision_profile_id=...)` also selects a complete
convention. Without a selector, runs retain the archive default and identify it
in their receipts. A model with no declared profiles returns `None` for
`model.precision_profiles` and refuses a profile selector. The standalone
`load_archive()` function does not infer a companion file: use `Library.load()`
for catalog-bound profile discovery, or pass an explicitly verified manifest as
`precision_profiles` to `load_archive()`.

`research.set_precision_profile(id)` replaces all mutable scalar inputs and
retains starting states, doses, covariates and solver settings. Subsequent scalar
edits or timed parameter changes produce a `modified` receipt, retaining the base
profile hash and actual starting parameter map. Selecting a profile does not
erase timed changes; remove them explicitly to run an unchanged convention.
Research copies refuse editing, saving or execution if their inspected profile
manifest changes. Reload and inspect before creating a fresh copy.

Receipts bind model version, archive, manifest, profile, scenario and complete
effective scalar inputs. Their parameter and manifest hashes use sorted compact
Python JSON, as declared in `hash_encoding`; native execution identity hashes
remain separate. Catalog descriptors additionally pin the exact profile file
bytes. A returned profile is a copy, so inspecting or editing it does not modify
the library.

## Interpret differences

Native unit `1` retains the archived source numerical scale. Source labels and
rounding conventions do not establish physical dimensional qualification. A
different convention can legitimately change trajectories; record the entire
profile rather than combining constants to match individual readouts. Such
differences alone do not show failed biology. These fixed-parameter runs do not
qualify population inference, clinical decisions or complete paper reproduction.

Unknown profiles, stale manifests, checksum mismatches and incomplete parameter
maps are refused. Inspect the exact version and reselect from its verified
manifest. A solver failure remains an execution failure; inspect the saved
request and its separate starting-state and protocol choices.
