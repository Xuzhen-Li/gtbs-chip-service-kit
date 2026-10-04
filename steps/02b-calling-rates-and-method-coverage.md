# Step 02b — Calling rates and method coverage

## Input

- QC and VCF products from Steps 01b–02a.
- Profile site count (`panel_n_sites`) and whether frozen assets are present (PCA, ADMIXTURE, phenotypes).
- Separate panel versus VCF calling rates, and declare which downstream methods are available or unavailable.

## Do

```bash
grapeancestry qc --bam results/bam/Ages.markdup.bam --vcf results/Ages.vcf.gz --sample Ages
grapeancestry analyze --sample Ages
src/grapeancestry/core/qc.py
src/grapeancestry/report/build_report.py
```

## Get

- Panel calling rate: called divided by all chip sites.
- VCF-site calling rate: called divided by sites present in this VCF.
- Method coverage rows: PCA, selection, GWAS, damage, and GS, each available or unavailable.
- Method-coverage table in Sample validity, and conclusion bullets in the HTML.
- Calling-rate fields come from `grapeancestry qc` and `analyze`. Method-coverage rows are assembled in the report builder.
- Unavailable methods must be labeled unavailable. Do not invent placeholder statistics.
