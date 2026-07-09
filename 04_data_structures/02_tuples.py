# ============================================================
# 📘 Lesson 2: Tuples
# ============================================================
# A tuple is like a list, but it CANNOT be changed (immutable).
# Created with parentheses: ( )
# Use tuples when data should NOT be modified.
# ============================================================

# --- Creating Tuples ---
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)           # ← Comma needed for single-item tuple!
not_a_tuple = (42)            # This is just the number 42, NOT a tuple
empty_tuple = ()

print("--- Tuples ---")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single item tuple: {single_item}, type: {type(single_item).__name__}")
print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple).__name__}")

# ============================================================
# 📗 Accessing Items (same as lists)
# ============================================================
print("\n--- Accessing ---")
fruits = ("apple", "banana", "mango", "grape", "kiwi")
print(f"First:  {fruits[0]}")
print(f"Last:   {fruits[-1]}")
print(f"Slice:  {fruits[1:3]}")  # ('banana', 'mango')
print(f"Length: {len(fruits)}")

# ============================================================
# 📗 Tuples are IMMUTABLE (Cannot Change!)
# ============================================================
# fruits[0] = "orange"  # ❌ TypeError! Cannot modify a tuple!
# fruits.append("pear") # ❌ No append! Tuples don't have it.
# del fruits[0]          # ❌ Cannot delete items!

# But you CAN reassign the whole variable:
my_tuple = (1, 2, 3)
my_tuple = (4, 5, 6)    # ✅ This creates a NEW tuple
print(f"\nReassigned tuple: {my_tuple}")

# ============================================================
# 📗 Tuple Packing & Unpacking
# ============================================================
print("\n--- Packing & Unpacking ---")

# Packing: putting values into a tuple
person = ("Amitesh", 25, "Developer")  # Packing

# Unpacking: extracting values into variables
name, age, job = person  # Unpacking
print(f"Name: {name}, Age: {age}, Job: {job}")

# Unpacking with * (star) — catch the rest
scores = (95, 87, 92, 78, 88)
first, second, *rest = scores
print(f"First: {first}, Second: {second}, Rest: {rest}")

# Swapping variables using tuple unpacking!
a = 10
b = 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a  # Tuple magic!
print(f"After swap:  a={a}, b={b}")

# ============================================================
# 📗 Tuple Methods & Operations
# ============================================================
print("\n--- Methods ---")
numbers = (1, 3, 5, 3, 7, 3, 9)
print(f"Count of 3: {numbers.count(3)}")   # 3
print(f"Index of 5: {numbers.index(5)}")   # 2

print(f"\n3 in tuple? {3 in numbers}")      # True
print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}")

# Concatenate tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(f"Combined: {combined}")   # (1, 2, 3, 4)

# Repeat
repeated = (0,) * 5
print(f"Repeated: {repeated}")  # (0, 0, 0, 0, 0)

# ============================================================
# 📗 When to Use Tuple vs List?
# ============================================================
# TUPLE (immutable):
#   ✅ Data that shouldn't change (coordinates, dates, RGB colors)
#   ✅ Dictionary keys (lists can't be dict keys!)
#   ✅ Function return values
#   ✅ Slightly faster than lists
#
# LIST (mutable):
#   ✅ Data that needs to change (shopping list, scores)
#   ✅ When you need append, remove, sort

# --- Practical: Function returning multiple values ---
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple!

data = [45, 12, 89, 3, 67]
minimum, maximum = get_min_max(data)
print(f"\nMin: {minimum}, Max: {maximum}")

# --- Converting between list and tuple ---
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # List → Tuple
back_to_list = list(my_tuple)  # Tuple → List
print(f"Tuple: {my_tuple}, List: {back_to_list}")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a tuple with 5 of your favorite movies
# 2. Unpack a tuple (name, age, city) into 3 variables
# 3. Try to modify a tuple — see the error message
# 4. Use tuple unpacking to swap two variables
# 5. Create a function that returns (sum, average) of a list
# ============================================================
