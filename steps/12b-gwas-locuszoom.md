# Step 12b — GWAS LocusZoom (trait leads)

## Input

- `results/gwas/**/locuszoom.json`, or the equivalent per-trait payload.
- Query VCF for the genotype strip.
- LocusZoom for panel GWAS leads (for example the OIV 225 region) with query genotype overlay.

## Do

```bash
grapeancestry gwas --pheno data/phenotype.tsv --curated
grapeancestry analyze --sample Ages
src/grapeancestry/report/interactive_dashboard.py
```

## Get

- Lead SNP genotype for this sample: overlay strip.
- Site table with p and beta: panel association context.
- GWAS LocusZoom plus genotype overlay bars and table.
- GWAS LocusZoom payloads live under `results/gwas/`.
- Strip colour is genotype, not LD.
- Panel association is not an observed customer phenotype. A GS score is not a phenotype.
