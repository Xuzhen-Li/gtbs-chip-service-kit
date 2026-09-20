# Repository layout (KEEP / CUT)

Slug: **`gtbs-chip-service-kit`**. Public title: **GBTS Chip Service Kit**.

## Split vs grapeancestry

| Repo | Role |
|------|------|
| **gtbs-chip-service-kit** | Species-agnostic GBTS/capture **service template + profile contract** |
| **grapeancestry** | Grapevine 167K **public walkthrough / GUIDELINE / demo HTML** |

## KEEP (public scaffold)

- `README.md`, `LICENSE`, `pyproject.toml`, `requirements.txt`
- `app.py` (thin: load profile → private plugin)
- `Dockerfile`, `docker-compose.yml`
- `config/` (defaults only)
- `platform/` — **thin contract docs** (SPI lives in `gtbs_kit.spi`)
- `src/gtbs_kit/` — **thin glue** (`load_profile`, CLI)
- `profiles/profile.schema.json`, `profiles/examples/grapevine_167k/`
- `templates/`, `tests/` (schema/contract)
- `docs/` (how to add a profile; no grapevine GUIDELINE paste)
- Optional: `workflow/` skeleton, `scripts/README`

## CUT from public tree

- Third-party binaries (`bin/admixture`, `bin/gcta64`, …)
- Heavy `data/` / `results/` (genomes, FASTQ, dosage caches)
- Thick `src/grapeancestry/` engines (use grapeancestry / private suite)
- Full pipeline/report/cloud **implementations** inside `platform/`

## Thin vs thick

| Layer | Public | Private / other repo |
|-------|--------|----------------------|
| `platform/` | Seams + docs | — |
| `gtbs_kit.spi` | Protocols | — |
| `src/gtbs_kit/` | load_profile, CLI | — |
| Engines | — | Snakemake bodies, HTML builders, matrix I/O |

**Acceptance:** read `platform/` + `profiles/examples/*`, write a third-crop `profile.yaml`, pass `tests/`—without cloning thick engines.
