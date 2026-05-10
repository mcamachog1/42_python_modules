#!/usr/bin/env python3


class GardenError(Exception):
    """ Base class for other garden-related exceptions."""
    pass


class LightError(GardenError):
    """ Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """ Raised when there is a watering sysem issue."""
    pass


class Plant():
    def __init__(
                self,
                name: str,
                water_level: int,
                sunlight_hours: int) -> None:
        self.name = name
        self._water_level = water_level
        self.sunlight_hours = sunlight_hours

    @property
    def name(self) -> str:
        """ Getter for the plant's name """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not name.split():
            raise GardenError("Plant name cannot be empty!")
        self._name = name

    @property
    def water_level(self) -> int:
        """ Getter for the plant's water level """
        return self._water_level

    def water(self) -> None:
        if self._water_level + 1 > 10:
            raise WaterError(
                f"Error: Water level {self._water_level + 1} "
                f"is too high (max 10)")
        self._water_level += 1
        print(f"Watering {self.name} - success to: {self._water_level}")

    def health(self) -> None:
        if self.water_level > 10:
            raise WaterError(
                f"Water level {self.water_level} is too high (max 10)")
        if self.water_level < 1:
            raise WaterError(
                f"Water level {self.water_level} is too low (min 1)")
        if self.sunlight_hours > 12:
            raise LightError(
                f"Sunlight hours {self.sunlight_hours} is too high (max 12)")
        if self.sunlight_hours < 2:
            raise LightError(
                f"Sunlight hours {self.sunlight_hours} is too low (min 2)")
        print(
            f"{self.name}: healthy (water: {self.water_level}, "
            f"sun: {self.sunlight_hours})")


class GardenManager():
    """
    Class for manage gardens
    """

    water_tank: int = 50

    def __init__(self, manager_name: str) -> None:
        self.manager_name = manager_name
        self.plant_list: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plant_list.append(plant)
        print(f"Added {plant.name} succesfully")

    def water_plants(self) -> None:
        for plant in self.plant_list:
            if GardenManager.water_tank < 20:
                raise GardenError("Not enough water in tank")
            try:
                GardenManager.water_tank -= 20
                plant.water()
            except WaterError as e:
                print(f"{e}")


def main() -> None:
    # Init test
    print("=== Garden Management System ===\n")

    # Create and fill garden
    garden: GardenManager = GardenManager("system")
    print("Adding plants to garden ...")
    try:
        tomato: Plant = Plant("tomato", 4, 8)
        garden.add_plant(tomato)
        lettuce: Plant = Plant("lettuce", 2, 6)
        garden.add_plant(lettuce)
        carrot: Plant = Plant(" ", 7, 5)
        garden.add_plant(carrot)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    # Water plants n-times
    print("\nWatering plants...")
    print("Opening watering system")
    try:
        for i in range(1):
            garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("Closing watering system (cleanup)")

    # Check plants health
    print("\nChecking plant health...")
    lettuce._water_level = 15
    for plant in garden.plant_list:
        try:
            plant.health()
        except GardenError as e:
            print(f"Error checking {plant.name}: {e}")

    # Check GardenError (water in tank)
    print("\nTesting error recovery...")
    try:
        garden.water_plants()
    except Exception as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    # Finish test with or without errors
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
