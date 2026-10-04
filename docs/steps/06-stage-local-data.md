# 6. Stage data on the machine, not in git

## Input

- A BED of panel sites for `sites_bed`, when you have it.
- The sample table for `panel_info`, when you have it.
- The dosage matrix your reports read, for `dosage_cache`, when you have it.
- `data/panel/`, `data/ref/`, and `data/fastq/` in this repo are placeholders.
- Binaries such as ADMIXTURE are not shipped.
- `docs/REPO_LAYOUT.md` says what stays public.

## Do

```bash
# No command was written down for this step.
```

## Get

- `sites_bed` uncommented and pointed at a BED of panel sites.
- `panel_info` uncommented and pointed at the sample table.
- `dosage_cache` uncommented and pointed at the dosage matrix your reports read.
- Those files stay on the machine. They are not committed.
