from pytest import mark
from problem_004 import is_palindrome, largest_palindrome


@mark.parametrize("n, expected", [
    (123, False),
    (121, True),
    (4, True),
    (9989, False),
    (9009, True),
])
def test_is_palindrome(n, expected):
    assert is_palindrome(n) == expected


@mark.parametrize("digits, expected", [
    (2, 9009),
    (3, 906609),
])
def test_largest_palindrome(digits, expected):
    assert max(largest_palindrome(digits=digits)) == expected
