# Install

Python 3.11 or newer.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
gtbs-kit --help
```

`environment.yml` defines a separate, older conda environment (named `grapeancestry-cloud`) built for the Streamlit cloud app. It includes streamlit, numpy, pandas, and other packages, but neither pytest nor this package. You do not need it to run `gtbs-kit` or the test suite.
