# Step 13b — Render sample-first V2 HTML

## Input

- Report bundle from 13a.
- Optional Plotly, D3, and LocusZoom assets under `assets/` when present.
- Write the v1 product HTML and the optional data sidecar. This is the DIY and Docker hand-in.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry run --config config/mbp_demo.yaml --samples config/samples_ages.yaml --sample Ages -j 4
grapeancestry analyze --sample HUN89 --as-query --source-sample HUN89
src/grapeancestry/report/build_report.py
src/grapeancestry/report/interactive_dashboard.py
src/grapeancestry/cli.py
```

## Get

- `{sample}.sample-first-v2.report.html`: the suite hand-in.
- Optional `*.report.data.json`: downloads sidecar.
- Provenance table: IDs, paths, and sizes.
- Public demo path: `demo/results/ramos2019_np.batch.report.html`.
- Full interactive report (PCA, ADMIXTURE, NJ, QC, and selection and GWAS doors when available). Theme: Light, Dark, or System.
- `render_full_html` is in `build_report.py`. `cli.py` runs `_post_analyze`.
- The independent-chip command above is for chip FASTQ whose passport ID is already in the panel.
- DIY no-kit and v1 HTML stop here (`00a`–`13b`). Steps 14a and 14b are optional Chip Companion JSON only.
- `HUN89` is not `HUN89_query`. PCA axes stay frozen. OIV 225 is the decision-grade GS trait. A score is not a phenotype.
