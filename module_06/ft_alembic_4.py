# Importing a module (package) does not require the name of the .py file where the function is defined.
# You can call the function directly using the PACKAGE NAME followed by the function name,
# as long as the function is EXPOSED in the package's __init__.py.
# In the __init__.py you will need to make an explicit import of the function and add it to the __all__ list.

import alchemy


print("=== Alembic 4 ===")
print("Accesing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print(
    "Now show that not all functions can be reached"
    "\nThis will raise an exception!"
)
print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
