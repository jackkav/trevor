def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if (x % i) == 0:
            break
        else:
            return True
        return False
