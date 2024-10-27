"""def fuel_needed(distance: int, mpg: float) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: float, price_per_gallon: float) -> float:
    print(fuel_needed(distance=distance, mpg=mpg) * price_per_gallon)


print(total_fuel_cost(distance=300.3, mpg=25, price_per_gallon=4))"""

"""conditional practice from CL07"""


"""def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")
"""

"""input: list[str] = ["hello", "bye"]


def size_string(input: list[str]) -> list[int]:
    new_list: list[int] = []
    for elem in input:
        new_list.append(len(elem))
    print(new_list)
    return new_list


size_string(input)"""


"""def insert_float(lst: list[float], index: int, num: float) -> list[float]:
    Insert a float into the list at the specified index without using the insert function.
    result: list[float] = []

    for x in range(0, len(lst)):
        if x == index:
            result.append(num)  # Add the new float at the specified index

        result.append(lst[x])  # Add the existing float

    # If the index is at the end, append the new float after the last element
    if index >= len(lst):
        result.append(num)

    return result
"""


def count_chars(string: str) -> dict[str, int]:
    """Return a dictionary with the frequency of each character in the input string."""
    result: dict[str, int] = {}
    for x in range(0, len(string)):
        if string[x] in result:
            result[string[x]] += 1
        else:
            result[string[x]] = 1
    return result


def count_chars_2(input: str) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    for idx in range(0, len(input)):
        char: str = input[idx]
        char_freq: int = 0
        for idx in range(0, len(input)):
            if char == input[idx]:
                char_freq += 1
        new_dict[char] = char_freq
    return new_dict
