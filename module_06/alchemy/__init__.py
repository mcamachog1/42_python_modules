__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_air
from .potions import strength_potion
from .potions import healing_potion as heal

# from .transmutation.recipes import lead_to_gold

# Since lead_to_gold is exposed in the 'transmutation' __init__.py,
# we can import it directly from 'transmutation' package
# without explicitly referencing the recipes.py file.

from .transmutation import lead_to_gold

__all__ = ["create_air", "heal", "strength_potion"]