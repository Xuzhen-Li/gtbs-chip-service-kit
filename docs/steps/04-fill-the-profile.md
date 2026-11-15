# 4. Fill the profile

## Input

- `profiles/examples/your_chip/profile.yaml`.
- `load_profile` requires `profile_id` and `panel_n_sites`.
- The schema also requires `label`, and `panel_n_sites` must be an integer of at least 1.
- The CLI does not read the schema file. The tests do.

## Do

```bash
python -m pytest -q tests/test_profile_schema.py
```

## Get

- `profile_id`: the folder name you chose.
- `label`: a sentence a reader can recognize.
- `panel_n_sites`: how many sites are on the chip.
- `coordinate_system`: the reference those sites use.
- Leave `sites_bed`, `panel_info`, and `dosage_cache` commented until those files exist on the machine that runs the suite.
- Do not commit genomes, FASTQ, VCFs, or dosage matrices.
- `tests/test_profile_schema.py` checks every `profiles/examples/*/profile.yaml` for the required keys and types in the schema. It also checks that `profile_id` matches the folder name. The copied template fails until `panel_n_sites` is at least 1 and `profile_id` is the folder name.
