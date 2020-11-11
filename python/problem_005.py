"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
 numbers from 1 to 20?
"""
import math
from multiprocessing import Pool

from utils import measure_execution_time


def main():
    print("Problem 5")
    limit = 20
    with measure_execution_time():
        result = smallest_evenly_divisible_number(limit)
    print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {limit} is {result}.")


def smallest_evenly_divisible_number(n):
    x = n

    factors = calc_factors(n)
    for x in range(n, math.factorial(n) + 1, n):
        if is_evenly_divisible(x, factors):
            return x


def calc_factors(n):
    """To increase performance, we do not divide the number with all the factors
    (the numbers from 1 to 20).

    Instead, we filter out the smaller ones that evenly divide the larger ones.
    For example, if we have the factor 20, we don't need 10, 5, 4 or 2, as
    any number evenly divisible by 20 are also evenly divisible by 10, 5...

    In practice, this cuts out about half the factors.
    """
    factors = list(range(n, 1, -1))
    for x in range(n, 1, -1):
        for factor in range(1, x):
            if x % factor == 0 and factor in factors:
                factors.remove(factor)
    return factors


def is_evenly_divisible(n, factors):
    """Returns true if n is evenly divided by all the numbers in factors.

    This function is faster than using
        all(n % f == 0 for f in factors)
    by a factor of ~2.
    """
    for factor in factors:
        if not (n % factor == 0):
            return False
    return True


if __name__ == '__main__':
    main()
