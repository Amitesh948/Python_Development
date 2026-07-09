# ============================================================
# 🎯 MINI PROJECT: Personal Introduction Card
# ============================================================
# This project uses everything from Module 1:
# ✅ print() function
# ✅ Variables (strings, integers, floats, booleans)
# ✅ String methods & f-strings
# ✅ Number operations
# ✅ Type conversion
# ============================================================

# --- YOUR INFORMATION (Change these!) ---
name = "Amitesh"
age = 25
city = "India"
profession = "Developer"
favorite_language = "Python"
years_experience = 2
hobbies = "coding, reading, traveling"
is_learning_python = True

# --- CALCULATIONS ---
birth_year = 2026 - age
days_alive = age * 365
hours_coding = years_experience * 365 * 4  # ~4 hours per day

# --- DISPLAY THE CARD ---
border = "╔" + "═" * 48 + "╗"
separator = "╠" + "═" * 48 + "╣"
bottom = "╚" + "═" * 48 + "╝"
side = "║"

print()
print(border)
print(f"{side}{'PERSONAL INTRODUCTION CARD':^48}{side}")
print(separator)
print(f"{side}  👤 Name:       {name:<30}{side}")
print(f"{side}  🎂 Age:        {age} years (born ~{birth_year}){' ' * (18 - len(str(birth_year)))}{side}")
print(f"{side}  📍 City:       {city:<30}{side}")
print(f"{side}  💼 Profession: {profession:<30}{side}")
print(f"{side}  💻 Language:   {favorite_language:<30}{side}")
print(f"{side}  📅 Experience: {years_experience} years{' ' * 24}{side}")
print(separator)
print(f"{side}{'FUN FACTS':^48}{side}")
print(separator)
print(f"{side}  🌍 Days alive:        ~{days_alive:,}{' ' * 21}{side}")
print(f"{side}  ⌨️  Hours of coding:   ~{hours_coding:,}{' ' * 20}{side}")
print(f"{side}  📚 Currently learning: {str(is_learning_python):<24}{side}")
print(separator)
print(f"{side}  🎯 Hobbies: {hobbies:<34}{side}")
print(bottom)

# --- STRING OPERATIONS SHOWCASE ---
print(f"\n  Name in CAPS: {name.upper()}")
print(f"  Name reversed: {name[::-1]}")
print(f"  Name has {len(name)} letters")
print(f"  First letter: {name[0]}, Last letter: {name[-1]}")

print("\n✅ Module 1 Complete! Move on to 02_input_and_conditions/")
