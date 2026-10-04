# Step 00g — Cloud fingerprint pack (optional)

## Input

- Panel dosage subset for IBS and SDR windows.
- Optional GS payloads staged under `data/cloud/`.
- Optional for Cloud and Steps 14a–14b. Not required for DIY 13b HTML.
- Pack compact reference fingerprints for Streamlit Cloud and `chip-report`. No bwa on Cloud.

## Do

```bash
python scripts/build_cloud_pack.py --help
python -m grapeancestry.cloud --help
src/grapeancestry/cloud/pack.py
grapeancestry chip-report --vcf results/Ages.vcf.gz --out chip.json
```

## Get

- `data/cloud/fingerprint.npz`, `sdr.npz`, and `manifest.json`: the Cloud reference side.
- No plot at pack time.
- The pack scripts are not required for DIY HTML 13b.
- `grapeancestry chip-report` is the optional consumer (Chip Companion, Step 14).
- Optional for the DIY or Docker v1 HTML path, which stops at 13b.
- The Cloud path never runs bwa. It consumes the packed fingerprints and the query VCF.
