from problem_007 import n_th_prime_number, sieve_of_eratosthenes


def test_n_th_prime_number():
    assert n_th_prime_number(6) == 13


def test_sieve():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97]
    assert list(sieve_of_eratosthenes(100)) == expected
