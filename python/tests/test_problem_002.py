from problem_002 import fibonacci_sequence


def test_fibonacci():
    result = list(fibonacci_sequence(89))
    assert result == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
