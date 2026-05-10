# creature.py

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.type = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass
