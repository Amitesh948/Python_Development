# ============================================================
# 📘 Lesson 2: Parameters, Return Values & Advanced Functions
# ============================================================
# Functions can RETURN data back to the caller using 'return'.
# This is what makes functions truly powerful!
# ============================================================

# ============================================================
# 📗 The return Statement
# ============================================================

# --- Without return (just prints, doesn't give back data) ---
def add_and_print(a, b):
    print(f"  {a} + {b} = {a + b}")

# --- With return (gives back the result) ---
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

print("--- return vs print ---")
add_and_print(5, 3)     # Prints inside, but you can't save the result

result = add(5, 3)       # Returns 8, which we save in 'result'
print(f"  Result saved: {result}")
print(f"  Double it: {result * 2}")  # We can USE the returned value!

# --- return Stops the Function ---
def check_age(age):
    if age < 0:
        return "Invalid age!"      # Function stops here if age < 0
    if age >= 18:
        return "Adult ✅"
    return "Minor 🔒"              # Only reaches here if age >= 0 and < 18

print(f"\n  Age 25: {check_age(25)}")
print(f"  Age 10: {check_age(10)}")
print(f"  Age -5: {check_age(-5)}")

# --- Returning Multiple Values (as a tuple) ---
def get_stats(numbers):
    """Return min, max, and average of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [45, 12, 89, 3, 67, 34]
minimum, maximum, average = get_stats(data)
print(f"\n  Stats of {data}:")
print(f"  Min: {minimum}, Max: {maximum}, Avg: {average:.1f}")

# ============================================================
# 📗 *args — Accept ANY Number of Arguments
# ============================================================
print("\n--- *args ---")

def add_all(*numbers):
    """Add any number of arguments together."""
    print(f"  Received: {numbers}")  # It's a tuple!
    return sum(numbers)

print(f"  Sum: {add_all(1, 2, 3)}")
print(f"  Sum: {add_all(10, 20, 30, 40, 50)}")

# Practical: flexible greeting
def invite(*names):
    print(f"  Inviting {len(names)} people:")
    for name in names:
        print(f"    → {name}")

invite("Amitesh", "Priya", "Rahul", "Alice")

# ============================================================
# 📗 **kwargs — Accept ANY Number of Keyword Arguments
# ============================================================
print("\n--- **kwargs ---")

def build_profile(**info):
    """Build a profile from any keyword arguments."""
    print("  Profile:")
    for key, value in info.items():
        print(f"    {key}: {value}")

build_profile(name="Amitesh", age=25, city="Pune", job="Developer")
print()
build_profile(name="Priya", hobby="Reading")

# ============================================================
# 📗 Lambda Functions (One-Line Mini Functions)
# ============================================================
print("\n--- Lambda Functions ---")

# Normal function:
def square(x):
    return x ** 2

# Same thing as a lambda:
square_lambda = lambda x: x ** 2

print(f"  square(5) = {square(5)}")
print(f"  lambda(5) = {square_lambda(5)}")

# Useful with sort, map, filter
students = [("Amitesh", 85), ("Priya", 92), ("Rahul", 78)]
students.sort(key=lambda s: s[1], reverse=True)  # Sort by score
print(f"\n  Sorted by score: {students}")

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"  Doubled: {doubled}")

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(f"  Evens: {evens}")

# ============================================================
# 📗 Practical: Grade Calculator
# ============================================================
print("\n--- Grade Calculator ---")

def calculate_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90: return "A ⭐"
    elif score >= 80: return "B 👍"
    elif score >= 70: return "C 😊"
    elif score >= 60: return "D 😐"
    else: return "F ❌"

def report_card(name, **subjects):
    """Generate a report card for a student."""
    print(f"\n  📋 Report Card: {name}")
    print(f"  {'Subject':<12} {'Score':>6} {'Grade':>8}")
    print(f"  {'─' * 28}")
    
    scores = []
    for subject, score in subjects.items():
        grade = calculate_grade(score)
        print(f"  {subject:<12} {score:>6} {grade:>8}")
        scores.append(score)
    
    avg = sum(scores) / len(scores)
    print(f"  {'─' * 28}")
    print(f"  {'Average':<12} {avg:>6.1f} {calculate_grade(avg):>8}")

report_card("Amitesh", Math=95, Science=88, English=72, History=91)

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a function that returns the larger of two numbers
# 2. Create a function that returns (even_count, odd_count) from a list
# 3. Create a function using *args that returns the average
# 4. Use **kwargs to build a dictionary of a car's specs
# 5. Use lambda with filter to get words longer than 3 letters
# ============================================================
