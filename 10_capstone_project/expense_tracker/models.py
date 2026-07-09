# ============================================================
# 🏆 CAPSTONE: Expense Tracker — Models
# ============================================================
# This module defines the core data classes for the app.
#
# Concepts used:
#   ✅ Module 8: OOP — classes, inheritance, encapsulation
#   ✅ Module 7: Error handling — custom exceptions, validation
#   ✅ Module 9: Modules — this IS a custom module
# ============================================================

"""
models — Core data classes for the Expense Tracker.

Classes:
    Category    — expense category with budget tracking
    Expense     — a single expense entry
    ExpenseBook — manages all expenses and categories
"""

from datetime import datetime, date

# ============================================================
# 📗 Custom Exceptions
# ============================================================

class ExpenseError(Exception):
    """Base exception for expense tracker."""
    pass

class InvalidAmountError(ExpenseError):
    """Raised when expense amount is invalid."""
    def __init__(self, amount):
        super().__init__(f"Invalid amount: {amount}. Must be a positive number.")

class InvalidCategoryError(ExpenseError):
    """Raised when category is not recognized."""
    def __init__(self, category):
        super().__init__(f"Unknown category: '{category}'")

class DuplicateCategoryError(ExpenseError):
    """Raised when trying to add a category that already exists."""
    def __init__(self, name):
        super().__init__(f"Category '{name}' already exists!")

# ============================================================
# 📗 Category Class
# ============================================================

class Category:
    """An expense category with optional monthly budget."""

    def __init__(self, name, emoji="📁", budget=0.0):
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty!")
        self._name = name.strip().title()
        self._emoji = emoji
        self._budget = max(0.0, float(budget))

    @property
    def name(self):
        return self._name

    @property
    def emoji(self):
        return self._emoji

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Budget cannot be negative!")
        self._budget = float(value)

    def __str__(self):
        budget_str = f" (Budget: ₹{self._budget:,.2f})" if self._budget > 0 else ""
        return f"{self._emoji} {self._name}{budget_str}"

    def __eq__(self, other):
        if isinstance(other, Category):
            return self._name.lower() == other._name.lower()
        if isinstance(other, str):
            return self._name.lower() == other.lower()
        return False

    def __hash__(self):
        return hash(self._name.lower())

    def to_dict(self):
        return {
            "name": self._name,
            "emoji": self._emoji,
            "budget": self._budget,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("emoji", "📁"), data.get("budget", 0.0))

# ============================================================
# 📗 Expense Class
# ============================================================

class Expense:
    """A single expense entry."""

    _id_counter = 0

    def __init__(self, amount, category, description="", expense_date=None):
        # Validate amount
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise InvalidAmountError(amount)
        if amount <= 0:
            raise InvalidAmountError(amount)

        # Validate category
        if not category:
            raise ValueError("Category is required!")

        Expense._id_counter += 1
        self._id = Expense._id_counter
        self._amount = round(amount, 2)
        self._category = category.strip().title() if isinstance(category, str) else str(category)
        self._description = description.strip() if description else ""
        self._date = expense_date or date.today()
        self._created_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise InvalidAmountError(value)
        if value <= 0:
            raise InvalidAmountError(value)
        self._amount = round(value, 2)

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date

    def __str__(self):
        desc = f" — {self._description}" if self._description else ""
        return (f"  [{self._id:03d}] {self._date.strftime('%d %b')} | "
                f"₹{self._amount:>10,.2f} | {self._category}{desc}")

    def __repr__(self):
        return f"Expense(₹{self._amount}, '{self._category}', '{self._date}')"

    def __lt__(self, other):
        return self._date < other._date

    def to_dict(self):
        return {
            "id": self._id,
            "amount": self._amount,
            "category": self._category,
            "description": self._description,
            "date": self._date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        exp = cls.__new__(cls)
        exp._id = data["id"]
        exp._amount = data["amount"]
        exp._category = data["category"]
        exp._description = data.get("description", "")
        exp._date = date.fromisoformat(data["date"])
        exp._created_at = datetime.now()
        # Keep ID counter in sync
        if data["id"] >= Expense._id_counter:
            Expense._id_counter = data["id"]
        return exp

# ============================================================
# 📗 ExpenseBook Class — The Core Manager
# ============================================================

class ExpenseBook:
    """Manages all expenses and categories."""

    DEFAULT_CATEGORIES = [
        Category("Food", "🍔", 5000),
        Category("Transport", "🚗", 3000),
        Category("Shopping", "🛍️", 4000),
        Category("Bills", "📄", 6000),
        Category("Entertainment", "🎬", 2000),
        Category("Health", "🏥", 2000),
        Category("Education", "📚", 3000),
        Category("Other", "📦", 0),
    ]

    def __init__(self, owner="User"):
        self._owner = owner
        self._expenses = []
        self._categories = list(self.DEFAULT_CATEGORIES)

    @property
    def owner(self):
        return self._owner

    @property
    def expenses(self):
        return list(self._expenses)

    @property
    def categories(self):
        return list(self._categories)

    @property
    def category_names(self):
        return [c.name for c in self._categories]

    # --- Expense Operations ---

    def add_expense(self, amount, category_name, description="", expense_date=None):
        """Add a new expense."""
        if category_name.strip().title() not in self.category_names:
            raise InvalidCategoryError(category_name)
        expense = Expense(amount, category_name, description, expense_date)
        self._expenses.append(expense)
        return expense

    def delete_expense(self, expense_id):
        """Delete an expense by ID."""
        for i, exp in enumerate(self._expenses):
            if exp.id == expense_id:
                removed = self._expenses.pop(i)
                return removed
        raise ExpenseError(f"Expense #{expense_id} not found!")

    def edit_expense(self, expense_id, amount=None, description=None):
        """Edit an existing expense."""
        for exp in self._expenses:
            if exp.id == expense_id:
                if amount is not None:
                    exp.amount = amount
                if description is not None:
                    exp._description = description.strip()
                return exp
        raise ExpenseError(f"Expense #{expense_id} not found!")

    # --- Category Operations ---

    def add_category(self, name, emoji="📁", budget=0.0):
        """Add a new category."""
        new_cat = Category(name, emoji, budget)
        if new_cat in self._categories:
            raise DuplicateCategoryError(name)
        self._categories.append(new_cat)
        return new_cat

    def get_category(self, name):
        """Get a category by name."""
        for cat in self._categories:
            if cat == name:
                return cat
        return None

    # --- Query & Filter ---

    def get_expenses_by_category(self, category_name):
        """Get all expenses in a category."""
        return [e for e in self._expenses
                if e.category.lower() == category_name.lower()]

    def get_expenses_by_date_range(self, start_date, end_date):
        """Get expenses within a date range."""
        return [e for e in self._expenses
                if start_date <= e.date <= end_date]

    def get_expenses_by_month(self, year, month):
        """Get expenses for a specific month."""
        return [e for e in self._expenses
                if e.date.year == year and e.date.month == month]

    def search_expenses(self, query):
        """Search expenses by description or category."""
        query = query.lower()
        return [e for e in self._expenses
                if query in e.description.lower() or query in e.category.lower()]

    # --- Statistics ---

    def total_spent(self, expenses=None):
        """Calculate total amount spent."""
        exps = expenses if expenses is not None else self._expenses
        return sum(e.amount for e in exps)

    def category_totals(self, expenses=None):
        """Get spending totals per category."""
        exps = expenses if expenses is not None else self._expenses
        totals = {}
        for exp in exps:
            totals[exp.category] = totals.get(exp.category, 0) + exp.amount
        return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))

    def daily_average(self, expenses=None):
        """Calculate daily average spending."""
        exps = expenses if expenses is not None else self._expenses
        if not exps:
            return 0
        dates = set(e.date for e in exps)
        return self.total_spent(exps) / len(dates)

    def budget_status(self):
        """Check budget status for current month."""
        now = date.today()
        monthly = self.get_expenses_by_month(now.year, now.month)
        cat_totals = self.category_totals(monthly)

        status = []
        for cat in self._categories:
            if cat.budget > 0:
                spent = cat_totals.get(cat.name, 0)
                remaining = cat.budget - spent
                percent = (spent / cat.budget * 100) if cat.budget else 0
                status.append({
                    "category": cat,
                    "budget": cat.budget,
                    "spent": spent,
                    "remaining": remaining,
                    "percent": percent,
                })
        return status

    # --- Serialization ---

    def to_dict(self):
        return {
            "owner": self._owner,
            "expenses": [e.to_dict() for e in self._expenses],
            "categories": [c.to_dict() for c in self._categories],
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data.get("owner", "User"))
        book._categories = [Category.from_dict(c) for c in data.get("categories", [])]
        book._expenses = [Expense.from_dict(e) for e in data.get("expenses", [])]
        return book

    def __len__(self):
        return len(self._expenses)

    def __str__(self):
        return (f"ExpenseBook(owner='{self._owner}', "
                f"expenses={len(self._expenses)}, "
                f"categories={len(self._categories)})")
