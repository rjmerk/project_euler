"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import numpy as np

from utils import measure_execution_time


SIZE = 20


def main():
    print("Problem 15")
    with measure_execution_time():
        # we add 1 to size as a NxN grid has N+1xN+1 intersections.
        result = nr_routes_in_grid(SIZE + 1)
        print(f"the number of routes through a {SIZE}x{SIZE} grid = {result}")


def nr_routes_in_grid(size):
    # We use dtype object, so we can have integers bigger than 64-bits
    # The performance loss is negligible and while bigints aren't needed for
    # size 20 grids, it's a nice extra feature.
    grid = np.zeros(shape=(size, size), dtype='object')
    # the right-most column and bottom row have route lengths 1
    grid[size - 1, 0:size] = 1
    grid[0:size, size - 1] = 1

    # We now iterate over all the inner values, starting at the bottom right
    # (position size - 2, size - 2).
    for x in range(size - 2, -1, -1):
        for y in range(size - 2, -1, -1):
            # The nr. of routes in a grid position is the nr. of routes
            # to the right plus the nr. of routes to the bottom.
            grid[y, x] = grid[y+1, x] + grid[y, x+1]
    return grid[0, 0]


if __name__ == '__main__':
    main()
