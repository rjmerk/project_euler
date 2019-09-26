"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
"""
from math import sqrt
import numpy as np

from utils import measure_execution_time

LIMIT = 2_000_000


def main():
    print("Problem 10")
    with measure_execution_time():
        result = np.sum(sieve_of_eratosthenes(LIMIT))
    print(f"The sum of all primes below {LIMIT:,} is {result:,}.")


def sieve_of_eratosthenes(n):
    """See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

    n is the highest number to which the sieve checks for primes.

    return: np.Array
    """
    if n < 5:
        return np.array([2, 3])
    primes = np.full(n, True)
    primes[1] = False
    primes[4::2] = False

    for i in range(1, int(sqrt(n)), 2):
        if primes[i]:
            primes[i*i:n:i] = False
            # Using the above is about 10x faster than the code below
            # for j in range(i ** 2, n, i):
            #     primes[j] = 0
    return np.flatnonzero(primes)


if __name__ == '__main__':
    main()
