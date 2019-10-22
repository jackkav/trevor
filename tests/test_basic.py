from functools import reduce


def test_basics():
    assert "hello" == "olleh"[::-1]
    assert "UPPER" == "upper".upper()
    assert "hello" == "".join(["he", "llo"])
    assert 6 == sum([1, 2, 3])
    assert any([0, 1, 0]) is True
    assert all([1, 1, 1]) is True

    # remove falsey
    assert [1, 1] == list(filter(None, [1, 0, 1]))
    assert ["a", "b"] == list(filter(None, ["a", "", "b"]))
    assert [1, 1] == [x for x in [1, 0, 1] if x]
    # mutate
    assert [2, 3, 4] == list(map(lambda x: x + 1, [1, 2, 3]))
    # generate list of numbers
    assert [0, 1, 2] == list(range(3))

    assert [1, 3, 5] == list(filter(lambda x: x % 2, range(6)))
    assert [0, 2, 4] == list(filter(lambda x: not x % 2, range(6)))
    assert [("a", 1), ("b", 2)] == list(map(lambda x: (chr(97 + x), x + 1), range(2)))
    # reduce
    assert 24 == reduce((lambda x, y: x * y), [1, 2, 3, 4])
    # trimming
    assert "llo" == "hello"[2:]
    assert "he" == "hello"[:2]
    assert "hell" == "hello"[:-1]
    assert "h" == "hello"[:1]
    assert "o" == "hello"[-1:]
    # binary
    assert "110" == bin(6)[2:]
    assert 6 == int("110", 2)
    assert ["h", "i"] == list("hi")
    # frequency
    assert {"a": 3, "b": 1} == (lambda a: {x: a.count(x) for x in a})(
        ["a", "a", "a", "b"]
    )
    assert {"a": 1, "b": 2} == (lambda a: {x: a.count(x) for x in a})(["a", "b", "b"])

    assert 10 == (lambda f: (f - 32) * 5 / 9)(50)
    # add a secondary property [{'a':3,'b':2},{'a':3,'b':2}].map(x=>({...x,c:x.b}))
    # assert [{"a": 3, "b": 2}, {"a": 3, "b": 2}] == list(
    #     map(lambda x: x if x.get("b") else x.b, [{"a": 3, "b": 2}, {"a": 3, "b": 2}])
    # )

    # computed

    # assert {"first": "jack", "last": "kavanagh", "full": "jack kavanagh"} == (
    #     lambda first, last: {first, last, full:=first+last}
    # )({"first": "jack", "last": "kavanagh"})
