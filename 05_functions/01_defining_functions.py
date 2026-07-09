# ============================================================
# 📘 Lesson 1: Defining Functions
# ============================================================
# A function is a REUSABLE block of code that does a specific job.
# Instead of writing the same code again and again, put it in
# a function and CALL it whenever you need it.
#
# Syntax:
#   def function_name():
#       code here
# ============================================================

# --- Your First Function ---
def greet():
    """This function prints a greeting."""
    print("Hello! Welcome to Python! 🐍")

# IMPORTANT: Defining a function does NOT run it!
# You must CALL the function:
greet()       # Call it once
greet()       # Call it again — reusable!

# --- Function with Parameters ---
# Parameters let you pass data INTO a function
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}! Nice to meet you! 👋")

greet_person("Amitesh")
greet_person("Priya")
greet_person("Rahul")

# --- Multiple Parameters ---
def introduce(name, age, city):
    """Introduce a person with details."""
    print(f"  Hi! I'm {name}, {age} years old, from {city}.")

print("\n--- Introductions ---")
introduce("Amitesh", 25, "Pune")
introduce("Alice", 30, "Mumbai")

# --- Default Parameters ---
# You can give parameters a default value
def greet_with_style(name, greeting="Hello"):
    """Greet with a customizable greeting."""
    print(f"  {greeting}, {name}!")

print("\n--- Default Parameters ---")
greet_with_style("Amitesh")                    # Uses default: "Hello"
greet_with_style("Amitesh", "Good morning")    # Custom greeting
greet_with_style("Priya", "Namaste")

# --- Keyword Arguments ---
# You can specify arguments by name (order doesn't matter!)
def create_profile(name, age, job):
    print(f"  {name} | Age: {age} | Job: {job}")

print("\n--- Keyword Arguments ---")
create_profile("Amitesh", 25, "Developer")           # Positional
create_profile(job="Designer", name="Priya", age=23)  # Keyword (any order!)

# --- Docstrings ---
# The triple-quoted string right after def is called a docstring.
# It documents what the function does. Access it with help()
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area (length * width)
    """
    return length * width

print("\n--- Docstring ---")
help(calculate_area)  # Shows the docstring

# --- Functions Calling Other Functions ---
def get_full_name(first, last):
    return f"{first} {last}"

def formal_greeting(first, last):
    full = get_full_name(first, last)  # Call another function!
    print(f"  Good day, Mr./Ms. {full}!")

print("\n--- Functions Calling Functions ---")
formal_greeting("Amitesh", "Kumar")

# --- Practical: Menu Printer ---
def print_menu(title, options):
    """Print a formatted menu."""
    border = "═" * (len(title) + 8)
    print(f"\n╔{border}╗")
    print(f"║    {title}    ║")
    print(f"╠{border}╣")
    for i, option in enumerate(options, 1):
        padding = border[:-1]
        print(f"║  {i}. {option:<{len(border) - 5}} ║")
    print(f"╚{border}╝")

print_menu("MY APP", ["Start Game", "Settings", "Help", "Exit"])

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a function say_hello() that prints "Hello, World!"
# 2. Create a function with 2 parameters that prints their sum
# 3. Create a function with a default parameter for language
#    like: def code_message(name, lang="Python")
# 4. Create a function that prints a box around any text
# 5. Create 3 small functions that call each other
# ============================================================
