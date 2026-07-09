# ============================================================
# 📘 Lesson 3: Dictionaries
# ============================================================
# A dictionary stores data as KEY: VALUE pairs.
# Like a real dictionary: word (key) → definition (value)
# Created with curly braces: { }
# Keys must be unique! Values can repeat.
# ============================================================

# --- Creating Dictionaries ---
person = {
    "name": "Amitesh",
    "age": 25,
    "city": "India",
    "is_developer": True
}

print("--- Dictionary ---")
print(f"Person: {person}")
print(f"Length: {len(person)} key-value pairs")

# Empty dictionary
empty = {}
also_empty = dict()

# ============================================================
# 📗 Accessing Values
# ============================================================
print("\n--- Accessing Values ---")

# Method 1: Square brackets (throws error if key doesn't exist)
print(f"Name: {person['name']}")
print(f"Age:  {person['age']}")

# Method 2: .get() — returns None if key doesn't exist (SAFER!)
print(f"City: {person.get('city')}")
print(f"Email: {person.get('email')}")           # None (no error!)
print(f"Email: {person.get('email', 'N/A')}")    # 'N/A' (custom default)

# ============================================================
# 📗 Adding, Updating, Removing
# ============================================================
print("\n--- Modifying ---")
student = {"name": "Amitesh", "grade": "A"}
print(f"Original: {student}")

# Add new key-value
student["age"] = 25
student["city"] = "Pune"
print(f"After adding: {student}")

# Update existing value
student["grade"] = "A+"
print(f"After update: {student}")

# Update multiple at once
student.update({"email": "amitesh@email.com", "grade": "S"})
print(f"After update(): {student}")

# Remove items
removed = student.pop("email")       # Remove & return value
print(f"Popped: {removed}")
print(f"After pop: {student}")

del student["city"]                  # Delete a key
print(f"After del: {student}")

# student.clear()                    # Remove ALL items

# ============================================================
# 📗 Dictionary Methods
# ============================================================
print("\n--- Dictionary Methods ---")
car = {"brand": "Toyota", "model": "Camry", "year": 2024, "color": "Blue"}

# Get all keys, values, or both
print(f"Keys:   {list(car.keys())}")
print(f"Values: {list(car.values())}")
print(f"Items:  {list(car.items())}")

# Check if key exists
print(f"\n'brand' in car? {'brand' in car}")     # True
print(f"'price' in car? {'price' in car}")       # False

# ============================================================
# 📗 Looping Through Dictionaries
# ============================================================
print("\n--- Looping ---")
scores = {"Math": 95, "Science": 88, "English": 92, "History": 78}

# Loop through keys
print("Subjects:")
for subject in scores:
    print(f"  {subject}")

# Loop through values
print(f"\nAll scores: ", end="")
for score in scores.values():
    print(score, end=" ")
print()

# Loop through key-value pairs (MOST COMMON)
print("\nReport Card:")
for subject, score in scores.items():
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"  {subject:10s} → {score} ({grade})")

# ============================================================
# 📗 Nested Dictionaries
# ============================================================
print("\n--- Nested Dictionaries ---")
students = {
    "student1": {
        "name": "Amitesh",
        "age": 25,
        "grades": {"math": 95, "science": 88}
    },
    "student2": {
        "name": "Priya",
        "age": 23,
        "grades": {"math": 92, "science": 95}
    }
}

# Accessing nested values
print(f"Student 1 name: {students['student1']['name']}")
print(f"Student 1 math: {students['student1']['grades']['math']}")

# Loop through nested dict
for key, student in students.items():
    print(f"\n  {student['name']} (age {student['age']}):")
    for subject, grade in student['grades'].items():
        print(f"    {subject}: {grade}")

# ============================================================
# 📗 Dictionary Comprehension
# ============================================================
print("\n--- Dictionary Comprehension ---")

# Create dict from calculation
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter a dictionary
scores = {"Math": 95, "Art": 65, "Science": 88, "PE": 55}
passed = {k: v for k, v in scores.items() if v >= 70}
print(f"Passed subjects: {passed}")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a dict for a movie (title, year, director, rating)
# 2. Add a "genre" key, update the rating, remove the director
# 3. Create a scores dict, loop through it, print subject & grade
# 4. Create a nested dict of 3 friends with name, age, hobby
# 5. Use dict comprehension: {word: len(word)} for a list of words
# ============================================================
