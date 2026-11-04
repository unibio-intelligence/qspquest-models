# QSPQuest models

Browse pharmacology models and run simulations with fixed parameters.
The package includes the model catalog, model archives, model guides and source notices.

```sh
python -m pip install qspquest-models==0.1.0
python -m qspquest_models --search rituximab --runnable
```

To simulate, install the matching `qspquest==0.1.0` Python package or set
`QSPQUEST_EXECUTABLE` to the matching CLI executable:

```sh
python -m qspquest_models \
  --model qspquest_serkland_2025_rituximab_ms_pkpd --model-version 0.3.1 \
  --scenario population-typical-1000mg-full-ode --csv rituximab.csv
```

The result has 201 rows. CD19+ B cells start at 199.57 and end near 8.70521.
Choose a new output filename for each run. Pass `--library PATH` to use another
extracted library. In Python, use `qspquest_models.Library()` to browse and
inspect models.

This prerelease is for research. A model that runs or has stored results is not
thereby scientifically validated, and units have not been independently checked.
Read the model guide and source terms before reuse, and do not use these
examples to choose clinical doses.
