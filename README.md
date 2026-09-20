# GBTS Chip Service Kit

**GBTS Chip Service Kit** is a reusable companion stack for standing up automated **GBTS** (genotyping-by-target-sequencing) and capture-panel analysis services for any crop. It packages calling pipelines, report engines, and cloud interfaces as one deployable template so labs can ship a genotyping dashboard without rebuilding the stack. The grapevine **167K** panel ships only as an example profile — raw reads through interactive diagnostic reports — not as the only supported species.

Repo slug: [`gtbs-chip-service-kit`](https://github.com/Xuzhen-Li/gtbs-chip-service-kit).

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

## Quick start

```bash
pip install -e .
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
gtbs-kit list-examples
```

## License

MIT — [LICENSE](LICENSE). **Xuzhen Li** · [ORCID](https://orcid.org/0000-0003-3670-6657)
