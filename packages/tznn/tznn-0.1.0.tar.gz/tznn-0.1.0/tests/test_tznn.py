import pytest

from tznn import tznn


@pytest.fixture()
def tz_helper():
    return tznn()


def test_get_available_time_zones_returns_sorted_list(tz_helper):
    zones = tz_helper.get_available_time_zones()
    assert isinstance(zones, list)
    assert all(isinstance(z, str) for z in zones)
    # Sorted check: list equals its sorted version
    assert zones == sorted(zones)
    # Sanity: non-empty and contains a well-known IANA zone
    assert len(zones) > 0
    assert "America/New_York" in zones
    assert "Asia/Singapore" in zones


def test_get_all_available_time_zones_returns_mapping(tz_helper):
    mapping = tz_helper.get_all_available_time_zones()
    assert isinstance(mapping, dict)
    # Known entries exist and are strings
    assert "America/New_York" in mapping
    assert isinstance(mapping["America/New_York"], str)
    assert "Asia/Singapore" in mapping
    assert isinstance(mapping["Asia/Singapore"], str)


@pytest.mark.parametrize(
    "zone, expected",
    [
        ("Asia/Singapore", "SGT"),
        ("America/New_York", "EDT"),
    ],
)
def test_get_abbr_known_zones(tz_helper, zone, expected):
    assert tz_helper.get_abbr(zone) == expected


def test_get_abbr_invalid_zone_raises(tz_helper):
    with pytest.raises(ValueError):
        tz_helper.get_abbr("America/Singapour")  # misspelled on purpose
