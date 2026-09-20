# gtbs-chip-service-kit

A reusable companion stack for **GBTS / capture-panel** genotyping services: config-driven calling → sample-first reports → optional cloud card—so **any panel** can stand up its own analysis platform. The grapevine 167K layout in `config/` + `profiles/examples/grapevine-167k/` is an **example**, not the product boundary.

**Repo slug:** `gtbs-chip-service-kit` (lab shorthand GTBS). Public English prose uses **GBTS** = Genotyping by Target Sequencing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3670--6657-a6ce39)](https://orcid.org/0000-0003-3670-6657)

## What you get

| Path | Role |
|------|------|
| `src/grapeancestry/` | Full Python package: pipeline domains, viz, sample-first V2 report, cloud card |
| `workflow/Snakefile` | FASTQ → panel-site VCF |
| `scripts/` | Panel ADMIXTURE archive / phenotype ETL helpers |
| `config/` | Example demo YAML (grapevine paths—replace for your chip) |
| `platform/` | Contracts for pipeline · report · viz · cloud (generic layer) |
| `profiles/` | How to add a panel profile + grapevine-167k stub |
| `docs/SCRIPTS.md` | **Detailed** script map (pipeline / viz / report) |
| `bin/` | ADMIXTURE 1.3.0 + GCTA wrappers (optional on PATH) |

**Not in this clone:** dosage matrices, FASTQ/BAM, reference genomes. Stage under `data/` (see `data/MANIFEST.md`).

Grapevine **public walkthrough + Ages HTML:** [Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry).

## Quick install (lab machine with your data staged)

```bash
conda env create -f environment.yml   # or use existing env `ga`
conda activate ga
pip install -e ".[dev,web]"
export PATH="$PWD/bin:$PATH"
grapeancestry --help
```

## Start here

1. [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)  
2. [docs/SCRIPTS.md](docs/SCRIPTS.md) — full script map  
3. [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — platform vs profile  
4. [profiles/README.md](profiles/README.md) — add your chip  

## License

MIT — [LICENSE](LICENSE). **Xuzhen Li** · [ORCID](https://orcid.org/0000-0003-3670-6657)
