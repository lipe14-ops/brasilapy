from datetime import datetime

import pytest

from brasilapy.utils import parse_date


def test_dates():
    assert type(parse_date("2012-02-24")) is datetime

    date = parse_date("1987-10-11")
    assert date.day == 11
    assert date.month == 10
    assert date.year == 1987


def test_invalid_date():

    with pytest.raises(ValueError):
        parse_date("9999-32-13")

    with pytest.raises(ValueError):
        parse_date("1987-31-01")
