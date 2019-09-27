"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits."""
from utils import measure_execution_time


def main():
    print("Problem 30")
    with measure_execution_time():
        result = sum_numbers_that_are_sum_of_fifth_powers_of_their_digits()
    print(f"the sum of all the numbers that can be written as the sum of fifth powers of their digits is {result}")


def sum_numbers_that_are_sum_of_fifth_powers_of_their_digits():
    # With 4 digits, the highest possible sum is 4 * 9^5 = 236196 (6 digits)
    # with 5 digits, the same = 5* 9^5 = 295245 (6 digits)
    # with 6 digis 6 * 9^5 = 354294 (6 digits)
    # with 7 digits, 7 * 9^5 = 354294 (6 digits)
    # with 8 digits, 8 * 9^5 = 472392 (6 digits)
    # So apparently the highest possible candidate can only have 6 digits
    limit = 6 * 9**5
    result = 0
    # Pre-calculate fifth powers for performance
    fifth_power = [n**5 for n in range(10)]
    # start at 10 as we need at least 2 digits
    for n in range(10, limit):
        if n == sum(fifth_power[digit] for digit in digits(n)):
            result += n
    return result


def digits(n):
    while n > 0:
        yield n % 10
        n = n // 10


if __name__ == '__main__':
    main()
