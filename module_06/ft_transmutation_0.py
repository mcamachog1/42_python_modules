import alchemy.transmutation.recipes


print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")

lead_to_gold: str = alchemy.transmutation.recipes.lead_to_gold()
print(f"Testing lead to gold: {lead_to_gold}")