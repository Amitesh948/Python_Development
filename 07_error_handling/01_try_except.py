# ============================================================
# 📘 Lesson 1: Try / Except — Handling Errors Gracefully
# ============================================================
# Errors happen! Users type letters when you expect numbers,
# files go missing, networks fail. Instead of your program
# CRASHING, you can CATCH errors and handle them.
#
# Syntax:
#   try:
#       risky code here
#   except SomeError:
#       what to do if it fails
#
# This is called EXCEPTION HANDLING.
# ============================================================

# ============================================================
# 📗 Without try/except — Program CRASHES
# ============================================================
# Uncomment the line below to see a crash:
# result = 10 / 0   # ZeroDivisionError — program stops dead!

# ============================================================
# 📗 Basic try/except
# ============================================================
print("--- Basic try/except ---")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("  ❌ Cannot divide by zero!")

print("  ✅ Program keeps running! (didn't crash)\n")

# ============================================================
# 📗 Catching the Error Object
# ============================================================
# Use "as e" to capture the actual error message

print("--- Catching Error Details ---")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Error type:    {type(e).__name__}")
    print(f"  Error message: {e}")

# ============================================================
# 📗 Common Exception Types
# ============================================================
print("\n--- Common Exception Types ---\n")

# 1. ZeroDivisionError
print("  1. ZeroDivisionError:")
try:
    x = 100 / 0
except ZeroDivisionError as e:
    print(f"     {e}\n")

# 2. ValueError
print("  2. ValueError:")
try:
    num = int("hello")   # Can't convert "hello" to int!
except ValueError as e:
    print(f"     {e}\n")

# 3. TypeError
print("  3. TypeError:")
try:
    result = "hello" + 42   # Can't add string + int!
except TypeError as e:
    print(f"     {e}\n")

# 4. IndexError
print("  4. IndexError:")
try:
    fruits = ["apple", "banana"]
    print(fruits[10])       # Index doesn't exist!
except IndexError as e:
    print(f"     {e}\n")

# 5. KeyError
print("  5. KeyError:")
try:
    person = {"name": "Amitesh"}
    print(person["age"])    # Key doesn't exist!
except KeyError as e:
    print(f"     {e}\n")

# 6. FileNotFoundError
print("  6. FileNotFoundError:")
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"     {e}\n")

# 7. AttributeError
print("  7. AttributeError:")
try:
    num = 42
    num.append(10)          # int has no .append()!
except AttributeError as e:
    print(f"     {e}\n")

# ============================================================
# 📗 Multiple except Blocks
# ============================================================
# You can handle DIFFERENT errors in DIFFERENT ways

print("--- Multiple except Blocks ---")

def safe_divide(a, b):
    """Safely divide with multiple error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("  ❌ Cannot divide by zero!")
    except TypeError:
        print("  ❌ Both values must be numbers!")
    return None

safe_divide(10, 0)          # ZeroDivisionError
safe_divide("ten", 2)       # TypeError
result = safe_divide(10, 3) # Works fine!
print(f"  ✅ 10 / 3 = {result:.2f}")

# ============================================================
# 📗 Catching Multiple Exceptions in One Line
# ============================================================
print("\n--- Multiple in One Line ---")

try:
    # Could fail different ways
    numbers = [1, 2, 3]
    print(numbers[10])
except (IndexError, KeyError, TypeError) as e:
    print(f"  Caught: {type(e).__name__} — {e}")

# ============================================================
# 📗 The Generic except (Use Carefully!)
# ============================================================
# A bare "except" catches ANY error. Use sparingly — it can
# hide bugs! Always prefer specific exception types.

print("\n--- Generic except ---")

try:
    result = int("not a number")
except Exception as e:
    print(f"  Caught: {type(e).__name__} — {e}")
    # At least we know WHAT went wrong

# ❌ BAD — hides all errors silently:
# try:
#     something()
# except:
#     pass   # Never do this! Bugs become invisible!

# ============================================================
# 📗 try / except / else
# ============================================================
# The 'else' block runs ONLY if NO exception occurred.
# Great for code that should only run on success.

print("\n--- try/except/else ---")

def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  ❌ {a}/{b} — Cannot divide by zero!")
    else:
        # Only runs if try succeeded!
        print(f"  ✅ {a}/{b} = {result:.2f}")

divide_with_else(10, 3)   # else runs
divide_with_else(10, 0)   # except runs

# ============================================================
# 📗 try / except / finally
# ============================================================
# 'finally' ALWAYS runs — error or no error!
# Perfect for cleanup: closing files, connections, etc.

print("\n--- try/except/finally ---")

def read_file_safe(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        print(f"  ✅ Read {len(content)} characters")
    except FileNotFoundError:
        print(f"  ❌ File '{filename}' not found!")
    finally:
        # Always runs — cleanup!
        if file and not file.closed:
            file.close()
            print("  🔒 File closed in finally block")
        print("  🏁 Finally block executed\n")

read_file_safe("nonexistent.txt")   # Error path

# Create a temp file to test success path
with open("_temp_test.txt", "w") as f:
    f.write("test content")
read_file_safe("_temp_test.txt")     # Success path
import os
os.remove("_temp_test.txt")

# ============================================================
# 📗 The Full Pattern: try/except/else/finally
# ============================================================
print("--- Full Pattern ---")

def full_pattern_demo(value):
    print(f"  Converting '{value}':")
    try:
        number = int(value)
    except ValueError:
        print("    ❌ except: Not a valid number!")
    else:
        print(f"    ✅ else: Got number {number}")
    finally:
        print("    🏁 finally: Always runs!\n")

full_pattern_demo("42")      # try → else → finally
full_pattern_demo("hello")   # try → except → finally

# ============================================================
# 📗 Nested try/except
# ============================================================
print("--- Nested try/except ---")

def process_data(data):
    """Process data with nested error handling."""
    try:
        print(f"  Processing: {data}")
        try:
            number = int(data)
            result = 100 / number
        except ValueError:
            print("    ⚠️ Inner: Not a number, using default (1)")
            result = 100 / 1
        except ZeroDivisionError:
            print("    ⚠️ Inner: Zero detected, using default (1)")
            result = 100 / 1
        print(f"    Result: {result}")
    except Exception as e:
        print(f"    ❌ Outer: Unexpected error — {e}")

process_data("5")
process_data("abc")
process_data("0")

# ============================================================
# 📗 Practical: Safe User Input
# ============================================================
print("\n--- Safe Input Function ---")

def get_integer(prompt, min_val=None, max_val=None):
    """Safely get an integer from the user with validation."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  ⚠️ Must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"  ⚠️ Must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("  ❌ Please enter a valid whole number!")

# Demo (only one call so lesson doesn't need lots of input)
age = get_integer("  Enter your age (1-120): ", 1, 120)
print(f"  ✅ Your age: {age}\n")

# ============================================================
# 📗 Practical: Safe List Access
# ============================================================
print("--- Safe List Access ---")

def safe_get(lst, index, default=None):
    """Safely get an item from a list."""
    try:
        return lst[index]
    except (IndexError, TypeError):
        return default

colors = ["red", "green", "blue"]
print(f"  Index 0: {safe_get(colors, 0)}")         # red
print(f"  Index 5: {safe_get(colors, 5, 'N/A')}")  # N/A (safe!)
print(f"  Index 'a': {safe_get(colors, 'a', 'N/A')}")  # N/A

# ============================================================
# 📗 Practical: Safe Dictionary Access
# ============================================================
print("\n--- Safe Dict Access ---")

def safe_lookup(dictionary, *keys):
    """Safely navigate nested dictionaries."""
    current = dictionary
    for key in keys:
        try:
            current = current[key]
        except (KeyError, TypeError, IndexError):
            return None
    return current

user = {
    "name": "Amitesh",
    "address": {
        "city": "Pune",
        "pin": "411001"
    }
}

print(f"  Name:    {safe_lookup(user, 'name')}")
print(f"  City:    {safe_lookup(user, 'address', 'city')}")
print(f"  Country: {safe_lookup(user, 'address', 'country')}")  # None
print(f"  Missing: {safe_lookup(user, 'phone', 'mobile')}")     # None

# ============================================================
# 📗 Exception Hierarchy (Good to Know)
# ============================================================
print("\n--- Exception Hierarchy ---")

hierarchy = """
  BaseException
  └── Exception
      ├── ArithmeticError
      │   ├── ZeroDivisionError
      │   └── OverflowError
      ├── LookupError
      │   ├── IndexError
      │   └── KeyError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError
      ├── PermissionError
      ├── AttributeError
      └── RuntimeError
"""
print(hierarchy)

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Write a function that safely converts a string to float
# 2. Write a program that opens a file safely (handle missing)
# 3. Create a function that divides two user inputs safely
# 4. Write a safe_pop(lst, index) that never crashes
# 5. Use try/except/else/finally in one function
# ============================================================
