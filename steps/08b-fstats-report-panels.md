# Step 08b — f-statistic report panels

## Input

- f3 and f4 contrast tables from 08a (report payload).
- Surface the highest shared drift and the largest absolute Z summaries in the UI.

## Do

```bash
grapeancestry analyze --sample Ages
src/grapeancestry/popgen/fstats_report.py
src/grapeancestry/report/interactive_dashboard.py
```

## Get

- Summary strings in the payload: highest shared drift and absolute-Z highlights.
- Optional `results/{sample}.fstats.png`: static card when written.
- Outgroup-f3 and pairwise f4 panels in the interactive HTML.
- Report path only, the same as 08a.
- Exploratory only. Not ADMIXTOOLS qp graphs.
- No dedicated f-stats CLI. Panels are assembled by the report builder.
