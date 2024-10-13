"""def fuel_needed(distance: int, mpg: float) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: float, price_per_gallon: float) -> float:
    print(fuel_needed(distance=distance, mpg=mpg) * price_per_gallon)


print(total_fuel_cost(distance=300.3, mpg=25, price_per_gallon=4))"""

"""conditional practice from CL07"""


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")
