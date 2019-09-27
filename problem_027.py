"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible
by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤79. The product of the coefficients,
 −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n

e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
from utils import measure_execution_time


def main():
    print("Problem 27")
    with measure_execution_time():
        result = product_of_coefficients()
    print(f"The product of a and b for the quadric expression with maximum number of primes is {result}")


def product_of_coefficients():
    max_a = max_b = max_nr_primes = 0
    # a must be odd.
    # when n = 1, the quadratic equals 1 + a + b. As shown below, b is prime
    # (and thus odd). If a is odd, then 1 + a + b is even. But as we want to
    # find prime quadratics, the quadratic cannot be even. Thus a must be odd.
    for a in range(-1001, 1000, 2):
        # When n = 0, the quadratic equals b. As we want to find prime
        # quadratics, this means b must be prime.
        # So for b, we can skip negative and even values.
        for b in range(1, 1001, 2):
            n = 0
            q = n*n + a*n + b
            while is_prime(q):
                n += 1
                q = n*n + a*n + b
            if n > max_nr_primes:
                max_nr_primes = n
                max_a = a
                max_b = b
    return max_a * max_b


def is_prime(n):
    if n <= 1:
        return False
    for f in range(2, int(n**0.5)):
        if n % f == 0:
            return False
    return True


if __name__ == '__main__':
    main()
