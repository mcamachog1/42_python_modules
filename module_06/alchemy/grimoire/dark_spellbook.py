# dark_spellbook.py
# from .dark_validator import validate_ingredients

from .dark_coordinator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"