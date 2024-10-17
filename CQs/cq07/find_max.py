"""Unit Test Challenge Question- CQ07"""

__author__ = "730477451"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1  # return at the top so that it leaves function before other code
    idx_1: int = 0
    max_num: int = input[idx_1]
    while idx_1 < len(input):
        if input[idx_1] > max_num:
            max_num = input[idx_1]
        idx_1 += 1
    idx_2: int = 0
    while idx_2 < len(input):
        if input[idx_2] == max_num:
            input.pop(idx_2)
        else:
            idx_2 += 1  # needs to be in an else clause so that you don't skip over
            # elements when they all shift after removal
    return max_num
