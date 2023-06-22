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
to try every route to solve this problem, as there are 2^99 altogether! If you
could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""
from utils import measure_execution_time

from problem_018 import find_longest_path_triangle

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    data = [
        ("2021-11-01", 101),
        ("2021-11-02", 104),
        ("2021-11-03", None),
        ("2021-11-04", 102),
        ("2021-11-05", 103),
        ("2021-11-06", 103),
        ("2021-11-07", 103),
        ("2021-11-08", 103),
        ("2021-11-09", 102),
        ("2021-11-10", None),
        ("2021-11-11", None),
        ("2021-11-12", None),
        ("2021-11-13", 98),
        ("2021-11-14", 98),
    ]
    x_values = [d[0] for d in data]
    y_values = [d[1] for d in data]


    ax.plot(x_values, y_values)  # Plot some data on the axes.
    ax.xaxis.set_major_locator(plt.MultipleLocator(7))
    ax.set_ylim([75, 110])
    plt.savefig("plot.png", format="png")

    # print("Problem 67")
    # with measure_execution_time():
    #     result = find_longest_path_triangle(get_triangle_from_file())
    # print(f"The maximum total from top to bottom of the triangle is {result}")


def get_triangle_from_file():
    result = []
    with open("../resources/p067_triangle.txt", "r") as file:
        for line in file:
            result.append([int(n) for n in line.split(" ")])
    return result


if __name__ == '__main__':
    main()
