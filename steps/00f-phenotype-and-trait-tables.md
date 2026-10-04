# Step 00f — Phenotype and trait tables

## Input

- Long-table phenotypes joined to panel IDs.
- Trait scale rules (ordinal or binary). OIV and trait locus tables as available.
- Stage phenotypes and trait dictionaries for panel GWAS and GS. Skip this step for ancestry-only doors.

## Do

```bash
python scripts/build_phenotype.py --help
src/grapeancestry/breeding/phenotype.py
src/grapeancestry/resource/oiv.py
grapeancestry gwas --pheno data/phenotype.tsv --curated
grapeancestry gs-train --pheno data/phenotype.tsv --curated
```

## Get

- `data/phenotype.tsv`: training input. Suite rule of thumb is at least 50 overlapping panel IDs per trait.
- Trait dictionary and template TSVs: binary rules and labels (`data/phenotype_template.tsv`).
- No plot at prep. The tables are used later in Steps 10–11 cards.
- There is no `grapeancestry` phenotype subcommand. The ETL helper is `scripts/build_phenotype.py`.
- Declare which traits are decision-grade in profile `CLAIMS.md` before treating scores as rankable.
- Grapevine example: only OIV 225 colour GS is decision-grade. Other traits may be exploratory.
- Uti (WINE/TABLE) is not used as a breeding trait.
