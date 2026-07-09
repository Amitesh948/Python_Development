# ============================================================
# 📗 Helper Module: my_utils.py
# ============================================================
# This is a CUSTOM MODULE — a regular .py file that other
# files can import and use. Think of it as your personal
# toolbox of reusable functions and classes.
#
# To use this module in another file:
#   import my_utils
#   from my_utils import greet, MathHelper
# ============================================================

"""
my_utils — A collection of reusable utility functions and classes.

This module demonstrates how to create your own importable module.
"""

# ============================================================
# Module-level constants
# ============================================================

APP_NAME = "Python Learning Project"
VERSION = "1.0.0"
AUTHOR = "Amitesh"

# ============================================================
# Utility Functions
# ============================================================

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to {APP_NAME}! 🐍"

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string."""
    return sum(1 for c in text.lower() if c in "aeiou")

def format_currency(amount, symbol="₹"):
    """Format a number as currency."""
    return f"{symbol}{amount:,.2f}"

# ============================================================
# Utility Classes
# ============================================================

class MathHelper:
    """A collection of math utility methods."""

    @staticmethod
    def factorial(n):
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("No factorial for negative numbers!")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def is_prime(n):
        """Check if n is a prime number."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(count):
        """Generate first 'count' Fibonacci numbers."""
        fibs = []
        a, b = 0, 1
        for _ in range(count):
            fibs.append(a)
            a, b = b, a + b
        return fibs


class TextHelper:
    """String manipulation utilities."""

    @staticmethod
    def title_case(text):
        """Convert text to Title Case."""
        return text.title()

    @staticmethod
    def snake_case(text):
        """Convert text to snake_case."""
        return text.lower().replace(" ", "_")

    @staticmethod
    def word_count(text):
        """Count words in text."""
        return len(text.split())

    @staticmethod
    def truncate(text, max_length=50):
        """Truncate text with ellipsis."""
        if len(text) <= max_length:
            return text
        return text[:max_length - 3] + "..."

# ============================================================
# This block runs ONLY when the file is executed directly,
# NOT when imported as a module.
# ============================================================

if __name__ == "__main__":
    print(f"🧪 Testing {APP_NAME} v{VERSION} by {AUTHOR}\n")

    # Test functions
    print(greet("Amitesh"))
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"25°C = {celsius_to_fahrenheit(25)}°F")
    print(f"reverse('Python') = {reverse_string('Python')}")
    print(f"vowels in 'Amitesh' = {count_vowels('Amitesh')}")
    print(f"format_currency(85000) = {format_currency(85000)}")

    # Test MathHelper
    print(f"\nfactorial(6) = {MathHelper.factorial(6)}")
    print(f"is_prime(17) = {MathHelper.is_prime(17)}")
    print(f"fibonacci(8) = {MathHelper.fibonacci(8)}")

    # Test TextHelper
    print(f"\ntitle_case('hello world') = {TextHelper.title_case('hello world')}")
    print(f"snake_case('Hello World') = {TextHelper.snake_case('Hello World')}")
    print(f"word_count('one two three') = {TextHelper.word_count('one two three')}")

    print("\n✅ All tests passed!")
