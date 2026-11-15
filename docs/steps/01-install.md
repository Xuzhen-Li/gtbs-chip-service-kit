# 1. Install

## Input

- A clone of this repo.
- `environment.yml` is an optional conda file, not a second entry point.
- `workflow/Snakefile` is a skeleton. Its only rule points at `results/.gitkeep`.

## Do

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
gtbs-kit --help
```

## Get

- `gtbs-kit --help` lists two commands: `validate-profile` and `list-examples`.
- There is no calling, PCA, or report command in this package.
- Do not treat `snakemake` here as the analysis.
