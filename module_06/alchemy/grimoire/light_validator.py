# light_validator.py


def validate_ingredients(ingredients: str) -> str:
    # Local import to avoid circular dependency
    from .light_spellbook import light_spell_allowed_ingredients

    ingredients_list = ingredients.split()
    for ingredient in ingredients_list:
        if ingredient.lower() not in light_spell_allowed_ingredients():
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"