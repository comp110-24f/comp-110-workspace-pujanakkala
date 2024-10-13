"""Tea Party Assignment"""

__author__: str = "730477451"


# function to print all the other functions at once, instead of having to call each one
# separately
# you need to set keyword arguements in order for functions to pull appropriate
# variables
def main_planner(guests: int) -> None:
    """function to serve as the entrypoint of the tea party program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # put functions local variable first, then current functions parameter
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """function to comupte the number of tea bags needed based on
    the number of guests if guests drink 2 cups of tea each"""
    return people * 2


def treats(people: int) -> int:
    """function to compute the number of treats needed based on the
    number of guests if guests drink, on average, 1.5 treats per tea"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """function to compute the cost of the tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


# need at end of code for main function to run
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
