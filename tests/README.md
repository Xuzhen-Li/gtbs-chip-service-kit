# Tests

The tests load the example profile and check every `profiles/examples/*/profile.yaml` against the required keys and types in `profiles/profile.schema.json`. They do not download data.

```bash
python -m pytest -q tests
```
