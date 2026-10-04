# Step 00a — Panel sites and sample metadata

## Input

- Target site list as a BED, one row per chip site.
- Panel sample list and metadata table (ID, origin, Grp, use, and the other columns the table already has).
- Optional probe or loci BED for on-target QC.
- Cross-crop profile contract: [gtbs-chip-service-kit](https://github.com/Xuzhen-Li/gtbs-chip-service-kit). Grapevine paths via `config/`.
- Grapevine demo paths: `config/*.yaml`.
- Define the chip: which sites belong to the panel, and which reference sample IDs and groups exist.
- First fork point for other chips: your BED and metadata replace the grapevine 167K example.
- Keep panel IDs distinct from independent recapture stems (for example panel `HUN89` is not report `HUN89_query`).
- No dedicated `grapeancestry` CLI. Prepare files and declare them in config.

## Do

```bash
src/grapeancestry/resource/panel_export.py
```

## Get

- `data/panel/*.sites.bed` (local): calling and QC intervals.
- `data/panel/*.info` or the sample annotation: Grp colours and passport fields.
- Profile `panel_n_sites`: declared site count for method coverage.
- No plot is required. Document site count and ID rules in the profile README or `CLAIMS.md`.
- Document the inventory in `data/MANIFEST.md`. Paths are local. Matrices stay out of git.
- The helper is a library or export, not a suite CLI.
