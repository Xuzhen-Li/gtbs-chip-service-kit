# What is in this repository

Repository: `gtbs-chip-service-kit`. Title: Genotyping by Target Sequencing Chip Service Kit.

## How it relates to grapeancestry

| Repository | Holds |
|------|------|
| gtbs-chip-service-kit | The profile format for any crop's capture panel, a template, and the checker |
| grapeancestry | The grapevine 167K walkthrough, guideline, and demo HTML |

## Kept here

- `README.md`, `LICENSE`, `pyproject.toml`, `requirements.txt`
- `app.py`: loads a profile in a browser page; the analysis plugin it would hand off to is private
- `Dockerfile`, `docker-compose.yml`
- `config/`: default settings only
- `platform/`: interface notes (the interfaces are in `gtbs_kit.spi`)
- `src/gtbs_kit/`: `load_profile` and the CLI
- `profiles/profile.schema.json`, `profiles/examples/grapevine_167k/`
- `templates/`, `tests/`
- `docs/`: how to add a profile (the grapevine guideline is not copied here)
- `workflow/` skeleton and `scripts/README.md`

## Not kept here

- Third-party binaries (`bin/admixture`, `bin/gcta64`, and so on)
- Large `data/` and `results/` files (genomes, FASTQ, dosage caches)
- The analysis engine (`src/grapeancestry/`); use grapeancestry or the private suite
- Full pipeline, report, and cloud code under `platform/`

## Test for a new crop

Someone should be able to read `platform/` and `profiles/examples/*`, write a `profile.yaml` for a third crop, and pass `tests/` without the analysis engine.
