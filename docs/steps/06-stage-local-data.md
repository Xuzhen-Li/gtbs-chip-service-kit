# 6. Stage data on the machine, not in git

When you have them, uncomment and point:

- `sites_bed` at a BED of panel sites
- `panel_info` at the sample table
- `dosage_cache` at the dosage matrix your reports read

`data/panel/`, `data/ref/`, and `data/fastq/` in this repo are placeholders. Binaries such as ADMIXTURE are not shipped. See `docs/REPO_LAYOUT.md` for what stays public.

Back to [the step list](../steps.md).
