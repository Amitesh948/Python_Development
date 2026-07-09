# ============================================================
# 📘 Lesson 4: Numbers (Integers & Floats)
# ============================================================
# Python has two main number types:
#   int   → Whole numbers (no decimal): 1, 42, -7, 0
#   float → Decimal numbers: 3.14, -0.5, 2.0
# ============================================================

# --- Integers (int) ---
age = 25
year = 2026
temperature = -5
population = 1000000

print(f"Age: {age} (type: {type(age).__name__})")
print(f"Year: {year}")
print(f"Temperature: {temperature}")

# --- Floats (float) ---
price = 99.99
pi = 3.14159
weight = 65.5

print(f"\nPrice: {price} (type: {type(price).__name__})")
print(f"Pi: {pi}")

# ============================================================
# 📗 Arithmetic Operators
# ============================================================

a = 15
b = 4

print("\n--- Arithmetic Operations ---")
print(f"{a} + {b} = {a + b}")     # Addition:        19
print(f"{a} - {b} = {a - b}")     # Subtraction:     11
print(f"{a} * {b} = {a * b}")     # Multiplication:  60
print(f"{a} / {b} = {a / b}")     # Division:        3.75 (always returns float!)
print(f"{a} // {b} = {a // b}")   # Floor Division:  3 (rounds down, no decimal)
print(f"{a} % {b} = {a % b}")     # Modulus:         3 (remainder after division)
print(f"{a} ** {b} = {a ** b}")   # Exponent:        50625 (15 to the power of 4)

# --- Important: Division ALWAYS returns a float ---
print(f"\n10 / 2 = {10 / 2}")         # 5.0 (float, not int!)
print(f"10 // 2 = {10 // 2}")         # 5   (int, floor division)

# ============================================================
# 📗 Useful Number Functions
# ============================================================

print("\n--- Built-in Number Functions ---")
print(f"abs(-42) = {abs(-42)}")          # Absolute value: 42
print(f"round(3.7) = {round(3.7)}")      # Round: 4
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # Round to 2 decimals: 3.14
print(f"max(10, 20, 5) = {max(10, 20, 5)}")        # Maximum: 20
print(f"min(10, 20, 5) = {min(10, 20, 5)}")        # Minimum: 5
print(f"pow(2, 8) = {pow(2, 8)}")        # Power: 256 (same as 2**8)

# ============================================================
# 📗 Shorthand Operators
# ============================================================

print("\n--- Shorthand Operators ---")
score = 100
print(f"Start: {score}")

score += 10    # Same as: score = score + 10
print(f"After += 10: {score}")   # 110

score -= 20    # Same as: score = score - 20
print(f"After -= 20: {score}")   # 90

score *= 2     # Same as: score = score * 2
print(f"After *= 2: {score}")    # 180

score //= 3   # Same as: score = score // 3
print(f"After //= 3: {score}")   # 60

# ============================================================
# 📗 Number Formatting for Display
# ============================================================

print("\n--- Number Formatting ---")
price = 49.99
print(f"Price: ${price:.2f}")              # Always show 2 decimal places
print(f"Large number: {1000000:,}")        # Add commas: 1,000,000
print(f"Percentage: {0.85:.0%}")           # Show as percentage: 85%
print(f"Padded: {42:05d}")                 # Pad with zeros: 00042

# ============================================================
# 📗 Order of Operations (PEMDAS / BODMAS)
# ============================================================

print("\n--- Order of Operations ---")
# Python follows math rules: Parentheses, Exponents, Multiply/Divide, Add/Subtract
result1 = 2 + 3 * 4          # 3*4 first, then +2
print(f"2 + 3 * 4 = {result1}")            # 14

result2 = (2 + 3) * 4        # (2+3) first because of parentheses
print(f"(2 + 3) * 4 = {result2}")          # 20

result3 = 2 ** 3 + 1         # 2**3 first (exponent), then +1
print(f"2 ** 3 + 1 = {result3}")           # 9

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Calculate the area of a rectangle (length * width) — use variables!
# 2. Calculate the remainder when 100 is divided by 7
# 3. Convert a temperature from Celsius to Fahrenheit
#    Formula: F = (C * 9/5) + 32
#    Try with C = 37
# 4. What is 2 to the power of 10? (use **)
# 5. Format the number 1234567.891 with commas and 2 decimal places
# ============================================================
