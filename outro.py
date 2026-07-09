# ============================================================
# 🎓 OUTRO: Your Python Journey — Complete! 🐍🏆
# ============================================================
# Congratulations, Amitesh! You've completed all 10 modules
# of the Python Learning Project. This file is a recap of
# everything you've learned and where to go next.
#
# Run this file for a fun summary!
# ============================================================

from datetime import datetime, date

# ============================================================
# 📗 Your Learning Journey Recap
# ============================================================

def show_journey():
    """Display the complete learning journey."""

    print("\n" + "═" * 56)
    print("   🎓 PYTHON LEARNING JOURNEY — COMPLETE! 🐍🏆")
    print("═" * 56)
    print(f"   Completed: {date.today().strftime('%d %B %Y')}")
    print(f"   Student:   Amitesh")
    print("═" * 56)

    modules = [
        ("01", "📘 Basics",
         "Variables, strings, numbers, print(), f-strings",
         ["Variables hold data", "Strings are text in quotes",
          "f-strings for formatting", "type() to check types"]),

        ("02", "📗 Input & Conditions",
         "input(), if/elif/else, comparison operators",
         ["input() gets user data (always a string!)",
          "if/elif/else for decisions",
          "==, !=, <, >, and, or, not"]),

        ("03", "📙 Loops",
         "for loops, while loops, break/continue",
         ["for — loop a known number of times",
          "while — loop until condition is False",
          "break exits, continue skips"]),

        ("04", "📕 Data Structures",
         "Lists, tuples, dictionaries, sets",
         ["Lists [] — ordered, mutable",
          "Tuples () — ordered, immutable",
          "Dicts {} — key:value pairs",
          "Sets {} — unique items only"]),

        ("05", "📒 Functions",
         "def, parameters, return, scope, *args/**kwargs",
         ["Functions = reusable code blocks",
          "Parameters pass data in, return sends it back",
          "Local vs global scope",
          "*args and **kwargs for flexible params"]),

        ("06", "📓 File Handling",
         "read/write files, CSV, JSON",
         ["open() with 'r', 'w', 'a' modes",
          "'with' statement auto-closes files",
          "csv module for spreadsheet data",
          "json module for structured data"]),

        ("07", "📔 Error Handling",
         "try/except, custom exceptions, raise, assert",
         ["try/except catches errors gracefully",
          "finally always runs (cleanup!)",
          "raise triggers errors on purpose",
          "Custom exceptions for your own error types"]),

        ("08", "📚 OOP",
         "Classes, objects, inheritance, encapsulation",
         ["class = blueprint, object = instance",
          "__init__ sets up objects, self = this object",
          "Inheritance: child gets parent's abilities",
          "@property controls attribute access"]),

        ("09", "📖 Modules & Packages",
         "import, pip, virtualenv, custom modules",
         ["import brings in other code",
          "Your .py files ARE modules!",
          "pip installs third-party packages",
          "virtualenv isolates project dependencies"]),

        ("10", "🏆 Capstone Project",
         "Expense Tracker CLI — everything combined!",
         ["Multi-file architecture (models, utils, main)",
          "OOP + error handling + file I/O",
          "Real-world app you can actually use",
          "All 9 previous modules in action"]),
    ]

    for num, title, topics, takeaways in modules:
        print(f"\n  ┌─ Module {num} ─────────────────────────────────┐")
        print(f"  │ {title:<46} │")
        print(f"  │ {topics:<46} │")
        print(f"  ├──────────────────────────────────────────────┤")
        for t in takeaways:
            print(f"  │   ✅ {t:<42} │")
        print(f"  └──────────────────────────────────────────────┘")

# ============================================================
# 📗 Skills You've Gained
# ============================================================

def show_skills():
    """Display all Python skills acquired."""

    skills = {
        "🧱 Core Python": [
            "Variables & data types",
            "String manipulation & f-strings",
            "Numbers & arithmetic",
            "Type conversion",
            "User input & output",
        ],
        "🔀 Control Flow": [
            "if / elif / else",
            "for loops & while loops",
            "break, continue, pass",
            "Nested loops & conditions",
            "Comprehensions",
        ],
        "📦 Data Structures": [
            "Lists & list methods",
            "Dictionaries & dict methods",
            "Tuples (immutable sequences)",
            "Sets (unique collections)",
            "Nested data structures",
        ],
        "⚡ Functions": [
            "Defining & calling functions",
            "Parameters & return values",
            "Default & keyword arguments",
            "*args and **kwargs",
            "Variable scope (local/global)",
            "Lambda functions",
        ],
        "📂 File I/O": [
            "Reading text files",
            "Writing & appending files",
            "CSV processing",
            "JSON read/write",
            "File path operations (os.path)",
        ],
        "🛡️ Error Handling": [
            "try / except / else / finally",
            "Catching specific exceptions",
            "Custom exception classes",
            "raise & assert statements",
            "Defensive programming",
        ],
        "🏗️ OOP": [
            "Classes & objects",
            "Constructors (__init__)",
            "Methods & self",
            "Inheritance & super()",
            "Encapsulation & @property",
            "Dunder methods (__str__, __eq__, etc.)",
        ],
        "📦 Modules": [
            "import / from / as",
            "Standard library (math, os, json, etc.)",
            "Creating your own modules",
            "Packages with __init__.py",
            "pip & virtual environments",
        ],
    }

    print("\n" + "═" * 56)
    print("   🛠️  SKILLS ACQUIRED")
    print("═" * 56)

    total = 0
    for category, items in skills.items():
        print(f"\n  {category}")
        for skill in items:
            print(f"    ✅ {skill}")
            total += 1

    print(f"\n  ─────────────────────────────────────")
    print(f"  🎯 Total skills: {total}")

# ============================================================
# 📗 What's Next — Your Roadmap Forward
# ============================================================

def show_whats_next():
    """Suggest next steps in the Python journey."""

    print("\n" + "═" * 56)
    print("   🚀 WHAT'S NEXT?")
    print("═" * 56)

    paths = [
        ("🌐 Web Development", [
            "Flask — lightweight web framework (start here!)",
            "Django — full-featured web framework",
            "FastAPI — modern async APIs",
            "HTML/CSS/JavaScript basics",
        ]),
        ("📊 Data Science", [
            "NumPy — numerical computing",
            "Pandas — data analysis",
            "Matplotlib / Seaborn — visualization",
            "Jupyter Notebooks",
        ]),
        ("🤖 Automation & Scripting", [
            "Web scraping (BeautifulSoup, Selenium)",
            "File/folder automation (os, shutil)",
            "API integration (requests)",
            "Task scheduling (cron, schedule)",
        ]),
        ("🧪 Testing & Quality", [
            "pytest — testing framework",
            "Type hints (typing module)",
            "Linting (pylint, flake8)",
            "Git & GitHub for version control",
        ]),
        ("🎮 Fun Projects", [
            "Pygame — 2D games",
            "Discord/Telegram bots",
            "GUI apps (tkinter, PyQt)",
            "CLI tools (click, argparse)",
        ]),
    ]

    for path_name, items in paths:
        print(f"\n  {path_name}:")
        for item in items:
            print(f"    → {item}")

    print(f"""
  ═══════════════════════════════════════════════════
  💡 TIPS FOR CONTINUED GROWTH:

    1. Build projects — that's how you truly learn
    2. Read other people's code (GitHub!)
    3. Contribute to open source
    4. Join communities (Reddit, Discord, Stack Overflow)
    5. Teach what you learn — it deepens understanding
    6. Code every day, even if just 15 minutes
    7. Don't memorize — understand concepts, Google syntax
  ═══════════════════════════════════════════════════
""")

# ============================================================
# 📗 Project Ideas to Keep Building
# ============================================================

def show_project_ideas():
    """Suggest projects to build next."""

    print("═" * 56)
    print("   💡 PROJECT IDEAS")
    print("═" * 56)

    projects = [
        ("🟢 Beginner", [
            "To-Do List CLI with file storage",
            "Unit converter (temp, weight, distance)",
            "Flashcard quiz app",
            "Simple password manager",
            "Markdown to HTML converter",
        ]),
        ("🟡 Intermediate", [
            "Weather app using an API (requests + API key)",
            "Personal budget tracker with charts",
            "Web scraper that saves to CSV",
            "URL shortener",
            "File organizer (sorts files by type)",
        ]),
        ("🔴 Advanced", [
            "Blog website with Flask/Django",
            "REST API for your expense tracker",
            "Chat application with sockets",
            "Data dashboard with Pandas + Matplotlib",
            "Automation bot for daily tasks",
        ]),
    ]

    for level, ideas in projects:
        print(f"\n  {level}:")
        for i, idea in enumerate(ideas, 1):
            print(f"    {i}. {idea}")

# ============================================================
# 🎮 Run the Outro
# ============================================================

if __name__ == "__main__":
    show_journey()

    input("\n  Press Enter to see your skills... ")
    show_skills()

    input("\n  Press Enter to see what's next... ")
    show_whats_next()
    show_project_ideas()

    print("═" * 56)
    print("   🎓 CONGRATULATIONS, AMITESH! 🎉")
    print("═" * 56)
    print("   You are now a Python programmer.")
    print("   The fundamentals are SOLID.")
    print("   Now go build something amazing! 🚀")
    print("═" * 56)
    print()
