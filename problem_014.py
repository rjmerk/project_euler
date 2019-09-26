"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
 10 terms. Although it has not been proved yet (Collatz Problem), it is
thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from utils import measure_execution_time


def main():
    print("Problem 14")
    with measure_execution_time():
        longest = 0
        result = 0
        chain_length_dict = dict()

        for n in range(1_000_000):
            chain = length_of_chain(n, chain_length_dict)
            if chain > longest:
                longest = chain
                result = n
    print(f"The starting number under 1 million with longest Collatz chain is {result}")


def length_of_chain(starting_number, chain_length_dict):
    n = starting_number
    i = 0
    while n > 1:
        if n in chain_length_dict:
            result = i + chain_length_dict[n]
            chain_length_dict[starting_number] = result
            return result
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i += 1
    chain_length_dict[starting_number] = i
    return i


if __name__ == '__main__':
    main()
