# Step 03a — Clone and parent-offspring screen

## Input

- Query VCF at panel sites.
- Panel dosage cache (Step 00c).
- Sample id (report stem).
- Flag Identical and Parent-Offspring hits against the reference screen, non-self.

## Do

```bash
grapeancestry identity --vcf results/HUN89_query.vcf.gz --sample HUN89_query --out-tsv results/HUN89_query.ibs.tsv
grapeancestry analyze --sample HUN89 --as-query
src/grapeancestry/identity/run_ibs.py
parentage.py
fingerprint.py
ibs.py
```

## Get

- Clone and parent-offspring hit table: Identical and parent-offspring only. Empty if none.
- Self-in-panel QC: if the query ID is already in the panel, report self, then the nearest non-self.
- Identity section "Clone + PO list", with click-to-pin in the interactive HTML.
- Panel `HUN89` is not stem `HUN89_query` (independent chip FASTQ). Do not strip `_query` to look up Q or passport.
- The clone screen is non-self Identical and Parent-Offspring only.
