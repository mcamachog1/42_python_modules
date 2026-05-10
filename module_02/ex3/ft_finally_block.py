#!/usr/bin/env python3

"""
Exercise 3: Finally Block - Always
Clean Up
"""


def water_plants(plant_list: list[str]) -> None:
    """
    Water a list of plants (plants need valid names)
    if a plant name starts with "_" it is an invalid name

    Args:
        plant_lists (list[str]): a list of plant names.
    """

    print("Opening watering system")
    for plant in plant_list:
        if not plant.strip():
            raise Exception("Cannot water None - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plants: list[str] = ['tomato', 'lettuce', 'carrots']
    try:
        water_plants(plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed succesfully!")

    print("\nTesting with error...")
    plants.clear()
    plants.extend(['tomato', ' '])
    try:
        water_plants(plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
