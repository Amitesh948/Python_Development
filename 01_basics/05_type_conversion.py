# ============================================================
# 📘 Lesson 5: Type Conversion
# ============================================================
# Convert data from one type to another using int(), str(), float(), bool()
# ============================================================

# --- Checking Types ---
name = "Amitesh"
age = 25
height = 5.6

print(f"name type: {type(name).__name__}")    # str
print(f"age type: {type(age).__name__}")      # int
print(f"height type: {type(height).__name__}") # float

# --- String to Number ---
age_str = "25"
age_num = int(age_str)
print(f"'{age_str}' → int → {age_num}, math: {age_num + 5}")

price_str = "99.99"
price_num = float(price_str)
print(f"'{price_str}' → float → {price_num}")

# --- Number to String ---
score = 100
print("Score: " + str(score))  # Must convert to concat with +

# --- Float ↔ Int ---
print(f"float(10) = {float(10)}")    # 10.0
print(f"int(9.99) = {int(9.99)}")    # 9 (truncates, NOT rounds!)
print(f"round(9.99) = {round(9.99)}") # 10

# --- Bool Conversions ---
print(f"bool(0) = {bool(0)}")        # False
print(f"bool(1) = {bool(1)}")        # True
print(f"bool('') = {bool('')}")       # False
print(f"bool('hi') = {bool('hi')}")   # True

# --- Practical: Simple Receipt ---
print("\n" + "=" * 30)
print("  🧾 RECEIPT")
print("=" * 30)
item = "Python Book"
qty = 2
price = 29.99
total = qty * price
print(f"  {item} x{qty}: ${total:.2f}")
print("=" * 30)

# ============================================================
# 🏋️ PRACTICE:
# 1. Convert "42" to int and add 8
# 2. Convert 99.7 to int — what happens?
# 3. What does bool("0") return? (hint: it's not False!)
# ============================================================
