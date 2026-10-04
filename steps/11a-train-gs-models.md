# Step 11a — Train GS models

## Input

- `data/phenotype.tsv` (Step 00f).
- Panel dosage cache.
- Trait filters named in the notes: `--curated`, `--trait`, …
- Train panel genomic-selection models and record cross-validation metrics and provenance.

## Do

```bash
grapeancestry gs-train --pheno data/phenotype.tsv --cache results/cache/panel_dosage_167k.npz --curated --min-n 50 --k-folds 3
src/grapeancestry/breeding/gs.py
gs_models.py
provenance.py
src/grapeancestry/cli.py
```

## Get

- `results/gs/index.tsv`: cross-validation r and the best model name per trait.
- Training provenance JSON: reproducibility metadata.
- No plot is required. Tables and the index are the record.
- Grapevine decision-grade example: OIV 225 colour (`cv_r≈0.62`, `best_model=topk_ridge` in the local index).
- OIV 241 and other traits may be exploratory only. Declare that in `CLAIMS.md`.
