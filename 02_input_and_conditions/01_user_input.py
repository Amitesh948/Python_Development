# ============================================================
# 📘 Lesson 1: User Input — Getting Data from the User
# ============================================================
# The input() function pauses your program and waits
# for the user to type something, then returns it as a STRING.
# ============================================================

# --- Basic Input ---
# input("prompt message") → shows message, waits for user to type
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python! 🐍")

# --- IMPORTANT: input() ALWAYS returns a STRING ---
# Even if the user types a number, it comes back as text!
age_str = input("How old are you? ")
print(f"You entered: {age_str}")
print(f"Type of input: {type(age_str).__name__}")  # str, NOT int!

# --- Converting Input to Numbers ---
# To do math with input, you must convert it first
age = int(age_str)  # Convert string to integer
next_year_age = age + 1
print(f"Next year you will be {next_year_age} years old!")

# --- One-Line Input + Conversion ---
# You can combine input() and int() in one line
height = float(input("Your height in feet (e.g. 5.6): "))
print(f"Your height: {height} feet")
print(f"In centimeters: {round(height * 30.48, 1)} cm")

# --- Getting Multiple Inputs ---
print("\n--- Tell me about yourself ---")
city = input("Which city are you from? ")
food = input("What's your favorite food? ")
color = input("What's your favorite color? ")

print(f"\n🎉 Nice! You're from {city}, you love {food}, and your favorite color is {color}!")

# --- Input with Default Behavior ---
# You can use 'or' to set a default if user presses Enter without typing
nickname = input("Enter a nickname (or press Enter to skip): ") or "No nickname"
print(f"Nickname: {nickname}")

# ============================================================
# 🏋️ PRACTICE: Try these yourself!
# ============================================================
# 1. Ask the user for their first and last name separately,
#    then print their full name
# 2. Ask for two numbers, convert to int, and print their sum
# 3. Ask for a temperature in Celsius, convert to Fahrenheit
#    Formula: F = (C * 9/5) + 32
# 4. Ask for the user's birth year and calculate their age
# ============================================================
