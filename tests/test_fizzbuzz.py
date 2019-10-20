def fizzbuzz(i):
    return (i % 3 < 1) * "Fizz" + (i % 5 < 1) * "Buzz" or i


def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(15) == "FizzBuzz"


def fizzbuzz_to(x):
    t = ""
    for i in range(1, x):
        t = t + f"{(i % 3 < 1) * 'Fizz' + (i % 5 < 1) * 'Buzz' or i}\n"
    return t


def test_fizzbuzz_to():
    assert fizzbuzz_to(3) == "1\n2\n"
    assert fizzbuzz_to(5) == "1\n2\nFizz\n4\n"


#     assert (
#         fizzbuzz_to(100)
#         == """1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# FizzBuzz
# 46
# 47
# Fizz
# 49
# Buzz
# Fizz
# 52
# 53
# Fizz
# Buzz
# 56
# Fizz
# 58
# 59
# FizzBuzz
# 61
# 62
# Fizz
# 64
# Buzz
# Fizz
# 67
# 68
# Fizz
# Buzz
# 71
# Fizz
# 73
# 74
# FizzBuzz
# 76
# 77
# Fizz
# 79
# Buzz
# Fizz
# 82
# 83
# Fizz
# Buzz
# 86
# Fizz
# 88
# 89
# FizzBuzz
# 91
# 92
# Fizz
# 94
# Buzz
# Fizz
# 97
# 98
# Fizz
# Buzz"""
#     )
