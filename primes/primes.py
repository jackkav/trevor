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

