from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "profiles/examples/grapevine_167k/profile.yaml"


def test_example_profile_loads():
    from gtbs_kit.load_profile import load_profile

    data = load_profile(EXAMPLE)
    assert data["profile_id"] == "grapevine_167k"
    assert data["panel_n_sites"] == 167433
    assert "grapeancestry" in data.get("walkthrough_url", "")


def test_example_yaml_is_mapping():
    raw = yaml.safe_load(EXAMPLE.read_text())
    assert isinstance(raw, dict)


SCHEMA = ROOT / "profiles/profile.schema.json"


def _check_against_schema(data, schema):
    """Check the required keys and simple types the schema lists (no extra dependency)."""
    problems = []
    for key in schema["required"]:
        if key not in data:
            problems.append(f"missing {key}")
    types = {"string": str, "integer": int, "object": dict}
    for key, rule in schema["properties"].items():
        if key not in data:
            continue
        value = data[key]
        want = types.get(rule.get("type"))
        if want is not None and (not isinstance(value, want) or isinstance(value, bool)):
            problems.append(f"{key} should be {rule['type']}")
            continue
        if "minimum" in rule and value < rule["minimum"]:
            problems.append(f"{key} must be at least {rule['minimum']}")
        if "minLength" in rule and len(value) < rule["minLength"]:
            problems.append(f"{key} must not be empty")
    return problems


def test_every_example_profile_matches_schema():
    import json

    schema = json.loads(SCHEMA.read_text())
    profiles = sorted((ROOT / "profiles/examples").glob("*/profile.yaml"))
    assert profiles
    for path in profiles:
        data = yaml.safe_load(path.read_text())
        assert _check_against_schema(data, schema) == [], path


def test_blank_template_is_caught():
    import json

    schema = json.loads(SCHEMA.read_text())
    data = yaml.safe_load((ROOT / "templates/profile.yaml").read_text())
    assert "panel_n_sites must be at least 1" in _check_against_schema(data, schema)
