from problem_025 import fibonacci_index


def test_fibonacci_index():
    assert fibonacci_index(nr_digits=2) == 7
    assert fibonacci_index(nr_digits=3) == 12
    assert fibonacci_index(nr_digits=1_000) == 4782
