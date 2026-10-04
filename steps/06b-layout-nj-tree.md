# Step 06b — Layout NJ tree

## Input

- IBS distances from 06a.
- Tip IDs: the query plus the subsampled panel.
- Produce circular and rectangular NJ tree layout and interactive tips for the report.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry run --sample Ages
src/grapeancestry/popgen/tree_nj.py
src/grapeancestry/report/interactive_data.py
interactive_dashboard.py
```

## Get

- Tip order and coordinates, embedded in the report payload.
- Optional `results/{sample}.nj_tree.png`: static card when written.
- Report NJ tree, circular by default, with a query marker.
- No dedicated NJ CLI. Layout is report-path only.
- Library functions named in the notes: `build_nj_tree`, `tip_xy_circular`, `tip_xy_rectangular`, and `to_newick`.
- No standalone `grapeancestry` tree command. Do not invent one.
