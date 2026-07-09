# ============================================================
# 📘 Lesson 4: Sets
# ============================================================
# A set is an UNORDERED collection of UNIQUE items.
# No duplicates! No indexing! Created with { }
# ============================================================

# --- Creating Sets ---
fruits = {"apple", "banana", "mango"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # NOT {} — that creates an empty dict!

print("--- Sets ---")
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")

# --- Sets Remove Duplicates Automatically! ---
print("\n--- No Duplicates ---")
with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique = set(with_dupes)
print(f"List: {with_dupes} → Set: {unique}")

# --- Adding & Removing ---
print("\n--- Modifying ---")
colors = {"red", "blue", "green"}
colors.add("yellow")
print(f"After add: {colors}")
colors.discard("blue")  # Safe remove (no error if missing)
print(f"After discard: {colors}")

# --- Set Operations ---
print("\n--- Set Operations ---")
python_devs = {"Amitesh", "Alice", "Bob"}
java_devs = {"Bob", "David", "Alice"}

print(f"Union (all):         {python_devs | java_devs}")
print(f"Intersection (both): {python_devs & java_devs}")
print(f"Only Python:         {python_devs - java_devs}")
print(f"Exclusive:           {python_devs ^ java_devs}")

# --- Membership Check ---
print(f"\n'Amitesh' in set? {'Amitesh' in python_devs}")

# --- Comparison Table ---
print("\n" + "=" * 55)
print(f"{'Feature':<15} {'List':^10} {'Tuple':^10} {'Set':^10} {'Dict':^10}")
print("=" * 55)
print(f"{'Syntax':<15} {'[ ]':^10} {'( )':^10} {'{ }':^10} {'{k:v}':^10}")
print(f"{'Ordered':<15} {'Yes':^10} {'Yes':^10} {'No':^10} {'Yes':^10}")
print(f"{'Mutable':<15} {'Yes':^10} {'No':^10} {'Yes':^10} {'Yes':^10}")
print(f"{'Duplicates':<15} {'Yes':^10} {'Yes':^10} {'No':^10} {'No':^10}")
print("=" * 55)

# ============================================================
# 🏋️ PRACTICE:
# 1. Remove duplicates from [1,1,2,2,3,3] using set
# 2. Find common hobbies between two sets
# 3. Check if {1,2} is a subset of {1,2,3,4}
# ============================================================
