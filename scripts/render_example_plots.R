# Run from the library checkout: Rscript scripts/render_example_plots.R
# Previews use stored trajectories and require only base R.
stopifnot(file.exists('catalog.json'))
read_result <- function(model, version, scenario) {
  path <- file.path('models', model, version, 'results', scenario, 'qspquest.csv.gz')
  read.csv(gzfile(path))
}
rituximab <- read_result('qspquest_serkland_2025_rituximab_ms_pkpd', '0.1.0',
                        'population-typical-1000mg-full-ode')
svg('tutorials/rituximab-bcells.svg', width = 7, height = 4)
par(mar = c(4.5, 4.5, 2.5, 1), las = 1)
plot(rituximab$time, rituximab$cd19_cells_mm3, type = 'l', lwd = 2.5,
     col = '#0369a1', xlab = 'Time (days)', ylab = 'CD19+ B cells (source scale)',
     main = 'Rituximab: typical-parameter experiment', bty = 'l')
dev.off()
scenarios <- c('Balanced gate' = 'balanced_gate_30nmol_iv',
               'No tumor gate' = 'no_tumor_gate_30nmol_iv',
               'Systemic leakage' = 'leaky_systemic_gate_30nmol_iv',
               'No dose' = 'no_dose_homeostasis')
trajectories <- lapply(scenarios, function(scenario)
  read_result('qspquest_ubi_2026_target_gated_cargo_qsp', '2.0.0', scenario))
svg('tutorials/qsp-occupancy.svg', width = 11, height = 4.5)
par(mfrow = c(1, 2), mar = c(4.5, 4.5, 2.5, 1), las = 1)
colors <- c('#0284c7', '#ea580c', '#16a34a', '#64748b')
for (column in c('tumor_receptor_occupancy_percent', 'central_receptor_occupancy_percent')) {
  plot(0, 0, type = 'n', xlim = c(0, 336), ylim = c(0, 100), bty = 'l',
       xlab = 'Time (hours)', ylab = 'Occupancy (%; source scale)',
       main = if (startsWith(column, 'tumor')) 'Tumor receptor occupancy' else 'Central receptor occupancy')
  for (i in seq_along(trajectories)) {
    d <- trajectories[[i]]
    lines(d$time, d[[column]], col = colors[i], lty = i, lwd = 2.5)
  }
  legend('topright', names(trajectories), col = colors, lty = seq_along(colors),
         lwd = 2.5, cex = 0.8, bty = 'n')
}
dev.off()
