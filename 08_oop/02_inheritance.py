# ============================================================
# 📘 Lesson 2: Inheritance
# ============================================================
# Inheritance lets one class INHERIT attributes and methods
# from another class. This avoids repeating code!
#
#   Parent class (base/super)  → general behavior
#   Child class  (derived/sub) → specialized behavior
#
# Think of it:
#   Animal → Dog, Cat, Bird  (all animals, but different!)
#   Vehicle → Car, Truck, Motorcycle
# ============================================================

# ============================================================
# 📗 Basic Inheritance
# ============================================================
print("--- Basic Inheritance ---\n")

class Animal:
    """Parent class — general animal behavior."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"  {self.name} makes a sound")

    def info(self):
        print(f"  🐾 {self.name} ({self.species})")

# Child classes INHERIT from Animal
class Dog(Animal):
    """Dog inherits everything from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent's __init__
        self.breed = breed

    def speak(self):
        """Override parent's speak — dogs bark!"""
        print(f"  {self.name}: Woof! Woof! 🐕")

    def fetch(self):
        """Dog-specific method — only dogs can fetch."""
        print(f"  {self.name} fetches the ball! 🎾")

class Cat(Animal):
    """Cat inherits from Animal."""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        print(f"  {self.name}: Meow! 🐱")

    def purr(self):
        print(f"  {self.name} purrs... 😺")

# Create objects
buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers", "orange")

# Inherited methods work!
buddy.info()        # From Animal
buddy.speak()       # Overridden in Dog
buddy.fetch()       # Dog-only method

whiskers.info()     # From Animal
whiskers.speak()    # Overridden in Cat
whiskers.purr()     # Cat-only method

# ============================================================
# 📗 super() — Calling the Parent
# ============================================================
# super() lets you call the PARENT class's methods.
# Most commonly used in __init__ to set up parent attributes.

print("\n--- super() in Action ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"  Hi! I'm {self.name}, {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)    # Set up Person part
        self.company = company         # Employee-specific
        self.salary = salary

    def introduce(self):
        super().introduce()            # Call parent's introduce
        print(f"  I work at {self.company}.")

    def work(self):
        print(f"  {self.name} is working at {self.company}... 💼")

emp = Employee("Amitesh", 25, "TechCorp", 80000)
emp.introduce()    # Calls both parent + child
emp.work()

# ============================================================
# 📗 Method Overriding
# ============================================================
# When a child class defines a method with the SAME NAME as
# the parent, it OVERRIDES (replaces) the parent's version.

print("\n--- Method Overriding ---")

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0    # Default — child should override

    def describe(self):
        print(f"  {self.name}: area = {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):      # Override!
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):      # Override!
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):      # Override!
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    shape.describe()     # Each calls its OWN area()!

# ============================================================
# 📗 isinstance() and issubclass()
# ============================================================
print("\n--- isinstance() & issubclass() ---")

print(f"  buddy is Dog:    {isinstance(buddy, Dog)}")       # True
print(f"  buddy is Animal: {isinstance(buddy, Animal)}")    # True!
print(f"  buddy is Cat:    {isinstance(buddy, Cat)}")       # False

print(f"  Dog subclass of Animal: {issubclass(Dog, Animal)}")    # True
print(f"  Cat subclass of Animal: {issubclass(Cat, Animal)}")    # True
print(f"  Dog subclass of Cat:    {issubclass(Dog, Cat)}")       # False

# ============================================================
# 📗 Multi-Level Inheritance
# ============================================================
# A chain: Grandparent → Parent → Child

print("\n--- Multi-Level Inheritance ---")

class LivingThing:
    def breathe(self):
        print(f"  {self.name} is breathing... 🫁")

class Mammal(LivingThing):
    def __init__(self, name):
        self.name = name

    def feed_young(self):
        print(f"  {self.name} feeds its young 🍼")

class Wolf(Mammal):
    def __init__(self, name, pack):
        super().__init__(name)
        self.pack = pack

    def howl(self):
        print(f"  {self.name}: Awooo! 🐺 (Pack: {self.pack})")

wolf = Wolf("Shadow", "Northern Pack")
wolf.breathe()       # From LivingThing (grandparent!)
wolf.feed_young()    # From Mammal (parent)
wolf.howl()          # From Wolf (self)

# ============================================================
# 📗 Multiple Inheritance
# ============================================================
# A class can inherit from MULTIPLE parent classes.
# Use carefully — can get confusing!

print("\n--- Multiple Inheritance ---")

class Flyable:
    def fly(self):
        print(f"  {self.name} is flying! ✈️")

class Swimmable:
    def swim(self):
        print(f"  {self.name} is swimming! 🏊")

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")

    def speak(self):
        print(f"  {self.name}: Quack! 🦆")

donald = Duck("Donald")
donald.info()     # From Animal
donald.speak()    # Overridden
donald.fly()      # From Flyable
donald.swim()     # From Swimmable

# Check MRO (Method Resolution Order)
print(f"\n  MRO: {[c.__name__ for c in Duck.__mro__]}")

# ============================================================
# 📗 Practical: Employee Hierarchy
# ============================================================
print("\n--- Employee Hierarchy ---")

class BaseEmployee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def __str__(self):
        pay = self.calculate_pay()
        return f"  [{self.emp_id}] {self.name} — ₹{pay:,.0f}/month"

class Manager(BaseEmployee):
    def __init__(self, name, emp_id, base_salary, team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size

    def calculate_pay(self):
        # Managers get ₹2000 bonus per team member
        return self.base_salary + (self.team_size * 2000)

class Developer(BaseEmployee):
    def __init__(self, name, emp_id, base_salary, tech_stack):
        super().__init__(name, emp_id, base_salary)
        self.tech_stack = tech_stack

    def calculate_pay(self):
        # Devs get ₹5000 bonus per technology
        return self.base_salary + (len(self.tech_stack) * 5000)

class Intern(BaseEmployee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id, stipend)

    # No override — uses base calculate_pay()

team = [
    Manager("Priya", "MGR-01", 90000, 8),
    Developer("Amitesh", "DEV-01", 75000, ["Python", "JS", "SQL"]),
    Developer("Rahul", "DEV-02", 70000, ["Python", "Java"]),
    Intern("Sneha", "INT-01", 15000),
]

print("  Company Payroll:")
total = 0
for emp in team:
    print(emp)
    total += emp.calculate_pay()
print(f"\n  Total payroll: ₹{total:,.0f}/month")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create Vehicle → Car, Motorcycle, Truck with different
#    fuel_efficiency() methods
# 2. Create a Shape hierarchy with area() and perimeter()
#    for Circle, Square, and Triangle
# 3. Create Person → Student → GradStudent (3-level chain)
# 4. Create a Smartphone class that inherits from both
#    Phone and Camera classes (multiple inheritance)
# 5. Build a game character hierarchy: Character → Warrior,
#    Mage, Archer — each with different attack() methods
# ============================================================
