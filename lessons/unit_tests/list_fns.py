"""CL16 - 10/14 list practice"""


def get_first(input: list[str]) -> str:
    """return first element"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """remove first element"""
    input.pop(0)


def get_and_remove_list(input: list[str]) -> str:
    """return and remove first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
