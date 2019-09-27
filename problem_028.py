"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

*21 22 23 24 *25
 20 *7  8 *9  10
 19  6 *1  2  11
 18 *5  4 *3  12
*17 16 15 14 *13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""

from utils import measure_execution_time

LIMIT = 1001


def main():
    print("Problem 28")
    with measure_execution_time():
        result = sum_of_spiral_diagonals(LIMIT)
    print(f"The sum of the numbers on the diagonals of a {LIMIT} by {LIMIT} spiral is {result}")


def sum_of_spiral_diagonals(limit):
    result = 1
    for layer in range(3, limit + 2, 2):
        previous_layer_size = (layer - 2)**2
        # the first number in the current layer
        start_of_layer = previous_layer_size + 1
        # The start of the layer is always 1 step lower than the top right
        # diagonal
        right_bottom = start_of_layer + layer - 2
        # The three other diagonals are a multiple of layer - 1 away from
        # the right-bottom diagonal.
        result += sum(right_bottom + n * (layer - 1) for n in range(4))
    return result


if __name__ == '__main__':
    main()
