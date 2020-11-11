"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

from utils import measure_execution_time


def main():
    print("Problem 16")
    with measure_execution_time():
        result = sum([int(s) for s in str(2**1000)])

    print(f"the sum of the digits of the number 2^1000 is {result}")


if __name__ == '__main__':
    main()
