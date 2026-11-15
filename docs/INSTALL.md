# Install

Python 3.11 or newer.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
gtbs-kit --help
```

`environment.yml` is a different, older conda environment (named `grapeancestry-cloud`) for the Streamlit cloud app. It has streamlit, numpy, pandas and other packages, but not pytest and not this package. You do not need it for `gtbs-kit` or the tests.
