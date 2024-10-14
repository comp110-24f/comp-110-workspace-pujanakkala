"""writing a test unit"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_list


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"
