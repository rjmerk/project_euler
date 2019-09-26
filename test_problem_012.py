from pytest import mark

from problem_012 import calc_divisors


@mark.parametrize('n, nr_divisors', [
    (6, 4),
    (19, 2),
    (21, 4),
    (28, 6),
    (48, 10),
    (50, 6),
])
def test_divisors(n, nr_divisors):
    assert calc_divisors(n) == nr_divisors
