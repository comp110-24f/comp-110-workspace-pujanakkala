"""- CQ07"""

__author__ = "730477451"


from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_value() -> None:
    """test that function returns the correct max value"""
    num_list: list[int] = [4, 6, 3, 7, 2]
    assert find_and_remove_max(num_list) == 7


def test_find_and_remove_max_mutation() -> None:
    """test that function correctly removes max value from the list."""
    num_list: list[int] = [5, 8, 6, 8, 2]
    find_and_remove_max(num_list)
    assert num_list == [5, 6, 2]


def test_find_and_remove_max_empty_list() -> None:
    """test edge case where the input list is empty"""
    num_list: list[int] = []
    assert find_and_remove_max(num_list) == -1
    assert num_list == []
