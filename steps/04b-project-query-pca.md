# Step 04b — Project query onto PCA

## Input

- Query VCF at panel sites.
- Frozen axes from 04a and 00d.
- Optional `data/panel/2449.info` for the colour column.
- Least-squares (GCTA-consistent) projection of the query onto the frozen 2449 axes.

## Do

```bash
grapeancestry project --vcf results/Ages.vcf.gz --sample Ages --info data/panel/2449.info --out-tsv results/Ages.pca.tsv
grapeancestry analyze --sample Ages --pca-color Grp
src/grapeancestry/adna/project.py
pca_lock.py
src/grapeancestry/cli.py
```

## Get

- Query PC1, PC2, and PC3: header print, and `results/{sample}.pca.tsv` when written.
- Panel reference coordinates from the freeze, not a refit.
- Interactive 2D and 3D PCA in the sample-first HTML (query star; pin as a yellow diamond).
- Method metadata: `GCTA64 GRM-PCA (panel167k_nogwas)`. Frozen axes plus least-squares query projection.
- Do not claim smartPCA as the shipped result.
