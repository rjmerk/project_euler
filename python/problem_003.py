"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from utils import measure_execution_time


def main():
    n = 600_851_475_143
    with measure_execution_time():
        prime_factors = calc_prime_factors(n)
    print("Problem 3")
    print("the largest prime factor of the number {} = {}".format(
        n, max(prime_factors)))


def calc_prime_factors(n):
    """Returns all the prime factors of a positive integer"""

    # 2 is a special case. We calculate it seperately so that in the
    # general case, we case increase the factor by 2 instead of 1,
    # halving execution time.
    if n % 2 == 0:
        while n % 2 == 0:
            yield 2
            n /= 2

    # The general case
    factor = 3
    while n > 1:
        while n % factor == 0:
            yield factor
            n /= factor
        factor += 2


if __name__ == '__main__':
    main()
