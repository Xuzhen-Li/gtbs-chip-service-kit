from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_profile(path: str | Path) -> dict[str, Any]:
    """Load a panel profile YAML. Validates required keys lightly."""
    p = Path(path)
    data = yaml.safe_load(p.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"profile must be a mapping: {p}")
    for key in ("profile_id", "panel_n_sites"):
        if key not in data:
            raise ValueError(f"missing required key {key!r} in {p}")
    return data


def profile_root(profiles_dir: str | Path, profile_id: str) -> Path:
    return Path(profiles_dir) / profile_id
