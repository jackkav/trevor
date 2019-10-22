def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        return True
    return False


def prime_to(t):
    res = []
    for n in range(t):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                res.append(n)
    return "\n".join(map(str, res))


def test_prime_low_number():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True


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
