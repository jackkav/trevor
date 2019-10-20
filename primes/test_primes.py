from primes import is_prime, prime_to


def test_prime_low_number():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True


def test_prime_up_to_100():
    assert (
        prime_to(100)
        == """2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97"""
    )

