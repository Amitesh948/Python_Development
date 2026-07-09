# ============================================================
# 📘 Lesson 1: For Loops
# ============================================================
# A for loop repeats code FOR EACH item in a sequence.
# Think: "Do this for every item in the list"
# ============================================================

# --- Basic For Loop ---
# Looping through a string (character by character)
print("--- Looping through a string ---")
name = "Amitesh"
for letter in name:
    print(letter)
# Prints: A, m, i, t, e, s, h (each on a new line)

# --- For Loop with a List ---
print("\n--- Looping through a list ---")
fruits = ["apple", "banana", "mango", "grape"]
for fruit in fruits:
    print(f"I like {fruit}!")

# --- The range() Function ---
# range() generates a sequence of numbers
# range(stop)           → 0 to stop-1
# range(start, stop)    → start to stop-1
# range(start, stop, step) → start to stop-1, jumping by step

print("\n--- range(5) → 0 to 4 ---")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # new line

print("\n--- range(1, 6) → 1 to 5 ---")
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

print("\n--- range(0, 20, 5) → 0 to 19, step 5 ---")
for i in range(0, 20, 5):
    print(i, end=" ")  # 0 5 10 15
print()

print("\n--- range(10, 0, -1) → Countdown! ---")
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
print("\n🚀 Liftoff!")

# ============================================================
# 📗 Practical Examples
# ============================================================

# --- Sum of numbers 1 to 10 ---
print("\n--- Sum of 1 to 10 ---")
total = 0
for num in range(1, 11):
    total += num  # same as: total = total + num
print(f"Sum of 1 to 10 = {total}")  # 55

# --- Multiplication Table ---
print("\n--- Multiplication Table of 7 ---")
number = 7
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i:2d} = {result}")

# --- Looping with index using enumerate() ---
print("\n--- enumerate() gives you index + value ---")
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# Starting index from 1 instead of 0
print("\n--- enumerate with start=1 ---")
for rank, color in enumerate(colors, start=1):
    print(f"  Rank {rank}: {color}")

# --- Pattern Printing ---
print("\n--- Triangle Pattern ---")
for i in range(1, 6):
    print("⭐" * i)
# ⭐
# ⭐⭐
# ⭐⭐⭐
# ⭐⭐⭐⭐
# ⭐⭐⭐⭐⭐

# --- Right-aligned Triangle ---
print("\n--- Right-aligned Triangle ---")
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "⭐" * i
    print(f"{spaces}{stars}")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Print numbers from 1 to 20
# 2. Print all even numbers from 2 to 50
#    Hint: range(2, 51, 2)
# 3. Print the multiplication table of any number
# 4. Calculate the sum of all odd numbers from 1 to 100
# 5. Print this pattern:
#    *****
#    ****
#    ***
#    **
#    *
# ============================================================
