# ============================================================
# 📘 Lesson 1: Reading Files
# ============================================================
# Python can read text files from your computer — logs, data,
# configs, notes, anything! This is one of the most practical
# skills you'll learn.
#
# Key concepts:
#   open(filename, mode)  — opens a file
#   .read()               — read entire file as one string
#   .readline()           — read one line at a time
#   .readlines()          — read all lines into a list
#   with statement        — auto-closes the file for you ✅
# ============================================================

import os

# ============================================================
# 📗 Setup: Create a Sample File to Work With
# ============================================================
# We'll create a small text file right here so the lesson
# works even if you don't have any files yet!

sample_text = """Hello, Amitesh! 🐍
Welcome to File Handling in Python.
This is line 3 of our sample file.
Python makes reading files super easy.
Let's learn together!"""

# Write the sample file (we'll learn writing in detail in Lesson 2)
with open("sample.txt", "w") as f:
    f.write(sample_text)

print("✅ Created 'sample.txt' for this lesson!\n")

# ============================================================
# 📗 Method 1: read() — Read the Entire File
# ============================================================
# read() loads the ENTIRE file as one big string.
# Good for small files; careful with huge files (memory!).

print("--- Method 1: read() — Entire File ---")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print(f"\nType: {type(content)}")
print(f"Length: {len(content)} characters\n")

# ============================================================
# 📗 Method 2: readline() — Read One Line at a Time
# ============================================================
# readline() reads the NEXT line from the file.
# Each call moves to the next line — like a cursor.

print("--- Method 2: readline() — One Line at a Time ---")

with open("sample.txt", "r") as file:
    line1 = file.readline()    # First line
    line2 = file.readline()    # Second line
    print(f"  Line 1: {line1.strip()}")
    print(f"  Line 2: {line2.strip()}")
    # .strip() removes the trailing newline character (\n)

# ============================================================
# 📗 Method 3: readlines() — All Lines as a List
# ============================================================
# readlines() reads ALL lines and returns a LIST of strings.
# Each element is one line (with \n at the end).

print("\n--- Method 3: readlines() — List of Lines ---")

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"  Number of lines: {len(lines)}")
    print(f"  Type: {type(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"    [{i}] {line.strip()}")

# ============================================================
# 📗 Method 4: Iterate Directly (BEST for large files) ⭐
# ============================================================
# The most Pythonic and memory-efficient way!
# The file object is ITERABLE — you can loop over it.
# It reads one line at a time, so it works even with
# gigabyte-sized files.

print("\n--- Method 4: Direct Iteration (Recommended!) ---")

with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"  Line {line_number}: {line.strip()}")

# ============================================================
# 📗 The 'with' Statement Explained
# ============================================================
# 'with' is called a CONTEXT MANAGER. It automatically
# closes the file when the block ends — even if an error
# occurs! Always prefer 'with' over manual open/close.

# ❌ OLD WAY (don't do this):
# file = open("sample.txt", "r")
# content = file.read()
# file.close()   # Easy to forget! If error above, never closes!

# ✅ BETTER WAY (with statement):
# with open("sample.txt", "r") as file:
#     content = file.read()
# File is automatically closed here — even if error!

print("\n--- Checking if file is closed ---")
with open("sample.txt", "r") as file:
    print(f"  Inside 'with': file.closed = {file.closed}")   # False
print(f"  Outside 'with': file.closed = {file.closed}")      # True ✅

# ============================================================
# 📗 File Modes Cheat Sheet
# ============================================================
print("\n--- File Modes ---")
modes = {
    "r":  "Read (default) — file must exist",
    "w":  "Write — creates new / OVERWRITES existing!",
    "a":  "Append — adds to end of file",
    "x":  "Create — fails if file already exists",
    "r+": "Read + Write",
    "rb": "Read binary (images, PDFs, etc.)",
    "wb": "Write binary",
}
for mode, desc in modes.items():
    print(f"  '{mode}' → {desc}")

# ============================================================
# 📗 Practical: Check if File Exists Before Reading
# ============================================================
print("\n--- Safe File Reading ---")

filename = "sample.txt"
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
    print(f"  ✅ Read '{filename}' ({len(content)} chars)")
else:
    print(f"  ❌ File '{filename}' not found!")

# Try a file that doesn't exist
missing = "ghost_file.txt"
if os.path.exists(missing):
    with open(missing, "r") as file:
        content = file.read()
    print(f"  ✅ Read '{missing}'")
else:
    print(f"  ❌ File '{missing}' not found!")

# ============================================================
# 📗 Practical: Read & Analyze a File
# ============================================================
print("\n--- File Analysis ---")

with open("sample.txt", "r") as file:
    content = file.read()

# Count various things
char_count = len(content)
word_count = len(content.split())
line_count = content.count("\n") + 1
longest_line = max(content.splitlines(), key=len)

print(f"  📄 File: sample.txt")
print(f"  📏 Characters: {char_count}")
print(f"  📝 Words:      {word_count}")
print(f"  📑 Lines:      {line_count}")
print(f"  📐 Longest:    \"{longest_line}\" ({len(longest_line)} chars)")

# ============================================================
# 📗 Practical: Search for a Word in a File
# ============================================================
print("\n--- Search in File ---")

search_word = "Python"
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        if search_word.lower() in line.lower():
            print(f"  🔍 Found '{search_word}' on line {line_num}: {line.strip()}")

# ============================================================
# 🧹 Cleanup
# ============================================================
os.remove("sample.txt")
print("\n🧹 Cleaned up sample.txt")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a text file manually, then read it with read()
# 2. Read the file line by line and print line numbers
# 3. Count how many times a specific word appears in a file
# 4. Read a file and print only lines longer than 20 characters
# 5. Read a file and print it in REVERSE order (last line first)
# ============================================================
