# Step 07b — Damage and fragment-length plots

## Input

- Damage TSV and mapDamage outputs from 07a.
- Report builder context for the sample.
- Display terminal C→T and G→A curves, and the insert-size or fragment-length histogram.

## Do

```bash
grapeancestry analyze --sample Ages --source-sample Ages
src/grapeancestry/adna/damage_lite.py
src/grapeancestry/report/build_report.py
interactive_dashboard.py
```

## Get

- Position-1 misincorporation rates: figure caption and metadata.
- Damage panel payload: curves and histogram for the HTML.
- Sample validity damage panel: two curves and a histogram.
- Embedded by `analyze` and `run` report builders. There is no separate plot CLI.
- aDNA-specific visualization. Modern paired-end runs leave this door unavailable rather than fabricating curves.
