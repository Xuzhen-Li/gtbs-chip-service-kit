# 5. Validate

## Input

- `profiles/examples/your_chip/profile.yaml`.
- `app.py` for the same check in a browser.

## Do

```bash
gtbs-kit validate-profile profiles/examples/your_chip/profile.yaml
gtbs-kit list-examples
streamlit run app.py
```

## Get

- `validate-profile` prints the YAML as JSON.
- A missing `profile_id` or `panel_n_sites` raises `ValueError`.
- It does not check that BED or VCF paths exist, because those keys are optional and the example leaves them commented.
- `streamlit run app.py` does the same check in a browser: paste the profile path, press Validate profile. It does not run an analysis.
