# Step 10a — Panel GWAS scan

## Input

- `data/phenotype.tsv` with at least 50 IDs overlapping the panel, per trait.
- Panel dosage cache.
- Trait selection flags named in the notes: `--curated`, `--trait`, `--all-traits`, …
- Run association on panel dosages times phenotypes. Panel results, not customer phenotypes.

## Do

```bash
grapeancestry gwas --pheno data/phenotype.tsv --cache results/cache/panel_dosage_167k.npz --curated --pcs 3 --maf 0.05 --min-n 50
src/grapeancestry/breeding/gwas.py
mixed_model.py
src/grapeancestry/cli.py
```

## Get

- `results/gwas/**`: summaries, lead sites, p, beta, r², and case and control n.
- Per-trait tables: panel association statistics.
- Feeds 10b cards and Step 12b GWAS LocusZoom.
- GWAS p, beta, and r² are panel results. Query genotype overlay and GS scores are not observed phenotypes.
- Binary traits: surface case and control imbalance (EMMAX caveat).
