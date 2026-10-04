# Step 09a — Panel Fst / sweep scan

## Input

- Panel dosage and Grp labels.
- Optional half-window bp and top-N for named windows.
- Grp-versus-rest Fst and heterozygosity extremes on the 2449 panel only (unphased).

## Do

```bash
grapeancestry selection --half-bp 50000 --top 40
src/grapeancestry/cli.py
src/grapeancestry/popgen/selscan.py
src/grapeancestry/adna/selection.py
popgen/stats.py
popgen/selection_report.py
grapeancestry analyze
grapeancestry run
```

## Get

- `results/selection/named_windows.tsv`: named-window heterozygosity and Fst.
- `results/selection/by_grp_named.tsv`: per-Grp summaries.
- Sweep rows: Fst at or above the within-Grp 95th percentile, and windowed heterozygosity at or below the 5th percentile.
- `results/selection/locuszoom.json` when present. It feeds 12a.
- Manhattan and heat plots are built in 09b.
- Also wired into `grapeancestry analyze` and `run` when selection assets exist.
- Selection is panel-only. Query genotype is an overlay later, not evidence the sample was selected.
- `fst_sites()` is a simplified Fst contrast, not canonical Weir–Cockerham unless benchmarked.
- `GEO` is reserved for GEA and origin, not this selection door.
