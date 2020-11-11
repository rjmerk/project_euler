from problem_018 import find_longest_path_triangle


def test_find_longest_path_triangle():
    TEST_TRIANGLE = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    assert find_longest_path_triangle(TEST_TRIANGLE) == 23
