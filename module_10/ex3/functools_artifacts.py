#!/usr/bin/env python3
# functools_artifacts.py

import operator
from functools import partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:

    MAX_INT = 2147483647
    result: int = 0

    if operation not in ["add", "multiply", "max", "min"]:
        raise ValueError("Operation not allowed")

    if len(spells) == 0:
        result = 0

    if operation.lower() == "add":
        total_sum: int = 0
        for spell in spells:
            total_sum = operator.add(total_sum, spell)
        result = total_sum

    if operation.lower() == "multiply":
        total_prod: int = 1
        for spell in spells:
            total_prod = operator.mul(total_prod, spell)
        result = total_prod

    if operation.lower() == "max":
        max_value: int = 0
        for spell in spells:
            if spell > max_value:
                max_value = spell
        result = max_value

    if operation.lower() == "min":
        min_value: int = MAX_INT
        for spell in spells:
            if spell < min_value:
                min_value = spell
        result = min_value
    return result


# set default values for some parameters and leave others open.
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    f_wind_50 = partial(base_enchantment, 50, 'wind')
    f_earth_50 = partial(base_enchantment, 50, 'earth')
    f_light_50 = partial(base_enchantment, 50, 'lightning')
    return {
            'power_wind': f_wind_50,
            'power_earth': f_earth_50,
            'power_light': f_light_50
            }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def func_spell(spell: Any) -> str:
        return "Unknown spell type"

    @func_spell.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @func_spell.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @func_spell.register
    def _(spell: list) -> str:
        return f"multi-cast: {len(spell)} spells"

    return func_spell


def main() -> None:

    print("\nTesting spell reducer...")
    spell_powers = [1, 2, 3, 4]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print("\nTesting memoized fibonacci...")
    for i in [0, 1, 10, 15]:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(50))
    print(spell("fire"))
    print(spell([1, 2, 3]))
    print(spell(3.14))

    print("\nTesting partial enchanter...")

    def storm(power: int, element: str, target: str) -> str:
        return f"Enchanment element {element} to {target} for {power} power "

    my_partial = partial_enchanter(storm)
    print(my_partial['power_wind']('Dragon'))


if __name__ == "__main__":
    main()
