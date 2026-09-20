from __future__ import annotations

from typing import Any, Mapping, Protocol, runtime_checkable


@runtime_checkable
class Profile(Protocol):
    """Loaded panel profile (species-agnostic fields)."""

    profile_id: str
    panel_n_sites: int

    def as_dict(self) -> Mapping[str, Any]:
        ...


@runtime_checkable
class Caller(Protocol):
    """Map/call or accept a panel-sites VCF for one query sample."""

    def run(self, sample_id: str, profile: Profile) -> Mapping[str, Any]:
        """Return paths/metrics for QC hand-off. No HTML rendering here."""
        ...


@runtime_checkable
class ReportSink(Protocol):
    """Emit sample-first report artifact(s)."""

    def write(self, sample_id: str, payload: Mapping[str, Any], profile: Profile) -> str:
        """Return hand-in path (e.g. *.sample-first-v2.report.html)."""
        ...


@runtime_checkable
class CloudDoor(Protocol):
    """Emit cloud hand-in (e.g. chip.json) from a panel-sites VCF."""

    def emit(self, vcf_path: str, profile: Profile) -> str:
        ...
