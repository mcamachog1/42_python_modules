#!/usr/bin/env python3
"""
Exercise 6: Garden Analytics Platform
"""


class Plant():
    """
    A class representing a plant in the garden.
    """

    def __init__(self, name: str, height: float) -> None:
        """
        Initializes a Plant instance.

        Args:
            height (float): The height of the plant in centimeters.
            name (str): The name of the plant.
        """
        if not GardenManager.validate_height(height):
            raise ValueError("Height must be a positive number.")
        self.__height = height
        self.__name = name
        self.growth = 0

    @property
    def height(self) -> float:
        """Returns the height of the plant."""
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        """Sets the height of the plant."""
        if value < 0:
            raise ValueError("Height cannot be negative.")
        elif value < self.__height:
            raise ValueError("Height cannot decrease.")
        self.__height = value

    @property
    def name(self) -> str:
        """Returns the name of the plant."""
        return self.__name

    def grow(self, amount: float) -> None:
        """Increases the height of the plant by a specified amount."""
        if amount < 0:
            raise ValueError("Growth amount cannot be negative.")
        elif amount == 0:
            raise ValueError("Growth amount cannot be zero.")
        self.__height += amount
        self.growth += amount
        print(f"{self.__name} grew {amount}cm")


class FloweringPlant(Plant):
    """
    A class representing a flowering plant, which is a subclass of Plant.
    """

    def __init__(
            self,
            name: str,
            height: float,
            flower_color: str) -> None:
        """
        Constructor of flowering plants
        Args:
            name(str): name of the flower
            height(float): initial height of the flower in cm
            flower_color(str): color of the flower
        """

        super().__init__(name, height)
        self.flower_color = flower_color

    def bloom(self) -> str:
        """
        Return blooming message
        """

        return (f"{self.flower_color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """
    A class representing a Prize Flower.
    """

    def __init__(
            self,
            name: str,
            height: float,
            flower_color: str,
            prize_points: int) -> None:
        """
        A class representing a prize flower,
        which is a subclass of FloweringPlant.
        """
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_points(self) -> str:
        """
        Return a message with prize points of the flower
        """
        return (f"Prize points: {self.prize_points}")


class GardenManager():
    """
    A class representing a garden manager.
    """

    all_gardens: list['GardenManager'] = []

    def __init__(self, garden_name: str) -> None:
        """
        Initializes a GardenManager instance.

        Args:
            garden_name (str): The name of the garden.
            plants (list[Plant]): The list of plants in the garden.
        """
        self.garden_name: str = garden_name
        self.plants: list[Plant] = []
        GardenManager.all_gardens.append(self)

    @staticmethod
    def validate_height(height: float) -> bool:
        """Validates if the height is a positive number."""
        return height > 0

    @classmethod
    def create_garden_network(cls) -> int:
        """ Print all gardens created. """
        print("\nGarden managers:")
        for garden in cls.all_gardens:
            print(garden.garden_name)
        """Returns the total number of gardens."""
        return len(cls.all_gardens)

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.garden_name}'s garden")

    class GardenStats():
        """
        A nested class representing garden statistics.
        """
        @staticmethod
        def get_plant_counts(plants: list[Plant]) -> str:
            regular_plants: int = 0
            flowering_plants: int = 0
            prize_flowers: int = 0
            for plant in plants:
                if plant.__class__.__name__ == "Plant":
                    regular_plants += 1
                elif plant.__class__.__name__ == "FloweringPlant":
                    flowering_plants = +1
                elif plant.__class__.__name__ == "PrizeFlower":
                    prize_flowers += 1
            return (
                f"Plant types: {regular_plants} "
                f"regular, {flowering_plants} flowering, "
                f"{prize_flowers} prize flowers")

        @staticmethod
        def network_report() -> None:
            """
            Prints a message displaying the garden statistics.
            Args:
                manager (GardenManager): The garden manager
                for which to generate the report.
            """
            total_gardens = GardenManager.create_garden_network()
            print(
                f"Total gardens managed: "
                f"{total_gardens}\n")

        def calculate_garden_score(self, manager: 'GardenManager') -> int:
            """
            Calculates the total score for a specific garden.
            Score = Sum of heights + 10 + specific bonuses.
            """
            total_score = 0
            for plant in manager.plants:
                total_score += (plant.height + 10)
                # Add prize points if the plant has them
                if plant.__class__.__name__ == "PrizeFlower":
                    total_score += plant.prize_points
            return total_score

        def garden_report(self, manager: 'GardenManager') -> None:
            """Prints a report of the garden's plants."""
            print(f"\n=== {manager.garden_name}'s Garden Report ===")
            print("Plants in garden:")
            for plant in manager.plants:
                if plant.__class__.__name__ == "Plant":
                    print(f"- {plant.name}: {plant.height}cm")
                elif plant.__class__.__name__ == "FloweringPlant":
                    print(
                        f"- {plant.name}: {plant.height}cm"
                        f", {plant.flower_color} flowers (blooming)")
                elif plant.__class__.__name__ == "PrizeFlower":
                    print(
                        f"- {plant.name}: {plant.height}cm"
                        f", {plant.flower_color} flowers (blooming), "
                        f"Prize points: {plant.prize_points}")
            total_plants: int = len(manager.plants)
            total_growth: float = 0
            for plant in manager.plants:
                total_growth += plant.growth
            print(
                f"\nPlants added: {total_plants},"
                f" Total growth: {total_growth}cm")
            print(f"{self.get_plant_counts(manager.plants)}")


def main() -> None:
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    try:
        oak_tree = Plant("Oak Tree", 100)
        rose = FloweringPlant("Rose", 25, "red")
        sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
        sunflower_bob = PrizeFlower("Sunflower", 50, "yellow", 10)
    except ValueError as e:
        print(e)
    print("=== Garden Management System Demo ===\n")
    alice.add_plant(oak_tree)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    bob.add_plant(sunflower_bob)
    print(f"\n{alice.garden_name} is helping all plants grow ...")
    try:
        oak_tree.grow(1)
        rose.grow(1)
        sunflower.grow(1)
    except ValueError as e:
        print(e)
    stats = GardenManager.GardenStats()
    stats.garden_report(alice)
    stats.garden_report(bob)
    alice_score = stats.calculate_garden_score(alice)
    bob_score = stats.calculate_garden_score(bob)
    print()
    print(
        f"Height validation test: {GardenManager.validate_height(-5)}"
        f" (should be False)")
    print(
        f"Height validation test: {GardenManager.validate_height(5)}"
        f" (should be True)")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    stats.network_report()


if __name__ == "__main__":
    main()
