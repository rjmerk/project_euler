"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from utils import measure_execution_time


def main():
    print("Problem 9")
    with measure_execution_time():
        a, b, c = find_pythagorean_triplet_summing_up_to(1000)
    print(f"The Pythagorean triplet for which a + b + c = 1000 is {a}, {b}, {c}")
    print(f"The product for which is {a*b*c}")


def find_pythagorean_triplet_summing_up_to(n):
    """
    Once we know a and b, we can calculate c as the three need to add up to n.

    Furthermore, a or b cannot be larger than n/2, because this would mean
    that c can be at most half n minus 1. So if f.e. a is higher than n/2,
    then c^2 is already lower than a^2 alone, let alone a^2 + b^2.

    Lastly, we can asssume that b is at least n/2 - a, because a is at most
    n/2
    """
    for a in range(1, n//2):
        for b in range(n//2 - a, n//2):
            c = n - a - b
            if is_pythagorean_triplet(a, b, c):
                return (a, b, c)


def is_pythagorean_triplet(a, b, c):
    # It's about 4x faster to use a*a here than a**2!
    return a*a + b*b == c*c


if __name__ == '__main__':
    main()
