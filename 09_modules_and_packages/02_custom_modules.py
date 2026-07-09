# ============================================================
# 📘 Lesson 2: Custom Modules & Packages
# ============================================================
# You can split your code across multiple files and IMPORT
# your own code just like built-in modules!
#
# Key concepts:
#   A MODULE  = a single .py file you can import
#   A PACKAGE = a folder with __init__.py containing modules
#   if __name__ == "__main__"  = run-only-when-executed guard
# ============================================================

# ============================================================
# 📗 Importing Our Custom Module
# ============================================================
# We created my_utils.py in this same folder. Let's use it!

print("--- Importing Custom Module ---\n")

# Style 1: Import the whole module
import my_utils

print(my_utils.greet("Amitesh"))
print(f"  Version: {my_utils.VERSION}")
print(f"  Author:  {my_utils.AUTHOR}")

# Style 2: Import specific items
from my_utils import add, multiply, is_even, format_currency

print(f"\n  add(10, 5)     = {add(10, 5)}")
print(f"  multiply(4, 7) = {multiply(4, 7)}")
print(f"  is_even(42)    = {is_even(42)}")
print(f"  format_currency(85000) = {format_currency(85000)}")

# Style 3: Import classes
from my_utils import MathHelper, TextHelper

print(f"\n  factorial(5) = {MathHelper.factorial(5)}")
print(f"  is_prime(17) = {MathHelper.is_prime(17)}")
print(f"  fibonacci(8) = {MathHelper.fibonacci(8)}")

print(f"\n  title_case('hello world') = {TextHelper.title_case('hello world')}")
print(f"  snake_case('Hello World') = {TextHelper.snake_case('Hello World')}")

# Style 4: Import with alias
import my_utils as utils
print(f"\n  Alias: {utils.reverse_string('Python')}")

# ============================================================
# 📗 if __name__ == "__main__" — Explained!
# ============================================================
# When Python runs a file directly, it sets __name__ = "__main__"
# When a file is IMPORTED, __name__ = the module's name
#
# This lets you write code that runs ONLY when the file is
# executed directly, not when imported.

print("\n--- __name__ Demo ---\n")

# When WE run this file: __name__ == "__main__"
print(f"  This file's __name__:    {__name__}")

# When we IMPORTED my_utils: its __name__ was "my_utils"
print(f"  my_utils's __name__:     {my_utils.__name__}")

# That's why my_utils's test code at the bottom didn't run
# when we imported it — the if __name__ == "__main__" guard
# prevented it!

# ============================================================
# 📗 Module Search Path
# ============================================================
# When you write "import something", Python searches:
#   1. Current directory
#   2. PYTHONPATH environment variable
#   3. Standard library directories
#   4. site-packages (pip-installed packages)

print("\n--- Module Search Path ---\n")

import sys

print("  Python looks for modules in:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"    {i}. {path}")
if len(sys.path) > 5:
    print(f"    ... and {len(sys.path) - 5} more paths")

# ============================================================
# 📗 Creating a Package (Folder of Modules)
# ============================================================
# A PACKAGE is a folder containing:
#   my_package/
#   ├── __init__.py    ← Makes it a package (can be empty)
#   ├── math_tools.py
#   ├── text_tools.py
#   └── data_tools.py
#
# Then you can import like:
#   from my_package import math_tools
#   from my_package.text_tools import clean_text

# Let's create a mini package right here!
print("\n--- Creating a Package ---\n")

import os

pkg_dir = "my_package"
os.makedirs(pkg_dir, exist_ok=True)

# __init__.py — makes the folder a package
with open(f"{pkg_dir}/__init__.py", "w") as f:
    f.write('"""my_package — A demo package."""\n\n')
    f.write('PACKAGE_VERSION = "1.0.0"\n')

# math_tools.py — a module inside the package
with open(f"{pkg_dir}/math_tools.py", "w") as f:
    f.write('"""Math utility functions."""\n\n')
    f.write('def square(n):\n')
    f.write('    """Return n squared."""\n')
    f.write('    return n ** 2\n\n')
    f.write('def cube(n):\n')
    f.write('    """Return n cubed."""\n')
    f.write('    return n ** 3\n\n')
    f.write('def average(numbers):\n')
    f.write('    """Return the average of a list."""\n')
    f.write('    return sum(numbers) / len(numbers) if numbers else 0\n')

# text_tools.py — another module
with open(f"{pkg_dir}/text_tools.py", "w") as f:
    f.write('"""Text utility functions."""\n\n')
    f.write('def shout(text):\n')
    f.write('    """Return text in uppercase with !!!."""\n')
    f.write('    return text.upper() + "!!!"\n\n')
    f.write('def whisper(text):\n')
    f.write('    """Return text in lowercase with ...."""\n')
    f.write('    return text.lower() + "..."\n\n')
    f.write('def char_count(text):\n')
    f.write('    """Count characters excluding spaces."""\n')
    f.write('    return len(text.replace(" ", ""))\n')

print("  ✅ Created my_package/ with:")
print("     ├── __init__.py")
print("     ├── math_tools.py")
print("     └── text_tools.py")

# Now import from the package!
# NOTE: The linter may warn these imports can't be found — that's
# because my_package/ is created AT RUNTIME above. It works fine!
from my_package import math_tools  # type: ignore
from my_package.text_tools import shout, whisper  # type: ignore
from my_package import PACKAGE_VERSION  # type: ignore

print(f"\n  Package version: {PACKAGE_VERSION}")
print(f"  square(7)   = {math_tools.square(7)}")
print(f"  cube(3)     = {math_tools.cube(3)}")
print(f"  average([4,8,6]) = {math_tools.average([4, 8, 6])}")
print(f"  shout('hello')   = {shout('hello')}")
print(f"  whisper('HELLO') = {whisper('HELLO')}")

# ============================================================
# 📗 Module Inspection Tools
# ============================================================
print("\n--- Module Inspection ---\n")

# dir() — list everything in a module
items = [x for x in dir(my_utils) if not x.startswith("_")]
print(f"  my_utils contains {len(items)} public items:")
print(f"  {items}\n")

# __doc__ — module docstring
print(f"  my_utils.__doc__: {my_utils.__doc__.strip()}")

# __file__ — where the module lives
print(f"  my_utils.__file__: {my_utils.__file__}")

# ============================================================
# 📗 Reloading Modules (During Development)
# ============================================================
print("\n--- Reloading Modules ---\n")

# If you change a module while your program is running,
# you need to RELOAD it to pick up changes.
import importlib

importlib.reload(my_utils)
print("  ✅ my_utils reloaded (picks up any file changes)")

# ============================================================
# 📗 Practical: Module Best Practices
# ============================================================
print("\n--- Module Best Practices ---\n")

best_practices = [
    "1. One module = one responsibility (don't dump everything in one file)",
    "2. Use descriptive module names (math_utils.py, not mu.py)",
    "3. Always add docstrings to modules, functions, and classes",
    "4. Use if __name__ == '__main__' to protect test/demo code",
    "5. Keep imports at the top of the file",
    "6. Group imports: stdlib → third-party → your own modules",
    "7. Avoid 'from module import *' — be explicit!",
    "8. Use __init__.py to control what a package exports",
]

for practice in best_practices:
    print(f"  ✅ {practice}")

# ============================================================
# 🧹 Cleanup
# ============================================================
import shutil
if os.path.exists(pkg_dir):
    shutil.rmtree(pkg_dir)
print("\n🧹 Cleaned up my_package/")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a module called string_utils.py with 3 functions
#    and import them in another file
# 2. Create a package called "tools" with two modules inside
# 3. Write a module with functions AND test code using
#    if __name__ == "__main__"
# 4. Create a module with a class and import it elsewhere
# 5. Explore the 'os' module with dir(os) — find 3 functions
#    you haven't used yet and try them
# ============================================================
