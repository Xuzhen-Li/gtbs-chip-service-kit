# Genotyping by Target Sequencing Chip Service Kit

English | [中文](README.zh.md)

Describes a genotyping chip (capture panel) in a small `profile.yaml` and
checks that file. The Python package is `gtbs_kit`; the command is
`gtbs-kit`.

This repository does not genotype samples. It holds the profile format,
an example profile for the grapevine 167K panel, a template for a new
chip, and a written analysis order in [steps/](steps/). The scripts those
steps call are not in this repository. The grapevine run that does work end
to end is [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)
(demo report:
[ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html)).
How the grapevine sites were chosen is in
[grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip).

## Install

Python 3.11 or newer.

```bash
git clone https://github.com/Xuzhen-Li/gtbs-chip-service-kit.git
cd gtbs-chip-service-kit
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

## Try it

```bash
gtbs-kit list-examples
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
```

Output of the second command (run on 2026-11-15):

```json
{
  "claims_doc": "CLAIMS.md",
  "coordinate_system": "VS-1",
  "handin": {
    "cloud": "chip.json",
    "suite": "*.sample-first-v2.report.html"
  },
  "label": "Grapevine 167K genotyping by target sequencing / liquid-capture panel (example only)",
  "panel_n_sites": 167433,
  "profile_id": "grapevine_167k",
  "walkthrough_url": "https://github.com/Xuzhen-Li/grapeancestry"
}
```

## Add your own chip

```bash
cp -R templates profiles/examples/my_chip
# edit profiles/examples/my_chip/profile.yaml: profile_id, label, panel_n_sites, coordinate_system
gtbs-kit validate-profile profiles/examples/my_chip/profile.yaml
python -m pytest -q tests
```

`validate-profile` only checks that `profile_id` and `panel_n_sites` are
present. The tests check every profile under `profiles/examples/` against
the rules in `profiles/profile.schema.json` (for example,
`panel_n_sites` must be a whole number of at least 1), so the copied
template fails until you fill it in. Step-by-step notes:
[docs/steps.md](docs/steps.md).

Keep genomes, FASTQ, VCFs, and dosage matrices on your own machine. Point
`sites_bed`, `panel_info`, and `dosage_cache` at them there; do not commit
them.

## Files

| Path | What it is |
|------|------------|
| `src/gtbs_kit/` | Profile loader and the `gtbs-kit` command |
| `profiles/profile.schema.json` | Profile format |
| `profiles/examples/grapevine_167k/` | Example profile |
| `templates/` | Blank profile to copy |
| `steps/` | Analysis order, `00a` to `14b` (scripts not included) |
| `platform/` | Interface notes (`gtbs_kit.spi`) |
| `app.py` | Optional browser page for the same check (`pip install streamlit`, then `streamlit run app.py`) |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | What is kept public and what is not |

## License

MIT, see [LICENSE](LICENSE). Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657).
