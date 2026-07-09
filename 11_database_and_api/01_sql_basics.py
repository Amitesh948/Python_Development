# ============================================================
# 📘 Lesson 1: SQL Basics with SQLite
# ============================================================
# A DATABASE is an organized collection of data, stored in
# TABLES (like spreadsheets). Each table has:
#   - COLUMNS (fields) — define what data to store
#   - ROWS (records)   — each row is one entry
#
# SQL (Structured Query Language) is the language used to
# talk to databases — create tables, insert data, query it.
#
# SQLite is perfect for learning because:
#   ✅ Built into Python (no install needed!)
#   ✅ Stored as a single .db file
#   ✅ Same SQL syntax as MySQL, PostgreSQL, etc.
#
# Python module:
#   import sqlite3
#
# Core workflow:
#   1. Connect     → sqlite3.connect("mydb.db")
#   2. Get cursor  → conn.cursor()
#   3. Execute SQL → cursor.execute("SQL HERE")
#   4. Commit      → conn.commit()  (saves changes)
#   5. Close       → conn.close()
# ============================================================

import sqlite3
import os

# ============================================================
# 📗 PART 1: Connecting to a Database
# ============================================================
# sqlite3.connect() opens (or creates) a database file.
# Think of it as opening a spreadsheet application.
# The cursor is like your "mouse" — it executes commands.

print("=" * 55)
print("📗 PART 1: Connecting to a Database")
print("=" * 55)

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

print("\n  ✅ Connected to 'learning.db'")
print(f"  Type of conn:   {type(conn).__name__}")
print(f"  Type of cursor: {type(cursor).__name__}")

# You can also create an IN-MEMORY database (disappears when closed)
# conn = sqlite3.connect(":memory:")

# ============================================================
# 📗 PART 2: SQLite Data Types
# ============================================================
# SQLite has 5 core data types (much simpler than other DBs):

print("\n" + "=" * 55)
print("📗 PART 2: SQLite Data Types")
print("=" * 55)

data_types = {
    "TEXT":    "Strings          → 'Hello', 'Amitesh'",
    "INTEGER": "Whole numbers    → 1, 25, -10, 0",
    "REAL":   "Decimal numbers   → 3.14, 99.99",
    "BLOB":   "Binary data       → images, files (raw bytes)",
    "NULL":   "Empty/no value    → None in Python",
}

print()
for dtype, desc in data_types.items():
    print(f"  {dtype:<10} {desc}")

# Python ↔ SQLite type mapping:
print("\n  Python → SQLite mapping:")
print("  ─" * 22)
mapping = {
    "str":       "TEXT",
    "int":       "INTEGER",
    "float":     "REAL",
    "bytes":     "BLOB",
    "None":      "NULL",
}
for py_type, sql_type in mapping.items():
    print(f"    Python {py_type:<8} → SQLite {sql_type}")

# ============================================================
# 📗 PART 3: CREATE TABLE — Define Your Structure
# ============================================================
# CREATE TABLE defines the columns and their data types.
# Think of it as setting up the headers of a spreadsheet.
#
# Syntax:
#   CREATE TABLE table_name (
#       column1 TYPE CONSTRAINTS,
#       column2 TYPE CONSTRAINTS,
#       ...
#   );
#
# Common constraints:
#   PRIMARY KEY  — unique ID for each row (auto-increments)
#   NOT NULL     — column cannot be empty
#   UNIQUE       — no duplicate values allowed
#   DEFAULT val  — use this value if none is provided

print("\n" + "=" * 55)
print("📗 PART 3: CREATE TABLE")
print("=" * 55)

# Drop the table first if it exists (for re-running this script)
cursor.execute("DROP TABLE IF EXISTS students")

# Create a students table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT DEFAULT 'N/A',
        city TEXT,
        gpa REAL
    )
""")
conn.commit()

print("\n  ✅ Created 'students' table!")
print("\n  Table structure:")
print("  ┌──────┬─────────┬─────────────────────────────┐")
print("  │ Col  │ Type    │ Constraints                 │")
print("  ├──────┼─────────┼─────────────────────────────┤")
print("  │ id   │ INTEGER │ PRIMARY KEY AUTOINCREMENT    │")
print("  │ name │ TEXT    │ NOT NULL                    │")
print("  │ age  │ INTEGER │ NOT NULL                    │")
print("  │ grade│ TEXT    │ DEFAULT 'N/A'               │")
print("  │ city │ TEXT    │ (optional)                  │")
print("  │ gpa  │ REAL    │ (optional)                  │")
print("  └──────┴─────────┴─────────────────────────────┘")

# IF NOT EXISTS — prevents error if table already exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        credits INTEGER DEFAULT 3
    )
""")
conn.commit()
print("\n  ✅ Created 'courses' table (with IF NOT EXISTS)!")

# ============================================================
# 📗 PART 4: INSERT INTO — Adding Data
# ============================================================
# INSERT adds new rows to a table.
#
# Syntax:
#   INSERT INTO table (col1, col2) VALUES (val1, val2);
#
# ⚠️ ALWAYS use ? placeholders (parameterized queries)
#    to prevent SQL injection attacks!

print("\n" + "=" * 55)
print("📗 PART 4: INSERT INTO — Adding Data")
print("=" * 55)

# Method 1: Insert ONE row with parameterized query
print("\n  --- Method 1: Insert one row ---")

cursor.execute("""
    INSERT INTO students (name, age, grade, city, gpa)
    VALUES (?, ?, ?, ?, ?)
""", ("Amitesh", 25, "A", "Pune", 8.9))

conn.commit()
print("  ✅ Inserted: Amitesh")

# Method 2: Insert MULTIPLE rows with executemany()
print("\n  --- Method 2: Insert multiple rows ---")

more_students = [
    ("Priya",  23, "A+", "Mumbai",    9.5),
    ("Rahul",  24, "B+", "Delhi",     7.8),
    ("Sneha",  22, "A",  "Bangalore", 8.5),
    ("Arjun",  26, "B",  "Chennai",   7.2),
    ("Kavita", 21, "A+", "Pune",      9.1),
    ("Vikram", 25, "A",  "Mumbai",    8.3),
    ("Deepa",  23, "B+", "Delhi",     7.6),
    ("Rohan",  24, "A",  "Bangalore", 8.7),
    ("Anita",  22, "A+", "Chennai",   9.3),
]

cursor.executemany("""
    INSERT INTO students (name, age, grade, city, gpa)
    VALUES (?, ?, ?, ?, ?)
""", more_students)

conn.commit()
print(f"  ✅ Inserted {len(more_students)} more students!")

# Method 3: Insert with DEFAULT values
print("\n  --- Method 3: Insert with defaults ---")

cursor.execute("""
    INSERT INTO students (name, age)
    VALUES (?, ?)
""", ("Newcomer", 20))

conn.commit()
print("  ✅ Inserted: Newcomer (grade defaults to 'N/A')")

# ⚠️ WHY parameterized queries? SECURITY!
print("\n  ⚠️ Why use ? placeholders?")
print("  ─" * 22)
print("  ❌ NEVER do this (SQL injection risk!):")
print('     cursor.execute(f"SELECT * FROM users WHERE name = \'{name}\'")')
print()
print("  ✅ ALWAYS do this (safe!):")
print('     cursor.execute("SELECT * FROM users WHERE name = ?", (name,))')

# ============================================================
# 📗 PART 5: SELECT — Reading Data
# ============================================================
# SELECT retrieves data from a table.
#
# Key methods:
#   cursor.fetchone()   — get ONE row (or None)
#   cursor.fetchall()   — get ALL rows as list of tuples
#   cursor.fetchmany(n) — get N rows
#
# You can also iterate directly over the cursor!

print("\n" + "=" * 55)
print("📗 PART 5: SELECT — Reading Data")
print("=" * 55)

# --- Select ALL rows ---
print("\n  --- SELECT * (all columns, all rows) ---")

cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print(f"\n  Total students: {len(all_students)}")
print(f"  {'ID':<4} {'Name':<10} {'Age':<5} {'Grade':<6} {'City':<12} {'GPA':<5}")
print("  " + "─" * 45)
for student in all_students:
    sid, name, age, grade, city, gpa = student
    city = city or "—"
    grade = grade or "N/A"
    gpa_str = f"{gpa:.1f}" if gpa else "—"
    print(f"  {sid:<4} {name:<10} {age:<5} {grade:<6} {city:<12} {gpa_str:<5}")

# --- Select SPECIFIC columns ---
print("\n  --- SELECT specific columns ---")

cursor.execute("SELECT name, city FROM students")
for row in cursor.fetchall():
    print(f"    {row[0]} from {row[1] or 'Unknown'}")

# --- fetchone() — Get first result ---
print("\n  --- fetchone() — single row ---")

cursor.execute("SELECT * FROM students WHERE id = 1")
first = cursor.fetchone()
print(f"    First student: {first}")
# Returns a tuple: (1, 'Amitesh', 25, 'A', 'Pune', 8.9)

# --- Iterate directly over cursor ---
print("\n  --- Direct iteration (memory efficient) ---")

cursor.execute("SELECT name, gpa FROM students WHERE gpa IS NOT NULL")
count = 0
for name, gpa in cursor:   # No need for fetchall()!
    if count < 3:           # Show first 3 only
        print(f"    {name}: GPA {gpa}")
    count += 1
print(f"    ... and {count - 3} more") if count > 3 else None

# ============================================================
# 📗 PART 6: WHERE — Filtering Data
# ============================================================
# WHERE lets you filter rows based on conditions.
#
# Operators:
#   =, !=, <, >, <=, >=
#   AND, OR, NOT
#   LIKE (pattern matching)
#   IN (match from a list)
#   BETWEEN (range)
#   IS NULL, IS NOT NULL

print("\n" + "=" * 55)
print("📗 PART 6: WHERE — Filtering Data")
print("=" * 55)

# --- Basic comparison ---
print("\n  --- Students from Pune ---")
cursor.execute("SELECT name, city FROM students WHERE city = ?", ("Pune",))
for row in cursor.fetchall():
    print(f"    {row[0]} — {row[1]}")

# --- AND / OR ---
print("\n  --- Age > 23 AND grade is 'A' ---")
cursor.execute("""
    SELECT name, age, grade FROM students
    WHERE age > 23 AND grade = 'A'
""")
for row in cursor.fetchall():
    print(f"    {row[0]}: age {row[1]}, grade {row[2]}")

# --- LIKE (pattern matching) ---
print("\n  --- Names starting with 'A' (LIKE) ---")
cursor.execute("SELECT name FROM students WHERE name LIKE 'A%'")
# % = any number of characters
# _ = exactly one character
for row in cursor.fetchall():
    print(f"    {row[0]}")

print("\n  LIKE patterns cheat sheet:")
print("    'A%'     → starts with A")
print("    '%a'     → ends with a")
print("    '%it%'   → contains 'it'")
print("    '_a%'    → second letter is 'a'")

# --- IN (match from a list) ---
print("\n  --- Students from Pune or Mumbai (IN) ---")
cursor.execute("""
    SELECT name, city FROM students
    WHERE city IN ('Pune', 'Mumbai')
""")
for row in cursor.fetchall():
    print(f"    {row[0]} — {row[1]}")

# --- BETWEEN ---
print("\n  --- GPA between 8.0 and 9.0 (BETWEEN) ---")
cursor.execute("""
    SELECT name, gpa FROM students
    WHERE gpa BETWEEN 8.0 AND 9.0
""")
for row in cursor.fetchall():
    print(f"    {row[0]}: GPA {row[1]}")

# --- IS NULL / IS NOT NULL ---
print("\n  --- Students with no GPA (IS NULL) ---")
cursor.execute("SELECT name, gpa FROM students WHERE gpa IS NULL")
for row in cursor.fetchall():
    print(f"    {row[0]}: GPA = {row[1]}")

# ============================================================
# 📗 PART 7: ORDER BY & LIMIT — Sorting & Limiting
# ============================================================
# ORDER BY sorts results. LIMIT restricts how many rows.
#
#   ORDER BY column ASC   — ascending (default)
#   ORDER BY column DESC  — descending
#   LIMIT n               — only return n rows
#   OFFSET n              — skip n rows (for pagination!)

print("\n" + "=" * 55)
print("📗 PART 7: ORDER BY & LIMIT")
print("=" * 55)

# --- Sort by GPA descending ---
print("\n  --- Top students by GPA (DESC) ---")
cursor.execute("""
    SELECT name, gpa FROM students
    WHERE gpa IS NOT NULL
    ORDER BY gpa DESC
""")
for i, (name, gpa) in enumerate(cursor.fetchall(), 1):
    medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
    print(f"    {medal} #{i} {name}: GPA {gpa}")

# --- LIMIT — Top 3 only ---
print("\n  --- Top 3 students (LIMIT) ---")
cursor.execute("""
    SELECT name, gpa FROM students
    WHERE gpa IS NOT NULL
    ORDER BY gpa DESC
    LIMIT 3
""")
for name, gpa in cursor.fetchall():
    print(f"    {name}: GPA {gpa}")

# --- OFFSET — Pagination ---
print("\n  --- Pagination: Page 1 (rows 1-3) ---")
cursor.execute("""
    SELECT name, age FROM students
    ORDER BY name
    LIMIT 3 OFFSET 0
""")
for row in cursor.fetchall():
    print(f"    {row[0]} (age {row[1]})")

print("\n  --- Pagination: Page 2 (rows 4-6) ---")
cursor.execute("""
    SELECT name, age FROM students
    ORDER BY name
    LIMIT 3 OFFSET 3
""")
for row in cursor.fetchall():
    print(f"    {row[0]} (age {row[1]})")

# ============================================================
# 📗 PART 8: UPDATE — Modifying Data
# ============================================================
# UPDATE changes existing rows.
#
# Syntax:
#   UPDATE table SET col1 = val1, col2 = val2 WHERE condition;
#
# ⚠️ ALWAYS use WHERE! Without it, ALL rows get updated!

print("\n" + "=" * 55)
print("📗 PART 8: UPDATE — Modifying Data")
print("=" * 55)

# --- Update one row ---
print("\n  --- Update Amitesh's GPA ---")

cursor.execute("SELECT name, gpa FROM students WHERE name = 'Amitesh'")
print(f"    Before: {cursor.fetchone()}")

cursor.execute("""
    UPDATE students SET gpa = 9.2
    WHERE name = 'Amitesh'
""")
conn.commit()

cursor.execute("SELECT name, gpa FROM students WHERE name = 'Amitesh'")
print(f"    After:  {cursor.fetchone()}")

# --- Update multiple columns ---
print("\n  --- Update multiple columns ---")

cursor.execute("""
    UPDATE students
    SET grade = 'A+', gpa = 9.0
    WHERE name = 'Rohan'
""")
conn.commit()

cursor.execute("SELECT name, grade, gpa FROM students WHERE name = 'Rohan'")
print(f"    Rohan: {cursor.fetchone()}")

# --- Update based on condition ---
print("\n  --- Bump all B+ grades to A- ---")

cursor.execute("SELECT name, grade FROM students WHERE grade = 'B+'")
print(f"    B+ students before: {cursor.fetchall()}")

cursor.execute("""
    UPDATE students SET grade = 'A-'
    WHERE grade = 'B+'
""")
conn.commit()
print(f"    ✅ Updated {cursor.rowcount} students")
# cursor.rowcount tells you how many rows were affected!

# --- ⚠️ WARNING: UPDATE without WHERE ---
print("\n  ⚠️ DANGER: UPDATE without WHERE")
print("  ─" * 22)
print("  This would update EVERY row in the table:")
print("  UPDATE students SET grade = 'F'  ← ALL students get F!")
print("  Always include WHERE to target specific rows!")

# ============================================================
# 📗 PART 9: DELETE — Removing Data
# ============================================================
# DELETE removes rows from a table.
#
# Syntax:
#   DELETE FROM table WHERE condition;
#
# ⚠️ ALWAYS use WHERE! Without it, ALL rows get deleted!

print("\n" + "=" * 55)
print("📗 PART 9: DELETE — Removing Data")
print("=" * 55)

# --- Count before delete ---
cursor.execute("SELECT COUNT(*) FROM students")
count_before = cursor.fetchone()[0]
print(f"\n  Students before: {count_before}")

# --- Delete one row ---
print("\n  --- Delete 'Newcomer' ---")
cursor.execute("DELETE FROM students WHERE name = 'Newcomer'")
conn.commit()
print(f"  ✅ Deleted {cursor.rowcount} row(s)")

# --- Delete with condition ---
print("\n  --- Delete students with GPA below 7.5 ---")
cursor.execute("SELECT name, gpa FROM students WHERE gpa < 7.5")
print(f"    Will delete: {cursor.fetchall()}")

cursor.execute("DELETE FROM students WHERE gpa < 7.5")
conn.commit()
print(f"  ✅ Deleted {cursor.rowcount} row(s)")

# --- Count after delete ---
cursor.execute("SELECT COUNT(*) FROM students")
count_after = cursor.fetchone()[0]
print(f"\n  Students after: {count_after} (removed {count_before - count_after})")

# --- ⚠️ WARNING: DELETE without WHERE ---
print("\n  ⚠️ DANGER: DELETE without WHERE")
print("  ─" * 22)
print("  DELETE FROM students  ← Deletes ALL rows!")
print("  Always include WHERE to target specific rows!")

# ============================================================
# 📗 PART 10: Aggregate Functions
# ============================================================
# SQL has built-in functions to calculate summaries:
#   COUNT()  — number of rows
#   SUM()    — total of a column
#   AVG()    — average value
#   MIN()    — smallest value
#   MAX()    — largest value
#   GROUP BY — group results by a column

print("\n" + "=" * 55)
print("📗 PART 10: Aggregate Functions")
print("=" * 55)

# --- COUNT ---
cursor.execute("SELECT COUNT(*) FROM students")
print(f"\n  Total students: {cursor.fetchone()[0]}")

# --- AVG ---
cursor.execute("SELECT AVG(gpa) FROM students WHERE gpa IS NOT NULL")
avg_gpa = cursor.fetchone()[0]
print(f"  Average GPA:    {avg_gpa:.2f}")

# --- MIN / MAX ---
cursor.execute("SELECT MIN(gpa), MAX(gpa) FROM students WHERE gpa IS NOT NULL")
min_gpa, max_gpa = cursor.fetchone()
print(f"  GPA Range:      {min_gpa} — {max_gpa}")

# --- SUM ---
cursor.execute("SELECT SUM(age) FROM students")
print(f"  Total age sum:  {cursor.fetchone()[0]}")

# --- GROUP BY — Count students per city ---
print("\n  --- Students per city (GROUP BY) ---")
cursor.execute("""
    SELECT city, COUNT(*) as count, AVG(gpa) as avg_gpa
    FROM students
    WHERE city IS NOT NULL
    GROUP BY city
    ORDER BY count DESC
""")
print(f"    {'City':<12} {'Count':<8} {'Avg GPA':<8}")
print("    " + "─" * 28)
for city, count, avg_gpa in cursor.fetchall():
    avg_str = f"{avg_gpa:.2f}" if avg_gpa else "—"
    print(f"    {city:<12} {count:<8} {avg_str:<8}")

# --- GROUP BY with HAVING (filter groups) ---
print("\n  --- Cities with 2+ students (HAVING) ---")
cursor.execute("""
    SELECT city, COUNT(*) as count
    FROM students
    WHERE city IS NOT NULL
    GROUP BY city
    HAVING count >= 2
""")
for city, count in cursor.fetchall():
    print(f"    {city}: {count} students")

# ============================================================
# 📗 PART 11: Practical — Checking Table Info
# ============================================================
# Useful commands to inspect your database structure.

print("\n" + "=" * 55)
print("📗 PART 11: Inspect Your Database")
print("=" * 55)

# --- List all tables ---
print("\n  --- All tables in database ---")
cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
""")
for (table_name,) in cursor.fetchall():
    print(f"    📋 {table_name}")

# --- Table column info ---
print("\n  --- Column info for 'students' ---")
cursor.execute("PRAGMA table_info(students)")
print(f"    {'#':<4} {'Name':<10} {'Type':<10} {'NotNull':<8} {'Default':<10} {'PK'}")
print("    " + "─" * 48)
for col in cursor.fetchall():
    cid, name, dtype, notnull, default, pk = col
    print(f"    {cid:<4} {name:<10} {dtype:<10} {'Yes' if notnull else 'No':<8} {str(default):<10} {'✅' if pk else ''}")

# --- Row count ---
cursor.execute("SELECT COUNT(*) FROM students")
print(f"\n    Total rows: {cursor.fetchone()[0]}")

# ============================================================
# 📗 PART 12: SQL Quick Reference
# ============================================================

print("\n" + "=" * 55)
print("📗 SQL Quick Reference")
print("=" * 55)

reference = """
  ┌─────────────────────────────────────────────────────────┐
  │  CREATE TABLE name (col TYPE, ...)   Create a table     │
  │  INSERT INTO name (cols) VALUES (?)  Add a row          │
  │  SELECT cols FROM name               Read data          │
  │  SELECT * FROM name WHERE cond       Filter rows        │
  │  UPDATE name SET col=? WHERE cond    Modify rows        │
  │  DELETE FROM name WHERE cond         Remove rows        │
  │  ORDER BY col ASC/DESC               Sort results       │
  │  LIMIT n OFFSET m                    Pagination         │
  │  COUNT(), AVG(), SUM(), MIN(), MAX() Aggregates         │
  │  GROUP BY col HAVING cond            Group & filter     │
  │  DROP TABLE name                     Delete a table     │
  └─────────────────────────────────────────────────────────┘
"""
print(reference)

# ============================================================
# 📗 Final: Show the remaining data
# ============================================================

print("=" * 55)
print("📗 Final: Current Database State")
print("=" * 55)

cursor.execute("SELECT * FROM students ORDER BY gpa DESC")
all_data = cursor.fetchall()

print(f"\n  {'ID':<4} {'Name':<10} {'Age':<5} {'Grade':<6} {'City':<12} {'GPA':<5}")
print("  " + "─" * 45)
for student in all_data:
    sid, name, age, grade, city, gpa = student
    city = city or "—"
    grade = grade or "N/A"
    gpa_str = f"{gpa:.1f}" if gpa else "—"
    print(f"  {sid:<4} {name:<10} {age:<5} {grade:<6} {city:<12} {gpa_str:<5}")

print(f"\n  Total: {len(all_data)} students in database")

# ============================================================
# 🧹 Cleanup — Close connection & remove DB file
# ============================================================
conn.close()
print("\n  ✅ Database connection closed")

# Remove the database file
if os.path.exists("learning.db"):
    os.remove("learning.db")
    print("  🧹 Cleaned up learning.db")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a "books" table with: id, title, author, year,
#    rating (REAL). Insert 8 books, then query:
#    a) All books sorted by rating (highest first)
#    b) Books published after 2010
#    c) Average rating of all books
#    d) Count books per author
#
# 2. Create an "employees" table with: id, name, department,
#    salary. Then:
#    a) Find employees earning above average salary
#    b) Total salary per department
#    c) Update salary for a specific employee
#    d) Delete employees from a specific department
#
# 3. Build a simple "todo" table. Write functions for:
#    add_task(), list_tasks(), complete_task(), delete_task()
#
# 4. Challenge: Create TWO related tables (orders & products)
#    and try inserting data into both!
# ============================================================
