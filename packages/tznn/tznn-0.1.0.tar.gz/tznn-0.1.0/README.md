# tznn

![Platform](https://img.shields.io/badge/platform-cross--platform-lightgray.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/tznn.svg)](https://pypi.org/project/tznn/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tznn.svg)](https://pypi.org/project/tznn/)
[![CI](https://github.com/chuongmep/tznn/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chuongmep/tznn/actions)
[![Publish](https://github.com/chuongmep/tznn/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/chuongmep/tznn/actions)
[![PyPI Downloads](https://img.shields.io/pypi/dm/tznn.svg?color=blue&label=Downloads)](https://pypi.org/project/tznn/)
[![HitCount](https://hits.dwyl.com/chuongmep/tznn.svg?style=flat-square)](http://hits.dwyl.com/chuongmep/tznn)
<a href="https://twitter.com/intent/follow?screen_name=chuongmep">
<img src="https://img.shields.io/twitter/follow/chuongmep?style=social&logo=twitter" alt="follow on Twitter"></a>

Tiny helper for IANA time zones and abbreviations.

This package provides a small utility class backed by a static mapping in `timezone.json` to:

- List available IANA time zone names
- Look up the time zone abbreviation (e.g., SGT, EDT) for a given zone

Notes:
- Abbreviations are static values from `timezone.json` and are not date-aware (no DST transitions).
- On Windows, `tzdata` is listed as a dependency in case you choose to extend functionality using IANA tzdata; the current implementation only reads `timezone.json` and does not require system tzdata at runtime.

## Install

From the project root:

```powershell
pip install .
```

For development (tests, etc.):

```powershell
pip install -r requirements.txt
```

## Quick start

```python
from tznn import tznn

tz = tznn()

# 1) Get a sorted list of available IANA time zone names
zones = tz.get_available_time_zones()
print(len(zones), zones[:5])

# 2) Get the abbreviation for a known time zone
print(tz.get_abbr("Asia/Singapore"))      # -> "SGT"
print(tz.get_abbr("America/New_York"))    # -> e.g., "EDT" per timezone.json

# 3) Get the full mapping of zone -> abbreviation
mapping = tz.get_all_available_time_zones()
print(mapping["America/New_York"])        # -> "EDT"
```

#### Why use this package?

Default Python libraries do not provide a simple way to get static time zone abbreviations from IANA zone names. This package fills that gap with a lightweight solution. Example : 

```python
from datetime import datetime
from zoneinfo import ZoneInfo

dt_utc = datetime(2025, 9, 23, 3, 2, 7)
dt_vn = dt_utc.astimezone(ZoneInfo("Asia/Ho_Chi_Minh"))
print(dt_vn.strftime("%d/%m/%Y %H:%M:%S %Z %z"))  # → 23/09/2025 10:02:07 ICT +0700
```
> The result is 23/09/2025 02:02:07 +07 +0700 but expectation should be 23/09/2025 10:02:07 ICT +0700

## API

Class: `tznn`

- `get_available_time_zones() -> list[str]`
	- Returns a sorted list of all IANA zone names present in `timezone.json`.

- `get_all_available_time_zones() -> dict[str, str]`
	- Returns the entire mapping of `zone_name -> abbreviation` loaded from `timezone.json`.

- `get_abbr(tz_name: str) -> str`
	- Returns the abbreviation for the given IANA time zone name.
	- Raises `ValueError` if the zone name is not found in the mapping.

## Data source and limitations

- Data is loaded from the local `timezone.json` file included in the repository.
- Abbreviations are static and may not reflect historical or future DST changes. If you need date-aware abbreviations,
	consider using Python's `zoneinfo` module (Python 3.9+) together with an appropriate tz database.

## Testing

Run the test suite from the project root:

```powershell
pytest -q
```

The tests validate:
- The list of available zones is sorted and non-empty.
- The mapping includes known zones and string abbreviations.
- `get_abbr` returns correct abbreviations and raises on invalid zones.

## Roadmap (ideas)

- Optional date-aware abbreviation lookup using `zoneinfo` (or `pytz` for older Pythons).
- Utilities for DST-aware conversions and current time by zone.


## Knowledge
- https://adamj.eu/tech/2021/05/06/how-to-list-all-timezones-in-python/
- https://stackoverflow.com/questions/78580391/zoneinfo-is-missing-timezone-names-that-pytz-has
- https://docs.python.org/3/library/zoneinfo.html
- https://github.com/python/tzdata/issues/111
- https://discuss.python.org/t/get-local-time-zone/4169/10
