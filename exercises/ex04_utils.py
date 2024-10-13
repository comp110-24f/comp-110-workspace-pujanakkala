"""EX04- list Utility Functions"""

__author__: str = "730477451"


def all(list: list[int], num: int) -> bool:
    """function to see if num is in the list"""
    idx: int = 0
    if len(list) == 0:
        return False
    while idx < len(list):
        if list[idx] != num:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # raises the error that there are no ints in the list
    max_num: int = input[0]  # sets the max num as the first int in the list
    idx: int = 0
    while idx < len(input):
        if input[idx] > max_num:
            max_num = input[
                idx
            ]  # replaces max num with a highest number as it goes through each int
            # in the list
        idx += 1
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while idx < len(list_1):
        if (
            list_1[idx] != list_2[idx]
        ):  # only want one idx, not 2 because we want to know if the numbers are
            # at the same idx too, not just if the lists contain the same numbers
            return False
        idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])
        idx += 1


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
c: list[int] = [7, 8]
