"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import islice, permutations
from utils import measure_execution_time

LIMIT = 1_000_000


def main():
    print("Problem 24")
    with measure_execution_time():
        nth_permutation_iterator = islice(
            permutations(range(10)),
            LIMIT - 1,
            LIMIT)
        nth_permutation = list(nth_permutation_iterator)[0]
        result = ''.join(str(d) for d in nth_permutation)
    print(f"The {LIMIT}th lexicographic permutation of the digits 0 to 9 is {result}")


if __name__ == '__main__':
    main()
