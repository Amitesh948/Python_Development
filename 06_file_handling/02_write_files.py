# ============================================================
# 📘 Lesson 2: Writing Files
# ============================================================
# Writing files lets you SAVE data — logs, reports, exports.
# Key modes:
#   "w" — Write (OVERWRITES existing content!)
#   "a" — Append (adds to end, keeps existing)
#   "x" — Create (fails if file already exists)
# ============================================================

import os
from datetime import datetime

# ============================================================
# 📗 Writing a New File (mode "w")
# ============================================================

print("--- Writing a New File ---")

with open("greeting.txt", "w") as file:
    file.write("Hello, Amitesh!\n")
    file.write("This file was created by Python. 🐍\n")
    file.write("File handling is awesome!\n")

with open("greeting.txt", "r") as file:
    print(file.read())

# ============================================================
# 📗 DANGER: "w" Mode Overwrites! ⚠️
# ============================================================

print("--- Overwrite Demo ---")

with open("overwrite_demo.txt", "w") as file:
    file.write("Original content — version 1\n")

# This REPLACES everything!
with open("overwrite_demo.txt", "w") as file:
    file.write("New content — version 2 (original is gone!)\n")

with open("overwrite_demo.txt", "r") as file:
    print(f"  Result: {file.read().strip()}")

# ============================================================
# 📗 Appending to a File (mode "a")
# ============================================================
# "a" ADDS to the end without erasing existing content.

print("\n--- Appending to a File ---")

with open("log.txt", "w") as file:
    file.write("=== Application Log ===\n")

for i in range(1, 4):
    with open("log.txt", "a") as file:
        timestamp = datetime.now().strftime("%H:%M:%S")
        file.write(f"[{timestamp}] Log entry #{i}\n")

with open("log.txt", "r") as file:
    print(file.read())

# ============================================================
# 📗 Exclusive Creation (mode "x")
# ============================================================
# "x" creates a new file but FAILS if it already exists.

print("--- Exclusive Creation ---")

if os.path.exists("unique_file.txt"):
    os.remove("unique_file.txt")

with open("unique_file.txt", "x") as file:
    file.write("I was safely created!\n")
print("  ✅ Created unique_file.txt")

try:
    with open("unique_file.txt", "x") as file:
        file.write("This will fail!\n")
except FileExistsError:
    print("  ❌ File already exists! (x mode prevents overwrite)")

# ============================================================
# 📗 writelines() — Write a List of Strings
# ============================================================
# NOTE: writelines() does NOT add newlines — include \n yourself!

print("\n--- writelines() ---")

shopping = ["🍎 Apples\n", "🥛 Milk\n", "🍞 Bread\n", "🧀 Cheese\n"]

with open("shopping.txt", "w") as file:
    file.write("=== Shopping List ===\n")
    file.writelines(shopping)

with open("shopping.txt", "r") as file:
    print(file.read())

# ============================================================
# 📗 Writing Formatted Data
# ============================================================

print("--- Formatted Data ---")

students = [
    ("Amitesh", 92, "A"), ("Priya", 87, "B+"),
    ("Rahul", 95, "A+"), ("Sneha", 78, "B"),
]

with open("grades.txt", "w") as file:
    file.write(f"{'Name':<12} {'Score':>6} {'Grade':>6}\n")
    file.write("=" * 28 + "\n")
    for name, score, grade in students:
        file.write(f"{name:<12} {score:>6} {grade:>6}\n")
    avg = sum(s[1] for s in students) / len(students)
    file.write("=" * 28 + "\n")
    file.write(f"{'Average':<12} {avg:>6.1f}\n")

with open("grades.txt", "r") as file:
    print(file.read())

# ============================================================
# 📗 Practical: Simple Logger
# ============================================================

print("--- Simple Logger ---")

def log(message, level="INFO"):
    """Write a timestamped log entry to file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level:>7}] {message}\n"
    with open("app_log.txt", "a") as file:
        file.write(entry)
    print(f"  📝 {entry.strip()}")

with open("app_log.txt", "w") as f:
    f.write("=== Application Log ===\n\n")

log("Application started")
log("User 'Amitesh' logged in")
log("Invalid password attempt", "WARNING")
log("Database connection lost!", "ERROR")

# ============================================================
# 📗 Practical: Copy a File
# ============================================================

print("\n--- File Copy ---")

def copy_file(source_path, dest_path):
    """Copy contents from one file to another."""
    if not os.path.exists(source_path):
        print(f"  ❌ Source '{source_path}' not found!")
        return
    with open(source_path, "r") as src:
        content = src.read()
    with open(dest_path, "w") as dst:
        dst.write(content)
    print(f"  ✅ Copied '{source_path}' → '{dest_path}' ({len(content)} chars)")

copy_file("grades.txt", "grades_backup.txt")

# ============================================================
# 🧹 Cleanup
# ============================================================
for f in ["greeting.txt", "overwrite_demo.txt", "log.txt",
          "unique_file.txt", "shopping.txt", "grades.txt",
          "app_log.txt", "grades_backup.txt"]:
    if os.path.exists(f):
        os.remove(f)

print("\n🧹 Cleaned up all demo files!")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Write a program that asks for your name and saves it
# 2. Create a to-do app that appends tasks to "todo.txt"
# 3. Write a function that saves a list, one item per line
# 4. Read a file, convert to UPPERCASE, save as new file
# 5. Create a "guest book" — each run appends name + timestamp
# ============================================================
