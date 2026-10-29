# QSPQuest models

Browse pharmacology models and run fixed-parameter simulations with checksum-verified OMEX archives.
The package includes its catalog, model archives, scientific source notices and model guides.

```sh
python -m pip install qspquest-models==0.1.0rc1
python -m qspquest_models --search rituximab --runnable
```

To simulate, install the matching `qspquest==0.1.0rc1` Python package or set
`QSPQUEST_EXECUTABLE` to the matching CLI executable:

```sh
python -m qspquest_models \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.0 \
  --scenario population-typical-1000mg-full-ode --csv rituximab.csv
```

The result has 201 rows. CD19+ B cells start at 199.57 and end near 8.70521.
Choose a new output filename for each run. Pass `--library PATH` to use another
extracted library. Python also provides `qspquest_models.Library()` for discovery
and archive inspection.

This prerelease provides fixed-parameter research workflows. Availability and stored
evidence do not establish complete scientific or physical-unit qualification.
Read the selected model guide and source terms before reuse; do not use these
examples for clinical dose selection.
