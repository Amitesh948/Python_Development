# ============================================================
# 🎯 MINI PROJECT: Crash-Proof Calculator 🛡️🧮
# ============================================================
# Uses everything from Module 7:
# ✅ try/except      — catch division by zero, bad input, etc.
# ✅ Multiple except — different handlers for different errors
# ✅ else/finally    — success handling and cleanup
# ✅ Custom exceptions — domain-specific error types
# ✅ raise           — validate inputs manually
# ✅ Error logging   — save errors to a log file
#
# This is an UPGRADED version of Module 5's calculator that
# NEVER crashes — no matter what the user throws at it!
# ============================================================

import json
import os
from datetime import datetime

# ============================================================
# 📗 Custom Exceptions
# ============================================================

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an unknown operation is selected."""
    def __init__(self, operation):
        self.operation = operation
        super().__init__(f"Unknown operation: '{operation}'")

class InputOverflowError(CalculatorError):
    """Raised when a number is too large to process."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Number too large: {value}")

class NegativeFactorialError(CalculatorError):
    """Raised when factorial is attempted on negative number."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Cannot calculate factorial of negative number: {value}")

# ============================================================
# 📗 Error Logger
# ============================================================

ERROR_LOG = "calculator_errors.log"

def log_error(error, context=""):
    """Log an error to file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {type(error).__name__}: {error}"
    if context:
        entry += f" | Context: {context}"
    entry += "\n"
    try:
        with open(ERROR_LOG, "a") as f:
            f.write(entry)
    except IOError:
        pass  # If we can't log, at least don't crash!

# ============================================================
# 📗 History Manager (with file persistence)
# ============================================================

HISTORY_FILE = "calc_history.json"

def load_history():
    """Load history from JSON file safely."""
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("  ⚠️ History file corrupted, starting fresh.")
        return []

def save_history(history):
    """Save history to JSON file safely."""
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)
    except IOError as e:
        print(f"  ⚠️ Could not save history: {e}")

def add_to_history(history, expression, result):
    """Add a calculation to history."""
    entry = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "expression": expression,
        "result": str(result),
    }
    history.append(entry)
    save_history(history)

def show_history(history):
    """Display calculation history."""
    if not history:
        print("\n  📭 No calculations yet!")
        return
    print(f"\n  📋 History ({len(history)} entries):")
    for i, entry in enumerate(history, 1):
        print(f"    {i}. [{entry['timestamp']}] {entry['expression']} = {entry['result']}")

def clear_history(history):
    """Clear all history."""
    history.clear()
    save_history(history)
    print("  🗑️  History cleared!")

# ============================================================
# 📗 Safe Input Functions
# ============================================================

def get_number(prompt):
    """Get a number from user — never crashes!"""
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                raise ValueError("Empty input")

            number = float(raw)

            # Check for overflow-sized numbers
            if abs(number) > 1e15:
                raise InputOverflowError(raw)

            return number

        except ValueError:
            print("  ❌ Please enter a valid number!")
        except InputOverflowError as e:
            print(f"  ❌ {e}. Keep numbers reasonable!")
            log_error(e, f"Input: {raw}")

def get_two_numbers():
    """Get two numbers from the user."""
    a = get_number("  Enter first number:  ")
    b = get_number("  Enter second number: ")
    return a, b

def format_number(n):
    """Format number for display — remove .0 for whole numbers."""
    try:
        if isinstance(n, float) and n == int(n):
            return str(int(n))
        if isinstance(n, float):
            return f"{n:.6g}"
        return str(n)
    except (ValueError, OverflowError):
        return str(n)

# ============================================================
# 📗 Calculator Operations (All crash-proof!)
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a, b):
    try:
        result = a ** b
        # Check if result is too large
        if isinstance(result, float) and (result == float('inf') or result != result):
            raise InputOverflowError(f"{a}^{b}")
        return result
    except OverflowError:
        raise InputOverflowError(f"{a}^{b} is too large!")

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero!")
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot floor-divide by zero!")
    return a // b

def square_root(a, _=None):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return a ** 0.5

def factorial(n, _=None):
    if n < 0:
        raise NegativeFactorialError(n)
    if n != int(n):
        raise ValueError("Factorial requires a whole number!")
    n = int(n)
    if n > 170:
        raise InputOverflowError(f"{n}! is astronomically large!")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def percentage(part, total):
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero!")
    return (part / total) * 100

# ============================================================
# 📗 Operation Registry
# ============================================================

# Maps choice → (function, symbol, needs_two_inputs)
operations = {
    "1":  (add,           "+",   True,  "Add"),
    "2":  (subtract,      "-",   True,  "Subtract"),
    "3":  (multiply,      "×",   True,  "Multiply"),
    "4":  (divide,        "÷",   True,  "Divide"),
    "5":  (power,         "^",   True,  "Power"),
    "6":  (modulus,       "%",   True,  "Modulus"),
    "7":  (floor_divide,  "//",  True,  "Floor Divide"),
    "8":  (square_root,   "√",   False, "Square Root"),
    "9":  (factorial,     "!",   False, "Factorial"),
    "10": (percentage,    "% of", True, "Percentage"),
}

# ============================================================
# 📗 Display Functions
# ============================================================

def show_menu():
    """Display the calculator menu."""
    print("\n╔══════════════════════════════════════╗")
    print("║     🛡️  CRASH-PROOF CALCULATOR 🧮    ║")
    print("╠══════════════════════════════════════╣")
    print("║  1.  Add (+)                         ║")
    print("║  2.  Subtract (-)                    ║")
    print("║  3.  Multiply (×)                    ║")
    print("║  4.  Divide (÷)                      ║")
    print("║  5.  Power (^)                       ║")
    print("║  6.  Modulus (%)                      ║")
    print("║  7.  Floor Divide (//)                ║")
    print("║  8.  Square Root (√)                  ║")
    print("║  9.  Factorial (n!)                   ║")
    print("║  10. Percentage                       ║")
    print("║  ──────────────────────────────────── ║")
    print("║  11. 📋 View History                  ║")
    print("║  12. 🗑️  Clear History                ║")
    print("║  13. 📄 View Error Log                ║")
    print("║  0.  👋 Exit                          ║")
    print("╚══════════════════════════════════════╝")

def show_error_log():
    """Display the error log file."""
    try:
        with open(ERROR_LOG, "r") as f:
            content = f.read().strip()
        if content:
            print(f"\n  📄 Error Log:\n")
            for line in content.split("\n"):
                print(f"    {line}")
        else:
            print("\n  ✅ No errors logged!")
    except FileNotFoundError:
        print("\n  ✅ No errors logged yet!")

# ============================================================
# 🎮 MAIN LOOP — The Unbreakable Calculator
# ============================================================

print("Welcome to the Crash-Proof Calculator! 🛡️🧮")
print("This calculator NEVER crashes — try your worst!\n")

history = load_history()
print(f"  Loaded {len(history)} previous calculations.")

while True:
    try:
        show_menu()
        choice = input("\n  Choose (0-13): ").strip()

        if choice == "0":
            save_history(history)
            print("\n  👋 Goodbye! Your history is saved.")
            print("  ✅ Module 7 Complete! Move on to 08_oop/")
            break

        elif choice in operations:
            func, symbol, needs_two, name = operations[choice]

            try:
                if needs_two:
                    a, b = get_two_numbers()
                    result = func(a, b)
                    a_str = format_number(a)
                    b_str = format_number(b)
                    expr = f"{a_str} {symbol} {b_str}"
                else:
                    a = get_number("  Enter number: ")
                    result = func(a, None)
                    a_str = format_number(a)
                    if symbol == "!":
                        expr = f"{a_str}!"
                    else:
                        expr = f"{symbol}({a_str})"

                result_str = format_number(result)
                print(f"\n  ✅ {expr} = {result_str}")
                add_to_history(history, expr, result_str)

            except ZeroDivisionError as e:
                print(f"\n  ❌ Math Error: {e}")
                log_error(e, f"Operation: {name}")
            except NegativeFactorialError as e:
                print(f"\n  ❌ {e}")
                log_error(e, f"Operation: {name}")
            except InputOverflowError as e:
                print(f"\n  ❌ Overflow: {e}")
                log_error(e, f"Operation: {name}")
            except ValueError as e:
                print(f"\n  ❌ Invalid Value: {e}")
                log_error(e, f"Operation: {name}")
            except OverflowError as e:
                print(f"\n  ❌ Number too large to compute!")
                log_error(e, f"Operation: {name}")

        elif choice == "11":
            show_history(history)

        elif choice == "12":
            clear_history(history)

        elif choice == "13":
            show_error_log()

        else:
            raise InvalidOperationError(choice)

    except InvalidOperationError as e:
        print(f"\n  ❌ {e}. Please pick 0-13.")
        log_error(e)

    except KeyboardInterrupt:
        # User pressed Ctrl+C
        print("\n\n  ⚠️ Interrupted! Use option 0 to exit properly.")
        continue

    except Exception as e:
        # The ultimate safety net — catch ANYTHING unexpected
        print(f"\n  🔴 Unexpected error: {type(e).__name__}: {e}")
        print("  But we didn't crash! 💪")
        log_error(e, "Unexpected error in main loop")

# ============================================================
# 🧹 Cleanup (optional — remove log/history files)
# ============================================================
# Uncomment the lines below to clean up after running:
# for f in [ERROR_LOG, HISTORY_FILE]:
#     if os.path.exists(f):
#         os.remove(f)
# print("🧹 Cleaned up files!")
