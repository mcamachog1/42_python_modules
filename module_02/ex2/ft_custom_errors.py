#!/usr/bin/env python3

"""
Exercise 2: Making Your Own Error
Types
"""


class GardenError(Exception):
    """ Base class for other garden-related exceptions."""
    pass


class PlantError(GardenError):
    """ Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """ Raised when there is a watering sysem issue."""
    pass


def set_plant_status(issue: str, plant_name: str) -> None:
    if issue == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")
    elif issue == "dry":
        # raise WaterError(f"The {plant_name} plants needs water!")
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        set_plant_status("wilting", "tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nTesting WaterError...")
    try:
        set_plant_status("dry", "tomato")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nTesting catching all garden errors...")
    try:
        set_plant_status("wilting", "tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        set_plant_status("dry", "tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


def test_good_and_error_data() -> None:
    print("\n=== Extra Demo with correct data and error data ===")
    plants: list[str] = ['tomato', 'carrot', 'letucce', 'onion']
    status: list[str] = ['OK', 'dry', 'wilting', 'OK']
    for i in range(len(plants)):
        try:
            set_plant_status(status[i], plants[i])
            print(f"Plant {plants[i]} is OK")
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    print("The test finished without crash.")


if __name__ == "__main__":
    test_custom_errors()
    test_good_and_error_data()
