# GBTS Chip Service Kit

How to build your own analysis suite from chip data you already have. This repo is the suite: profiles, reports, and the service scaffold. It does not tell you how to design the chip.

Designing a chip (choose sites, check them against the annotation, freeze a panel) is [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip). The grapevine 167K run of this suite is [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry). Demo report: [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).

**GBTS Chip Service Kit** is a reusable companion stack for standing up automated genotyping by target sequencing (GBTS) and capture-panel analysis services for any crop. It packages calling pipelines, report engines, and cloud interfaces as one deployable template so labs can ship a genotyping dashboard without rebuilding the stack. The grapevine **167K** panel ships only as an example profile — raw reads through interactive diagnostic reports — not as the only supported species.

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

## Grapevine walkthrough (separate repo)

Example profile points at **[Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)** (GUIDELINE, Ages demo HTML, step docs). That walkthrough is not duplicated here.

## How to operate

One file per step: [docs/steps.md](docs/steps.md). Install, copy `templates/`, fill `profile.yaml`, then `gtbs-kit validate-profile`. Calling and the HTML report are not commands in this repo. They are the step files in [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry/tree/main/steps).

## Quick start

These commands match `pyproject.toml` (`gtbs-kit = gtbs_kit.cli:main`) and `src/gtbs_kit/cli.py` in the public clone: `validate-profile` loads a profile YAML, `list-examples` lists directories under `profiles/examples` that contain `profile.yaml`.

```bash
pip install -e .
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
gtbs-kit list-examples
```

## License

MIT — [LICENSE](LICENSE). **Xuzhen Li** · [ORCID](https://orcid.org/0000-0003-3670-6657)
