# light_spellbook.py
from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
    return ["air", "fire", "earth", "water", "wind"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"