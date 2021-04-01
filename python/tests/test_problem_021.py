import pytest
from pytest import mark
from problem_021 import all_divisors_of, create_divisor_sums


@mark.parametrize("n, divisors", [
    (220, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]),
    (284, [1, 2, 4, 71, 142]),
    (12, [1, 2, 3, 4, 6]),
    (28, [1, 2, 4, 7, 14]),
    (4, [1, 2]),
])
def test_all_divisors_of(n, divisors):
    assert sum(divisors) == 22
    assert sorted(list(all_divisors_of(n))) == divisors


@pytest.fixture
def divisor_sums():
    return create_divisor_sums(286)


@mark.parametrize("n, expected", [
    (4, 3),
    (12, 16),
    (28, 28),
    (220, 284),
    (284, 220),
])
def test_divisor_sum(divisor_sums, n, expected):
    assert divisor_sums[n] == expected
