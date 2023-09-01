from main import f


def test_func():
    assert f([1, 2, 3, 4, 5]) == 5
    assert f([1, 2, 3, 4, 5, 6]) == 6
    assert f([1]) == 1
