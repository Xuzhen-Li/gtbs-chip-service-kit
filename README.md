# Genotyping by Target Sequencing Chip Service Kit

English | [中文](README.zh.md)

Registers an existing genotyping chip as a profile and checks it with `validate-profile`. Chip design is in [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip); the grapevine 167K run is [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry). Demo report: [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).

Repo slug: [`gtbs-chip-service-kit`](https://github.com/Xuzhen-Li/gtbs-chip-service-kit). Package import name: `gtbs_kit`.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Files

| Path | Role |
|------|------|
| `platform/` | Contract docs (SPI in `gtbs_kit.spi`) |
| `src/gtbs_kit/` | Load/validate profiles |
| `profiles/` | Schema + [`examples/grapevine_167k`](profiles/examples/grapevine_167k/) |
| `templates/` | Empty profile cookiecutter |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | KEEP/CUT rules |

Scripts, binaries, genomes, FASTQ, and dosage matrices are not shipped.

## Grapevine walkthrough

The analysis write-up is in [steps/](steps/), one file per step, from `00a` through `14b`. [Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry) is the grapevine 167K worked example that runs.

## Usage

The six profile steps are [docs/steps.md](docs/steps.md). The analysis order is [steps/README.md](steps/README.md). The commands in [steps/](steps/) call scripts that are not in this clone.

## Quick start

These commands match `pyproject.toml` (`gtbs-kit = gtbs_kit.cli:main`) and `src/gtbs_kit/cli.py` in the public clone: `validate-profile` loads a profile YAML, `list-examples` lists directories under `profiles/examples` that contain `profile.yaml`.

```bash
pip install -e .
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
gtbs-kit list-examples
```

## License

MIT, see [LICENSE](LICENSE). Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657)
