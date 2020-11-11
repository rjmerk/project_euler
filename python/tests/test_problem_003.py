from pytest import mark
from problem_003 import calc_prime_factors


@mark.parametrize(
    "n, expected",
    [
        (13195, [5, 7, 13, 29]),
        (4, [2, 2]),
        (-4, [2, 2]),
    ]
)
def test_calc_prime_factors(n, expected):
    result = list(calc_prime_factors(n))
    assert result == expected
