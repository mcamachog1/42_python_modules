#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1, factory2):
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(f"{creature1.describe()}\n vs\n{creature2.describe()}\n fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    print("Testing factory:")
    test_factory(FlameFactory())
    print("\nTesting factory:")
    test_factory(AquaFactory())

    print("\nTesting battle:")
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
