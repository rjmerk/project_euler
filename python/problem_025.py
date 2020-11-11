"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?
"""
from utils import measure_execution_time

NR_DIGITS = 1_000


def main():
    print("Problem 25")
    with measure_execution_time():
        result = fibonacci_index(NR_DIGITS)
    print(f"The index of the first term in the Fibonacci sequence to contain {NR_DIGITS} digits is {result}")


def fibonacci_index(nr_digits):
    a, b = 1, 1
    result = 1
    limit = 10 ** (nr_digits - 1)
    while a < limit:
        a, b = b, a + b
        result += 1
    return result


if __name__ == '__main__':
    main()
