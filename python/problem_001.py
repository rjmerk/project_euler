"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    limit = 1_000
    multiples_of_3 = range(3, limit, 3)
    multiples_of_5 = range(5, limit, 5)
    multiples_of_15 = range(15, limit, 15)
    result = sum(multiples_of_3) + sum(multiples_of_5) - sum(multiples_of_15)
    print("Problem 1")
    print(f"The sum of all the multiples of 3 or 5 below {limit} = {result}")


if __name__ == '__main__':
    main()
