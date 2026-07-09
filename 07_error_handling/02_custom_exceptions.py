# ============================================================
# 📘 Lesson 2: Custom Exceptions & Raising Errors
# ============================================================
# Sometimes Python's built-in exceptions aren't specific enough.
# You can CREATE your own exception types and RAISE them
# when something goes wrong in YOUR code.
#
# Key concepts:
#   raise          — manually trigger an error
#   class MyError(Exception) — define your own exception
#   assert         — quick checks during development
# ============================================================

# ============================================================
# 📗 raise — Manually Trigger Errors
# ============================================================
# Use 'raise' when YOUR code detects something invalid.
# You're telling Python: "This is wrong, stop here!"

print("--- raise — Triggering Errors ---")

def set_age(age):
    """Set age with validation."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be over 150!")
    print(f"  ✅ Age set to {age}")

# Test valid age
set_age(25)

# Test invalid ages
test_cases = [-5, 200, "twenty", 0, 100]
for test in test_cases:
    try:
        set_age(test)
    except (ValueError, TypeError) as e:
        print(f"  ❌ set_age({test!r}): {e}")

# ============================================================
# 📗 raise with Different Exception Types
# ============================================================
print("\n--- Raising Different Types ---")

def withdraw(balance, amount):
    """Withdraw money with validation."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError("Amount must be positive!")
    if amount > balance:
        raise ValueError(f"Insufficient funds! Balance: ₹{balance}, Requested: ₹{amount}")
    return balance - amount

# Test cases
tests = [
    (1000, 500),     # Valid
    (1000, 1500),    # Insufficient
    (1000, -100),    # Negative
    (1000, "five"),  # Wrong type
]

for balance, amount in tests:
    try:
        new_balance = withdraw(balance, amount)
        print(f"  ✅ Withdrew ₹{amount} → Balance: ₹{new_balance}")
    except (ValueError, TypeError) as e:
        print(f"  ❌ withdraw({balance}, {amount!r}): {e}")

# ============================================================
# 📗 Re-raising Exceptions
# ============================================================
# Sometimes you want to catch an error, log it, then let it
# continue up. Use 'raise' with no argument to re-raise.

print("\n--- Re-raising Exceptions ---")

def process_order(order_id, quantity):
    """Process order with logging and re-raising."""
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be positive!")
        print(f"  ✅ Order #{order_id}: {quantity} items processed")
    except ValueError as e:
        print(f"  📝 Logged error for order #{order_id}: {e}")
        raise  # Re-raise the same exception!

try:
    process_order(1, 5)     # Works
    process_order(2, -3)    # Fails, logs, then re-raises
except ValueError as e:
    print(f"  🔴 Caught re-raised error: {e}")

# ============================================================
# 📗 Custom Exception Classes
# ============================================================
# Create your own exceptions by inheriting from Exception.
# This makes your errors MORE SPECIFIC and easier to catch.

print("\n--- Custom Exception Classes ---")

# Simple custom exception
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass

# Custom exception with extra data
class InvalidAgeError(Exception):
    """Raised when age is not valid."""
    def __init__(self, age, message=None):
        self.age = age
        self.message = message or f"Invalid age: {age}"
        super().__init__(self.message)

# Custom exception with custom string representation
class PasswordTooWeakError(Exception):
    """Raised when password doesn't meet requirements."""
    def __init__(self, password, issues):
        self.password_length = len(password)
        self.issues = issues
        message = f"Password too weak! Issues: {', '.join(issues)}"
        super().__init__(message)

# --- Using Custom Exceptions ---
print("\n  Using InsufficientFundsError:")

def bank_withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw ₹{amount}. Balance: ₹{balance}"
        )
    return balance - amount

try:
    bank_withdraw(500, 1000)
except InsufficientFundsError as e:
    print(f"  ❌ {e}")

print("\n  Using InvalidAgeError:")

def register_user(name, age):
    if age < 13:
        raise InvalidAgeError(age, f"Must be 13+ to register (got {age})")
    if age > 120:
        raise InvalidAgeError(age)
    print(f"  ✅ Registered: {name}, age {age}")

for name, age in [("Amitesh", 25), ("Kid", 8), ("Ancient", 200)]:
    try:
        register_user(name, age)
    except InvalidAgeError as e:
        print(f"  ❌ {e} (received age: {e.age})")

print("\n  Using PasswordTooWeakError:")

def validate_password(password):
    issues = []
    if len(password) < 8:
        issues.append("too short (need 8+ chars)")
    if not any(c.isupper() for c in password):
        issues.append("needs uppercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("needs a digit")
    if issues:
        raise PasswordTooWeakError(password, issues)
    print(f"  ✅ Password accepted! ({len(password)} chars)")

for pwd in ["abc", "abcdefgh", "Abcdefgh", "Abcdefg1"]:
    try:
        validate_password(pwd)
    except PasswordTooWeakError as e:
        print(f"  ❌ '{pwd}': {e}")

# ============================================================
# 📗 Exception Hierarchy — Grouping Custom Exceptions
# ============================================================
# You can create a hierarchy of custom exceptions.
# Catching the parent catches all children too.

print("\n--- Exception Hierarchy ---")

class AppError(Exception):
    """Base exception for our application."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class ConnectionError_(AppError):
    """Network connection errors."""
    pass

class AuthenticationError(AppError):
    """Login/auth errors."""
    pass

def simulate_errors(error_type):
    if error_type == "db":
        raise DatabaseError("Table 'users' not found")
    elif error_type == "net":
        raise ConnectionError_("Server timeout after 30s")
    elif error_type == "auth":
        raise AuthenticationError("Invalid token")

for err in ["db", "net", "auth"]:
    try:
        simulate_errors(err)
    except AppError as e:
        # Catches ALL app errors (parent catches children!)
        print(f"  {type(e).__name__}: {e}")

# ============================================================
# 📗 assert — Quick Development Checks
# ============================================================
# assert checks a condition. If False → AssertionError.
# Great for catching bugs during development.
# NOTE: assert can be disabled with python -O flag!

print("\n--- assert Statements ---")

def calculate_average(scores):
    """Calculate average with assertions."""
    assert isinstance(scores, list), "Scores must be a list!"
    assert len(scores) > 0, "Scores list cannot be empty!"
    assert all(isinstance(s, (int, float)) for s in scores), "All scores must be numbers!"
    return sum(scores) / len(scores)

# Valid
avg = calculate_average([85, 92, 78, 95, 88])
print(f"  Average: {avg}")

# Invalid — caught by assert
test_cases = [
    ("not a list", "string input"),
    ([], "empty list"),
    ([85, "ninety", 78], "non-number in list"),
]

for data, label in test_cases:
    try:
        calculate_average(data)
    except AssertionError as e:
        print(f"  ❌ {label}: {e}")

# ============================================================
# 📗 Practical: Validated Data Class
# ============================================================
print("\n--- Validated Student Class ---")

class StudentValidationError(Exception):
    """Error in student data validation."""
    pass

class Student:
    """A student with validated data."""
    def __init__(self, name, age, grade):
        # Validate name
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise StudentValidationError("Name must be a non-empty string")
        # Validate age
        if not isinstance(age, int) or age < 5 or age > 100:
            raise StudentValidationError(f"Age must be 5-100, got {age}")
        # Validate grade
        valid_grades = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]
        if grade not in valid_grades:
            raise StudentValidationError(f"Invalid grade: {grade}")

        self.name = name.strip()
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.grade})"

# Test valid and invalid students
test_students = [
    ("Amitesh", 25, "A"),
    ("", 20, "B"),
    ("Priya", 3, "A"),
    ("Rahul", 24, "Z"),
]

for name, age, grade in test_students:
    try:
        s = Student(name, age, grade)
        print(f"  ✅ Created: {s}")
    except StudentValidationError as e:
        print(f"  ❌ Student({name!r}, {age}, {grade!r}): {e}")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a custom NegativeNumberError — raise it when a
#    function receives a negative number
# 2. Create an EmailValidationError with an 'email' attribute
# 3. Build a hierarchy: PaymentError → CardDeclined,
#    InsufficientBalance, ExpiredCard
# 4. Write a function using assert to validate a config dict
# 5. Create a Temperature class that raises errors for
#    impossible values (below -273.15°C)
# ============================================================
