#!/usr/bin/env python3

"""
Exercise 1: Garden Data Organizer
"""


class Plant:

    """
    A class to represent a plant in the garden.
    """

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """
        Allocate memory to create a new Plant instance.

        Args:
            name (str): plant name.
            height (float): plant height in centimeters.
            age_days (int): plant age in days.
        """
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days


def main() -> None:
    """
    Main function to create and display plant data.
    """

    garden: list[Plant] = []
    rose: Plant = Plant("Rose", 25.0, 30)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    cactus: Plant = Plant("Cactus", 15.0, 120)
    garden.extend([rose, sunflower, cactus])
    print("=== Gardden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age_days} days old")


if __name__ == "__main__":
    main()
