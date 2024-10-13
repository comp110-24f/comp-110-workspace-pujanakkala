"""EX02- Chardle- A cute step toward Wordle."""

__author__: str = "730477451"


def input_word() -> str:
    """to make word equal to user input that needs to be 5 characters"""
    word: str = input(
        "Enter a 5-character word: "
    )  # format for asking a question and setting input euqal to a variable
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # to exit function and not continue to contains_char and before it returns word
    return word


def input_letter() -> str:
    """to make character equal to user input that needs to be a single character"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # needs to be in if block to work when you want it to
    return letter


def contains_char(word: str, letter: str) -> None:
    """to check if each letter of the word matches the letter and find total count"""
    instances: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        instances += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        instances += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        instances += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        instances += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        instances += 1
    if instances == 0:
        # need separate if lines because it's no and not 0 instances
        print("No instances of " + letter + " found in " + word)
    elif instances == 1:
        print("1 instance of " + letter + " found in " + word)
        # need separate line because instance is singular
    else:
        print(str(instances) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
