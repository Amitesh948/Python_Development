# ============================================================
# 📘 Lesson 2: While Loops
# ============================================================
# A while loop repeats code WHILE a condition is True.
# Think: "Keep doing this until the condition becomes False"
#
# ⚠️ Be careful! If the condition never becomes False,
#    the loop runs FOREVER (infinite loop)!
# ============================================================

# --- Basic While Loop ---
print("--- Counting 1 to 5 ---")
count = 1
while count <= 5:
    print(count)
    count += 1  # IMPORTANT: without this, infinite loop!
# How it works:
# count=1 → 1<=5? Yes → print 1 → count=2
# count=2 → 2<=5? Yes → print 2 → count=3
# count=3 → 3<=5? Yes → print 3 → count=4
# count=4 → 4<=5? Yes → print 4 → count=5
# count=5 → 5<=5? Yes → print 5 → count=6
# count=6 → 6<=5? No  → STOP!

# --- Countdown ---
print("\n--- Countdown ---")
seconds = 5
while seconds > 0:
    print(f"  {seconds}...")
    seconds -= 1
print("  🚀 Go!")

# ============================================================
# 📗 While vs For — When to Use Which?
# ============================================================
# Use FOR when:  You know HOW MANY times to repeat
#   → "Print 10 numbers", "Loop through a list"
#
# Use WHILE when: You DON'T know how many times
#   → "Keep asking until correct", "Run until user quits"

# --- Example: Keep asking until correct ---
print("\n--- Password Checker ---")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input(f"Enter password ({max_attempts - attempts} tries left): ")
    attempts += 1

    if password == correct_password:
        print("✅ Access granted!")
        break  # Exit the loop early (we'll learn this in next lesson)
    else:
        print("❌ Wrong password!")

if attempts == max_attempts and password != correct_password:
    print("🔒 Account locked! Too many failed attempts.")

# --- Example: Adding Numbers Until User Stops ---
print("\n--- Number Adder ---")
print("Enter numbers to add them up. Type 'done' to stop.")
total = 0
count = 0

while True:  # This runs forever until we 'break' out
    user_input = input("  Enter a number (or 'done'): ")

    if user_input.lower() == "done":
        break  # Exit the loop

    # Try to convert to number
    number = float(user_input)
    total += number
    count += 1
    print(f"  Running total: {total}")

print(f"\n  You entered {count} numbers. Total = {total}")

# ============================================================
# 📗 Common While Loop Patterns
# ============================================================

# --- Pattern 1: Counter ---
print("\n--- Counter Pattern ---")
i = 0
while i < 3:
    print(f"  Iteration {i}")
    i += 1

# --- Pattern 2: Accumulator ---
print("\n--- Sum of 1 to 100 ---")
n = 1
total = 0
while n <= 100:
    total += n
    n += 1
print(f"  Sum = {total}")  # 5050

# --- Pattern 3: Sentinel (stop on special value) ---
# The password checker above is an example of this

# --- Pattern 4: Validation Loop ---
print("\n--- Age Validation ---")
while True:
    age_input = input("Enter your age (1-120): ")
    age = int(age_input)
    if 1 <= age <= 120:
        print(f"  ✅ Valid age: {age}")
        break
    else:
        print("  ❌ Invalid! Please enter a number between 1 and 120.")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Print all even numbers from 2 to 20 using a while loop
# 2. Create a "guess the number" game (simple version):
#    - Set a secret number (e.g., 7)
#    - Keep asking until user guesses correctly
# 3. Calculate factorial of a number using while loop
#    (e.g., 5! = 5 × 4 × 3 × 2 × 1 = 120)
# 4. Keep asking user for names until they type "stop",
#    then print all names entered
# ============================================================
