# Run and plot a model in Python

[Choose a model](../MODEL_CATALOG.md) · [Understand results](understand-results.md) · [Change an input](change-inputs.md)

Complete the [README setup](../README.md#setup), activate that environment,
and run the blocks below from any working directory. Core simulation needs no
plotting packages.

An [executable notebook](python-quickstart.ipynb) is also available; open it in Jupyter
after setup. It uses the installed bundled library and saves CSV output
in the notebook’s working directory.

## Run the first experiment

```python
from qspquest_models import Library

library = Library()
print(len(library.list_models()))  # 62 identities
model = library.load('qspquest_serkland_2025_rituximab_ms_pkpd', version='0.3.2')
print(model.scenario_ids)
result = model.run('population-typical-1000mg-full-ode')
assert len(result['times']) == 201
model.write_csv(result, 'rituximab-python.csv')
print('Saved rituximab-python.csv and its .manifest.json with', len(result['times']), 'rows')
```

`result` contains `times`, event `sides`, and named `outputs` and `states` with
their units. The CSV has 201 data rows from day 0 to day 200 with `time`, `side`,
`rituximab_concentration_mg_l`, `cd19_cells_mm3` as the primary readouts. The [model guide](../models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.2/MODEL_CARD.md) explains the available experiments.
[Understand results](understand-results.md) explains the units.

## Plot CD19+ B cells (optional)

Install matplotlib into the same environment with `python -m pip install matplotlib`.
Then continue in the same Python session:

```python
import matplotlib.pyplot as plt

cd19_cells_mm3 = next(c for c in result['outputs'] if c['name'] == 'cd19_cells_mm3')
plt.plot(result['times'], cd19_cells_mm3['values'])
plt.xlabel('Time (' + result['time_unit'] + ')')
plt.ylabel('CD19+ B cells (source scale)')
plt.show()
```

![Stored rituximab B-cell trajectory](rituximab-bcells.svg)

This preview shows the stored result from version 0.1.0; it is not a check of version 0.3.2.

The simulated B-cell readout starts at 199.57 and ends near 8.70521 at day 200.
This curve uses one typical parameter set. It does not show patient-to-patient
variability or recommend a redosing time.

## Run a synthetic benchmark

```python
model = library.load('qspquest_diffdose_2026_idr_benchmark')
result = model.run('lower_exposure')
```

## Find other models

Browse the [model catalog](../MODEL_CATALOG.md) for scientific descriptions and
experiment choices. In Python, you can filter the structured records:

```python
matches = [row for row in library.list_models()
           if 'rituximab' in row['name'].lower() and row['scenario_ids']]
for row in matches:
    print(row['name'], row['id'])
```

## Compare declared representations of a source

The rat AAV/mAb paper has a full and a reduced model. Use the installed library
to list both without running a simulation:

```bash
python - <<'FAMILY'
from qspquest_models import Library

library = Library()
family_id = 'liu-2026-aav-mab-targetx-rat-brain'
related = [row for row in library.list_models()
           if row.get('source_family', {}).get('family_id') == family_id]
assert len(related) == 2
canonical = related[0]['source_family']['canonical_model']
for row in related:
    assert row['source_family']['canonical_model'] == canonical
    print(row['model_fidelity'], row['id'], row['version'], len(row['scenario_ids']))
    print('archive:', row['omex_sha256'])
    print('units:', row['availability']['unit_status'])
print('canonical:', canonical['model_id'], canonical['version'])
FAMILY
```

Expect the full model at version `2.1.2` with 13 presets and the reduced model at
`0.1.0` with seven. Both list the full model as canonical, and both have unit
status `source_scale_unqualified`. Read each model guide before choosing an
experiment.

A model without `source_family` has no declared relative, even if its name looks
similar to another.

Continue with [comparing experiments or changing a dose](change-inputs.md).
For exact version selection and archive inspection, use the [technical reference](model-format.md).

To edit inputs reproducibly, follow the [input-binding tutorial](input-bindings.md).

This example needs the matching QSPQuest engine, which supports the `[cell]` count unit. The model reports rituximab concentration in `mg/L` and CD19+ cell density in `[cell]/mm3`; these units have not yet been independently checked. An `unknown_unit` error means your engine lacks `[cell]` support: install the matching engine instead of changing the unit to `1`.
