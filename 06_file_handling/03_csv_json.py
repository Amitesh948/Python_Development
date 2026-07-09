# ============================================================
# 📘 Lesson 3: CSV & JSON Files
# ============================================================
# Real-world data comes in structured formats. The two most
# common ones are:
#   CSV  — Comma-Separated Values (spreadsheet-like)
#   JSON — JavaScript Object Notation (API/config data)
#
# Python has built-in modules for both!
#   import csv   — read/write CSV files
#   import json  — read/write JSON files
# ============================================================

import csv
import json
import os

# ============================================================
# 📗 PART 1: CSV FILES
# ============================================================

print("=" * 50)
print("📗 PART 1: CSV FILES")
print("=" * 50)

# --- Create a CSV File ---
print("\n--- Writing CSV ---")

students = [
    ["Name", "Age", "Grade", "City"],           # Header
    ["Amitesh", 25, "A", "Pune"],
    ["Priya", 23, "A+", "Mumbai"],
    ["Rahul", 24, "B+", "Delhi"],
    ["Sneha", 22, "A", "Bangalore"],
    ["Arjun", 26, "B", "Chennai"],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)   # Write all rows at once

print("  ✅ Created students.csv")

# --- Read CSV with csv.reader ---
print("\n--- Reading CSV (csv.reader) ---")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)       # Skip/grab the header row
    print(f"  Columns: {header}")
    print()
    for row in reader:
        name, age, grade, city = row
        print(f"  {name:<10} Age: {age:<4} Grade: {grade:<3} City: {city}")

# --- Read CSV as Dictionaries (DictReader) ---
print("\n--- Reading CSV (DictReader) ⭐ ---")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)   # Each row becomes a dict!
    for row in reader:
        print(f"  {row['Name']} from {row['City']} got {row['Grade']}")

# --- Write CSV with DictWriter ---
print("\n--- Writing CSV (DictWriter) ---")

products = [
    {"name": "Laptop", "price": 85000, "stock": 15},
    {"name": "Mouse", "price": 500, "stock": 200},
    {"name": "Keyboard", "price": 1500, "stock": 80},
    {"name": "Monitor", "price": 22000, "stock": 30},
]

with open("products.csv", "w", newline="") as file:
    fieldnames = ["name", "price", "stock"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()        # Write the header row
    writer.writerows(products)  # Write all data rows

print("  ✅ Created products.csv")

with open("products.csv", "r") as file:
    print(file.read())

# ============================================================
# 📗 PART 2: JSON FILES
# ============================================================

print("=" * 50)
print("📗 PART 2: JSON FILES")
print("=" * 50)

# --- Write JSON ---
print("\n--- Writing JSON ---")

user_profile = {
    "name": "Amitesh",
    "age": 25,
    "city": "Pune",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_student": False,
    "projects": [
        {"name": "Calculator", "language": "Python"},
        {"name": "Portfolio", "language": "HTML/CSS"},
    ]
}

with open("profile.json", "w") as file:
    json.dump(user_profile, file, indent=4)
    # indent=4 makes it pretty-printed (human-readable)

print("  ✅ Created profile.json")

with open("profile.json", "r") as file:
    print(file.read())

# --- Read JSON ---
print("--- Reading JSON ---")

with open("profile.json", "r") as file:
    data = json.load(file)       # Parse JSON → Python dict

print(f"  Name:   {data['name']}")
print(f"  City:   {data['city']}")
print(f"  Skills: {', '.join(data['skills'])}")
print(f"  Projects: {len(data['projects'])}")

# --- JSON ↔ Python Type Mapping ---
print("\n--- JSON ↔ Python Types ---")
type_map = {
    "object {}":     "dict",
    "array []":      "list",
    "string":        "str",
    "number (int)":  "int",
    "number (float)":"float",
    "true/false":    "True/False (bool)",
    "null":          "None",
}
for json_type, py_type in type_map.items():
    print(f"  JSON {json_type:<18} → Python {py_type}")

# --- json.dumps() — Convert to JSON String ---
print("\n--- json.dumps() — To String ---")

config = {"theme": "dark", "font_size": 14, "auto_save": True}
json_string = json.dumps(config, indent=2)
print(f"  Type: {type(json_string)}")
print(f"  Value:\n{json_string}")

# --- json.loads() — Parse JSON String ---
print("\n--- json.loads() — From String ---")

raw = '{"status": "success", "count": 42, "items": ["a", "b"]}'
parsed = json.loads(raw)
print(f"  Type:   {type(parsed)}")
print(f"  Status: {parsed['status']}")
print(f"  Count:  {parsed['count']}")

# ============================================================
# 📗 Practical: Settings Manager
# ============================================================
print("\n--- Settings Manager ---")

SETTINGS_FILE = "settings.json"

def load_settings():
    """Load settings from JSON, or return defaults."""
    defaults = {"theme": "light", "language": "en", "font_size": 14}
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return defaults

def save_settings(settings):
    """Save settings to JSON."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

# Load → modify → save
settings = load_settings()
print(f"  Before: {settings}")

settings["theme"] = "dark"
settings["font_size"] = 18
save_settings(settings)

settings = load_settings()
print(f"  After:  {settings}")

# ============================================================
# 📗 Practical: CSV → JSON Converter
# ============================================================
print("\n--- CSV → JSON Converter ---")

def csv_to_json(csv_file, json_file):
    """Convert a CSV file to JSON."""
    data = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
    print(f"  ✅ Converted {csv_file} → {json_file} ({len(data)} records)")

csv_to_json("students.csv", "students.json")

with open("students.json", "r") as f:
    print(f.read())

# ============================================================
# 🧹 Cleanup
# ============================================================
for f in ["students.csv", "products.csv", "profile.json",
          "settings.json", "students.json"]:
    if os.path.exists(f):
        os.remove(f)

print("🧹 Cleaned up all demo files!")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a CSV of 5 books (title, author, year, rating)
# 2. Read the CSV and print only books with rating > 4
# 3. Create a JSON "contact book" with name, phone, email
# 4. Build a function that converts JSON back to CSV
# 5. Create a settings file — load it, change values, save it
# ============================================================
