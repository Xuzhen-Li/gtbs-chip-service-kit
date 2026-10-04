# Step 00b — Reference genome (coordinate system)

## Input

- Reference fasta and `.fai` (`paths.ref_fa` in `config/*.yaml`).
- Optional sub-reference and lift map for gated accelerated mapping.
- Config: `config/mbp_demo.yaml` or `hpc_full`, fields `paths.ref_fa` and subref.
- Fix the coordinate system every BAM and VCF in this profile must use.
- Contig naming must match the panel VCF and sites BED before Steps 01–04.

## Do

```bash
snakemake -s workflow/Snakefile --configfile config/mbp_demo.yaml --config samples_file=config/samples_demo.yaml lift_or_copy
python -m grapeancestry.core.lift --help
src/grapeancestry/core/lift.py
src/grapeancestry/core/subref.py
```

## Get

- `data/ref/*.fa` and `.fai` (local). Contig names must match the VCF and `@SQ`.
- Gate concordance stats when comparing subref versus full mapping (`src/grapeancestry/core/gate.py`).
- No plot.
- There is no dedicated `grapeancestry` CLI for staging the genome. Wire paths in config. Optional lift runs inside the Snakefile.
- A wrong coordinate system fails later projection and calling. Catch it here.
