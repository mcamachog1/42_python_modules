from ex0.factory import CreatureFactory
from ex0.creatures import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    name = "Healing"

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformingCreatureFactory(CreatureFactory):
    name = "Transform"

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
