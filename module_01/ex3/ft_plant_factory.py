#!/usr/bin/env python3


"""
Exercise 3: Plant Factory
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


def plant_factory(
        names: list[str],
        heights: list[float],
        ages: list[int]) -> list[Plant]:

    """
    Create a list of Plant instances from the provided data.

    Args:
        names (list[str]): List of plant names.
        heights (list[float]): List of plant heights in centimeters.
        ages (list[int]): List of plant ages in days.

    Returns:
        list[Plant]: List of Plant instances.
    """

    garden: list[Plant] = []
    for i in range(len(names)):
        plant: Plant = Plant(names[i], heights[i], ages[i])
        garden.append(plant)
    return garden


def main() -> None:
    names: list[str] = ["Rose", "Sunflower", "Cactus", "Palm", "Tulip"]
    heights: list[float] = [25.0, 80.0, 15.0, 110.8, 30.5]
    ages: list[int] = [30, 45, 120, 180, 25]
    plants: list[Plant] = plant_factory(names, heights, ages)
    print("=== Plant Factory Output===")
    for plant in plants:
        print(
            f"Created: {plant.name} "
            f"({plant.height}cm, {plant.age_days} days)"
        )
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
