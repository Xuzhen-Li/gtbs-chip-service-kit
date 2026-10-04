# 1. Install

From a clone of this repo:

```bash
pip install -e .
gtbs-kit --help
```

`gtbs-kit --help` lists two commands: `validate-profile` and `list-examples`. There is no calling, PCA, or report command in this package. `environment.yml` is an optional conda file, not a second entry point.

`workflow/Snakefile` is a skeleton. Its only rule points at `results/.gitkeep`. Do not treat `snakemake` here as the analysis.

Back to [the step list](../steps.md).
