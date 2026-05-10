# potions.py


from alchemy.elements import create_earth, create_air
import elements


def healing_potion() -> str:
    earth: str = create_earth()
    air: str = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire: str = elements.create_fire()
    water: str = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"


# def invisibility_potion() -> str:
#     air: str = create_air()
#     water: str = create_water()
#     return f"Invisibility potion brewed with {air} and {water}"


# def wisdom_potion() -> str:
#     fire: str = create_fire()
#     earth: str = create_earth()
#     air: str = create_air()
#     water: str = create_water()
#     all: str = f"{fire} {water} {earth} {air}"
#     return f"Wisdom potion brewed with {all}"
