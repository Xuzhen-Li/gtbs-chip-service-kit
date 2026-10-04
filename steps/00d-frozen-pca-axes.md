# Step 00d — Freeze PCA axes

## Input

- Panel dosage at the sites used for PCA (example family: `panel167k_nogwas`).
- Sample keep list and GCTA inputs produced in the lab archive.
- Binary `gcta64` on PATH.
- Compute the panel PCA and GRM axes once. Every customer query projects onto that frozen coordinate system.

## Do

```bash
src/grapeancestry/adna/pca_lock.py
src/grapeancestry/adna/project.py
src/grapeancestry/adna/smartpca_project.py
```

## Get

- GCTA freeze under `results/cache/` (lab): eigenvectors and eigenvalues reused by Step 04.
- `pca_lock` stamp metadata: provenance that the axes are frozen.
- Optional lab QC scatter of panel-only PCA. That scatter is not the customer hand-in.
- No dedicated `grapeancestry` freeze-fit CLI. The lab produces GCTA eigenvec and eigenval once. The suite loads the freeze.
- Load path, library only, used by `grapeancestry` project and analyze: `load_gcta_freeze()` and `locked_pca_for_sample()`.
- `src/grapeancestry/adna/smartpca_project.py` is a historical or alternative label only, not the default shipped PCA.
- Per-query projection is Step 04b (`grapeancestry project`).
- Shipped method label: GCTA64 GRM-PCA on frozen 2449 axes. Queries are least-squares projected. Do not unsupervised-refit panel+N per night.
- EIGENSOFT smartPCA is historical or alternative documentation only.
