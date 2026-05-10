#!/usr/bin/env python3

"""
Exercise 5: Specialized Plant Types
"""


class Plant:

    """
    A class to represent a plant.
    """

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """
        Allocate memory to create a new Plant instance.

        Args:
            name (str): plant name.
            height (float): plant height in centimeters.
            age_days (int): plant age in days.
        """
        self.name = name
        self.height = height
        self.age_days = age_days


class Flower(Plant):

    """
    A class to represent a flower, inheriting from Plant.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str) -> None:
        """
        Allocate memory to create a new Flower instance.

        Args:
            name (str): flower name.
            height (float): flower height in centimeters.
            age_days (int): flower age in days.
            color (str): flower color.
        """
        super().__init__(name, height, age_days)
        self.color = color
        self.type = "Flower"

    def bloom(self) -> str:
        """
        Simulate the blooming of the flower.
        Returns:
            str: blooming message.
        """
        return f"\n{self.name} is blooming beautifully!"

    def hello(self) -> str:
        """
        Return a greeting message from the flower.
        Returns:
            str: greeting message.
        """

        message: str = (f"\n{self.name} ({self.type}): {self.height}cm, "
                        f"{self.age_days} days, {self.color} color")
        message += self.bloom()
        return message


class Tree(Plant):

    """
    A class to represent a tree, inheriting from Plant.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            trunk_diameter: float) -> None:
        """
        Allocate memory to create a new Tree instance.

        Args:
            name (str): tree name.
            height (float): tree height in centimeters.
            age_days (int): tree age in days.
            trunk_diameter (float): tree trunk diameter in centimeters.
        """
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self.type = "Tree"

    def produce_shade(self) -> str:
        """
        Calculate and return the shade area produced by the tree.
        Returns:
            str: shade area information.
        """

        trunk_m: float = self.trunk_diameter / 100
        crown_radius: float = trunk_m * 10
        shade_area: float = 3.14 * (crown_radius ** 2)
        return (
            f"\n{self.name} provides {shade_area:.0f} "
            f"square meters of shade")

    def hello(self) -> str:
        """
        Return a greeting message from the tree.
        Returns:
            str: greeting message.
        """

        message: str = (
            f"\n{self.name} ({self.type}): {self.height}cm, "
            f"{self.age_days} days, {self.trunk_diameter}cm diameter")
        message += self.produce_shade()
        return message


class Vegetable(Plant):

    """
    A class to represent a vegetable, inheriting from Plant.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            harvest_season: str,
            nutritional_value: str) -> None:
        """
        Allocate memory to create a new Vegetable instance.

        Args:
            name (str): vegetable name.
            height (float): vegetable height in centimeters.
            age_days (int): vegetable age in days.
            harvest_season (str): season when the vegetable is harvested.
            nutritional_value (float): nutritional value of the vegetable.
        """
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.type = "Vegetable"

    def hello(self) -> str:
        """
        Return a greeting message from the vegetable.
        Returns:
            str: greeting message.
        """
        return (
            f"\n{self.name} ({self.type}): {self.height}cm, "
            f"{self.age_days} days, {self.harvest_season} harvest"
            f"\n{self.name} is rich in {self.nutritional_value}"
        )


def main() -> None:
    plants: list[Plant] = []
    flower: Flower = Flower("Rose", 30.0, 25, "red")
    tulip: Flower = Flower("Tulip", 20.0, 15, "yellow")
    oak: Tree = Tree("Oak", 500, 1825, 50)
    maple: Tree = Tree("Maple", 300, 1095, 30)
    carrot: Vegetable = Vegetable(
        "Carrot", 20.0, 90, "summer", "vitamin A"
    )
    tomato: Vegetable = Vegetable(
        "Tomato", 50.0, 60, "summer", "vitamin C"
    )
    plants.extend([flower, tulip, oak, maple, carrot, tomato])
    print("=== Garden Plant Types ===")
    for plant in plants:
        print(plant.hello())


if __name__ == "__main__":
    main()
