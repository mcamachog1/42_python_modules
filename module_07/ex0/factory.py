# factory.py

from abc import ABC, abstractmethod
from .creature import Creature


class CreatureFactory(ABC):
    name: str

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
