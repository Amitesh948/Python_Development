# ============================================================
# 🏆 CAPSTONE PROJECT: Expense Tracker CLI App 💰
# ============================================================
# The FINAL project — bringing together EVERYTHING you've
# learned across all 10 modules!
#
# Modules used:
#   ✅ 01 Basics         — variables, strings, numbers, print
#   ✅ 02 Input/Conds    — user input, if/else decisions
#   ✅ 03 Loops          — while loop for menu, for loop lists
#   ✅ 04 Data Structs   — lists, dicts for expenses & stats
#   ✅ 05 Functions      — modular, reusable code everywhere
#   ✅ 06 File Handling   — JSON save/load, CSV export
#   ✅ 07 Error Handling  — try/except, custom exceptions
#   ✅ 08 OOP            — Expense, Category, ExpenseBook classes
#   ✅ 09 Modules        — split into models.py, utils.py, main.py
#
# Run with:  python3 main.py
# ============================================================

# --- Standard library imports ---
import os
import sys
from datetime import date, datetime, timedelta

# --- Custom module imports ---
from models import (
    ExpenseBook, Expense, Category,
    ExpenseError, InvalidAmountError, InvalidCategoryError,
)
from utils import (
    save_data, load_data, export_to_csv,
    get_input, get_number, get_date, get_choice, confirm,
    format_currency, print_header, print_divider,
    progress_bar, get_month_name,
)

# ============================================================
# 📗 Main Menu
# ============================================================

def show_main_menu():
    """Display the main application menu."""
    print("\n╔══════════════════════════════════════════╗")
    print("║        💰 EXPENSE TRACKER                ║")
    print("╠══════════════════════════════════════════╣")
    print("║                                          ║")
    print("║   📝 EXPENSES                            ║")
    print("║   1.  Add Expense                        ║")
    print("║   2.  View All Expenses                  ║")
    print("║   3.  View by Category                   ║")
    print("║   4.  Search Expenses                    ║")
    print("║   5.  Edit Expense                       ║")
    print("║   6.  Delete Expense                     ║")
    print("║                                          ║")
    print("║   📊 REPORTS                             ║")
    print("║   7.  Monthly Summary                    ║")
    print("║   8.  Budget Status                      ║")
    print("║   9.  Category Breakdown                 ║")
    print("║                                          ║")
    print("║   ⚙️  SETTINGS                           ║")
    print("║   10. Manage Categories                  ║")
    print("║   11. Export to CSV                      ║")
    print("║   12. Quick Stats                        ║")
    print("║                                          ║")
    print("║   0.  Exit & Save                        ║")
    print("║                                          ║")
    print("╚══════════════════════════════════════════╝")

# ============================================================
# 📗 Feature Functions
# ============================================================

def add_expense(book):
    """Add a new expense entry."""
    print_header("➕ Add New Expense")

    # Pick category
    print("\n  Choose a category:")
    cat_name = get_choice("  Category", [str(c) for c in book.categories])
    # Extract just the category name (remove emoji prefix)
    cat_name = cat_name.split(" ", 1)[1].split(" (")[0].strip()

    # Get amount
    amount = get_number("  Amount (₹)", min_val=0.01)
    if amount is None:
        print("  ❌ Cancelled.")
        return

    # Get description
    description = get_input("  Description", required=False, default="")

    # Get date
    expense_date = get_date("  Date (YYYY-MM-DD)")

    try:
        expense = book.add_expense(amount, cat_name, description, expense_date)
        save_data(book)
        print(f"\n  ✅ Added: {format_currency(expense.amount)} → {expense.category}")
        if expense.description:
            print(f"     📝 {expense.description}")
    except ExpenseError as e:
        print(f"\n  ❌ {e}")


def view_expenses(book, expenses=None, title="All Expenses"):
    """Display expenses in a formatted list."""
    exps = expenses if expenses is not None else book.expenses

    if not exps:
        print(f"\n  📭 No expenses to show!")
        return

    exps_sorted = sorted(exps, key=lambda e: e.date, reverse=True)
    total = sum(e.amount for e in exps_sorted)

    print_header(f"📋 {title} ({len(exps_sorted)} entries)")
    print()

    current_month = None
    for exp in exps_sorted:
        month_key = exp.date.strftime("%B %Y")
        if month_key != current_month:
            current_month = month_key
            print(f"\n  ── {month_key} ──")
        print(exp)

    print_divider("═")
    print(f"  {'TOTAL':<38} {format_currency(total):>12}")
    print()


def view_by_category(book):
    """View expenses filtered by category."""
    print_header("📂 View by Category")
    print("\n  Choose a category:")
    cat_name = get_choice("  Category", [str(c) for c in book.categories])
    cat_name = cat_name.split(" ", 1)[1].split(" (")[0].strip()

    expenses = book.get_expenses_by_category(cat_name)
    view_expenses(book, expenses, f"{cat_name} Expenses")


def search_expenses(book):
    """Search expenses by keyword."""
    print_header("🔍 Search Expenses")
    query = get_input("\n  Search term")
    results = book.search_expenses(query)
    view_expenses(book, results, f"Results for '{query}'")


def edit_expense(book):
    """Edit an existing expense."""
    print_header("✏️ Edit Expense")

    if not book.expenses:
        print("\n  📭 No expenses to edit!")
        return

    # Show recent expenses
    recent = sorted(book.expenses, key=lambda e: e.date, reverse=True)[:10]
    print("\n  Recent expenses:")
    for exp in recent:
        print(exp)

    exp_id = get_number("\n  Expense ID to edit", allow_float=False)
    if exp_id is None:
        return

    try:
        # Get new values (empty = keep current)
        new_amount = get_number("  New amount (Enter to keep)", min_val=0.01)
        new_desc = input("  New description (Enter to keep): ").strip() or None

        expense = book.edit_expense(int(exp_id), new_amount, new_desc)
        save_data(book)
        print(f"\n  ✅ Updated expense #{int(exp_id)}")
        print(f"     {expense}")
    except ExpenseError as e:
        print(f"\n  ❌ {e}")


def delete_expense(book):
    """Delete an expense."""
    print_header("🗑️ Delete Expense")

    if not book.expenses:
        print("\n  📭 No expenses to delete!")
        return

    recent = sorted(book.expenses, key=lambda e: e.date, reverse=True)[:10]
    print("\n  Recent expenses:")
    for exp in recent:
        print(exp)

    exp_id = get_number("\n  Expense ID to delete", allow_float=False)
    if exp_id is None:
        return

    try:
        expense = book.delete_expense(int(exp_id))
        if confirm(f"  Delete {format_currency(expense.amount)} from {expense.category}?"):
            save_data(book)
            print(f"  ✅ Deleted expense #{int(exp_id)}")
        else:
            # Re-add if cancelled
            book._expenses.append(expense)
            print("  ↩️ Cancelled.")
    except ExpenseError as e:
        print(f"\n  ❌ {e}")


def monthly_summary(book):
    """Show summary for a specific month."""
    print_header("📅 Monthly Summary")

    now = date.today()
    year = get_number(f"\n  Year", min_val=2020, max_val=2030, allow_float=False)
    if year is None:
        year = now.year
    month = get_number(f"  Month (1-12)", min_val=1, max_val=12, allow_float=False)
    if month is None:
        month = now.month

    year, month = int(year), int(month)
    expenses = book.get_expenses_by_month(year, month)
    month_name = get_month_name(month)

    if not expenses:
        print(f"\n  📭 No expenses in {month_name} {year}!")
        return

    total = book.total_spent(expenses)
    cat_totals = book.category_totals(expenses)
    avg = book.daily_average(expenses)

    print(f"\n  📅 {month_name} {year}")
    print_divider()
    print(f"  💰 Total spent:    {format_currency(total)}")
    print(f"  📊 Daily average:  {format_currency(avg)}")
    print(f"  📝 Transactions:   {len(expenses)}")

    print(f"\n  By category:")
    for cat, amount in cat_totals.items():
        percent = amount / total * 100
        bar = "█" * int(percent / 5) + "░" * (20 - int(percent / 5))
        print(f"    {cat:<15} {format_currency(amount):>12}  [{bar}] {percent:.1f}%")


def budget_status(book):
    """Show budget status for current month."""
    print_header("📊 Budget Status")

    status = book.budget_status()
    now = date.today()
    month_name = get_month_name(now.month)

    if not status:
        print("\n  📭 No budgets set!")
        return

    print(f"\n  📅 {month_name} {now.year} — Budget Overview\n")

    total_budget = 0
    total_spent = 0

    for item in status:
        cat = item["category"]
        bar = progress_bar(item["spent"], item["budget"], width=20, label="")
        print(f"  {cat.emoji} {cat.name:<14} {bar}")
        print(f"     Spent: {format_currency(item['spent']):>10} / "
              f"{format_currency(item['budget'])}  "
              f"(Remaining: {format_currency(item['remaining'])})")
        print()

        total_budget += item["budget"]
        total_spent += item["spent"]

    print_divider("═")
    overall = progress_bar(total_spent, total_budget, width=20)
    print(f"  TOTAL: {format_currency(total_spent)} / "
          f"{format_currency(total_budget)}  {overall}")


def category_breakdown(book):
    """Show a detailed category breakdown."""
    print_header("📊 Category Breakdown")

    if not book.expenses:
        print("\n  📭 No expenses yet!")
        return

    cat_totals = book.category_totals()
    total = book.total_spent()

    print(f"\n  Total: {format_currency(total)}\n")

    for cat_name, amount in cat_totals.items():
        percent = amount / total * 100
        count = len(book.get_expenses_by_category(cat_name))
        cat = book.get_category(cat_name)
        emoji = cat.emoji if cat else "📁"

        bar_len = int(percent / 2.5)
        bar = "█" * bar_len + "░" * (40 - bar_len)

        print(f"  {emoji} {cat_name}")
        print(f"    {format_currency(amount):>12} ({percent:>5.1f}%) "
              f"| {count} expense(s)")
        print(f"    [{bar}]")
        print()


def manage_categories(book):
    """Add or view categories."""
    print_header("⚙️ Manage Categories")

    print("\n  Current categories:\n")
    for cat in book.categories:
        print(f"    {cat}")

    print(f"\n  1. Add new category")
    print(f"  2. Go back")

    choice = input("\n  Choice: ").strip()
    if choice == "1":
        name = get_input("  Category name")
        emoji = get_input("  Emoji", required=False, default="📁")
        budget = get_number("  Monthly budget (0 for none)", min_val=0) or 0

        try:
            cat = book.add_category(name, emoji, budget)
            save_data(book)
            print(f"\n  ✅ Added category: {cat}")
        except ExpenseError as e:
            print(f"\n  ❌ {e}")


def export_data(book):
    """Export expenses to CSV."""
    print_header("📤 Export to CSV")

    if not book.expenses:
        print("\n  📭 No expenses to export!")
        return

    filename = export_to_csv(book.expenses)
    if filename:
        print(f"\n  ✅ Exported {len(book.expenses)} expenses to:")
        print(f"     📄 {filename}")


def quick_stats(book):
    """Show quick overview statistics."""
    print_header("📊 Quick Stats")

    if not book.expenses:
        print("\n  📭 No expenses yet! Add some to see stats.")
        return

    now = date.today()
    all_expenses = book.expenses
    month_expenses = book.get_expenses_by_month(now.year, now.month)

    # All time
    total_all = book.total_spent()
    cat_totals = book.category_totals()
    top_category = list(cat_totals.keys())[0] if cat_totals else "N/A"

    # This month
    total_month = book.total_spent(month_expenses)
    avg_daily = book.daily_average(month_expenses)

    # Biggest expense
    biggest = max(all_expenses, key=lambda e: e.amount)
    smallest = min(all_expenses, key=lambda e: e.amount)

    month_name = get_month_name(now.month)

    print(f"""
  ╔═══════════════════════════════════════╗
  ║           📊 OVERVIEW                 ║
  ╠═══════════════════════════════════════╣
  ║                                       ║
  ║  📝 Total expenses:   {len(all_expenses):<15}║
  ║  💰 Total spent:      {format_currency(total_all):<15}║
  ║  🏷️  Top category:     {top_category:<15}║
  ║                                       ║
  ╠═══════════════════════════════════════╣
  ║  📅 {month_name} {now.year}                       ║
  ╠═══════════════════════════════════════╣
  ║                                       ║
  ║  💳 This month:       {format_currency(total_month):<15}║
  ║  📊 Daily average:    {format_currency(avg_daily):<15}║
  ║  📝 Transactions:     {len(month_expenses):<15}║
  ║                                       ║
  ╠═══════════════════════════════════════╣
  ║  🔝 Biggest:  {format_currency(biggest.amount)} ({biggest.category}){' ' * max(0, 7 - len(biggest.category))}║
  ║  🔻 Smallest: {format_currency(smallest.amount)} ({smallest.category}){' ' * max(0, 7 - len(smallest.category))}║
  ╚═══════════════════════════════════════╝
""")


# ============================================================
# 📗 Sample Data (for first run)
# ============================================================

def add_sample_data(book):
    """Add sample expenses so the app isn't empty on first run."""
    today = date.today()

    samples = [
        (250,   "Food",          "Morning coffee & breakfast",   today - timedelta(days=0)),
        (1500,  "Transport",     "Uber to office",               today - timedelta(days=0)),
        (450,   "Food",          "Lunch at cafe",                today - timedelta(days=1)),
        (2999,  "Shopping",      "New headphones",               today - timedelta(days=1)),
        (800,   "Entertainment", "Movie tickets",                today - timedelta(days=2)),
        (350,   "Food",          "Groceries",                    today - timedelta(days=2)),
        (1200,  "Bills",         "Phone recharge",               today - timedelta(days=3)),
        (5500,  "Bills",         "Electricity bill",             today - timedelta(days=4)),
        (200,   "Food",          "Evening snacks",               today - timedelta(days=4)),
        (3500,  "Health",        "Doctor visit",                 today - timedelta(days=5)),
        (150,   "Transport",     "Bus pass",                     today - timedelta(days=5)),
        (999,   "Education",     "Online course",                today - timedelta(days=6)),
        (680,   "Food",          "Dinner with friends",          today - timedelta(days=7)),
        (4200,  "Shopping",      "New shoes",                    today - timedelta(days=8)),
        (350,   "Entertainment", "Spotify subscription",         today - timedelta(days=10)),
    ]

    for amount, category, desc, exp_date in samples:
        book.add_expense(amount, category, desc, exp_date)

    save_data(book)
    print(f"  📦 Loaded {len(samples)} sample expenses to get you started!")


# ============================================================
# 🎮 MAIN APPLICATION LOOP
# ============================================================

def main():
    """Main application entry point."""
    print("\n" + "═" * 46)
    print("   💰 EXPENSE TRACKER — Capstone Project 🏆")
    print("═" * 46)
    print("   Bringing together ALL Python fundamentals!")
    print("═" * 46)

    # Load or create expense book
    data = load_data()
    if data:
        book = ExpenseBook.from_dict(data)
        print(f"\n  ✅ Loaded {len(book)} expenses for '{book.owner}'")
    else:
        name = get_input("\n  👤 What's your name", default="Amitesh")
        book = ExpenseBook(name)
        print(f"\n  🎉 Welcome, {name}! Created your expense book.")

        if confirm("  Load sample data to explore the app?"):
            add_sample_data(book)

    # Action mapping
    actions = {
        "1":  ("Add Expense",       lambda: add_expense(book)),
        "2":  ("View All",          lambda: view_expenses(book)),
        "3":  ("View by Category",  lambda: view_by_category(book)),
        "4":  ("Search",            lambda: search_expenses(book)),
        "5":  ("Edit Expense",      lambda: edit_expense(book)),
        "6":  ("Delete Expense",    lambda: delete_expense(book)),
        "7":  ("Monthly Summary",   lambda: monthly_summary(book)),
        "8":  ("Budget Status",     lambda: budget_status(book)),
        "9":  ("Category Breakdown", lambda: category_breakdown(book)),
        "10": ("Manage Categories", lambda: manage_categories(book)),
        "11": ("Export CSV",        lambda: export_data(book)),
        "12": ("Quick Stats",       lambda: quick_stats(book)),
    }

    # Main loop
    while True:
        try:
            show_main_menu()
            choice = input("\n  Choose (0-12): ").strip()

            if choice == "0":
                save_data(book)
                print(f"\n  💾 Data saved! ({len(book)} expenses)")
                print("  👋 Goodbye! Keep tracking those expenses!")
                print("\n  🏆 CONGRATULATIONS! 🏆")
                print("  You've completed all 10 modules of your")
                print("  Python Learning Journey! 🐍🎉")
                print()
                break

            elif choice in actions:
                name, action = actions[choice]
                action()

            else:
                print("  ❌ Invalid choice! Pick 0-12.")

        except KeyboardInterrupt:
            print("\n\n  ⚠️ Use option 0 to exit and save.")

        except ExpenseError as e:
            print(f"  ❌ {e}")

        except Exception as e:
            print(f"  🔴 Unexpected error: {type(e).__name__}: {e}")


# ============================================================
# 📗 Entry Point — if __name__ == "__main__"
# ============================================================

if __name__ == "__main__":
    main()
