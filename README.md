# GBTS Chip Service Kit

How to register a chip you already have, and where the analysis steps are written down. It does not tell you how to design the chip.

Designing a chip (choose sites, check them against the annotation, freeze a panel) is [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip). The grapevine 167K run of this suite is [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry). Demo report: [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).

This repo is how you register a chip you already have: a profile, checked with `validate-profile`. The analysis steps are written down in [steps/](steps/), one file per step. It does not ship the scripts, genomes, or dose matrices.

Repo slug: [`gtbs-chip-service-kit`](https://github.com/Xuzhen-Li/gtbs-chip-service-kit). Package import name: `gtbs_kit`.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3670--6657-a6ce39)](https://orcid.org/0000-0003-3670-6657)

## What stays public

| Path | Role |
|------|------|
| `platform/` | Contract docs (SPI in `gtbs_kit.spi`) |
| `src/gtbs_kit/` | Load/validate profiles |
| `profiles/` | Schema + [`examples/grapevine_167k`](profiles/examples/grapevine_167k/) |
| `templates/` | Empty profile cookiecutter |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | KEEP/CUT rules |

Binaries, genomes, FASTQ, and dosage matrices are **not** shipped.

## Grapevine walkthrough

The analysis write-up is in [steps/](steps/), one file per step, from `00a` through `14b`. **[Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)** is the grapevine 167K worked example that actually runs.

## How to operate

The six profile steps are [docs/steps.md](docs/steps.md). The analysis order is [steps/README.md](steps/README.md). The commands in [steps/](steps/) call scripts that are not in this clone.

## Quick start

These commands match `pyproject.toml` (`gtbs-kit = gtbs_kit.cli:main`) and `src/gtbs_kit/cli.py` in the public clone: `validate-profile` loads a profile YAML, `list-examples` lists directories under `profiles/examples` that contain `profile.yaml`.

```bash
pip install -e .
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
gtbs-kit list-examples
```

## License

MIT — [LICENSE](LICENSE). **Xuzhen Li** · [ORCID](https://orcid.org/0000-0003-3670-6657)
