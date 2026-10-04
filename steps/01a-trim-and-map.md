# Step 01a — Trim and map

## Input

- FASTQ paths from the sample YAML (`config/samples_*.yaml`, field `type`: `pe`, `se`, or `adna`).
- Reference fasta from Step 00b.
- Config: `config/mbp_demo.yaml` or `hpc_full.yaml`.
- Clean reads and align them to the profile reference (modern paired-end or aDNA single-end).
- Snakefile rules: `trim_pe`, `trim_se`, or `trim_adna`, then `map_pe`, `map_se`, or `map_aln`, then `lift_or_copy`.

## Do

```bash
grapeancestry run --config config/mbp_demo.yaml --samples config/samples_ages.yaml --sample Ages -j 4 --mapping full
snakemake -s workflow/Snakefile --configfile config/mbp_demo.yaml --config samples_file=config/samples_ages.yaml -j 4 results/bam/Ages.raw.bam
fastp
bwa mem
AdapterRemoval3
bwa aln -l 1024 -n 0.01
samse
python -m grapeancestry.core.lift
src/grapeancestry/core/gate.py
```

## Get

- `results/trim/*`: trimmed FASTQ plus fastp and AdapterRemoval reports.
- `results/bam/{sample}.raw.bam` or `.lifted.bam`: mapping product, before markdup.
- No plot is required. Trim HTML and JSON logs only.
- Modern paired-end: `fastp` (`trim_pe`), then `bwa mem` (`map_pe`), then optional `lift_or_copy`.
- aDNA single-end: AdapterRemoval3 (`trim_adna`, minimum length 25), then `bwa aln` and `samse` (`map_aln`, `-l 1024 -n 0.01`), then `lift_or_copy`.
- `mapping: full` after gate concordance (pipeline docs cite 0.959) uses the full reference. `subref` lifts via `python -m grapeancestry.core.lift`.
- The aDNA door also feeds Steps 07a and 07b (damage).
