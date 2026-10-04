# Step 05a — Resolve ADMIXTURE family (lookup vs project)

## Input

- Ingested Q and P under `data/panel/admixture/` (Step 00e).
- Query sample id and VCF.
- Mode flags from the CLI: `auto`, `lookup`, `nnls`, or `official`.
- Choose the frozen ADMIXTURE family and decide lookup (in-panel ID) versus `-P` or NNLS (new ID).

## Do

```bash
grapeancestry analyze --sample Ages --admix-mode auto
grapeancestry analyze --sample HUN89 --as-query --admix-mode auto
grapeancestry admix-project --vcf results/Ages.vcf.gz --admix-mode auto
src/grapeancestry/adna/admixture.py
admix_project.py
panel167k_nogwas.py
```

## Get

- Active family name: `panel167k_nogwas` when that ingest is complete, otherwise the Science `core_ld_sort` archive.
- Mode decision: lookup versus project. K set 2–8, or K8-only.
- No plot.
- Resolution happens inside `analyze` and `admix-project`. There is no standalone resolve CLI.
- Default family when ingested: `panel167k_nogwas`. Otherwise the Science archive is used for lookup.
- `--admix-k8-only` applies to `run` and `analyze` report paths, not to `admix-project`.
