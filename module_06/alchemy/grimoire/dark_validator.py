# dark_validator.py

# If there is no '.' before dark_spellbook,
# Python searches for a module with that name in the current location or in the Python path.
# The absence of a dot means it is treated as a top-level module or package,
# located at the project root or somewhere in the Python path.

# The '.' (dot) means: import the file from my current location
# alchemy/grimoire/dark_validator.py

# from .dark_spellbook import dark_spell_allowed_ingredients
from .dark_coordinator import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ingredients.split()
    for ingredient in ingredients_list:
        if ingredient.lower() not in dark_spell_allowed_ingredients():
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
