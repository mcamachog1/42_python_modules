# strategies.py


from .strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class NormalStrategy(BattleStrategy):
    name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    name = "Aggresive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:

        if not hasattr(creature, "transform"):
            raise AttributeError(f"Invalid creature '{creature.name}' "
                                 "for this aggressive strategy")
        transform: str = creature.transform()  # type: ignore

        if not hasattr(creature, "attack"):
            raise AttributeError(f"The creature {creature.name} "
                                 "does not attack")
        attack: str = creature.attack()

        if not hasattr(creature, "revert"):
            raise AttributeError(
                f"Invalid creature '{creature.name}' "
                "for this aggressive strategy")
        revert: str = creature.revert()  # type: ignore

        return f"{transform}\n{attack}\n{revert}"


class DefensiveStrategy(BattleStrategy):
    name = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:

        if not hasattr(creature, "attack"):
            raise AttributeError(
                f"The creature {creature.name} "
                "does not attack")
        attack: str = creature.attack()

        if not hasattr(creature, "heal"):
            raise AttributeError(
                f"Invalid creature '{creature.name}' "
                "for this defensive strategy")
        heal: str = creature.heal()  # type: ignore

        return f"{attack}\n{heal}"
