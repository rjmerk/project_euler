"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt

from utils import measure_execution_time

LIMIT = 10_000


def main() -> None:
    print("Problem 21")
    with measure_execution_time("old"):
        result = all_amicable_numbers_under(LIMIT)
    with measure_execution_time("new"):
        divisor_sums = create_divisor_sums(30_000)
        result2 = sum(all_amicable_numbers_under_fast(LIMIT, divisor_sums))

    assert result == result2
    print(f"The sum of all the amicable numbers under {LIMIT} is {result}")


def all_amicable_numbers_under(limit):
    result = 0
    for a in range(limit):
        b = d(a)
        if b > a and d(b) == a:
            result += a + b
    return result


def all_amicable_numbers_under_fast(limit, divisor_sums):
    for a in range(limit):
        b = divisor_sums[a]
        try:
            if b > a and divisor_sums[b] == a:
                yield a
                yield b
        except IndexError:
            raise Exception(f"a={a} b ={b}")


def create_divisor_sums(limit):
    divisor_sums = [1] * limit
    for i in range(2, limit // 2):
        for j in range(2*i, limit, i):
            divisor_sums[j] += i

    return divisor_sums


def d(n):
    return sum(all_divisors_of(n))


def all_divisors_of(n):
    yield 1
    for d_ in range(2, int(sqrt(n)) + 1):
        if n % d_ == 0:
            yield d_
            if n // d_ != d_:
                yield n // d_


if __name__ == '__main__':
    main()
