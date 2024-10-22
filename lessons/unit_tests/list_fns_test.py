"""writing a test unit"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_list


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_value() -> None:
    """test that remove first returns None."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert if remove_first(fruits) is None


def test_remove_first_behavior() -> None:
    """test that remove first removes first element"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]
