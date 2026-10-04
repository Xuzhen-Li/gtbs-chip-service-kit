# Step 14a — Cloud analyze query VCF (optional)

## Input

- Optional. Not required for v1 Docker or DIY HTML.
- A 167K-site query VCF on the Cloud Chip Companion path.

## Do

```bash
grapeancestry chip-report
src/grapeancestry/cloud/analyze.py
vcf_py.py
sites.py
```

## Get

- Intermediate card stats before the JSON dump: IBS, SDR proxy, MAS, and GS.
- Streamlit progressive sections (`app.py`).
