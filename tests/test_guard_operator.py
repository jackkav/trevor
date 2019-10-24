def guard(condition):
    output = ""
    if condition:
        output = "a"
    return output


def guard_trick(condition):
    output = condition * "a"
    return output


def guard_trick_one_line(condition, valueToTest, default):
    return condition * valueToTest or default


def test_guard_operator():
    assert guard(True) == "a"
    assert guard(False) == ""
    assert guard_trick(True) == "a"
    assert guard_trick(False) == ""
    assert guard_trick_one_line(True, "a", "") == "a"
    assert guard_trick_one_line(False, "a", "") == ""
