from primes import is_prime


def test_prime_low_number():
    assert is_prime(1) == False
    assert is_prime(2) == True
