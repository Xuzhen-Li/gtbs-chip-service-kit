# Step 03b — IBS and kinship ranks

## Input

- The same identity inputs as 03a: query VCF and dosage cache.
- Rank reference samples by IBS and KING-related metrics for the query.

## Do

```bash
grapeancestry identity --vcf results/Ages.vcf.gz --sample Ages --cache results/cache/panel_dosage_167k.npz --out-tsv results/Ages.ibs.tsv
grapeancestry analyze
grapeancestry run
src/grapeancestry/identity/ibs.py
run_ibs.py
```

## Get

- `results/{sample}.ibs.tsv`: top IBS neighbours.
- `results/{sample}.kinship_top.tsv`: top kinship ranks, when written.
- Summary TSVs: counts and nearest non-self.
- Side-by-side IBS top and kinship top tables in the report.
- The same tables are also produced by `grapeancestry analyze` and `run`.
- Italy 4K-style IBS versus the panel cache. Prefer the 167k dosage when it is available.
