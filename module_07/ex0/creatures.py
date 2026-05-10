# creatures.py

from .creature import Creature


class Flameling(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses  Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses  Hydro Pump!"
