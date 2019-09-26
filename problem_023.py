"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from problem_021 import all_divisors_of
from utils import measure_execution_time

LIMIT = 28124


def main() -> None:
    print("Problem 23")
    with measure_execution_time():
        result = sum(integers_not_sum_abundant(LIMIT))
    print(f"the sum of all the positive integers which cannot be written as the sum of two abundant numbers is {result}")


def integers_not_sum_abundant(limit):
    abundant_number_list = [n for n in range(limit)
                            if sum(all_divisors_of(n)) > n]

    abundant_sum_set = set()

    for i, a in enumerate(abundant_number_list):
        # we only iterate the second number from i on, to avoid identical pairs

        for b in abundant_number_list[:i]:
            abundant_sum_set.add(a + b)

    for n in range(limit):
        if n not in abundant_sum_set:
            yield n


if __name__ == '__main__':
    main()
