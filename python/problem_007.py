"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt
from utils import measure_execution_time


LIMIT = 10_001

# The sieve step size determines how quickly we grow the sieve when the
# number of found primes is too low. This determines the speed of finding
# the nth prime.
SIEVE_STEP_SIZE = 10


def main() -> None:
    print("Problem 7")
    with measure_execution_time():
        result = n_th_prime_number(LIMIT)
    print(f'The {LIMIT}st prime number is {result}')


def n_th_prime_number(n):
    """
    The approach is to incrementally calculate larger and larger
    sieves of Eratosthenes until we have n primes.
    """
    sieve_seize = SIEVE_STEP_SIZE * n
    primes = set()
    while len(primes) < n:
        primes = sieve_of_eratosthenes(sieve_seize)
        sieve_seize += SIEVE_STEP_SIZE * n
    return list(primes)[n - 1]


def sieve_of_eratosthenes(n):
    """See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

    n is the highest number to which the sieve checks for primes.
    """
    primes = set(range(2, n))
    for i in range(2, int(sqrt(n))):
        if i in primes:
            for j in range(i * 2, n + 1, i):
                primes.discard(j)
    return primes


if __name__ == '__main__':
    main()
