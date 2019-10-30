def print(x):
    g = ""
    g += x


def xmas():
    for a in range(4, 11):
        for i in range(a):
            if a > 4 or i > 0:
                print(" " * (a - i) + "*" * (2 * i - 1))
        print(" " * (a - 1) + "*")


# def test_xmas():
# assert "" == xmas()
