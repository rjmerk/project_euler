"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from utils import measure_execution_time
from typing import Iterator


def main() -> None:
    print("Problem 4")
    digits = 3
    with measure_execution_time():
        result = max(largest_palindrome(digits))
    print(f"The largest palindrome of the product of two {digits}-digit \
    numbers is {result}")


def largest_palindrome(digits: int) -> Iterator[int]:
    max_value = 10 ** digits
    min_value = 10 ** (digits - 1)
    for n in range(max_value, min_value, -1):
        # To prevent checking numbers twice, we only consider values for m
        # less than n.
        for m in range(n, min_value, -1):
            p = n * m
            if is_palindrome(p):
                yield p


def is_palindrome(n: int) -> bool:
    s = str(n)
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
    return True


if __name__ == '__main__':
    main()
