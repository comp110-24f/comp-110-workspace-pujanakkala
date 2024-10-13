"""EX03- Structured Wordle"""

__author__: str = "730477451"


def input_guess(secret_word_len: int) -> str:
    """function that prompts user to input a guess of the correct length"""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # f string notation uses {} and no + signs
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """function that searches the secret word for matching characters of the guess"""
    assert len(char_guess) == 1  # condition that char_guess is equal to one char
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True  # want to return a bool so that it can be used in the elif
            # in the next function
        index += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """function that will show the user which letters of their guess are in the secret
    word and where"""
    assert len(guess) == len(
        secret_word
    )  # if they don't have the same length the code won't run
    index: int = 0
    emojis: str = ""  # need to create empty string so you can add to it
    WHITE_BOX: str = "\U00002B1C"  # emoji codes
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret_word):
        if guess[index] == secret_word[index]:
            emojis += GREEN_BOX
        elif contains_char(
            secret_word, guess[index]
        ):  # uses previous function to go through each char in guess
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return emojis


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    correct: bool = False
    while (
        turn <= 6 and correct is False
    ):  # not "correct == False", but "correct is False"
        # combines all previous functions
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            len(secret_word)
        )  # need to input these variables as they are local
        emojis: str = emojified(guess, secret_word)
        if guess == secret_word:
            print(emojis)
            correct = True  # so you can enter the next if statement when you win
        else:
            print(emojis)
            turn += 1
    if correct is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if (
    __name__ == "__main__"
):  # so that when importing the function it won't run and we can use whatever
    # code word we want each time
    main(secret_word="codes")
