# Step 13a — Build report payload

## Input

- Per-sample results from Steps 02–12: QC, identity, PCA, ADMIXTURE, trees, f-stats, selection, GWAS and GS, and damage.
- Configured root layout under `results/` and `data/`.
- Gather those artifacts into a structured bundle and interactive JSON payload, with provenance and method coverage.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry run --sample Ages --analyze
src/grapeancestry/report/build_report.py
src/grapeancestry/report/interactive_data.py
src/grapeancestry/cli.py
```

## Get

- In-memory or sidecar payload: QC, identity, Q, PC, trees, coverage flags, and provenance IDs.
- Optional `*.report.data.json`: downloads sidecar when written.
- No plot until the HTML render (13b).
- Payload build is inside `analyze` and `run`. There is no standalone bundle CLI.
- `build_report.py` exposes `build_bundle`. `cli.py` runs `_post_analyze`.
- Provenance must record `query_id`, `source_sample_id`, artifact paths, and method coverage.
- Unavailable methods stay labeled unavailable.
