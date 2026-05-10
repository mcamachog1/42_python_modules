#!/usr/bin/env python3
# higher_magic.py


from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heals restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def water_blast(target: str, power: int) -> str:
    return f"Water Blast hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1: str = spell1(target, power)
        result2: str = spell2(target, power)
        # return a tuple
        return result1, result2
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        result: str = f"Original: {power}, Amplified: {power * multiplier}"
        return result
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def check_condition(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return 'Spell fizzled'
    return check_condition


def spell_sequence(spells: list[Callable]) -> Callable:
    def apply_spell(target: str, power: int) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return apply_spell


def main() -> None:

    print("Testing spell combiner...")

    # The function returned another function,
    # which was assigned to the variable.
    combo = spell_combiner(fireball, heal)
    # Function returned, store on the variable,
    # is expecting arguments for real execution
    print(
        f"Combined spell result: {combo('Dragon',50)[0]}, "
        f"{combo('Dragon',50)[1]}"
    )

    print("\nTesting power amplifier...")
    amplify = power_amplifier(fireball, 5)
    print(amplify("Bird", 10))

    print("\nTesting conditional caster...")

    # helper function
    def func_condition(target: str, power: int) -> bool:
        return power < 50

    condition = conditional_caster(func_condition, heal)
    print(f"right condition: {condition('Bird', 40)}")
    print(f"wrong condition: {condition('Dragon', 60)}")

    print("\nTesting spell sequence...")
    # spell list
    spells: list[Callable] = [heal, fireball, water_blast, condition]
    sequence = spell_sequence(spells)

    print(sequence("Dragon", 40))


if __name__ == "__main__":
    main()
