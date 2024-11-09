"""File to define Bear class."""

__author__: str = "730477451"


class Bear:
    """New bear class with 2 attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize attributes."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Update attributes after a day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Update hunger after eating."""
        self.hunger_score += num_fish
