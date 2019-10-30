def test_sets():
    assert {"e", "q", "t", "w", "r", "y"} == set("qwerty")
    assert {1, 2, 3} == {3, 2, 3, 1}

    assert set({1, 2, 3}) == {3, 2, 3, 1}
    assert {1, 2} == {3, 2, 3, 1} & {1, 2, 4}
    assert {1, 2} == {3, 2, 3, 1}.intersection({1, 2, 4})
