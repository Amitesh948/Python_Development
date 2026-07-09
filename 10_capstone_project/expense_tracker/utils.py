# ============================================================
# 🏆 CAPSTONE: Expense Tracker — Utilities
# ============================================================
# Helper functions for I/O, formatting, and display.
#
# Concepts used:
#   ✅ Module 6: File handling — JSON read/write
#   ✅ Module 6: CSV export
#   ✅ Module 5: Functions — reusable helpers
#   ✅ Module 9: Built-in modules — os, json, csv, datetime
# ============================================================

"""
utils — Utility functions for the Expense Tracker.

Functions for file I/O, user input, formatting, and display.
"""

import json
import csv
import os
from datetime import date, datetime

# ============================================================
# 📗 File I/O
# ============================================================

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")

def ensure_data_dir():
    """Create the data directory if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

def save_data(expense_book):
    """Save expense book to JSON file."""
    ensure_data_dir()
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expense_book.to_dict(), f, indent=2)
        return True
    except IOError as e:
        print(f"  ❌ Could not save data: {e}")
        return False

def load_data():
    """Load expense book from JSON file. Returns dict or None."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("  ⚠️ Data file is corrupted. Starting fresh.")
        return None

def export_to_csv(expenses, filename=None):
    """Export expenses to CSV file."""
    ensure_data_dir()
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(DATA_DIR, f"expenses_export_{timestamp}.csv")

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Date", "Category", "Amount", "Description"])
            for exp in sorted(expenses, key=lambda e: e.date):
                writer.writerow([
                    exp.id,
                    exp.date.isoformat(),
                    exp.category,
                    f"{exp.amount:.2f}",
                    exp.description,
                ])
        return filename
    except IOError as e:
        print(f"  ❌ Export failed: {e}")
        return None

# ============================================================
# 📗 Input Helpers
# ============================================================

def get_input(prompt, required=True, default=None):
    """Get string input with optional default."""
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{prompt}{suffix}: ").strip()
        if not value and default:
            return default
        if value or not required:
            return value
        print("  ❌ This field is required!")

def get_number(prompt, min_val=None, max_val=None, allow_float=True):
    """Get a numeric input with validation."""
    while True:
        try:
            raw = input(f"{prompt}: ").strip()
            if not raw:
                return None
            value = float(raw) if allow_float else int(raw)
            if min_val is not None and value < min_val:
                print(f"  ❌ Must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"  ❌ Must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("  ❌ Please enter a valid number!")

def get_date(prompt, default_today=True):
    """Get a date input (YYYY-MM-DD format)."""
    while True:
        default_str = date.today().isoformat() if default_today else ""
        suffix = f" [{default_str}]" if default_str else ""
        raw = input(f"{prompt}{suffix}: ").strip()

        if not raw and default_today:
            return date.today()
        if not raw:
            print("  ❌ Date is required!")
            continue

        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("  ❌ Use YYYY-MM-DD format (e.g., 2026-07-07)")

def get_choice(prompt, options):
    """Get a choice from numbered options. Returns the chosen option."""
    for i, option in enumerate(options, 1):
        print(f"    {i}. {option}")
    while True:
        try:
            choice = int(input(f"\n{prompt}: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print(f"  ❌ Pick 1-{len(options)}")
        except ValueError:
            print("  ❌ Enter a number!")

def confirm(prompt):
    """Ask yes/no confirmation."""
    return input(f"{prompt} (y/N): ").strip().lower() == "y"

# ============================================================
# 📗 Display / Formatting Helpers
# ============================================================

def format_currency(amount):
    """Format number as Indian Rupee currency."""
    return f"₹{amount:,.2f}"

def print_header(title):
    """Print a styled section header."""
    width = max(len(title) + 8, 40)
    print(f"\n  ╔{'═' * width}╗")
    print(f"  ║{title:^{width}}║")
    print(f"  ╚{'═' * width}╝")

def print_divider(char="─", width=50):
    """Print a divider line."""
    print(f"  {char * width}")

def print_table(headers, rows, col_widths=None):
    """Print a formatted table."""
    if not col_widths:
        col_widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=5)) + 2
                      for i, h in enumerate(headers)]

    # Header
    header_line = "  "
    for h, w in zip(headers, col_widths):
        header_line += f"{h:<{w}}"
    print(header_line)
    print("  " + "─" * sum(col_widths))

    # Rows
    for row in rows:
        row_line = "  "
        for val, w in zip(row, col_widths):
            row_line += f"{str(val):<{w}}"
        print(row_line)

def progress_bar(current, total, width=20, label=""):
    """Create a text-based progress bar."""
    if total == 0:
        return f"{label} [{'░' * width}] 0%"
    percent = min(current / total, 1.0)
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)

    if percent >= 1.0:
        color_icon = "🔴"
    elif percent >= 0.75:
        color_icon = "🟡"
    else:
        color_icon = "🟢"

    return f"{label} {color_icon} [{bar}] {percent * 100:.0f}%"

def get_month_name(month_num):
    """Get month name from number."""
    months = ["", "January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]
    return months[month_num] if 1 <= month_num <= 12 else "Unknown"
