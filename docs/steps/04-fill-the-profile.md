# 4. Fill the profile

## Input

- `profiles/examples/your_chip/profile.yaml`.
- `load_profile` requires `profile_id` and `panel_n_sites`.
- The schema also requires `label`, and `panel_n_sites` must be an integer of at least 1.
- The CLI does not check the schema file.

## Do

```bash
tests/test_profile_schema.py
```

## Get

- `profile_id`: the folder name you chose.
- `label`: a sentence a reader can recognize.
- `panel_n_sites`: how many sites are on the chip.
- `coordinate_system`: the reference those sites use.
- Leave `sites_bed`, `panel_info`, and `dosage_cache` commented until those files exist on the machine that runs the suite.
- Do not commit genomes, FASTQ, VCFs, or dosage matrices.
- `tests/test_profile_schema.py` checks the schema. The CLI does not.
