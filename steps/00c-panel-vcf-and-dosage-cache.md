# Step 00c — Panel VCF and dosage cache

## Input

- Panel VCF at chip sites (GT).
- Sample order matching the metadata from Step 00a.
- Build the analysis matrix: panel genotypes at chip sites as a dosage cache, preferred over merging huge VCFs every run.

## Do

```bash
python -m grapeancestry.core.dosage --panel-vcf data/panel/panel167k_2449.vcf.gz --out-npz results/cache/panel_dosage_167k.npz --full
src/grapeancestry/core/dosage.py
src/grapeancestry/core/merge_ref.py
```

## Get

- `results/cache/panel_dosage_*.npz`: the primary analysis matrix for IBS, PCA, ADMIXTURE, and GS.
- Prefer `panel_dosage_167k.npz`. Smoke tests may fall back to a smaller cache.
- Optional merged VCF: a convenience 2449+query file, not the analysis matrix.
- No plot at build time.
- The dosage build is a module entry, not a `grapeancestry` subcommand.
- Downstream identity, project, and GS resolve the cache via `src/grapeancestry/core/dosage.py` (`resolve_cache`).
