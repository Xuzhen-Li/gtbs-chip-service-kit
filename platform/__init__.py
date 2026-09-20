"""Thin platform contracts (SPI). Implementations stay private or in profile-specific packages."""

from platform.spi import Caller, CloudDoor, ReportSink, Profile

__all__ = ["Caller", "CloudDoor", "ReportSink", "Profile"]
