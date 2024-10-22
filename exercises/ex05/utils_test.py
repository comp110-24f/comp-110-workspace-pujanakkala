from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Tests for only_evens function"""


def test_only_evens_only_odds() -> None:
    """test that only_evens returns an empty list if only odd numbers"""
    input: list[int] = [1, 7, 9]
    assert only_evens(input) == []


def test_only_evens_empty_list() -> None:
    """test that only_evens returns an empty list if input is an empty list"""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_return_value() -> None:
    """test that only_evens returns the even numbers of the list"""
    input: list[int] = [1, 4, 4, 7, 6]
    assert only_evens(input) == [4, 4, 6]


def test_only_evens_no_mutation() -> None:
    """test that only_evens does not mutate input list"""
    input: list[int] = [1, 4, 4, 7, 6]
    only_evens(input)
    assert input == [1, 4, 4, 7, 6]


"""Tests for sub function"""


def test_sub_empty_list() -> None:
    """test that sub returns an empty list if input is an empty list"""
    input: list[int] = []
    assert sub(input, 0, 3) == []


def test_sub_return_value() -> None:
    """test that sub returns a list which is a subset of the input list between the
    start idx and end idx -1"""
    input: list[int] = [1, 4, 4, 7, 6, 4, 9, 8, 2]
    assert sub(input, 2, 5) == [4, 7, 6]


def test_sub_no_mutation() -> None:
    """test that sub does not mutate the input list"""
    input: list[int] = [1, 4, 4, 7, 6, 4, 9, 8, 2]
    sub(input, 2, 5)
    assert input == [1, 4, 4, 7, 6, 4, 9, 8, 2]


"""Tests for add_at_index function"""


def test_add_at_index_insert_start() -> None:
    """tests that add_at_index inserts element at start of input list"""
    input: list[int] = [4, 4, 7, 6]
    add_at_index(input, 1, 0)
    assert input == [1, 4, 4, 7, 6]


def test_add_at_index_return_value() -> None:
    """tests that add_at_index returns None"""
    input: list[int] = [1, 4, 4, 7, 6]
    assert add_at_index(input, 9, 2) is None


def test_add_at_index_mutation() -> None:
    """tests that add_at_index mutates the input list"""
    input: list[int] = [1, 4, 4, 7, 6]
    add_at_index(input, 9, 2)
    assert input == [1, 4, 9, 4, 7, 6]


def test_add_at_index_raises_indexerror():
    """test that add_at_index raises an IndexError for an invalid index"""
    input: list[int] = [1, 4, 4, 7, 6]
    with pytest.raises(IndexError):
        add_at_index(input, 2, 9)
