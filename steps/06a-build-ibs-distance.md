# Step 06a — Build IBS distance for tree

## Input

- Query dosage from the VCF, plus the panel dosage cache.
- Tip subsample and keep rules inside the tree builder.
- Compute identity distances between the query and the panel tips used in the NJ tree.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry run --sample Ages
src/grapeancestry/popgen/tree_nj.py
```

## Get

- Distance matrix or condensed vector, in memory or cache, for the layout in 06b.
- No plot yet. Layout is 06b.
- No dedicated `grapeancestry` NJ or distance CLI. Distance prep runs on the report path.
- Library functions named in the notes: `ibs_distance_to_rows`, `ibs_distance_matrix`, `load_or_compute_panel_ibs_d`, and `assemble_tree_distance`.
- There is no `grapeancestry nj` or `tree` subcommand. Use `analyze` or `run`, or call `tree_nj` from Python.
