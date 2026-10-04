# Step 07a — Run mapDamage (or lite)

## Input

- Source markdup BAM. Use `--source-sample` lineage when the report id is `*_query`.
- Reference fasta.
- Sample type `adna` in the samples YAML.
- Estimate an aDNA damage profile from the source BAM (aDNA door).

## Do

```bash
grapeancestry run --config config/mbp_demo.yaml --samples config/samples_ages.yaml --sample Ages -j 4
grapeancestry analyze --sample Ages --source-sample Ages
src/grapeancestry/adna/damage_lite.py
```

## Get

- `results/{sample}.damage.tsv`: terminal misincorporation summary.
- `results/{sample}.mapDamage/`: mapDamage2 directory when the binary succeeds.
- Plots are produced in 07b.
- Preferred path: the full aDNA run, with damage after markdup. There is no dedicated `grapeancestry` damage CLI. `damage_lite.py` is the mapDamage2 wrapper and the lite fallback.
- Modern paired-end libraries typically mark damage unavailable in method coverage.
- Keep `--source-sample` when analyzing a renamed `*_query` VCF so the BAM lineage stays correct.
