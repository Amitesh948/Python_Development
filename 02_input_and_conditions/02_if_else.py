# ============================================================
# 📘 Lesson 2: If, Elif, Else — Making Decisions
# ============================================================
# Programs need to make decisions! if/elif/else lets Python
# choose different paths based on conditions.
# ============================================================

# --- Basic if Statement ---
# "If this condition is True, run this code"
age = 20

if age >= 18:
    print("You are an adult! ✅")
    # ↑ This line is INDENTED (4 spaces) — that's how Python
    #   knows it belongs inside the 'if'

# --- if / else ---
# "If True, do this. Otherwise, do that."
temperature = 35

if temperature > 30:
    print("🔥 It's hot outside! Stay hydrated!")
else:
    print("🌤️ The weather is nice!")

# --- if / elif / else ---
# "Check multiple conditions, one by one"
# elif = "else if" (another condition to check)
score = 75

print(f"\nYour score: {score}")
if score >= 90:
    print("Grade: A ⭐")
elif score >= 80:
    print("Grade: B 👍")
elif score >= 70:
    print("Grade: C 😊")
elif score >= 60:
    print("Grade: D 😐")
else:
    print("Grade: F ❌")

# --- How It Works ---
# Python checks conditions TOP to BOTTOM
# As soon as ONE condition is True, it runs that block and SKIPS the rest
# 'else' catches everything that didn't match any condition above

# ============================================================
# 📗 Indentation is CRUCIAL in Python!
# ============================================================
# Python uses indentation (spaces) to group code, not { } brackets
# Standard is 4 spaces per level

# ✅ CORRECT:
x = 10
if x > 5:
    print("x is big")     # 4 spaces indent
    print("really big")   # same 4 spaces = same block

# ❌ WRONG (would cause IndentationError):
# if x > 5:
# print("no indent!")     # Missing indentation = ERROR

# ============================================================
# 📗 Nested if Statements (if inside if)
# ============================================================
print("\n--- Nested If Example ---")
age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("And you have a license — you can drive! 🚗")
    else:
        print("But you need to get a license first! 📋")
else:
    print("You are too young to drive 🚫")

# ============================================================
# 📗 Real-World Example: Login Check
# ============================================================
print("\n--- Simple Login ---")
correct_password = "python123"

password = input("Enter password: ")

if password == correct_password:
    print("✅ Login successful! Welcome!")
else:
    print("❌ Wrong password! Try again.")

# ============================================================
# 📗 Truthy & Falsy Values
# ============================================================
# In Python, some values are considered "False" in if statements:
# False, 0, 0.0, "" (empty string), None, [] (empty list)
# Everything else is "True"

print("\n--- Truthy / Falsy ---")
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty!")  # This runs because "" is falsy

number = 0
if number:
    print(f"Number is {number}")
else:
    print("Number is zero or empty!")  # This runs because 0 is falsy

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Ask the user's age and tell them if they can vote (18+)
# 2. Ask for a number, print if it's positive, negative, or zero
# 3. Create a simple "even or odd" checker:
#    Hint: a number is even if number % 2 == 0
# 4. Ask for a temperature and suggest clothing:
#    > 30°C = "Wear light clothes"
#    20-30°C = "Wear a t-shirt"
#    10-20°C = "Wear a jacket"
#    < 10°C = "Wear a warm coat"
# ============================================================
