# strategy.py


from abc import ABC, abstractmethod
from ex0.creature import Creature


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass
