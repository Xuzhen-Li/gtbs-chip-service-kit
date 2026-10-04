# How to use this kit

Two layers.

What this package runs is the six steps below: install, read the grapevine 167K example profile, copy `templates/`, fill `profile.yaml`, `validate-profile`, and point the BED, the sample table, and the dosage file at local paths. Do not commit genomes, FASTQ, VCF, or dosage.

[steps/](../steps/) (`00a` through `14b`) is the analysis write-up, one file per step. Scripts, data, and the sibling docs those pages link (`REPO_MAP.md`, `docs/SCRIPTS.md`, `docs/PIPELINE.md`, `docs/GUIDELINE.md`) are not in this repo. The grapevine 167K worked example that actually runs is [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry). Demo: [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).

Order, written out in [steps/README.md](../steps/README.md): before any new sample, `00a` through `00e` (skip `00f` and `00g` for ancestry only); each sample, `01a` through `13b`, ending at `*.sample-first-v2.report.html`; `14a` and `14b` are optional, emit `chip.json`, and are not needed for the v1 HTML. Another crop reuses the same step ids and replaces the files behind `00a`–`00e`. Designing sites is [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip), not this repo.

1. [Install](steps/01-install.md)
2. [Read the example](steps/02-read-the-example.md)
3. [Copy a profile](steps/03-copy-a-profile.md)
4. [Fill the profile](steps/04-fill-the-profile.md)
5. [Validate](steps/05-validate.md)
6. [Stage data locally](steps/06-stage-local-data.md)
7. [Run the suite](steps/07-run-the-suite.md)
