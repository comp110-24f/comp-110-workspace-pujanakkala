"""While Loops Challenge Question"""

___author___ = "730477451"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        else:
            count = count
        index = index + 1
    return print(count)
