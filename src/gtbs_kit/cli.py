from __future__ import annotations

import json
from pathlib import Path

import click

from gtbs_kit.load_profile import load_profile


@click.group()
def main() -> None:
    """GBTS Chip Service Kit — profile utilities (thin public CLI)."""


@main.command("validate-profile")
@click.argument("profile_yaml", type=click.Path(exists=True, dir_okay=False))
def validate_profile(profile_yaml: str) -> None:
    """Load profile.yaml and print normalized JSON."""
    data = load_profile(profile_yaml)
    click.echo(json.dumps(data, indent=2, sort_keys=True))


@main.command("list-examples")
@click.option("--profiles-dir", default="profiles/examples", show_default=True)
def list_examples(profiles_dir: str) -> None:
    root = Path(profiles_dir)
    if not root.exists():
        raise SystemExit(f"missing {root}")
    for child in sorted(root.iterdir()):
        if child.is_dir() and (child / "profile.yaml").exists():
            click.echo(child.name)


if __name__ == "__main__":
    main()
