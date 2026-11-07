# Select a complete source precision profile

Purpose: run the Yuan CD3×5T4 model with one consistent set of the paper's
rounded constants, and record that choice with the result. This uses version
`2.0.2`. No paper download or data files are needed.

Prerequisites: CPython 3.10+, the library checkout and the QSPQuest engine.
Complete [setup](../README.md#setup), keep that environment active, and run from
the library root:

```sh
python tutorials/precision_profiles.py --library-dir .
```

The [complete script](precision_profiles.py) compares two conventions for
`mda_mb_468_duobody_6_86nm_et8`, using the backward differentiation formula (BDF) solver, 72 hours, eleven post-event time points,
relative integration tolerance `1e-10` and absolute tolerance `1e-12`. It saves
the inputs and a receipt (a record of the choice) for each convention, runs both,
and checks that each CSV manifest keeps its receipt. To select the CLI
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
same inputs without simulating. Both modes check that a later edit is labeled
`modified` and that an unknown profile is rejected before running.

Outputs are written below `research-output/precision-profiles/`, one directory per
profile. Each `inputs/` contains native model and request JSON, input bindings,
provenance and `precision-profile.json`. Each simulation adds `trajectory.csv`
and `trajectory.csv.manifest.json`. Use a new `--output-dir` for repeat runs;
existing outputs are never overwritten.

## The named choices

Every profile sets all 33 editable parameters for each of the eleven scenarios;
the two fixed unit-basis parameters keep their defaults. Profile identifiers
combine these three choices:

| Choice | Reported rounded convention | Alternative calculation |
| --- | --- | --- |
| Cell-line parameters | `stratified_s5`: supplementary Table S5 constants | `covariate_table_ii`: exponentiated Table II coefficients, with Table S3 cell-line and Table S4 donor assignments |
| Molecule conversion | `rounded_eq1`: displayed `1.1e-11` | `geometric_eq1`: Eq. 1 calculation with the reported 150 µL medium volume and `6.022e23` molecule/mol |
| Half-life constant | `displayed_0693`: literal `0.693` | `exact_ln2`: natural logarithm of two |

The default is `stratified_s5-rounded_eq1-displayed_0693`. Five model equations
contain `0.693`. For `exact_ln2`, the profile multiplies their durations by
`0.693 / ln(2)` instead; this adjusts the calculation, not the biological
half-life. The receipt records this, and the profile file cites the source DOI,
equations and tables.

## Inspect and select

```python
from qspquest_models import Library

model = Library('.').load('qspquest_yuan_2026_cd3x5t4_in_vitro_qsp', version='2.0.2')
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

`model.run(scenario_id, precision_profile_id=...)` also selects a profile.
Without one, runs use the default and record it in their receipts. Models without
profiles return `None` for `model.precision_profiles` and reject a profile
selector. Load the model with `Library.load()` to find its profiles; standalone
`load_archive()` has them only if you pass the manifest as `precision_profiles`.

`research.set_precision_profile(id)` replaces all editable parameters and keeps
starting states, doses, covariates and solver settings. Any later parameter edit
or timed parameter change marks the receipt `modified`. Selecting a profile does
not remove timed changes; remove them yourself to run the profile unchanged. If
the profile file changes, research copies stop working: reload the model and make
a new copy.

Receipts record the model version, profile, scenario and every parameter value
used. A returned profile is a copy, so editing it does not change the library.

## Interpret differences

A different convention can legitimately change trajectories; that alone does not
mean the biology is wrong. Report the whole profile rather than mixing constants
to match individual readouts. Unit `1` has not been checked as a physical unit,
and these fixed-parameter runs are not for population inference or clinical
decisions.

Unknown profiles, changed profile files and incomplete parameter sets are
rejected; reload the version and select again. If the solver fails, inspect the
saved request.
