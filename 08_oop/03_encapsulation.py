# ============================================================
# 📘 Lesson 3: Encapsulation
# ============================================================
# Encapsulation is about PROTECTING data inside a class and
# controlling how the outside world can access or modify it.
#
# Think of it like a TV remote:
#   You press buttons (public interface)
#   But you don't touch the circuit board (private internals)
#
# Python conventions:
#   public      — name        (anyone can access)
#   protected   — _name       (hint: internal use, don't touch)
#   private     — __name      (name-mangled, hard to access)
#   property    — @property   (controlled access with getters/setters)
# ============================================================

# ============================================================
# 📗 Public vs Protected vs Private
# ============================================================
print("--- Access Levels ---\n")

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public — anyone can access
        self._salary = salary      # Protected — "please don't touch"
        self.__ssn = ssn           # Private — name-mangled by Python

emp = Employee("Amitesh", 80000, "123-45-6789")

# Public — works fine
print(f"  Public (name):     {emp.name}")

# Protected — works, but you SHOULDN'T access it directly
print(f"  Protected (salary): {emp._salary}")
print(f"    ⚠️  Convention only — Python won't stop you!")

# Private — direct access fails!
try:
    print(emp.__ssn)
except AttributeError as e:
    print(f"  Private (ssn):     ❌ {e}")

# But Python name-mangles it to _ClassName__attribute
print(f"  Mangled access:    {emp._Employee__ssn}")
print(f"    ⚠️  Possible but strongly discouraged!\n")

# ============================================================
# 📗 @property — The Pythonic Way (Getters & Setters)
# ============================================================
# Properties let you control attribute access with methods
# while keeping the simple attribute syntax: obj.attribute

print("--- @property (Getters & Setters) ---\n")

class Temperature:
    """Temperature with controlled access via @property."""

    def __init__(self, celsius):
        self._celsius = celsius    # Store internally

    @property
    def celsius(self):
        """Getter — called when you READ .celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter — called when you WRITE .celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Read-only computed property."""
        return self._celsius * 9/5 + 32

    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit:.1f}°F)"

temp = Temperature(25)
print(f"  Temperature: {temp}")

# Looks like attribute access, but calls the getter!
print(f"  Celsius:    {temp.celsius}")
print(f"  Fahrenheit: {temp.fahrenheit}")

# Looks like assignment, but calls the setter with validation!
temp.celsius = 100
print(f"  After set:  {temp}")

# Validation catches bad values
try:
    temp.celsius = -300
except ValueError as e:
    print(f"  ❌ {e}")

# fahrenheit is read-only (no setter defined)
try:
    temp.fahrenheit = 72
except AttributeError:
    print(f"  ❌ Can't set fahrenheit — it's read-only!")

# ============================================================
# 📗 Real Example: BankAccount with Encapsulation
# ============================================================
print("\n--- Encapsulated Bank Account ---\n")

class BankAccount:
    """Bank account with proper encapsulation."""

    _interest_rate = 0.04   # Protected class attribute (4%)

    def __init__(self, owner, initial_balance=0):
        self._owner = owner
        self.__balance = initial_balance    # Private!
        self.__transactions = []           # Private history

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        """Read-only balance — no direct setting allowed!"""
        return self.__balance

    @property
    def transaction_count(self):
        return len(self.__transactions)

    def deposit(self, amount):
        """The ONLY way to add money."""
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.__balance += amount
        self.__transactions.append(f"+₹{amount}")
        print(f"  💰 Deposited ₹{amount} → Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        """The ONLY way to remove money."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        self.__transactions.append(f"-₹{amount}")
        print(f"  💸 Withdrew ₹{amount} → Balance: ₹{self.__balance}")

    def get_statement(self):
        """View transaction history."""
        print(f"\n  📋 Statement for {self._owner}:")
        print(f"  {'─' * 30}")
        for i, t in enumerate(self.__transactions, 1):
            print(f"    {i}. {t}")
        print(f"  {'─' * 30}")
        print(f"  Balance: ₹{self.__balance}\n")

# Usage — data is safe!
acc = BankAccount("Amitesh", 5000)
acc.deposit(3000)
acc.withdraw(1000)

# Can READ balance via property
print(f"  Balance: ₹{acc.balance}")

# Can NOT set balance directly!
try:
    acc.balance = 1000000
except AttributeError:
    print("  ❌ Can't set balance directly — use deposit/withdraw!")

# Can NOT access private attributes
try:
    print(acc.__balance)
except AttributeError:
    print("  ❌ Can't access __balance from outside!")

acc.get_statement()

# ============================================================
# 📗 Property for Validation
# ============================================================
print("--- Property Validation ---\n")

class User:
    """User with validated properties."""

    def __init__(self, username, email, age):
        # Using setters for validation during __init__!
        self.username = username
        self.email = email
        self.age = age

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Username must be 3+ characters!")
        self._username = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value.strip().lower()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError(f"Age must be 0-150, got {value}")
        self._age = value

    def __str__(self):
        return f"  👤 {self._username} | {self._email} | Age: {self._age}"

# Valid user
user = User("Amitesh", "amitesh@example.com", 25)
print(user)

# Validation works during creation AND later updates
user.email = "NEW@EMAIL.COM"    # Setter normalizes to lowercase
print(f"  Updated email: {user.email}")

# Invalid values are caught
test_cases = [
    ("username", "ab"),
    ("email", "not-an-email"),
    ("age", -5),
]
for attr, bad_value in test_cases:
    try:
        setattr(user, attr, bad_value)
    except ValueError as e:
        print(f"  ❌ {attr} = {bad_value!r}: {e}")

# ============================================================
# 📗 Practical: Inventory Item
# ============================================================
print("\n--- Inventory Item ---\n")

class InventoryItem:
    """An item with controlled stock management."""

    def __init__(self, name, price, quantity=0):
        self._name = name
        self.price = price        # Uses setter
        self._quantity = max(0, quantity)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = round(value, 2)

    @property
    def quantity(self):
        return self._quantity

    @property
    def total_value(self):
        """Computed property — always up to date."""
        return self._price * self._quantity

    def add_stock(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        self._quantity += amount
        print(f"  📦 Added {amount} {self._name}(s) → Stock: {self._quantity}")

    def sell(self, amount):
        if amount > self._quantity:
            raise ValueError(f"Only {self._quantity} in stock!")
        self._quantity -= amount
        revenue = amount * self._price
        print(f"  🛒 Sold {amount} {self._name}(s) → "
              f"Revenue: ₹{revenue:.2f} | Stock: {self._quantity}")
        return revenue

    def __str__(self):
        return (f"  {self._name} | ₹{self._price:.2f} | "
                f"Stock: {self._quantity} | Value: ₹{self.total_value:.2f}")

# Build inventory
laptop = InventoryItem("Laptop", 85000, 10)
mouse = InventoryItem("Mouse", 499.99, 50)

print(laptop)
print(mouse)

laptop.sell(3)
mouse.add_stock(20)

print(f"\n  After transactions:")
print(laptop)
print(mouse)

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a Password class with a private __password that
#    can only be set if it meets strength requirements
# 2. Create a Circle class with a radius property where
#    setting radius auto-updates area and circumference
# 3. Create a Student class with a grade property that only
#    accepts values A-F
# 4. Create a Config class with read-only properties that
#    are set only once during __init__
# 5. Create a ShoppingCart class with encapsulated items list
#    and total_price computed property
# ============================================================
