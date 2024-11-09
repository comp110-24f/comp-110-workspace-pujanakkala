"""File to define Fish class."""

__author__: str = "730477451"


class Fish:
    """New fish class with one attribute."""

    age: int

    def __init__(self):
        """Initialize age."""
        self.age = 0
        return None

    def one_day(self):
        """Update age after 1 day."""
        self.age += 1
        return None
