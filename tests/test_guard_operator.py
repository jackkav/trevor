def guard(condition):
    output = ""
    if condition:
        output = "a"
    return output


def guard_trick(condition):
    output = condition * "a"
    return output


def test_guard_operator():
    assert guard(True) == "a"
    assert guard(False) == ""
    assert guard_trick(True) == "a"
    assert guard_trick(False) == ""
