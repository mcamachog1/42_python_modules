#!/usr/bin/env python3
# capabilities.py


from ex1.factories import HealingCreatureFactory, TransformingCreatureFactory


def test_healing():
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transforming():
    print("\nTesting Creature with transforming capability")
    factory = TransformingCreatureFactory()

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main():
    test_healing()
    test_transforming()


if __name__ == "__main__":
    main()
