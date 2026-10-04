# Step 10b — GWAS trait cards

## Input

- GWAS summaries from 10a.
- Query VCF only for genotype overlay fields.
- Present per-trait GWAS results and imbalance warnings on the report and Cloud cards.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry chip-report --vcf results/Ages.vcf.gz --out chip.json
src/grapeancestry/breeding/methods_doc.py
src/grapeancestry/cloud/mas.py
card.py
src/grapeancestry/report/build_report.py
```

## Get

- Card fields: top site, N, coverage, and Bayes or p summaries as available.
- Imbalance warnings: binary case and control n when relevant.
- Sample evidence and MAS cards in the HTML or the Cloud UI.
- Cards are assembled on the report and Cloud paths.
- DIY and the v1 product stop at 13b (`*.sample-first-v2.report.html`). `chip-report` to `chip.json` is Steps 14 only.
- Panel GWAS is not a customer measured phenotype.
- A score is not a phenotype (see also GS Step 11b).
