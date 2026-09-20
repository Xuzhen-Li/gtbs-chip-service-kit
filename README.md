# chip-companion

A reusable companion stack for **GBTS / capture-panel** genotyping services: config-driven calling → sample-first reports → optional cloud card—so any panel can stand up its own analysis platform. The grapevine 167K profile is an **example**, not the product boundary.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3670--6657-a6ce39)](https://orcid.org/0000-0003-3670-6657)

## What this is

| Layer | Role |
|-------|------|
| **`platform/`** | Generic service modules: pipeline orchestration, sample-first report builders, viz helpers, optional cloud (`chip.json`) skeleton |
| **`profiles/`** | Panel-specific configs (sites, frozen axes pointers, claim boundaries). Add yours here |
| **`templates/`** | Empty profile cookiecutter |
| **`docs/`** | How to stand up a companion service (English) |

**Not shipped here:** panel dosage matrices, FASTQ/BAM/full VCFs, reference genomes, frozen PCA/ADMIXTURE binaries, private passport/phenotype DBs. Stage those locally; see each profile’s manifest notes.

## Worked example (grapevine)

Public walkthrough + Ages demo HTML live on **[Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)** (docs face for the 167K panel).  
This repo’s `profiles/examples/grapevine-167k/` is only an **example profile stub** that points at that face.

## Layout

```text
chip-companion/
  docs/                 # getting started, architecture, claims
  platform/             # pipeline · report · viz · cloud (generic)
  profiles/examples/grapevine-167k/
  templates/            # empty profile
  tests/                # tiny synthetic fixtures (later)
```

## Status

Skeleton + English docs boundary (2026-09). Runnable thin modules land next; heavy compute stays in your private suite.

## License

MIT — see [LICENSE](LICENSE). **Xuzhen Li** · [ORCID](https://orcid.org/0000-0003-3670-6657)
