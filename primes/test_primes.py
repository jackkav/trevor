from primes import is_prime


def test_prime_low_number():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
