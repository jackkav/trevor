def get_ordinal(n):
    last = int(n) % 10

    last_two = int(n) % 100
    if 15 > int(last_two) > 10:
        return n + "th"

    suffix = "th,st,nd,rd".split(",")[last] if last < 4 else "th"
    return n + suffix


def golfed_ordinal(n):
    return (
        n + "th"
        if 15 > int(n) % 100 > 10
        else n + ("th,st,nd,rd".split(",")[int(n) % 10] if int(n) % 10 < 4 else "th")
    )


def split_on_indexes(s):
    return s


def test_split():
    assert ["test", "123"] == "test,123".split(",")


def test_ordinals():
    assert "0th" == get_ordinal("0")
    assert "1st" == get_ordinal("1")
    assert "2nd" == get_ordinal("2")
    assert "3rd" == get_ordinal("3")
    assert "4th" == get_ordinal("4")
    assert "5th" == get_ordinal("5")
    assert "11th" == get_ordinal("11")
    assert "21st" == get_ordinal("21")
    assert "92nd" == get_ordinal("92")
    assert "192nd" == get_ordinal("192")
