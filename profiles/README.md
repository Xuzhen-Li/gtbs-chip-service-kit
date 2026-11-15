# Profiles

1. Copy `../templates/` to `profiles/examples/<chip_slug>/`.
2. Fill in `profile.yaml`. The rules are in `profile.schema.json`.
3. Run `python -m pytest -q tests` from the repository root.
4. Keep large files (genomes, FASTQ, VCF, dosage) out of git.

Example: [`examples/grapevine_167k/`](examples/grapevine_167k/).
