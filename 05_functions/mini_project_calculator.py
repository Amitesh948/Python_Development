# ============================================================
# 🎯 MINI PROJECT: Calculator App 🧮
# ============================================================
# Uses everything from Module 5:
# ✅ Defining functions — each operation is a function
# ✅ Parameters & return — pass numbers, return results
# ✅ *args — for multi-number operations
# ✅ Lambda — for quick operations
# ✅ Scope — proper variable management
# ============================================================

# ============================================================
# 📗 Calculator Functions
# ============================================================

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b. Returns error message if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero! 🚫"
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def modulus(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        return "Error: Cannot divide by zero! 🚫"
    return a % b

def floor_divide(a, b):
    """Floor division of a by b."""
    if b == 0:
        return "Error: Cannot divide by zero! 🚫"
    return a // b

# --- Advanced Functions ---

def average(*numbers):
    """Calculate average of any count of numbers using *args."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def factorial(n):
    """Calculate factorial of n (n!)."""
    if n < 0:
        return "Error: No factorial for negative numbers!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def percentage(part, total):
    """Calculate what percentage 'part' is of 'total'."""
    if total == 0:
        return "Error: Total cannot be zero!"
    return (part / total) * 100

# ============================================================
# 📗 History Tracker (demonstrates scope & closures)
# ============================================================

history = []  # Store calculation history

def save_to_history(expression, result):
    """Save a calculation to history."""
    history.append(f"  {expression} = {result}")

def show_history():
    """Display calculation history."""
    if not history:
        print("\n  📭 No calculations yet!")
        return
    print(f"\n  📋 Calculation History ({len(history)} entries):")
    for i, entry in enumerate(history, 1):
        print(f"    {i}. {entry}")

def clear_history():
    """Clear all history."""
    history.clear()
    print("  🗑️  History cleared!")

# ============================================================
# 📗 Input Helper Function
# ============================================================

def get_number(prompt):
    """Safely get a number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Please enter a valid number!")

def get_two_numbers():
    """Get two numbers from the user."""
    a = get_number("  Enter first number:  ")
    b = get_number("  Enter second number: ")
    return a, b  # Return as tuple

# ============================================================
# 📗 Display Functions
# ============================================================

def show_menu():
    """Display the calculator menu."""
    print("\n╔══════════════════════════════════╗")
    print("║        🧮 CALCULATOR APP         ║")
    print("╠══════════════════════════════════╣")
    print("║  1.  Add (+)                     ║")
    print("║  2.  Subtract (-)                ║")
    print("║  3.  Multiply (×)                ║")
    print("║  4.  Divide (÷)                  ║")
    print("║  5.  Power (^)                   ║")
    print("║  6.  Modulus (%)                  ║")
    print("║  7.  Floor Divide (//)            ║")
    print("║  8.  Average (multiple numbers)   ║")
    print("║  9.  Factorial (n!)               ║")
    print("║  10. Percentage                   ║")
    print("║  11. History                      ║")
    print("║  12. Clear History                ║")
    print("║  0.  Exit                         ║")
    print("╚══════════════════════════════════╝")

def display_result(expression, result):
    """Display result and save to history."""
    print(f"\n  ✅ {expression} = {result}")
    save_to_history(expression, result)

# ============================================================
# 📗 Operation Mapping (dict of functions!)
# ============================================================

# Map choice to (function, symbol) — functions are first-class objects!
operations = {
    "1": (add, "+"),
    "2": (subtract, "-"),
    "3": (multiply, "×"),
    "4": (divide, "÷"),
    "5": (power, "^"),
    "6": (modulus, "%"),
    "7": (floor_divide, "//"),
}

# ============================================================
# 🎮 MAIN LOOP
# ============================================================

print("Welcome to Calculator App! 🧮")

while True:
    show_menu()
    choice = input("\n  Choose operation (0-12): ").strip()

    if choice == "0":
        print("\n  👋 Goodbye! Thanks for calculating!")
        print("  ✅ Module 5 Complete! Move on to 06_file_handling/")
        break

    elif choice in operations:
        func, symbol = operations[choice]
        a, b = get_two_numbers()
        result = func(a, b)
        # Format display numbers (remove .0 for whole numbers)
        a_str = int(a) if a == int(a) else a
        b_str = int(b) if b == int(b) else b
        display_result(f"{a_str} {symbol} {b_str}", result)

    elif choice == "8":
        print("  Enter numbers separated by spaces:")
        nums_input = input("  Numbers: ").strip().split()
        try:
            nums = [float(n) for n in nums_input]
            result = average(*nums)  # Unpack list as *args!
            display_result(f"avg({', '.join(nums_input)})", round(result, 2))
        except ValueError:
            print("  ❌ Invalid input!")

    elif choice == "9":
        n = get_number("  Enter a number: ")
        result = factorial(int(n))
        display_result(f"{int(n)}!", result)

    elif choice == "10":
        part = get_number("  Enter the part:  ")
        total = get_number("  Enter the total: ")
        result = percentage(part, total)
        p_str = int(part) if part == int(part) else part
        t_str = int(total) if total == int(total) else total
        display_result(f"{p_str} is what % of {t_str}", f"{result:.2f}%")

    elif choice == "11":
        show_history()

    elif choice == "12":
        clear_history()

    else:
        print("  ❌ Invalid choice! Pick 0-12.")
