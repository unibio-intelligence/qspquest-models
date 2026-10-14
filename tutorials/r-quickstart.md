# Run and plot a model in R

[Choose a model](../MODEL_CATALOG.md) · [Understand results](understand-results.md) · [Change an input](change-inputs.md)

Complete the [README setup](../README.md#setup). R uses a local Python
bridge to the same standalone engine. Start R from the activated environment in
the library checkout, or set `QSPQUEST_PYTHON` to that environment's Python path.

Install the one R dependency if needed:

```r
install.packages('jsonlite')
```

## Run the first experiment

```r
source('tutorials/qspquest-models.R')
models <- qspquest_library(getwd())
length(models$models())  # 72 identities
model <- 'qspquest_serkland_2025_rituximab_ms_pkpd'
models$scenarios(model, version = '0.3.0')
result <- models$run(model, 'population-typical-1000mg-full-ode', csv = 'rituximab-r.csv', version = '0.3.0')
trajectory <- qspquest_data_frame(result)
stopifnot(nrow(trajectory) == 201L)
head(trajectory)
saved <- qspquest_read_table('rituximab-r.csv')
stopifnot(nrow(saved) == 201L)
```

The table contains `time`, event `side`, `rituximab_concentration_mg_l`,
`cd19_cells_mm3` as the primary readouts. The result also records
engine identity, archive checksum and units. The [model guide](../models/qspquest_serkland_2025_rituximab_ms_pkpd/0.3.0/MODEL_CARD.md) explains the experiments;
[output interpretation](understand-results.md) explains their numerical scale.
The optional `version` argument pins the exact catalog selection. An unavailable
pin fails before execution; omit it to select the current default. The same pin
is accepted by `models$inputs(model, scenario, version = '0.3.0')`.

## Plot B-cell dynamics

```r
plot(trajectory$time, trajectory$cd19_cells_mm3, type = 'l',
     xlab = result$time_unit, ylab = 'CD19+ B cells (source scale)')
```

![Stored rituximab B-cell trajectory](rituximab-bcells.svg)

This preview uses the retained version 0.1.0 result. Its numerical reference
applies to that archive and recorded execution; inspect the selected version’s
`evidence.json` before treating a new run as qualified.

The B-cell readout starts at 199.57 and ends near 8.70521 at day 200.
This is a fixed-parameter trajectory, rather than a population distribution.

## Try a synthetic benchmark

```r
model <- 'qspquest_diffdose_2026_idr_benchmark'
scenarios <- models$scenarios(model)
result <- models$run(model, 'lower_exposure')
trajectory <- qspquest_data_frame(result)
```

Use the [model catalog](../MODEL_CATALOG.md) to choose another model and read its
experiment descriptions. The bridge returns runnable experiments only.
The [input-change guide](change-inputs.md) includes supported Python, R and CLI examples for editing doses and initial states.

If Python cannot import the loader, select the environment where `pip install -e .`
ran: `Sys.setenv(QSPQUEST_PYTHON = '/absolute/path/to/.venv/bin/python')`.
If no engine is found, set `QSPQUEST_EXECUTABLE` to the CLI's absolute path.
Recreate `models` after changing these variables. See the
[executable R Markdown](r-quickstart.Rmd) for a complete run.

This example requires the matching QSPQuest engine with `[cell]` count-unit support. The selected model uses `mg/L` rituximab concentration and `[cell]/mm3` CD19-positive cell density; its dimensional and numerical qualification remain pending. An `unknown_unit` error means the engine build lacks count-unit support: install the matching engine rather than substituting unit `1`.
