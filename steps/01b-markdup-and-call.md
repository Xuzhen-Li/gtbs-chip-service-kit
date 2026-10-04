# Step 01b — Markdup and call at panel sites

## Input

- Lifted or aligned BAM from Step 01a.
- Sites BED and reference fasta.
- The same config and samples YAML as 01a.
- Deduplicate alignments and call genotypes only at chip sites (sites BED from 00a).

## Do

```bash
grapeancestry run --config config/mbp_demo.yaml --samples config/samples_demo.yaml --sample HUN89 -j 4 --no-analyze
snakemake -s workflow/Snakefile --configfile config/mbp_demo.yaml --config samples_file=config/samples_demo.yaml -j 4 results/HUN89.vcf.gz
samtools sort
samtools fixmate
samtools markdup
bcftools mpileup/call -T sites BED
```

## Get

- `results/bam/{sample}.markdup.bam` and `.bai`: deduplicated alignments.
- `results/{sample}.vcf.gz` and `.tbi`: query VCF at panel sites.
- Plots for this product are listed later in Sample validity provenance (Step 13).
- Rules: `sort_markdup`, then `call`. `sort_markdup` is `samtools sort`, `fixmate`, and `markdup`. `call` is `bcftools mpileup` and `call` with `-T` on the sites BED.
- The analysis matrix for IBS and PCA remains the panel dosage cache (00c), not a merged VCF.
- Independent chip FASTQ for a panel ID should use `--as-query` later so the report stem is `{id}_query`.
