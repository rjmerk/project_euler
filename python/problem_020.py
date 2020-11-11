"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math
from utils import measure_execution_time

NUMBER = 100


def main() -> None:
    print("Problem 20")
    with measure_execution_time():
        result = sum(int(char) for char in str(math.factorial(NUMBER)))
    print(f"The sum of digits in the number {NUMBER}! is {result}")


if __name__ == '__main__':
    main()
