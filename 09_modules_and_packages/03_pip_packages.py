# ============================================================
# 📘 Lesson 3: pip, Packages & Virtual Environments
# ============================================================
# pip is Python's package manager — it downloads and installs
# third-party packages from PyPI (Python Package Index).
#
# PyPI has 500,000+ packages for everything:
#   requests  — HTTP requests (APIs)
#   flask     — web apps
#   pandas    — data analysis
#   pygame    — games
#   pillow    — image processing
#
# This lesson EXPLAINS the concepts. Run the pip commands
# in your terminal, not inside Python!
# ============================================================

import subprocess
import sys
import os

# ============================================================
# 📗 pip — The Package Manager
# ============================================================
print("--- pip Basics ---\n")

print("  pip commands (run these in your TERMINAL, not Python!):\n")

pip_commands = {
    "pip install requests":       "Install a package",
    "pip install requests==2.28": "Install specific version",
    "pip install --upgrade requests": "Upgrade a package",
    "pip uninstall requests":     "Remove a package",
    "pip list":                   "List installed packages",
    "pip show requests":          "Show package details",
    "pip freeze":                 "List packages in requirements format",
    "pip freeze > requirements.txt": "Save all packages to a file",
    "pip install -r requirements.txt": "Install from requirements file",
    "pip search <query>":         "Search PyPI (may be disabled)",
}

for cmd, desc in pip_commands.items():
    print(f"  $ {cmd:<42} # {desc}")

# ============================================================
# 📗 What's Currently Installed?
# ============================================================
print("\n--- Currently Installed Packages ---\n")

# We can run pip from Python using subprocess
result = subprocess.run(
    [sys.executable, "-m", "pip", "list", "--format=columns"],
    capture_output=True, text=True
)
lines = result.stdout.strip().split("\n")
print(f"  You have {max(0, len(lines) - 2)} packages installed.")
# Show first few
for line in lines[:7]:
    print(f"  {line}")
if len(lines) > 7:
    print(f"  ... and {len(lines) - 7} more")

# ============================================================
# 📗 Virtual Environments — ESSENTIAL! ⭐
# ============================================================
print("\n--- Virtual Environments ---\n")

print("""  WHY use virtual environments?
  ─────────────────────────────────────────────────
  Without them, ALL projects share the SAME packages.
  
  Problem:
    Project A needs requests==2.25
    Project B needs requests==2.31
    💥 They conflict!

  Solution: Virtual environments!
    Each project gets its OWN isolated Python + packages.
    No conflicts, clean installs, easy sharing.
""")

print("  HOW to create and use a virtual environment:\n")

venv_steps = [
    ("python3 -m venv myenv",       "Create a virtual environment"),
    ("source myenv/bin/activate",   "Activate it (Linux/Mac)"),
    ("myenv\\Scripts\\activate",      "Activate it (Windows)"),
    ("pip install requests",        "Install packages (isolated!)"),
    ("pip freeze > requirements.txt", "Save package list"),
    ("deactivate",                  "Leave the virtual environment"),
    ("rm -rf myenv",                "Delete it (when done)"),
]

for i, (cmd, desc) in enumerate(venv_steps, 1):
    print(f"  {i}. $ {cmd:<38} # {desc}")

# ============================================================
# 📗 requirements.txt — Sharing Dependencies
# ============================================================
print("\n--- requirements.txt ---\n")

print("""  requirements.txt lets others install the EXACT same packages:

  1. Create it:  $ pip freeze > requirements.txt
  2. Share it with your code (e.g., on GitHub)
  3. Others install: $ pip install -r requirements.txt

  Example requirements.txt:
  ┌─────────────────────────┐
  │ requests==2.31.0        │
  │ flask==3.0.0            │
  │ pandas==2.1.4           │
  │ python-dotenv==1.0.0    │
  └─────────────────────────┘
""")

# Create a sample requirements.txt
sample_requirements = [
    "# Python Learning Project Dependencies",
    "# Install with: pip install -r requirements.txt",
    "",
    "requests>=2.28.0",
    "python-dotenv>=1.0.0",
]

with open("requirements_sample.txt", "w") as f:
    f.write("\n".join(sample_requirements) + "\n")
print("  ✅ Created requirements_sample.txt (example file)")

# ============================================================
# 📗 Popular Third-Party Packages
# ============================================================
print("\n--- Popular Third-Party Packages ---\n")

popular = {
    "Web Development": [
        ("flask", "Lightweight web framework"),
        ("django", "Full-featured web framework"),
        ("fastapi", "Modern async API framework"),
    ],
    "Data Science": [
        ("pandas", "Data analysis & manipulation"),
        ("numpy", "Numerical computing"),
        ("matplotlib", "Charts & graphs"),
    ],
    "HTTP & APIs": [
        ("requests", "HTTP requests made easy"),
        ("httpx", "Async HTTP client"),
        ("beautifulsoup4", "Web scraping"),
    ],
    "Utilities": [
        ("python-dotenv", "Load .env files"),
        ("click", "CLI app framework"),
        ("rich", "Beautiful terminal output"),
    ],
    "Testing": [
        ("pytest", "Testing framework"),
        ("coverage", "Code coverage reporting"),
    ],
}

for category, packages in popular.items():
    print(f"  📦 {category}:")
    for name, desc in packages:
        print(f"     • {name:<20} — {desc}")
    print()

# ============================================================
# 📗 Checking If a Package Is Available
# ============================================================
print("--- Checking Package Availability ---\n")

def check_package(name):
    """Check if a package is installed."""
    try:
        __import__(name)
        return True
    except ImportError:
        return False

packages_to_check = ["json", "csv", "requests", "flask", "pandas", "numpy"]
for pkg in packages_to_check:
    status = "✅ Installed" if check_package(pkg) else "❌ Not installed"
    print(f"  {pkg:<12} {status}")

# ============================================================
# 📗 Practical: Project Setup Checklist
# ============================================================
print("\n--- Project Setup Checklist ---\n")

checklist = """
  When starting a new Python project:

  ⬜ 1. Create a project folder
       $ mkdir my_project && cd my_project

  ⬜ 2. Create a virtual environment
       $ python3 -m venv venv

  ⬜ 3. Activate it
       $ source venv/bin/activate

  ⬜ 4. Install packages you need
       $ pip install requests flask

  ⬜ 5. Save dependencies
       $ pip freeze > requirements.txt

  ⬜ 6. Create a .gitignore (exclude venv/)
       $ echo "venv/" > .gitignore

  ⬜ 7. Write your code!
       $ code .   (open in editor)

  ⬜ 8. When done, deactivate
       $ deactivate
"""
print(checklist)

# ============================================================
# 🧹 Cleanup
# ============================================================
if os.path.exists("requirements_sample.txt"):
    os.remove("requirements_sample.txt")
print("🧹 Cleaned up sample files!")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a virtual environment, activate it, and install
#    the 'requests' package
# 2. Run 'pip freeze' and save the output to requirements.txt
# 3. Check which packages are installed with 'pip list'
# 4. Try importing a package that's not installed — see the
#    ImportError message
# 5. Create a requirements.txt for a project with 3 packages
# ============================================================
