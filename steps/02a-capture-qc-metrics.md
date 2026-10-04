# Step 02a — Capture QC metrics

## Input

- Markdup BAM (`results/bam/{sample}.markdup.bam`).
- Sites BED (default `data/panel/panel167k.sites.bed`).
- Optional query VCF for calling-rate fields.
- Compute on-target, depth, and breadth statistics for the query library.

## Do

```bash
grapeancestry qc --bam results/bam/Ages.markdup.bam --bed data/panel/panel167k.sites.bed --vcf results/Ages.vcf.gz --sample Ages --out-tsv results/Ages.qc.tsv
grapeancestry run
grapeancestry analyze
src/grapeancestry/core/qc.py
```

## Get

- `results/{sample}.qc.tsv`: on-target percent, fold enrichment, breadth at 1×, 5×, and 10×, mean and median depth, and read counts.
- Report Sample validity QC cards and the metrics table (Step 13b).
- The same metrics are also produced inside `grapeancestry run` and `grapeancestry analyze`.
- No universal pass or fail threshold is recorded. QC stays method- and data-specific.
