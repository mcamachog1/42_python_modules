from alchemy.grimoire.dark_spellbook import dark_spell_record


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")

spell: str = dark_spell_record("Fantasy", "earth wind fire")
print(f"Testing record dark spell: {spell}")
