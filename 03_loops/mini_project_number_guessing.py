# ============================================================
# 🎯 MINI PROJECT: Number Guessing Game 🎲
# ============================================================
# This project uses everything from Module 3:
# ✅ while loop — keep the game running
# ✅ for loop — display history
# ✅ break — exit when player wins
# ✅ continue — skip invalid input
# ✅ if/elif/else — check guesses
# ✅ input() and type conversion
# ============================================================

import random  # Built-in module to generate random numbers

# ============================================================
# 🎮 GAME SETUP
# ============================================================
print()
print("╔" + "═" * 48 + "╗")
print("║" + "🎲 NUMBER GUESSING GAME 🎲".center(48) + "║")
print("╠" + "═" * 48 + "╣")
print("║  I'm thinking of a number between 1 and 100!  ║")
print("║  Can you guess it?                             ║")
print("║  I'll give you hints: higher ⬆️  or lower ⬇️    ║")
print("╚" + "═" * 48 + "╝")
print()

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0
guess_history = []
won = False

# ============================================================
# 🎮 GAME LOOP
# ============================================================
while attempts < max_attempts:
    remaining = max_attempts - attempts
    print(f"── Attempt {attempts + 1}/{max_attempts} ({remaining} left) ──")

    # Get user's guess
    user_input = input("  Your guess: ").strip()

    # Validate input — skip if not a number
    if not user_input.isdigit():
        print("  ⚠️  Please enter a valid number!")
        continue  # Don't count this as an attempt

    guess = int(user_input)

    # Validate range
    if guess < 1 or guess > 100:
        print("  ⚠️  Number must be between 1 and 100!")
        continue

    # Count this attempt
    attempts += 1
    guess_history.append(guess)

    # Check the guess
    if guess == secret_number:
        won = True
        break  # Exit the loop — player wins!
    elif guess < secret_number:
        diff = secret_number - guess
        if diff <= 5:
            print("  🔥 So close! Just a little HIGHER!")
        elif diff <= 15:
            print("  ⬆️  Higher! You're getting warm!")
        else:
            print("  ⬆️  Higher! Keep trying.")
    else:
        diff = guess - secret_number
        if diff <= 5:
            print("  🔥 So close! Just a little LOWER!")
        elif diff <= 15:
            print("  ⬇️  Lower! You're getting warm!")
        else:
            print("  ⬇️  Lower! Keep trying.")
    print()

# ============================================================
# 📊 GAME RESULTS
# ============================================================
print()
print("═" * 50)

if won:
    print(f"  🏆 CONGRATULATIONS! You guessed it!")
    print(f"  The number was: {secret_number}")
    print(f"  You got it in {attempts} attempt(s)!")

    # Rating based on attempts
    if attempts <= 3:
        print("  ⭐⭐⭐ AMAZING! You're a genius!")
    elif attempts <= 5:
        print("  ⭐⭐ Great job! Very impressive!")
    elif attempts <= 7:
        print("  ⭐ Good work! Nice guessing!")
    else:
        print("  👍 You made it! Just in time!")
else:
    print(f"  😔 Game Over! You ran out of attempts.")
    print(f"  The secret number was: {secret_number}")

# Show guess history using for loop
print(f"\n  📋 Your guesses ({len(guess_history)} total):")
for i, guess in enumerate(guess_history, start=1):
    # Show if guess was high or low
    if guess < secret_number:
        arrow = "⬆️ (low)"
    elif guess > secret_number:
        arrow = "⬇️ (high)"
    else:
        arrow = "✅ (correct!)"
    print(f"     {i}. {guess} {arrow}")

# Visual progress bar
print(f"\n  📊 How close were your guesses:")
for guess in guess_history:
    position = int((guess / 100) * 40)
    target_pos = int((secret_number / 100) * 40)
    bar = "░" * 40
    bar = bar[:position] + "🔵" + bar[position + 1:]
    bar = bar[:target_pos] + "🎯" + bar[target_pos + 1:]
    print(f"     [{bar}] {guess}")

print("\n" + "═" * 50)
print("✅ Module 3 Complete! Move on to 04_data_structures/")
print("═" * 50)
