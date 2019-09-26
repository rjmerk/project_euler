from pytest import mark
from problem_019 import is_leap_year, sundays_on_day_of_month


@mark.parametrize("year, is_leap", [
    (1900, False),
    (1903, False),
    (1904, True),
    (1996, True),
    (2000, True),
])
def test_is_leap_year(year, is_leap):
    assert is_leap_year(year) == is_leap


def test_sundays():
    result = sundays_on_day_of_month(
        day_of_month=1,
        start_year=1901,
        end_year=2001)
    assert result == 172
