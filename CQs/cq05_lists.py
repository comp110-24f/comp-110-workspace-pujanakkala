"""Mutating functions."""

___author___ = "730477451"


def manual_append(list: list[int], num_1: int) -> None:
    """function to add items to the list"""
    list.append(num_1)


def double(list: list[int]) -> None:
    """function to dobule all the values in the list"""
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
