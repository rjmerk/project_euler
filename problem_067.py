"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""
from utils import measure_execution_time

from problem_018 import find_longest_path_triangle


def main() -> None:
    print("Problem 67")
    with measure_execution_time():
        result = find_longest_path_triangle(get_triangle_from_file())
    print(f"The maximum total from top to bottom of the triangle is {result}")


def get_triangle_from_file():
    result = []
    with open("p067_triangle.txt", "r") as file:
        for line in file:
            result.append([int(n) for n in line.split(" ")])
    return result


if __name__ == '__main__':
    main()
