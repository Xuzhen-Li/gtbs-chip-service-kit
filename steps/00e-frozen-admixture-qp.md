# Step 00e — Freeze ADMIXTURE Q/P

## Input

- Panel BED and fam for the chosen site family (`panel167k_nogwas` when ingested).
- HPC or local ADMIXTURE runs (`admixture` 1.3.0 on PATH).
- Fit or ingest frozen ADMIXTURE P and panel Q for K=2–8 so new samples only project (`admixture -P` or NNLS).

## Do

```bash
scripts/prep_admixture_bed.py
scripts/run_admixture_local.sh
scripts/ingest_admixture_qp.py
scripts/admixture_fit_qc.py
scripts/rebuild_manual_qp.py
src/grapeancestry/adna/admixture.py
panel167k_nogwas.py
grapeancestry admix-project --vcf results/Ages.vcf.gz
scripts/plot_*.py
```

## Get

- Frozen `*.P` and `*.Q` per K under `data/panel/admixture/`. Column order must match the sites file.
- Family provenance and manifest: which archive is active (`panel167k_nogwas` preferred).
- Lab purest-align and K-check PNGs from `scripts/plot_*.py`. Archive QC only, not v1 product HTML.
- The fit and ingest scripts are not `grapeancestry` subcommands. Customer or batch projection after ingest is `grapeancestry admix-project`.
- In-panel IDs use Q lookup. New IDs project with frozen P.
- Do not unsupervised-refit 2449+N customers each night.
- `grapeancestry run` and `analyze` accept `--admix-k8-only`. That flag is not an `admix-project` option.
