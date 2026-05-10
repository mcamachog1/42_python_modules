#!/usr/bin/env python3
# scope_mysteries.py


from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accum_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accum_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    result: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        result[key] = value
        return f"Store '{key}' = {value}"

    def recall(key: str) -> str:
        return f"Recall '{key}': {result.get(key, 'Memory not found')}"

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("Testing mage counter...")
    f_counter_a: Callable = mage_counter()
    print(f"counter_a call 1: {f_counter_a()}")
    print(f"counter_a call 2: {f_counter_a()}")
    f_counter_b: Callable = mage_counter()
    print(f"counter_b call 1: {f_counter_b()}")

    print("\nTesting spell accumulator...")
    f_accum_power_20 = spell_accumulator(20)
    f_accum_power_30 = spell_accumulator(30)
    print(f"Base 100, add 20: {f_accum_power_20(100)}")
    print(f"Base 100, add 30: {f_accum_power_30(100)}")

    print("\nTesting enchantment factory...")
    items_to_enchant = ['Sword', 'Shield']
    f_enchantment_factory_1 = enchantment_factory('Flaming')
    f_enchantment_factory_2 = enchantment_factory('Frozen')
    for item in items_to_enchant:
        print(f_enchantment_factory_1(item))
        print(f_enchantment_factory_2(item))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print(vault['store']('secret', 42))
    print(vault['recall']('secret'))
    print(vault['recall']('unknown'))


if __name__ == "__main__":
    main()
