from pytest import mark
from problem_005 import smallest_evenly_divisible_number, calc_factors


@mark.parametrize("n, expected", [
    (10, 2520),
    (3, 6),
    (5, 60),
    (12, 27720),
])
def test_smallest_evenly_divisible_number(n, expected):
    assert smallest_evenly_divisible_number(n) == expected


@mark.parametrize("n, expected", [
    (3, [3, 2]),
    (5, [5, 4, 3]),
    (12, [12, 11, 10, 9, 8, 7]),
    (20, [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]),
])
def test_calc_factors(n, expected):
    assert calc_factors(n) == expected
