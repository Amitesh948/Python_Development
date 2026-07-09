# ============================================================
# 📘 Lesson 3: Comparison & Logical Operators
# ============================================================
# Comparison operators COMPARE two values → return True or False
# Logical operators COMBINE multiple conditions
# ============================================================

# ============================================================
# 📗 Comparison Operators
# ============================================================
a = 10
b = 20

print("--- Comparison Operators ---")
print(f"{a} == {b}  → {a == b}")    # Equal to:              False
print(f"{a} != {b}  → {a != b}")    # Not equal to:          True
print(f"{a} > {b}   → {a > b}")     # Greater than:          False
print(f"{a} < {b}   → {a < b}")     # Less than:             True
print(f"{a} >= {b}  → {a >= b}")    # Greater than or equal: False
print(f"{a} <= {b}  → {a <= b}")    # Less than or equal:    True

# --- Comparing Strings ---
print("\n--- String Comparison ---")
print(f"'apple' == 'apple' → {'apple' == 'apple'}")   # True
print(f"'apple' == 'Apple' → {'apple' == 'Apple'}")   # False (case matters!)
print(f"'a' < 'b' → {'a' < 'b'}")                      # True (alphabetical order)

# ============================================================
# 📗 Logical Operators: and, or, not
# ============================================================
print("\n--- Logical Operators ---")

# 'and' → Both conditions must be True
age = 25
has_id = True
print(f"age >= 18 AND has_id → {age >= 18 and has_id}")  # True

# 'or' → At least ONE condition must be True
is_weekend = False
is_holiday = True
print(f"is_weekend OR is_holiday → {is_weekend or is_holiday}")  # True

# 'not' → Flips True to False, and False to True
is_raining = False
print(f"NOT is_raining → {not is_raining}")  # True

# ============================================================
# 📗 Combining Operators in if Statements
# ============================================================
print("\n--- Practical Examples ---")

# Example 1: AND — both must be true
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("✅ You qualify for the loan!")
else:
    print("❌ You don't qualify.")

# Example 2: OR — at least one must be true
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("🎉 It's the weekend!")
else:
    print("💼 It's a working day.")

# Example 3: NOT — inverting a condition
is_banned = False

if not is_banned:
    print("✅ You can access the website.")
else:
    print("🚫 You are banned!")

# Example 4: Combining all three
print("\n--- Movie Ticket Checker ---")
age = 15
has_parent = True
has_money = True

if has_money and (age >= 18 or has_parent):
    print("🎬 You can watch the movie!")
else:
    print("❌ Sorry, you can't watch this movie.")
# ↑ Parentheses matter! (age >= 18 or has_parent) is evaluated first

# ============================================================
# 📗 The 'in' Operator — Check if Something is Inside
# ============================================================
print("\n--- The 'in' Operator ---")

# Check if a character/word is in a string
sentence = "Python is amazing"
print(f"'Python' in sentence → {'Python' in sentence}")   # True
print(f"'Java' in sentence → {'Java' in sentence}")       # False

# Very useful with if statements!
favorite_fruits = "apple, banana, mango"
fruit = input("Enter a fruit: ")

if fruit.lower() in favorite_fruits:
    print(f"🎉 {fruit} is one of my favorites!")
else:
    print(f"🤔 {fruit} is not in my list, but I'll try it!")

# ============================================================
# 📗 Ternary Operator (One-Line if/else)
# ============================================================
print("\n--- One-Line if/else ---")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} → {status}")

# Same as writing:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# More examples:
number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")

temp = 35
weather = "Hot 🔥" if temp > 30 else "Cool 🌤️"
print(f"{temp}°C → {weather}")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Ask for a username and password. Check if BOTH are correct
#    (use: username == "admin" and password == "1234")
# 2. Ask for a year, check if it's a leap year:
#    A year is a leap year if:
#    (divisible by 4 AND not by 100) OR (divisible by 400)
# 3. Ask for 3 numbers, print the largest using if/elif/else
# 4. Use the ternary operator to check if a number is positive
# ============================================================
