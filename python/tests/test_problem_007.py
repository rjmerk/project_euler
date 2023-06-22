from problem_007 import n_th_prime_number, sieve_of_eratosthenes
from problem_010 import sieve_of_eratosthenes as sieve_of_eratosthenes_numpy
from utils import measure_execution_time



def test_n_th_prime_number():
    n = 1_000_000
    print()

    with measure_execution_time("set"):
        sieve_of_eratosthenes(n)

    with measure_execution_time("numpy"):
        sieve_of_eratosthenes_numpy(n)

    assert n_th_prime_number(6) == 14


def test_sieve():
    expected = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
        47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]
    assert list(sieve_of_eratosthenes(100)) == expected

