from __future__ import annotations

from pathlib import Path


def resolve_under(root: Path, maybe_relative: str | None) -> Path | None:
    if not maybe_relative:
        return None
    p = Path(maybe_relative)
    return p if p.is_absolute() else (root / p)
