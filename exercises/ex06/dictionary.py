"""EX06- Dictionary Utility Functions"""

__author__: str = "730477451"


def invert(input: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    for key in input:
        if input[key] in new_dict:
            raise KeyError("Duplicate keys in new dict is not allowed")
        new_dict[input[key]] = key
    return new_dict


def favorite_colors(input: dict[str, str]) -> str:
    """function that takes a list of favorite colors and returns the most popular color"""
    color_count: dict[str, int] = {}
    color_order = []

    for name in input:
        color: str = input[name]

        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
            color_order.append(color)

    max_color: str = color_order[0]
    max_count: int = color_count[max_color]

    for color in color_order:
        if color_count[color] > max_count:
            max_color = color
            max_count = color_count[color]

    return max_color


def count(input: list[str]) -> dict[str, int]:
    """function that creates a dict with the unique values of an input and their frequency"""
    new_dict: dict[str, int] = {}
    for elem in input:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """creates a dictionary with first letters and associated words"""
    new_dict: dict[str, list[str]] = {}
    for elem in input:
        first_letter: str = elem[0].lower()
        if first_letter in new_dict:
            new_dict[first_letter].append(elem)
        else:
            new_dict[first_letter] = [elem]
    return new_dict


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
