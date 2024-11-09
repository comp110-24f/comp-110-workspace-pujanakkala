"""File to define River class."""

__author__: str = "730477451"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """New river class with 3 attributes."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Method to check ages of animals still alive."""
        alive_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                alive_bears.append(bear)
        self.fish = alive_fish
        self.bears = alive_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Method to remove fish of a certain amount."""
        for _ in range(0, amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def bears_eating(self):
        """Method to update animals when bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Method to check make sure list is only alive bears."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Method to simulate fish mating."""
        new_fish_count: int = (len(self.fish) // 2) * 4
        for _ in range(0, new_fish_count):
            self.fish.append(Fish())
        return None
        return None

    def repopulate_bears(self):
        """Method to simulate bears mating."""
        new_bears_count: int = len(self.bears) // 2
        for _ in range(0, new_bears_count):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Method to visualize animal populations per day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
