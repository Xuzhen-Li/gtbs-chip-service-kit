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
