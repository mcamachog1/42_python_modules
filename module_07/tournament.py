#!/usr/bin/env python3
# tournament.py

from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformingCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)


def main():

    factory_normal_fire = FlameFactory()
    factory_normal_water = AquaFactory()
    factory_healing = HealingCreatureFactory()
    factory_transformed = TransformingCreatureFactory()

    strategy_normal = NormalStrategy()
    strategy_aggresive = AggressiveStrategy()
    strategy_defensive = DefensiveStrategy()

    def single_battle(
            opponents: List[Tuple[CreatureFactory, BattleStrategy]]):

        for i in range(len(opponents) - 1):
            creature_a = opponents[i][0].create_evolved()
            strategy_a = opponents[i][1]
            for opponent in opponents[i + 1:]:
                creature_b = opponent[0].create_evolved()
                strategy_b = opponent[1]
                print("\n* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print(" now fight!")
                try:
                    print(strategy_a.act(creature_a))
                    print(strategy_b.act(creature_b))
                except AttributeError as e:
                    print(f"Battle error, aborting tournament: {e}")

    opponents = [
            (factory_normal_fire, strategy_normal),
            (factory_healing, strategy_defensive),
            ]

    print("Tournament 0 (basic)")
    opponents_list = [
        f"({factory.name}+{strategy.name})"
        for factory, strategy in opponents]
    print(opponents_list)
    print("*** Tournament ***")
    print(f"{len(opponents_list)} opponents involved")
    single_battle(opponents)

    opponents.clear()
    opponents.append((factory_normal_fire, strategy_aggresive))
    opponents.append((factory_healing, strategy_defensive))
    print("\nTournament 1 (error)")
    opponents_list.clear()
    opponents_list = [
        f"({factory.name}+{strategy.name})"
        for factory, strategy in opponents]
    print(opponents_list)
    print("*** Tournament ***")
    print(f"{len(opponents_list)} opponents involved")
    single_battle(opponents)

    opponents.clear()
    opponents.append((factory_normal_water, strategy_normal))
    opponents.append((factory_healing, strategy_defensive))
    opponents.append((factory_transformed, strategy_aggresive))
    print("\nTournament 2 (multiple)")
    opponents_list.clear()
    opponents_list = [
        f"({factory.name}+{strategy.name})"
        for factory, strategy in opponents]
    print(opponents_list)
    print("*** Tournament ***")
    print(f"{len(opponents_list)} opponents involved")
    single_battle(opponents)


if __name__ == "__main__":
    main()
