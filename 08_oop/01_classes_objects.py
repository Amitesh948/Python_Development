# ============================================================
# 📘 Lesson 1: Classes & Objects
# ============================================================
# Object-Oriented Programming (OOP) lets you model real-world
# things as code. A CLASS is a blueprint, an OBJECT is the
# actual thing built from that blueprint.
#
# Think of it like:
#   Class  = Cookie cutter 🍪 (the shape/template)
#   Object = Actual cookie   (made from the cutter)
#
# Syntax:
#   class ClassName:
#       def __init__(self):    # Constructor
#           self.attribute = value
#       def method(self):
#           do something
# ============================================================

# ============================================================
# 📗 Your First Class
# ============================================================
print("--- Your First Class ---\n")

class Dog:
    """A simple Dog class — our first blueprint!"""

    def __init__(self, name, breed, age):
        """Constructor — runs automatically when creating a Dog."""
        self.name = name      # Instance attribute
        self.breed = breed
        self.age = age

    def bark(self):
        """Make the dog bark."""
        print(f"  {self.name}: Woof! Woof! 🐕")

    def info(self):
        """Display dog information."""
        print(f"  🐶 {self.name} | Breed: {self.breed} | Age: {self.age}")

# Creating objects (instances) from the class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "German Shepherd", 5)
dog3 = Dog("Luna", "Labrador", 2)

# Using methods
dog1.info()
dog1.bark()
dog2.info()
dog3.info()

# Accessing attributes directly
print(f"\n  {dog1.name} is {dog1.age} years old")

# ============================================================
# 📗 Understanding 'self'
# ============================================================
# 'self' refers to the CURRENT object. When you call
# dog1.bark(), Python passes dog1 as 'self' automatically.
#
#   dog1.bark()  →  Dog.bark(dog1)  ← Python does this!
#
# self.name means "this particular dog's name"

print("\n--- Understanding self ---")

class Cat:
    def __init__(self, name):
        self.name = name     # self.name belongs to THIS cat

    def introduce(self):
        # self refers to whichever cat calls this method
        print(f"  Meow! I'm {self.name} 🐱")

cat1 = Cat("Whiskers")
cat2 = Cat("Mittens")
cat1.introduce()   # self = cat1, so self.name = "Whiskers"
cat2.introduce()   # self = cat2, so self.name = "Mittens"

# ============================================================
# 📗 __init__ — The Constructor
# ============================================================
# __init__ is called AUTOMATICALLY when you create an object.
# Use it to set up the object's initial state.

print("\n--- Constructor Patterns ---")

class Player:
    """A game player with default values."""

    def __init__(self, name, level=1, health=100):
        self.name = name
        self.level = level
        self.health = health
        self.score = 0           # Always starts at 0
        self.inventory = []      # Always starts empty

    def status(self):
        print(f"  🎮 {self.name} | Lv.{self.level} | "
              f"HP: {self.health} | Score: {self.score}")

p1 = Player("Amitesh")           # Uses defaults
p2 = Player("Priya", level=5, health=200)
p1.status()
p2.status()

# ============================================================
# 📗 Methods — Functions Inside Classes
# ============================================================
print("\n--- Methods ---")

class BankAccount:
    """A bank account with methods for operations."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"  💰 {self.owner}: Deposited ₹{amount} → Balance: ₹{self.balance}")
        else:
            print(f"  ❌ Invalid deposit amount!")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            print(f"  ❌ Insufficient funds! Balance: ₹{self.balance}")
        elif amount <= 0:
            print(f"  ❌ Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"  💸 {self.owner}: Withdrew ₹{amount} → Balance: ₹{self.balance}")

    def get_balance(self):
        """Return current balance."""
        return self.balance

acc = BankAccount("Amitesh", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(5000)    # Insufficient
print(f"  Final balance: ₹{acc.get_balance()}")

# ============================================================
# 📗 Class Attributes vs Instance Attributes
# ============================================================
# Class attributes are SHARED by all instances.
# Instance attributes are unique to each object.

print("\n--- Class vs Instance Attributes ---")

class Student:
    # Class attribute — shared by ALL students
    school = "Python Academy"
    student_count = 0

    def __init__(self, name, grade):
        # Instance attributes — unique to each student
        self.name = name
        self.grade = grade
        Student.student_count += 1   # Modify class attribute

    def info(self):
        print(f"  📚 {self.name} | Grade: {self.grade} | School: {self.school}")

s1 = Student("Amitesh", "A")
s2 = Student("Priya", "A+")
s3 = Student("Rahul", "B+")

s1.info()
s2.info()
print(f"\n  Total students: {Student.student_count}")   # 3
print(f"  School: {Student.school}")                     # Shared!

# ============================================================
# 📗 Dunder (Magic) Methods
# ============================================================
# Methods with double underscores (__name__) are special
# methods that Python calls automatically in certain situations.

print("\n--- Dunder Methods ---")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Called by print() and str() — human-friendly."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Called in debugger/console — developer-friendly."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """Called by len() — return page count."""
        return self.pages

    def __eq__(self, other):
        """Called by == — compare two books."""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """Called by < — compare by page count."""
        return self.pages < other.pages

book1 = Book("Python Basics", "Amitesh", 350)
book2 = Book("Advanced Python", "Priya", 500)
book3 = Book("Python Basics", "Amitesh", 350)

print(f"  str:  {book1}")                # __str__
print(f"  repr: {repr(book1)}")          # __repr__
print(f"  len:  {len(book1)} pages")     # __len__
print(f"  ==:   book1 == book3 → {book1 == book3}")   # __eq__ → True
print(f"  <:    book1 < book2  → {book1 < book2}")    # __lt__ → True

# Sorting works because we defined __lt__!
books = [book2, book1]
books.sort()
print(f"  Sorted: {[str(b) for b in books]}")

# ============================================================
# 📗 Practical: Todo Item Class
# ============================================================
print("\n--- Todo Item Class ---")

class TodoItem:
    """A single todo item with status tracking."""

    _id_counter = 0   # Class-level counter

    def __init__(self, task, priority="medium"):
        TodoItem._id_counter += 1
        self.id = TodoItem._id_counter
        self.task = task
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "⬜"
        pri = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(self.priority, "⚪")
        return f"  {status} [{self.id}] {pri} {self.task}"

# Create todos
todos = [
    TodoItem("Learn OOP", "high"),
    TodoItem("Build mini project", "high"),
    TodoItem("Review notes", "medium"),
    TodoItem("Take a break", "low"),
]

todos[0].complete()   # Mark first as done

print("  My Todos:")
for todo in todos:
    print(todo)

# ============================================================
# 📗 Practical: Point Class (Math example)
# ============================================================
print("\n--- Point Class ---")

class Point:
    """A 2D point with operations."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """Calculate distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __add__(self, other):
        """Add two points with +."""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(6, 8)
p3 = p1 + p2          # Uses __add__!

print(f"  p1 = {p1}")
print(f"  p2 = {p2}")
print(f"  p1 + p2 = {p3}")
print(f"  Distance: {p1.distance_to(p2):.2f}")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a Car class with make, model, year, and a drive()
#    method that prints "Vroom!"
# 2. Create a Rectangle class with width, height, area(),
#    and perimeter() methods
# 3. Add __str__, __eq__, and __lt__ to your Rectangle
# 4. Create a Contact class (name, phone, email) with a
#    class attribute to count total contacts
# 5. Create a Dice class with a roll() method that returns
#    a random number 1-6 (import random)
# ============================================================
