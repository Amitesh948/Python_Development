# ============================================================
# 📘 Lesson 3: Loop Control — break, continue, else, nested
# ============================================================
# These keywords give you more control over how loops behave.
# ============================================================

# ============================================================
# 📗 break — Exit the Loop Immediately
# ============================================================
print("--- break: Stop the loop early ---")

# Find the first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break  # Stop! Don't check the rest

# Search for a name in a list
print("\n--- Searching a list ---")
students = ["Alice", "Bob", "Amitesh", "David", "Eve"]
search = "Amitesh"

for student in students:
    print(f"  Checking: {student}")
    if student == search:
        print(f"  ✅ Found {search}!")
        break
else:
    # This 'else' runs only if the loop completed WITHOUT break
    print(f"  ❌ {search} not found!")

# ============================================================
# 📗 continue — Skip to the Next Iteration
# ============================================================
print("\n--- continue: Skip this one, go to next ---")

# Print only odd numbers (skip even ones)
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip this iteration, go to next number
    print(i, end=" ")  # Only odd numbers: 1 3 5 7 9
print()

# Skip a specific item
print("\n--- Skip 'banana' ---")
fruits = ["apple", "banana", "mango", "grape"]
for fruit in fruits:
    if fruit == "banana":
        continue  # Skip banana
    print(f"  I like {fruit}")

# ============================================================
# 📗 for/while...else — Loop with Else Block
# ============================================================
print("\n--- Loop else: runs when loop finishes normally ---")

# 'else' after a loop runs ONLY if the loop completed
# without hitting a 'break'

# Example: Check if a number is prime
number = 17
print(f"Is {number} prime?")

for i in range(2, number):
    if number % i == 0:
        print(f"  No! {number} is divisible by {i}")
        break
else:
    # This runs only if no 'break' happened = number is prime
    print(f"  Yes! {number} is a prime number! ✅")

# ============================================================
# 📗 Nested Loops (Loop Inside a Loop)
# ============================================================
print("\n--- Nested Loops ---")

# Simple: Print a grid
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end="  ")
    print()  # New line after each row

# --- Pattern: Rectangle ---
print("\n--- Rectangle ---")
for row in range(3):
    for col in range(5):
        print("■", end=" ")
    print()

# --- Pattern: Right Triangle ---
print("\n--- Right Triangle ---")
for i in range(1, 6):
    for j in range(i):
        print("★", end=" ")
    print()

# --- Pattern: Number Pyramid ---
print("\n--- Number Pyramid ---")
for i in range(1, 6):
    # Print spaces for alignment
    print("  " * (5 - i), end="")
    # Print numbers
    for j in range(1, i + 1):
        print(f" {j}", end="")
    # Print numbers in reverse
    for j in range(i - 1, 0, -1):
        print(f" {j}", end="")
    print()

# ============================================================
# 📗 Practical: Times Table Grid
# ============================================================
print("\n--- Multiplication Table (1-5) ---")
print("     ", end="")
for i in range(1, 6):
    print(f"{i:4d}", end="")
print()
print("    " + "─" * 20)

for i in range(1, 6):
    print(f" {i}  │", end="")
    for j in range(1, 6):
        print(f"{i*j:4d}", end="")
    print()

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Loop 1-20, print numbers but skip multiples of 3 (use continue)
# 2. Find the first number between 100-200 divisible by 13 (use break)
# 3. Print this pattern using nested loops:
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5
# 4. Check if a number (e.g., 29) is prime using for...else
# 5. Print a 10x10 multiplication table
# ============================================================
