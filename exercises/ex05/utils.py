"""EX05- List Utility Functions"""

__author__: str = "730477451"


def only_evens(input: list[int]) -> list[int]:
    evens: list[int] = []
    for elem in input:
        if elem % 2 == 0:
            evens.append(elem)
    return evens


def sub(input: list[int], start_idx: int, end_idx: int) -> list[int]:
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(input):
        end_idx = len(input)
        # makes it stop at last value (len(input) -1 would exclude the last element)

    if len(input) == 0 or start_idx >= len(input) or end_idx <= 0:
        return []

    new_list: list[int] = []
    for idx in range(start_idx, end_idx):  # "range" already excludes the last value
        new_list.append(input[idx])

    return new_list


def add_at_index(input: list[int], num: int, idx: int) -> None:
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)
    # adds an extra value to end so you can move values over to create space for new num
    i = len(input) - 2
    # shift every element after idx one over to the right starting at the second to
    # last element and going backward
    while i >= idx:
        input[i + 1] = input[i]
        i -= 1

    input[idx] = num  # inserts the new num at the right idx
