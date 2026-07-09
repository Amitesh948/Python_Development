# ============================================================
# 📘 Lesson 1: Lists
# ============================================================
# A list is an ORDERED collection of items.
# Lists can hold any type and can be CHANGED (mutable).
# Created with square brackets: [ ]
# ============================================================

# --- Creating Lists ---
fruits = ["apple", "banana", "mango", "grape"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Amitesh", 25, True, 3.14]  # Can mix types!
empty = []  # Empty list

print("--- Lists ---")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty: {empty}")
print(f"Length of fruits: {len(fruits)}")

# ============================================================
# 📗 Accessing Items (Indexing)
# ============================================================
#         0        1        2       3
# fruits = ["apple", "banana", "mango", "grape"]
#        -4       -3       -2      -1

print("\n--- Indexing ---")
print(f"First fruit:  {fruits[0]}")    # apple
print(f"Second fruit: {fruits[1]}")    # banana
print(f"Last fruit:   {fruits[-1]}")   # grape
print(f"Second last:  {fruits[-2]}")   # mango

# --- Slicing ---
print(f"First two:    {fruits[0:2]}")  # ['apple', 'banana']
print(f"Last two:     {fruits[-2:]}")  # ['mango', 'grape']
print(f"Middle:       {fruits[1:3]}")  # ['banana', 'mango']

# ============================================================
# 📗 Modifying Lists
# ============================================================
print("\n--- Modifying Lists ---")
colors = ["red", "green", "blue"]
print(f"Original: {colors}")

# Change an item
colors[1] = "yellow"
print(f"After change: {colors}")

# Add items
colors.append("purple")          # Add to END
print(f"After append: {colors}")

colors.insert(1, "orange")       # Insert at specific position
print(f"After insert: {colors}")

# Remove items
colors.remove("blue")            # Remove by VALUE
print(f"After remove: {colors}")

popped = colors.pop()             # Remove & return LAST item
print(f"Popped: {popped}, List: {colors}")

popped2 = colors.pop(0)          # Remove & return item at index 0
print(f"Popped index 0: {popped2}, List: {colors}")

del colors[0]                    # Delete by index
print(f"After del: {colors}")

# ============================================================
# 📗 List Methods
# ============================================================
print("\n--- List Methods ---")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {nums}")

nums.sort()                      # Sort ascending (changes the list)
print(f"Sorted:   {nums}")

nums.sort(reverse=True)          # Sort descending
print(f"Reversed: {nums}")

nums.reverse()                   # Reverse the order
print(f"Reverse:  {nums}")

print(f"Count of 1: {nums.count(1)}")   # How many times 1 appears
print(f"Index of 5: {nums.index(5)}")   # Position of first 5

# Extend — add another list's items
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"Extended: {list1}")  # [1, 2, 3, 4, 5, 6]

# Copy a list
original = [1, 2, 3]
copy = original.copy()   # or: copy = original[:]
copy.append(4)
print(f"Original: {original}")  # [1, 2, 3] — unchanged!
print(f"Copy:     {copy}")      # [1, 2, 3, 4]

# ============================================================
# 📗 Looping Through Lists
# ============================================================
print("\n--- Looping ---")
animals = ["cat", "dog", "bird", "fish"]

# Method 1: Direct
for animal in animals:
    print(f"  I have a {animal}")

# Method 2: With index using enumerate
print()
for i, animal in enumerate(animals, start=1):
    print(f"  {i}. {animal}")

# ============================================================
# 📗 List Comprehension (Creating Lists in One Line)
# ============================================================
print("\n--- List Comprehension ---")

# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"Squares (loop):         {squares}")

# List comprehension — same result, one line!
squares2 = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares2}")

# With condition
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {evens}")

# Transform items
names = ["amitesh", "alice", "bob"]
capitalized = [name.capitalize() for name in names]
print(f"Capitalized: {capitalized}")

# ============================================================
# 📗 Useful Operations
# ============================================================
print("\n--- Useful Operations ---")
numbers = [10, 25, 3, 47, 8, 32]
print(f"List: {numbers}")
print(f"Min:  {min(numbers)}")    # 3
print(f"Max:  {max(numbers)}")    # 47
print(f"Sum:  {sum(numbers)}")    # 125
print(f"Avg:  {sum(numbers) / len(numbers):.1f}")  # 20.8

# Check if item exists
print(f"25 in list? {25 in numbers}")      # True
print(f"99 in list? {99 in numbers}")      # False

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a list of 5 cities, print the first and last
# 2. Add a city, remove a city, sort the list
# 3. Use list comprehension to create cubes of 1-10
# 4. Find the largest and smallest in [45, 12, 89, 3, 67]
# 5. Create a list of words, filter only words with length > 4
# ============================================================
