# Step 04a — Load frozen PCA axes

## Input

- Lab GCTA freeze artifacts under `results/cache/` (eigenvec and eigenval).
- Panel dosage cache for site alignment.
- Root layout expected by `pca_lock`.
- Resolve the frozen GCTA and `pca_lock` axis cache built in Step 00d. No refit.

## Do

```bash
src/grapeancestry/adna/pca_lock.py
src/grapeancestry/core/dosage.py
grapeancestry project --vcf results/Ages.vcf.gz --sample Ages
```

## Get

- In-memory `GctaFreeze`: axis files and eigenvalue fractions ready for projection.
- Lock stamp: confirms frozen axes, not a per-customer refit.
- No plot until 04b.
- No dedicated freeze-load CLI. Loading is library-only: `load_gcta_freeze()` and `locked_pca_for_sample()` in `pca_lock.py`, and `resolve_cache()` in `dosage.py`. Used internally by `grapeancestry project` and `analyze`.
- The customer projection CLI is Step 04b.
- If the freeze is missing, projection cannot invent new panel axes. Stage Step 00d first.
- Axes stay frozen. Only the query is least-squares projected.
