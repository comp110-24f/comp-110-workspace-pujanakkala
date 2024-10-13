"""Practice with Coordinates- CQ04"""

__author__ = "730477451"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print("(" + str(xs[index]) + "," + str(ys[index2]) + ")")
            index2 += 1
        index += 1
