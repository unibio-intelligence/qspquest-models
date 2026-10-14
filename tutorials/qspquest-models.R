# Named OMEX simulations through the QSPQuest engine.
qspquest_library <- function(root, python = Sys.getenv("QSPQUEST_PYTHON", "python3"), executable = Sys.getenv("QSPQUEST_EXECUTABLE", "")) {
  root <- normalizePath(root, mustWork = TRUE)
  invoke <- function(args) {
    # A local installed package supplies the loader. Pass paths as arguments.
    output <- tempfile(fileext = ".json"); on.exit(unlink(output))
    command <- c("-m", "qspquest_models", "--library", shQuote(root), "--format", "json")
    if (nzchar(executable)) command <- c(command, "--executable", shQuote(executable))
    value <- system2(python, c(command, args), stdout = TRUE, stderr = output)
    if (!is.null(attr(value, "status")) && attr(value, "status") != 0L) stop(paste(readLines(output), collapse = "\n"))
    paste(value, collapse = "\n")
  }
  model_args <- function(model, version) {
    args <- c("--model", shQuote(model))
    if (!is.null(version)) {
      if (!is.character(version) || length(version) != 1L || is.na(version) || !nzchar(version))
        stop("version must be NULL or one nonempty exact model-version string")
      args <- c(args, "--model-version", shQuote(version))
    }
    args
  }
  list(
    models = function() jsonlite::fromJSON(invoke(character()), simplifyVector = FALSE),
    scenarios = function(model, version = NULL) jsonlite::fromJSON(invoke(model_args(model, version))),
    inputs = function(model, scenario, version = NULL) jsonlite::fromJSON(invoke(c(model_args(model, version), "--scenario", shQuote(scenario), "--inputs")), simplifyVector = FALSE),
    run = function(model, scenario, dose_index = NULL, dose_amount = NULL, initial_states = NULL, save_research = NULL, csv = NULL, version = NULL) {
      path <- tempfile(fileext = ".json"); on.exit(unlink(path))
      args <- c(model_args(model, version), "--scenario", shQuote(scenario), "--json", shQuote(path))
      if (xor(is.null(dose_index), is.null(dose_amount))) stop("Supply both dose_index and dose_amount")
      if (!is.null(dose_index)) args <- c(args, "--dose", shQuote(paste0(dose_index, "=", dose_amount)))
      if (!is.null(initial_states)) {
        if (is.null(names(initial_states)) || any(!nzchar(names(initial_states)))) stop("initial_states must have biological state names")
        for (name in names(initial_states)) args <- c(args, "--initial", shQuote(paste0(name, "=", initial_states[[name]])))
      }
      if (!is.null(csv)) args <- c(args, "--csv", shQuote(csv))
      if (!is.null(save_research)) args <- c(args, "--save-research", shQuote(save_research))
      invoke(args)
      jsonlite::fromJSON(path, simplifyVector = FALSE)
    }
  )
}
qspquest_data_frame <- function(result, all_readouts = FALSE) {
  out <- data.frame(time = unlist(result$times), side = unlist(result$sides))
  columns <- list()
  for (column in result$outputs) columns[[column$name]] <- column
  for (column in result$states) columns[[paste0("state__", column$name)]] <- column
  for (column in result$source_values) columns[[paste0("source__", column$name)]] <- column
  names <- names(columns)
  if (!all_readouts && !is.null(result$primary_readouts)) {
    names <- vapply(result$primary_readouts, function(r) paste0(
      switch(r$kind, state = "state__", source_parameter = "source__", output = ""), r$name), "")
  }
  for (name in names) {
    if (is.null(columns[[name]])) stop(paste("Missing primary readout:", name))
    out[[name]] <- unlist(columns[[name]]$values)
  }
  attr(out, "execution_identity") <- result$identity
  attr(out, "time_unit") <- result$time_unit
  out
}

# Validate the CSV/manifest pair before constructing an ordinary R data frame.
qspquest_read_table <- function(path, python = Sys.getenv("QSPQUEST_PYTHON", "python3")) {
  path <- normalizePath(path, mustWork = TRUE)
  errors <- tempfile(); on.exit(unlink(errors))
  metadata <- system2(python, c("-m", "qspquest_models", "--verify-table", shQuote(path), "--format", "json", "--json-errors"),
                      stdout = TRUE, stderr = errors)
  if (!is.null(attr(metadata, "status")) && attr(metadata, "status") != 0L)
    stop(paste(readLines(errors), collapse = "\n"))
  bundle <- jsonlite::fromJSON(paste(metadata, collapse = "\n"), simplifyVector = FALSE)
  manifest <- bundle$manifest
  names <- vapply(manifest$table$columns, function(column) column$name, "")
  columns <- lapply(names, function(name) {
    if (name == "side") vapply(bundle$rows, function(row) row[[name]], "")
    else vapply(bundle$rows, function(row) as.numeric(row[[name]]), 0.0)
  })
  names(columns) <- names
  table <- as.data.frame(columns, check.names = FALSE, stringsAsFactors = FALSE)
  attr(table, "manifest") <- manifest
  table
}
