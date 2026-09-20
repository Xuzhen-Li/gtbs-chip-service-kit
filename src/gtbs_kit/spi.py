from __future__ import annotations

from typing import Any, Mapping, Protocol, runtime_checkable


@runtime_checkable
class Profile(Protocol):
    profile_id: str
    panel_n_sites: int

    def as_dict(self) -> Mapping[str, Any]:
        ...


@runtime_checkable
class Caller(Protocol):
    def run(self, sample_id: str, profile: Profile) -> Mapping[str, Any]:
        ...


@runtime_checkable
class ReportSink(Protocol):
    def write(self, sample_id: str, payload: Mapping[str, Any], profile: Profile) -> str:
        ...


@runtime_checkable
class CloudDoor(Protocol):
    def emit(self, vcf_path: str, profile: Profile) -> str:
        ...
