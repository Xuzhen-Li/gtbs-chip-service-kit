# Step 05b — Project query ADMIXTURE Q

## Input

- Query VCF or VCFs at panel sites.
- Complete `panel167k_nogwas` P and Q ingest, required for `admix-project`.
- `admixture` 1.3.0 on PATH.
- Write query Q for each requested K using frozen P (`admixture -P` or NNLS).

## Do

```bash
grapeancestry admix-project --vcf results/Ages.vcf.gz --vcf results/HUN89_query.vcf.gz --out-dir results/admix_project --admix-mode auto
grapeancestry analyze --sample Ages --admix-all-k
grapeancestry run --sample Ages --admix-all-k
admixture -P
src/grapeancestry/adna/admix_project.py
admixture.py
```

## Get

- `results/{sample}.admix.K{k}.Q.tsv`, or the same under `--out-dir`: query Q per K.
- Optional `{sid}.report.html` from `admix-project --html`: a K=2–8 interactive ADMIXTURE-only report.
- ADMIXTURE bar chart with K tabs. The query column is highlighted in the full HTML or in the admix-project HTML.
- New samples on `panel167k_nogwas` use `admixture -P` for K=2–8, with the same P rows as the sites file.
- The report states the linkage-equilibrium assumption is violated (no extra LD prune).
- If P is not ingested, `admix-project` exits with a clear warning. Do not invent Q.
