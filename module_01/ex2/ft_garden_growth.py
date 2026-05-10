#!/usr/bin/env python3

"""
Exercise 2: Plant Growth Simulator
"""


class GrowingPlant():
    """
    A class to represent a plant growing.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float) -> None:
        """
        Allocate memory to create a new Plant Growing
        instance and save init data.

        Args:
            name (str): plant name.
            height (float): plant height in centimeters.
            age_days (int): plant age in days.
            growth_rate (float): plant growth rate in centimeters per day.
        """

        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate: float = growth_rate
        self.last_growth: float = 0.0

    def grow(self, cm: float) -> None:
        """
        Add cm to the plant height.

        Args:
            cm (float): number of centimeters to add to the plant height.
        """

        if cm > 0:
            self.height += cm
            self.last_growth = cm

    def age(self, days: int) -> None:
        """
        Add days to the plant age.

        Args:
            days (int): number of days to add to the plant age.
        """

        if days > 0:
            self.age_days += days
            self.grow(self.growth_rate * days)

    def get_info(self) -> str:
        """
        Get the plant information as a string.

        Returns:
            str: a string containing the plant's name, height, and age.
        """

        return (
            f"{self.name}: {self.height}cm, {self.age_days} days old"
        )


def main() -> None:

    garden: list[GrowingPlant] = []
    rose: GrowingPlant = GrowingPlant("Rose", 25, 30, 1)
    sunflower: GrowingPlant = GrowingPlant("Sunflower", 80, 45, 2)
    cactus: GrowingPlant = GrowingPlant("Cactus", 15, 120, 0.5)
    garden.extend([rose, sunflower, cactus])
    print("=== Day 1 ===")
    for plant in garden:
        print(plant.get_info())
    for plant in garden:
        plant.age(6)
    print("=== Day 7 ===")
    for plant in garden:
        print(plant.get_info())
        print(f"Growth this week: +{plant.last_growth}cm")


if __name__ == "__main__":
    main()
