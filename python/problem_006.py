"""
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
from utils import measure_execution_time


def main() -> None:
    print("Problem 6")
    limit = 1_000
    with measure_execution_time():
        result = square_of_sum(limit) - sum_of_squares(limit)
    print(f'The difference between the sum of squares and the square of the sum for the first {limit} natural numbers is {result}')


def square_of_sum(n: int) -> int:
    return sum(range(1, n + 1)) ** 2


def sum_of_squares(n: int) -> int:
    return sum(x**2 for x in range(1, n + 1))


if __name__ == '__main__':
    main()
