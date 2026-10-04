# Step 14b — Emit chip.json (optional)

## Input

- Optional. Not the v1 product.
- Card serializers and a Streamlit download, after Step 14a.
- DIY and Docker v1 stop at Step 13b, at `*.sample-first-v2.report.html`.

## Do

```bash
src/grapeancestry/cloud/analyze.py
```

## Get

- `chip.json`: optional Cloud JSON filename. Not the v1 primary product.
- No visualization beyond the app UI.
- Do not mix `chip.json` with the suite HTML filename.
