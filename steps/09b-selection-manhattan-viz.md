# Step 09b — Selection Manhattan and heatmaps

## Input

- Selection scan products from 09a.
- Optional query VCF for the genotype overlay in the report.
- Plot panel selection context. Overlay query genotype only as annotation.

## Do

```bash
grapeancestry selection --top 40
grapeancestry analyze --sample Ages
src/grapeancestry/popgen/selection_viz.py
selscan.py
src/grapeancestry/report/interactive_dashboard.py
```

## Get

- Metric toggles, including Fst: interactive controls.
- Optional `results/{sample}.selection.png`: static card when written.
- Manhattan and heat in the Panel research section of the HTML.
- There is no separate selection-plot CLI.
- Query genotype is not "this sample was selected." Overlay only.
- Sweep rows focus exact Manhattan points, not arbitrary LocusZoom windows.
