from main import func


def test_func():
    assert func([1, 2, 3, 4, 5]) == 5
    assert func([1, 2, 3, 4, 5, 6]) == 6
    assert func([1]) == 1
