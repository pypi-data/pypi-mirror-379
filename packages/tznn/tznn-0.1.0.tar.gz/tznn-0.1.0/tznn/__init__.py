from __future__ import annotations
import json
from importlib.resources import files

__all__ = ["tznn"]
__version__ = "0.1.0"


class tznn:
    """Tiny helper for working with IANA time zones and abbreviations.

    Methods:
    - get_available_time_zones() -> list[str]: Get a sorted list of available IANA time zone names.
    - get_abbr(tz_name: str) -> str: Get the abbreviation (e.g., EDT) for the given time zone name.
    - get_all_available_time_zones() -> dict[str, str]: Get a dict of all available IANA time zone names and their abbreviations.
    """

    def __init__(self):
        # Load bundled timezone mapping from package data
        tz_path = files(__package__).joinpath("timezone.json")
        with tz_path.open("r", encoding="utf-8") as f:
            tz_abbreviations = json.load(f)
        self.tz_abbreviations = tz_abbreviations

    def get_all_available_time_zones(self) -> dict[str, str]:
        """Return a dict of all available IANA time zone names and their abbreviations."""
        return self.tz_abbreviations

    def get_available_time_zones(self) -> list[str]:
        """Return a sorted list of available IANA time zone names."""
        return sorted(self.tz_abbreviations.keys())

    def get_abbr(self, tz_name: str) -> str:
        """Return the time zone abbreviation for the given IANA time zone name.

        Args:
            tz_name (str): IANA time zone name (e.g., "America/New_York").
        Returns:
            str: Time zone abbreviation (e.g., "EDT").
        Raises:
            ValueError: If the time zone name is invalid.
        """
        if tz_name not in self.tz_abbreviations:
            raise ValueError(f"Invalid time zone name: {tz_name}")
        return self.tz_abbreviations[tz_name]
