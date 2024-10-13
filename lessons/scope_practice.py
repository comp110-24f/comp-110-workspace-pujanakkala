"""some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]  # or copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
