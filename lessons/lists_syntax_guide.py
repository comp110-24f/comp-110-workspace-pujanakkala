"""CL13 - Basic syntax of lists"""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# print(my_numbers)

# String Analogy
# my_name: str = "" #literal
# my_name: str = str() #constructor

# Adding an item to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# append is a method or a function that belongs to the list class

# print(my_numbers)

# Creating and already populated list
game_points: list[int] = [102, 86, 94]

# Subscription notation/ indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying by index
# (Because lists are mutable)
game_points[1] = 72
print(game_points)

# Getting the length
(len(game_points))

# Remove an item from a list
game_points.pop(1)  # number is the index, not the actual list value
print(game_points)


def display(input: list[int]) -> None:
    idx: int = 0
    while idx < len(input):
        print(input[idx])
        idx += 1


display(game_points)
