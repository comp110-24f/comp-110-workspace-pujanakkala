"""Practice with Conditionals- CQ02"""

__author__ = "730477451"


def guess_a_number() -> None:
    """function for a guessing number game which prompts you to guess a
    number and then tells you how you did"""
    secret: int = 7
    guess = input("Guess a number: ")
    print("Your guess was " + guess + ".")
    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
