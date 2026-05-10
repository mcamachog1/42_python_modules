import alchemy.grimoire as grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")

spell: str = grimoire.light_spell_record("Fantasy", "earth wind fire")
print(f"Testing record light spell: {spell}")
