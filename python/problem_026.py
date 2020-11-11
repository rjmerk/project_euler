"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""
from operator import itemgetter

from utils import measure_execution_time


LIMIT = 1_000


def main():
    print("Problem 26")
    with measure_execution_time():
        result = value_with_longest_recurring_cycle(LIMIT)
    print(f"The value of d < {LIMIT} for which 1/d contains the longest recurring cycle in its decimal fraction part is {result}")


def value_with_longest_recurring_cycle(limit):
    pairs = ((d, recurring_cycle_length(d)) for d in range(2, limit))
    highest_pair = max(pairs, key=itemgetter(1))
    return highest_pair[0]


def recurring_cycle_length(d):
    rest = 10 % d
    found_rests = set()
    while True:
        if rest == 0:  # terminating fraction
            return 0
        elif rest in found_rests:  # division starts to repeat
            return len(found_rests)
        else:
            found_rests.add(rest)
            rest = rest * 10 % d


if __name__ == '__main__':
    main()
