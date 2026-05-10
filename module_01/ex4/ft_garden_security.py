#!/usr/bin/env python3

"""
Exercise 4: Garden Security System
"""


class SecurePlant:
    """
    A class representing a plant with security checks
    on height and age updates.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int) -> None:
        """
        Allocate memory to create a new SecurePlant
        instance and save init data.

        Args:
            name (str): The name of the plant.
            height (float): The height of the plant in centimeters.
            age_days (int): The age of the plant in days.
        """

        self.__name = name
        self.__height = height
        self.__age_days = age_days

    @property
    def name(self) -> str:
        """
        Getter for the plant's name.
        """

        return self.__name

    @property
    def height(self) -> float:
        """
        Getter for the plant's height.
        """

        return self.__height

    @height.setter
    def height(self, height: float) -> None:
        """
        Setter for the plant's height.

        Args:
            height (float): The new height of the plant in centimeters.
        """

        if height > self.__height:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        elif (height < 0):
            print(
                f"\nInvalid operation attempted:"
                f" height {height}cm [REJECTED]")
            print("Security: Height cannot be negative")
        elif (height < self.__height):
            print(
                f"\nInvalid operation attempted:"
                f" height {height}cm [REJECTED]")
            print("Security: Height cannot decrease")

    @property
    def age_days(self) -> int:
        """
        Getter for the plant's age in days.
        """

        return self.__age_days

    @age_days.setter
    def age_days(self, age_days: int) -> None:
        """
        Setter for the plant's age in days.

        Args:
            age_days (int): The new age of the plant in days.
        """

        if age_days > self.__age_days:
            self.__age_days = age_days
            print(f"Age updated: {age_days} days [OK]")
        elif age_days < 0:
            print(
                f"\nInvalid operation attempted:"
                f" age {age_days} days [REJECTED]"
            )
            print("Security: Age cannot be negative")
        elif (age_days < self.__age_days):
            print(
                f"\nInvalid operation attempted:"
                f" age {age_days} days [REJECTED]"
            )
            print("Security: Age cannot decrease")


def main() -> None:
    plant = SecurePlant("Rose", 30.0, 100)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.height = 35.0  # Valid operation
    plant.age_days = 150  # Valid operation
    print()
    plant.height = -5  # Invalid operation
    plant.height = 15.0  # Invalid operation
    plant.age_days = 90  # Invalid operation
    plant.age_days = -3  # Invalid operation
    print(
        f"\nCurrent plant: {plant.name} "
        f"({plant.height}cm, {plant.age_days} days)"
    )


if __name__ == "__main__":
    main()
