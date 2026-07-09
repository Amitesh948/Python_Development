# ============================================================
# 📘 Lesson 3: Scope — Where Variables Live
# ============================================================
# "Scope" = where a variable can be accessed from.
# Understanding scope prevents confusing bugs!
# ============================================================

# ============================================================
# 📗 Local Scope — Variables INSIDE a Function
# ============================================================
print("--- Local Scope ---")

def my_function():
    secret = "I only exist inside this function!"  # LOCAL variable
    print(f"  Inside function: {secret}")

my_function()
# print(secret)  # ❌ NameError! 'secret' doesn't exist out here!

# ============================================================
# 📗 Global Scope — Variables OUTSIDE all Functions
# ============================================================
print("\n--- Global Scope ---")

name = "Amitesh"  # GLOBAL variable — accessible everywhere

def say_hello():
    print(f"  Hello, {name}!")  # ✅ Can READ global variables

say_hello()
print(f"  Global name: {name}")

# ============================================================
# 📗 The Name Conflict Problem
# ============================================================
print("\n--- Name Conflict ---")

color = "Blue"  # Global

def change_color():
    color = "Red"  # This creates a NEW local variable, doesn't change global!
    print(f"  Inside function: {color}")  # Red

change_color()
print(f"  Outside function: {color}")  # Still Blue!

# ============================================================
# 📗 The global Keyword — Modify Global from Inside Function
# ============================================================
print("\n--- global keyword ---")

score = 100  # Global

def add_points():
    global score        # Tell Python: I mean the GLOBAL score
    score += 50         # Now this modifies the global variable
    print(f"  Inside: score = {score}")

print(f"  Before: score = {score}")
add_points()
print(f"  After: score = {score}")  # 150 — it changed!

# ⚠️ WARNING: Using 'global' too much is bad practice!
# Better approach: pass as parameter and return new value

def add_points_better(current_score, bonus):
    """Better approach — no global needed."""
    return current_score + bonus

score2 = 100
score2 = add_points_better(score2, 50)
print(f"\n  Better approach: score = {score2}")  # 150

# ============================================================
# 📗 Nested Functions & Enclosing Scope
# ============================================================
print("\n--- Nested Functions ---")

def outer():
    message = "I'm from outer!"  # Enclosing scope
    
    def inner():
        print(f"  Inner says: {message}")  # Can access outer's variables
    
    inner()

outer()

# --- nonlocal keyword (modify enclosing scope) ---
def counter():
    count = 0  # Enclosing scope
    
    def increment():
        nonlocal count   # Modify the enclosing variable
        count += 1
        return count
    
    print(f"  Count: {increment()}")  # 1
    print(f"  Count: {increment()}")  # 2
    print(f"  Count: {increment()}")  # 3

print("\n--- nonlocal keyword ---")
counter()

# ============================================================
# 📗 LEGB Rule — How Python Searches for Variables
# ============================================================
# When you use a variable, Python searches in this order:
#
#   L - Local      → Inside the current function
#   E - Enclosing  → Inside any enclosing function (nested)
#   G - Global     → At the module/file level
#   B - Built-in   → Python's built-in names (print, len, etc.)
#
# Python uses the FIRST match it finds!

print("\n--- LEGB Rule Demo ---")

x = "Global x"

def outer_func():
    x = "Enclosing x"
    
    def inner_func():
        x = "Local x"
        print(f"  Inner sees: {x}")    # Local x
    
    inner_func()
    print(f"  Outer sees: {x}")        # Enclosing x

outer_func()
print(f"  Module sees: {x}")           # Global x

# ============================================================
# 📗 Practical: Score Tracker (Good vs Bad Design)
# ============================================================
print("\n--- Practical: Score Tracker ---")

# ❌ BAD: Using global variables
total_bad = 0
def add_score_bad(points):
    global total_bad
    total_bad += points

# ✅ GOOD: Using parameters and return values
def create_tracker():
    """Create a score tracker using a list (mutable object)."""
    scores = []
    
    def add(name, points):
        scores.append({"name": name, "points": points})
        print(f"  Added: {name} +{points}")
    
    def get_total():
        return sum(s["points"] for s in scores)
    
    def show():
        print(f"\n  📊 Scoreboard ({len(scores)} entries):")
        for s in scores:
            print(f"    {s['name']}: {s['points']}")
        print(f"    Total: {get_total()}")
    
    return add, get_total, show  # Return the functions!

add_score, get_total, show_scores = create_tracker()
add_score("Round 1", 100)
add_score("Round 2", 85)
add_score("Bonus", 50)
show_scores()

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a local and global variable with the same name,
#    print both to see the difference
# 2. Write a function that modifies a global list (append to it)
# 3. Rewrite #2 WITHOUT using global — use parameter + return
# 4. Create a nested function where inner reads outer's variable
# 5. Explain what LEGB stands for (write it in a comment!)
# ============================================================
