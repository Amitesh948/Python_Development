# ============================================================
# 📘 Lesson 1: Built-in Modules
# ============================================================
# Python comes with a HUGE standard library — hundreds of
# modules ready to use. No installation needed!
#
# Syntax:
#   import module             — import entire module
#   from module import thing  — import specific item
#   import module as alias    — rename for convenience
# ============================================================

# ============================================================
# 📗 Import Styles
# ============================================================
print("--- Import Styles ---\n")

# Style 1: Import entire module
import math
print(f"  math.pi = {math.pi}")
print(f"  math.sqrt(144) = {math.sqrt(144)}")

# Style 2: Import specific items
from math import ceil, floor
print(f"  ceil(4.2)  = {ceil(4.2)}")    # No need for math.ceil()
print(f"  floor(4.8) = {floor(4.8)}")

# Style 3: Import with alias
import datetime as dt
now = dt.datetime.now()
print(f"  Now: {now.strftime('%Y-%m-%d %H:%M')}")

# Style 4: Import everything (avoid this! ❌)
# from math import *   # Pollutes your namespace — hard to debug

# ============================================================
# 📗 math — Mathematical Functions
# ============================================================
print("\n--- math Module ---\n")

import math

print(f"  pi         = {math.pi}")
print(f"  e          = {math.e}")
print(f"  sqrt(49)   = {math.sqrt(49)}")
print(f"  pow(2, 10) = {math.pow(2, 10)}")
print(f"  ceil(3.2)  = {math.ceil(3.2)}")
print(f"  floor(3.8) = {math.floor(3.8)}")
print(f"  factorial(6) = {math.factorial(6)}")
print(f"  gcd(12, 8)   = {math.gcd(12, 8)}")
print(f"  log(100, 10) = {math.log(100, 10)}")
print(f"  sin(90°)     = {math.sin(math.radians(90)):.1f}")

# ============================================================
# 📗 random — Random Numbers & Choices
# ============================================================
print("\n--- random Module ---\n")

import random

print(f"  random()          = {random.random():.4f}")         # 0.0 to 1.0
print(f"  randint(1, 100)   = {random.randint(1, 100)}")      # 1 to 100
print(f"  uniform(1.0, 10.0) = {random.uniform(1.0, 10.0):.2f}")

# Choice from a list
colors = ["red", "blue", "green", "yellow", "purple"]
print(f"  choice(colors)    = {random.choice(colors)}")
print(f"  sample(colors, 3) = {random.sample(colors, 3)}")

# Shuffle a list (in-place)
deck = list(range(1, 6))
random.shuffle(deck)
print(f"  shuffle([1-5])    = {deck}")

# ============================================================
# 📗 os — Operating System Interface
# ============================================================
print("\n--- os Module ---\n")

import os

print(f"  Current dir:   {os.getcwd()}")
print(f"  OS name:       {os.name}")
print(f"  CPU count:     {os.cpu_count()}")

# Path operations (super useful!)
import os.path

filepath = "/home/user/documents/report.pdf"
print(f"\n  Path operations on: {filepath}")
print(f"    basename:  {os.path.basename(filepath)}")
print(f"    dirname:   {os.path.dirname(filepath)}")
print(f"    extension: {os.path.splitext(filepath)[1]}")
print(f"    exists:    {os.path.exists(filepath)}")

# List files in current directory
files = os.listdir(".")
print(f"\n  Files here: {files[:5]}{'...' if len(files) > 5 else ''}")

# ============================================================
# 📗 datetime — Dates and Times
# ============================================================
print("\n--- datetime Module ---\n")

from datetime import datetime, date, timedelta

# Current date/time
now = datetime.now()
print(f"  Now:        {now}")
print(f"  Date only:  {now.date()}")
print(f"  Time only:  {now.time()}")
print(f"  Year:       {now.year}")
print(f"  Month:      {now.month}")
print(f"  Day:        {now.day}")

# Formatting dates
print(f"\n  Formatted:  {now.strftime('%d %B %Y, %I:%M %p')}")
print(f"  ISO format: {now.isoformat()}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"\n  Tomorrow:   {tomorrow.strftime('%d %b %Y')}")
print(f"  Last week:  {last_week.strftime('%d %b %Y')}")

# Days until New Year
new_year = datetime(now.year + 1, 1, 1)
days_left = (new_year - now).days
print(f"  Days to {now.year + 1}: {days_left}")

# ============================================================
# 📗 string — String Constants
# ============================================================
print("\n--- string Module ---\n")

import string

print(f"  ascii_letters:  {string.ascii_letters[:26]}...")
print(f"  digits:         {string.digits}")
print(f"  punctuation:    {string.punctuation}")
print(f"  ascii_lowercase: {string.ascii_lowercase}")
print(f"  ascii_uppercase: {string.ascii_uppercase}")

# ============================================================
# 📗 sys — System-Specific Info
# ============================================================
print("\n--- sys Module ---\n")

import sys

print(f"  Python version: {sys.version.split()[0]}")
print(f"  Platform:       {sys.platform}")
print(f"  Max int size:   {sys.maxsize}")
print(f"  Path entries:   {len(sys.path)}")
# sys.path shows where Python looks for modules
print(f"  First path:     {sys.path[0]}")

# ============================================================
# 📗 json — JSON Encoding/Decoding (Review)
# ============================================================
print("\n--- json Module ---\n")

import json

data = {"name": "Amitesh", "skills": ["Python", "JS"], "level": 5}

# Python → JSON string
json_str = json.dumps(data, indent=2)
print(f"  To JSON:\n{json_str}")

# JSON string → Python
parsed = json.loads(json_str)
print(f"\n  Back to Python: {parsed['name']}, Level {parsed['level']}")

# ============================================================
# 📗 collections — Advanced Data Structures
# ============================================================
print("\n--- collections Module ---\n")

from collections import Counter, defaultdict, namedtuple

# Counter — count occurrences
words = "the cat sat on the mat the cat".split()
word_counts = Counter(words)
print(f"  Counter: {dict(word_counts)}")
print(f"  Top 2:   {word_counts.most_common(2)}")

# defaultdict — dict with default values
scores = defaultdict(list)
scores["math"].append(95)
scores["math"].append(87)
scores["science"].append(92)
print(f"  defaultdict: {dict(scores)}")

# namedtuple — lightweight class
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"  namedtuple: {p}, x={p.x}, y={p.y}")

# ============================================================
# 📗 Practical: Quick Utilities Using Built-ins
# ============================================================
print("\n--- Quick Utilities ---\n")

# 1. Generate a random color
def random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

print(f"  Random color: {random_hex_color()}")

# 2. Get file info
def file_info(path):
    if os.path.exists(path):
        size = os.path.getsize(path)
        name = os.path.basename(path)
        ext = os.path.splitext(path)[1]
        return f"{name} ({ext}) — {size} bytes"
    return "File not found"

this_file = os.path.abspath(__file__)
print(f"  This file: {file_info(this_file)}")

# 3. Days until a date
def days_until(month, day):
    today = date.today()
    target = date(today.year, month, day)
    if target < today:
        target = date(today.year + 1, month, day)
    return (target - today).days

print(f"  Days until Jan 1: {days_until(1, 1)}")
print(f"  Days until Oct 2: {days_until(10, 2)}")

# ============================================================
# 📗 How to Explore Any Module
# ============================================================
print("\n--- Exploring Modules ---\n")

# dir() shows everything in a module
math_items = [x for x in dir(math) if not x.startswith("_")]
print(f"  math has {len(math_items)} items:")
print(f"  {math_items[:10]}...\n")

# help() shows documentation (commented out — very verbose!)
# help(math.sqrt)

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Use random to simulate rolling two dice 1000 times,
#    count how often you get doubles
# 2. Use datetime to calculate your age in days
# 3. Use os to list all .py files in the current directory
# 4. Use Counter to find the most common letter in a sentence
# 5. Use math to calculate the hypotenuse of a right triangle
# ============================================================
