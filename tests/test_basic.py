from functools import reduce


def test_basics():
    assert "hello" == "olleh"[::-1]
    assert "UPPER" == "upper".upper()
    assert 6 == sum([1, 2, 3])
    assert True == any([0, 1, 0])
    assert True == all([1, 1, 1])
    # remove falsey
    assert [1, 1] == list(filter(None, [1, 0, 1]))
    assert [1, 1] == [x for x in [1, 0, 1] if x]

    assert [2, 3, 4] == list(map(lambda x: x + 1, [1, 2, 3]))
    assert 24 == reduce((lambda x, y: x * y), [1, 2, 3, 4])
    # generate list of numbers
    assert [0, 1, 2] == list(range(3))
    assert [1, 3, 5] == list(filter(lambda x: x % 2, range(6)))
    assert [0, 2, 4] == list(filter(lambda x: not x % 2, range(6)))
    assert [("a", 1), ("b", 2)] == list(map(lambda x: (chr(97 + x), x + 1), range(2)))

