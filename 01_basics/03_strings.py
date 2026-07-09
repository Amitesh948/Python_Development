# ============================================================
# 📘 Lesson 3: Strings (Text Data)
# ============================================================
# A string is text — any characters between quotes.
# You can use single quotes '' or double quotes ""
# ============================================================

# --- Creating Strings ---
greeting = "Hello, World!"
name = 'Amitesh'
message = "I'm learning Python"  # Use double quotes when text has apostrophes

# --- Multi-line Strings ---
# Use triple quotes for text that spans multiple lines
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
print(poem)
print()

# --- String Length ---
# len() tells you how many characters are in a string
text = "Python"
print(f"'{text}' has {len(text)} characters")  # 6

# --- Accessing Characters (Indexing) ---
# Each character has a position number (index), starting from 0
#   P  y  t  h  o  n
#   0  1  2  3  4  5
word = "Python"
print(f"First character: {word[0]}")   # P
print(f"Second character: {word[1]}")  # y
print(f"Last character: {word[-1]}")   # n (negative = from the end)

# --- Slicing (Getting a Part of a String) ---
# Syntax: string[start:end]  (end is NOT included)
language = "Python"
print(f"First 3 characters: {language[0:3]}")  # Pyt
print(f"Characters 2-4: {language[2:5]}")      # tho
print(f"From index 3 onwards: {language[3:]}")  # hon
print(f"Up to index 3: {language[:3]}")         # Pyt

# ============================================================
# 📗 String Methods — Built-in tools for working with strings
# ============================================================

sample = "  Hello, Python World!  "

# --- Case Methods ---
print("UPPER:", sample.upper())           # "  HELLO, PYTHON WORLD!  "
print("lower:", sample.lower())           # "  hello, python world!  "
print("Title:", sample.title())           # "  Hello, Python World!  "
print("Capitalize:", "hello".capitalize()) # "Hello"

# --- Whitespace Methods ---
print(f"Strip: '{sample.strip()}'")       # Removes spaces from both sides
print(f"Lstrip: '{sample.lstrip()}'")     # Removes spaces from left
print(f"Rstrip: '{sample.rstrip()}'")     # Removes spaces from right

# --- Search Methods ---
text = "I love Python programming"
print(f"Find 'Python': {text.find('Python')}")       # 7 (index where it starts)
print(f"Find 'Java': {text.find('Java')}")            # -1 (not found)
print(f"Contains 'Python': {'Python' in text}")       # True
print(f"Starts with 'I': {text.startswith('I')}")     # True
print(f"Ends with 'ing': {text.endswith('ing')}")     # True
print(f"Count 'o': {text.count('o')}")                # 2

# --- Replace ---
original = "I like Java"
modified = original.replace("Java", "Python")
print(f"Original: {original}")
print(f"Modified: {modified}")

# --- Split & Join ---
sentence = "Python is a great language"
words = sentence.split()           # Splits by spaces into a list
print(f"Words: {words}")           # ['Python', 'is', 'a', 'great', 'language']

joined = " - ".join(words)        # Joins list items with " - "
print(f"Joined: {joined}")        # "Python - is - a - great - language"

# --- String Concatenation (Joining Strings) ---
first = "Hello"
second = "World"
combined = first + " " + second   # Using +
print(combined)                    # "Hello World"

# --- String Repetition ---
laugh = "Ha" * 3
print(laugh)  # "HaHaHa"

border = "=" * 40
print(border)

# --- Escape Characters ---
# \n = new line, \t = tab, \\ = backslash, \" = double quote
print("Line 1\nLine 2")
print("Name:\tAmitesh")
print("She said \"Hello!\"")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Create a variable with your full name, print it in ALL CAPS
# 2. Get the first 3 letters of your name using slicing
# 3. Count how many times the letter 'a' appears in your name
# 4. Replace a word in a sentence
# 5. Split the sentence "apple,banana,mango" by comma
#    Hint: "apple,banana,mango".split(",")
# ============================================================
