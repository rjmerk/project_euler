from pytest import mark
from problem_021 import all_divisors_of


@mark.parametrize("n, divisors", [
    (220, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]),
    (284, [1, 2, 4, 71, 142]),
    (12, [1, 2, 3, 4, 6]),
    (28, [1, 2, 4, 7, 14]),
    (4, [1, 2]),
])
def test_all_divisors_of(n, divisors):
    assert sorted(list(all_divisors_of(n))) == divisors
