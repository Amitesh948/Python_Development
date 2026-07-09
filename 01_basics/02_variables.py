# ============================================================
# 📘 Lesson 2: Variables
# ============================================================
# A variable is like a labeled box where you store data.
# You give it a name, and put a value inside it.
# ============================================================

# --- Creating Variables ---
# Syntax: variable_name = value
name = "Amitesh"
age = 25
height = 5.6
is_student = True

# --- Printing Variables ---
print(name)        # Output: Amitesh
print(age)         # Output: 25
print(height)      # Output: 5.6
print(is_student)  # Output: True

# --- Using Variables with print() ---
print("Hello, my name is", name)
print("I am", age, "years old")

# --- f-strings (formatted strings) — the BEST way to print variables ---
# Put 'f' before the quotes, then use {variable_name} inside
print(f"Hello, my name is {name}")
print(f"I am {age} years old and {height} feet tall")

# --- Reassigning Variables ---
# You can change the value of a variable anytime
favorite_color = "Blue"
print(f"My favorite color is {favorite_color}")

favorite_color = "Green"  # Changed!
print(f"Actually, my favorite color is {favorite_color}")

# --- Variable Naming Rules ---
# ✅ VALID names:
my_name = "Amitesh"       # Use underscores for spaces
myName = "Amitesh"        # camelCase works too
name2 = "Amitesh"         # Numbers are OK (but not at the start)
_private = "secret"       # Can start with underscore

# ❌ INVALID names (these would cause errors — don't uncomment!):
# 2name = "Amitesh"       # ❌ Cannot start with a number
# my-name = "Amitesh"     # ❌ No hyphens allowed
# my name = "Amitesh"     # ❌ No spaces allowed
# class = "Python"        # ❌ 'class' is a reserved word

# --- Python Naming Convention ---
# In Python, we prefer snake_case (lowercase with underscores)
first_name = "Amitesh"    # ✅ Good (snake_case)
# firstName = "Amitesh"   # Works, but not the Python way

# --- Checking Variable Type ---
# type() tells you what kind of data a variable holds
print(type(name))        # <class 'str'>     (string)
print(type(age))         # <class 'int'>     (integer)
print(type(height))      # <class 'float'>   (decimal number)
print(type(is_student))  # <class 'bool'>    (boolean: True/False)

# --- Multiple Assignment ---
# Assign multiple variables in one line
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Assign same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Create variables for: your city, your favorite movie, your phone number
# 2. Print all of them using f-strings
# 3. Change one variable's value and print it before and after
# 4. Use type() to check what type each variable is
# 5. Create 3 variables in one line using multiple assignment
# ============================================================
