#!/usr/bin/env python3
#  decorator_mastery.py

from functools import wraps
from collections.abc import Callable
from typing import Any
from time import sleep
from time import perf_counter as take_time
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = take_time()
        result = func(*args, **kwargs)
        end: float = take_time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")
        return f"Result: {result}"
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args, **kwargs) -> Any:
            if power >= min_power:
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        count: int = 0

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal count
            while count < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    count += 1
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {count}/{max_attempts})"
                    )
            return (
                f"Spell casting failed after {max_attempts} attempts"
                f"\nWaaaaaaagh spelled !"
            )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        lower_name: str = name.lower()
        for c in lower_name:
            if (c < 'a' or c > 'z') and c != ' ':
                return False
        return True
    '''
        WITHOUT @power_validator
        return power_validator(10)(func_spell)(power, spell_name)

        WITH @power_validator
        return func_spell(power, spell_name)
        (return the wrap function, skip the decorator function)
    '''
    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def func_spell(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power "
        return func_spell(power, spell_name)


def main() -> None:

    # spell_timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    print(fireball())

    # retry_spell
    print("\nTesting retrying spell...")

    def random_error() -> str:
        flags: list[bool] = [
            True, True, True,
            False, False, False,
            False, False, False
        ]
        flag: bool = random.choice(flags)
        if not flag:
            raise ValueError
        else:
            return "function attempt succeeds"

    func_retry = retry_spell(3)
    print(func_retry(random_error)())

    # MageGuild
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(MageGuild.validate_mage_name("Phoenix"))
    print(MageGuild.validate_mage_name("Jo"))

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Earthquake", 8))

    # power_validator
    print("\nTesting power validator...")

    def attack(power: int, target: str) -> str:
        return f"Attack to {target} with {power} power"

    # I can change one condition for the function without
    # change the function itself
    attack_validator = power_validator(10)(attack)
    print(attack_validator(15, 'Dragon'))
    print(attack_validator(5, 'Goblin'))


if __name__ == "__main__":
    main()
