from pytest import mark
from problem_023 import generate_abundant_numbers


def test_abundant_numbers():
    result = list(generate_abundant_numbers(13))
    assert result == [12]
