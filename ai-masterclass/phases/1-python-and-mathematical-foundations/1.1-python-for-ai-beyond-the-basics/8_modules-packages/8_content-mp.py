"""
Modules & Packages - Topic File

Narrative sections converted to commented headers. All original runnable code is preserved exactly as in the source.
"""

# 1. Concept (What it is)
# Modules & Packages
# A module is a Python file (.py) containing code (functions, classes, variables).
# A package is a folder that groups related modules and may contain an __init__.py.

# 2. Why do we need modules?
# Splits large programs into focused files (data loading, cleaning, modeling, utils), improving maintainability.

# Mental model: a module is a toolbox (e.g., data_loader.py containing load_data(), read_csv(), ...)

# 3. Importing a Module (syntax highlights)
# import module
# from module import name
# import module as alias
# from package.module import name

# 4. Why use module.function()? It clarifies origin and prevents name conflicts.

# 5. from ... import ... allows direct use but can obscure origins if overused.

# 6. Import Aliases: Use import X as alias (e.g., import numpy as np) for readability in AI code.

# 7. Python's built-in modules (examples): math, random, datetime — available without pip.

# 8. Your own module example: text_utils.py with clean_text and word_count functions.

# 9. The __name__ variable & __main__ guard: use if __name__ == '__main__' for self-tests that shouldn't run on import.

# 10. Package structure: put related modules in folders and use __init__.py when needed.

# ----------------------
# Example code 
# ----------------------

# calculator.py example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

# Demonstrations using Python built-in modules
import math
import random
import datetime

print('\nExample: math module outputs ->')
print(math.sqrt(25))
print(math.pi)

print('\nExample: random module output ->')
number = random.randint(1, 10)
print(number)

print('\nExample: datetime module output ->')
today = datetime.datetime.now()
print(today)

# Your own module example: text_utils.py functions

def clean_text(text):
    return text.lower().strip()


def word_count(text):
    return len(text.split())

# Simulated main usage that uses text_utils
text = "  Hello AI World  "

cleaned = clean_text(text)

print(cleaned)
print(word_count(cleaned))

# __name__ variable demonstration
print('\n__name__ variable when running this file ->', __name__)

if __name__ == "__main__":
    print('\nRunning self-test: add(10,5) ->', add(10, 5))

# Package layout examples 
# project/
# ├── utils/
# │   ├── __init__.py
# #  │   ├── calculator.py
# #  │   └── text_utils.py
# #  └── main.py
# Importing from package example:
# from utils.calculator import add
# print(add(10, 20))

# Practical tips:
# - Use aliases for common libraries (np, pd, plt).
# - Keep modules focused on one responsibility.
# - Put example or test code under if __name__ == '__main__'.
