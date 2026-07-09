# ============================================================
# 🎯 MINI PROJECT: Python Quiz Game 🧠
# ============================================================
# This project uses everything from Module 2:
# ✅ input() — getting answers from the user
# ✅ if/elif/else — checking if answers are correct
# ✅ Comparison operators — ==, !=, >, <
# ✅ Logical operators — and, or, not
# ✅ Variables & strings from Module 1
# ============================================================

print("=" * 50)
print("    🐍 PYTHON QUIZ GAME 🧠")
print("=" * 50)
print("Test your Python knowledge!")
print("Answer each question. Let's see your score!\n")

score = 0
total_questions = 5

# --- Question 1: Multiple Choice ---
print("─" * 50)
print("Q1: What function is used to display output in Python?")
print("  a) echo()")
print("  b) print()")
print("  c) display()")
print("  d) output()")

answer1 = input("Your answer (a/b/c/d): ").lower().strip()

if answer1 == "b":
    print("✅ Correct! print() is used to display output.\n")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) print()\n")

# --- Question 2: True/False ---
print("─" * 50)
print("Q2: True or False — Python variable names can start with a number.")

answer2 = input("Your answer (true/false): ").lower().strip()

if answer2 == "false":
    print("✅ Correct! Variable names cannot start with a number.\n")
    score += 1
else:
    print("❌ Wrong! It's False — variables cannot start with numbers.\n")

# --- Question 3: Fill in the Blank ---
print("─" * 50)
print("Q3: What data type does input() always return?")
print("  Hint: Even if you type a number!")

answer3 = input("Your answer: ").lower().strip()

if answer3 == "string" or answer3 == "str":
    print("✅ Correct! input() always returns a string.\n")
    score += 1
else:
    print("❌ Wrong! input() always returns a string (str).\n")

# --- Question 4: Math Challenge ---
print("─" * 50)
print("Q4: What is the result of 17 % 5 in Python?")
print("  Hint: % gives the remainder after division.")

answer4 = input("Your answer: ").strip()

if answer4 == "2":
    print("✅ Correct! 17 ÷ 5 = 3 remainder 2.\n")
    score += 1
else:
    print("❌ Wrong! 17 % 5 = 2 (remainder of 17 ÷ 5).\n")

# --- Question 5: Code Output ---
print("─" * 50)
print("Q5: What will this code print?")
print('    x = "Hello"')
print('    print(x[0])')

answer5 = input("Your answer: ").strip()

if answer5 == "H":
    print("✅ Correct! Index 0 gives the first character.\n")
    score += 1
else:
    print("❌ Wrong! x[0] = 'H' — indexing starts at 0.\n")

# ============================================================
# 📊 RESULTS
# ============================================================
print("=" * 50)
print("    📊 QUIZ RESULTS")
print("=" * 50)

percentage = (score / total_questions) * 100
print(f"  Score: {score}/{total_questions}")
print(f"  Percentage: {percentage:.0f}%")
print()

# Grade based on score using if/elif/else
if score == total_questions:
    print("  🏆 PERFECT SCORE! You're a Python pro!")
elif score >= 4:
    print("  ⭐ Excellent! Almost perfect!")
elif score >= 3:
    print("  👍 Good job! Keep practicing!")
elif score >= 2:
    print("  😊 Not bad! Review the lessons.")
else:
    print("  📚 Keep learning! Go through Module 1 & 2 again.")

# Progress bar
filled = "█" * (score * 4)
empty = "░" * ((total_questions - score) * 4)
print(f"\n  [{filled}{empty}] {percentage:.0f}%")

print("\n" + "=" * 50)
print("✅ Module 2 Complete! Move on to 03_loops/")
print("=" * 50)
