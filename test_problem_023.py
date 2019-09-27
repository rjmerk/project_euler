from problem_023 import integers_not_sum_abundant


def test_abundant_numbers():
    result = list(integers_not_sum_abundant(13))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
