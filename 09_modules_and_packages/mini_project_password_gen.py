# ============================================================
# 🎯 MINI PROJECT: Password Generator 🔐
# ============================================================
# Uses everything from Module 9:
# ✅ Built-in modules  — random, string, os, json, hashlib
# ✅ Custom modules     — imports from my_utils.py
# ✅ Module patterns    — if __name__ == "__main__"
# ✅ Multiple imports   — organized by category
# ============================================================

# --- Standard library imports ---
import random
import string
import json
import os
import hashlib
from datetime import datetime

# --- Custom module import ---
from my_utils import format_currency, TextHelper

# ============================================================
# 📗 Password Generator Class
# ============================================================

class PasswordGenerator:
    """Generate secure, customizable passwords."""

    # Character pools
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    DIGITS = string.digits
    SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    AMBIGUOUS = "il1Lo0O"  # Characters that look similar

    def __init__(self):
        self._history = []

    def generate(self, length=16, uppercase=True, digits=True,
                 symbols=True, exclude_ambiguous=False):
        """Generate a random password with given constraints."""
        if length < 4:
            raise ValueError("Password must be at least 4 characters!")
        if length > 128:
            raise ValueError("Password cannot exceed 128 characters!")

        # Build character pool
        pool = self.LOWERCASE
        required = [random.choice(self.LOWERCASE)]

        if uppercase:
            pool += self.UPPERCASE
            required.append(random.choice(self.UPPERCASE))
        if digits:
            pool += self.DIGITS
            required.append(random.choice(self.DIGITS))
        if symbols:
            pool += self.SYMBOLS
            required.append(random.choice(self.SYMBOLS))

        # Remove ambiguous characters if requested
        if exclude_ambiguous:
            pool = "".join(c for c in pool if c not in self.AMBIGUOUS)

        # Fill remaining length with random choices
        remaining = length - len(required)
        password_chars = required + [random.choice(pool) for _ in range(remaining)]

        # Shuffle so required chars aren't always at the start
        random.shuffle(password_chars)
        password = "".join(password_chars)

        # Save to history
        self._history.append({
            "password": password,
            "length": length,
            "strength": self.check_strength(password),
            "created": datetime.now().strftime("%H:%M:%S"),
        })

        return password

    def generate_passphrase(self, word_count=4, separator="-"):
        """Generate a memorable passphrase from random words."""
        # Common English words for passphrases
        words = [
            "apple", "brave", "cloud", "dance", "eagle", "flame",
            "grace", "heart", "ivory", "jewel", "knife", "lemon",
            "magic", "night", "ocean", "pearl", "quest", "river",
            "stone", "tiger", "ultra", "vivid", "whale", "xenon",
            "youth", "zebra", "amber", "blaze", "coral", "drift",
            "ember", "frost", "gleam", "hover", "ingot", "joker",
            "karma", "lotus", "medal", "nexus", "oasis", "plume",
            "quilt", "radar", "solar", "tempo", "unity", "vault",
            "woven", "pixel", "yield", "zesty", "forge", "crypt",
            "delta", "prism", "scout", "lunar", "storm", "orbit",
        ]

        chosen = random.sample(words, min(word_count, len(words)))
        # Capitalize first letter of each word
        chosen = [w.capitalize() for w in chosen]
        # Add a random number for extra security
        chosen.append(str(random.randint(10, 99)))

        passphrase = separator.join(chosen)

        self._history.append({
            "password": passphrase,
            "length": len(passphrase),
            "strength": "Strong (passphrase)",
            "created": datetime.now().strftime("%H:%M:%S"),
        })

        return passphrase

    def generate_pin(self, length=6):
        """Generate a numeric PIN."""
        if length < 4 or length > 12:
            raise ValueError("PIN must be 4-12 digits!")
        pin = "".join(random.choice(string.digits) for _ in range(length))

        self._history.append({
            "password": pin,
            "length": length,
            "strength": "PIN",
            "created": datetime.now().strftime("%H:%M:%S"),
        })

        return pin

    @staticmethod
    def check_strength(password):
        """Evaluate password strength."""
        score = 0
        checks = {
            "Length ≥ 8":     len(password) >= 8,
            "Length ≥ 12":    len(password) >= 12,
            "Has lowercase":  any(c.islower() for c in password),
            "Has uppercase":  any(c.isupper() for c in password),
            "Has digit":      any(c.isdigit() for c in password),
            "Has symbol":     any(c in string.punctuation or c in "!@#$%^&*" for c in password),
            "Length ≥ 16":    len(password) >= 16,
        }

        passed = []
        for check, result in checks.items():
            if result:
                score += 1
                passed.append(check)

        if score <= 2:
            return "🔴 Weak"
        elif score <= 4:
            return "🟡 Medium"
        elif score <= 5:
            return "🟢 Strong"
        else:
            return "🔵 Very Strong"

    @staticmethod
    def hash_password(password):
        """Create a SHA-256 hash of the password (for demo)."""
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def history(self):
        return list(self._history)

    def clear_history(self):
        self._history.clear()


# ============================================================
# 📗 Password Vault (Save/Load with JSON)
# ============================================================

VAULT_FILE = "password_vault.json"

def load_vault():
    """Load saved passwords from JSON."""
    try:
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_vault(vault):
    """Save passwords to JSON."""
    try:
        with open(VAULT_FILE, "w") as f:
            json.dump(vault, f, indent=2)
    except IOError as e:
        print(f"  ❌ Could not save: {e}")

def add_to_vault(vault, label, password):
    """Add a password entry to the vault."""
    entry = {
        "label": label,
        "password": password,
        "hash": PasswordGenerator.hash_password(password),
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    vault.append(entry)
    save_vault(vault)

# ============================================================
# 📗 Display Functions
# ============================================================

def show_menu():
    print("\n╔══════════════════════════════════════╗")
    print("║      🔐 PASSWORD GENERATOR           ║")
    print("╠══════════════════════════════════════╣")
    print("║  1.  🔑 Generate Password            ║")
    print("║  2.  📝 Generate Passphrase           ║")
    print("║  3.  🔢 Generate PIN                  ║")
    print("║  4.  💪 Check Password Strength       ║")
    print("║  5.  🔒 Hash a Password               ║")
    print("║  6.  📋 View History                   ║")
    print("║  7.  💾 Save to Vault                  ║")
    print("║  8.  📂 View Vault                     ║")
    print("║  9.  🗑️  Clear History                 ║")
    print("║  0.  👋 Exit                           ║")
    print("╚══════════════════════════════════════╝")

def display_password(password, label="Password"):
    """Display a generated password with visual flair."""
    strength = PasswordGenerator.check_strength(password)
    print(f"\n  ╔{'═' * 50}╗")
    print(f"  ║  {label}:")
    print(f"  ║  🔑 {password}")
    print(f"  ║  📏 Length: {len(password)}")
    print(f"  ║  💪 Strength: {strength}")
    print(f"  ╚{'═' * 50}╝")

# ============================================================
# 🎮 MAIN PROGRAM
# ============================================================

if __name__ == "__main__":
    print("Welcome to Password Generator! 🔐")

    gen = PasswordGenerator()
    vault = load_vault()
    print(f"  Vault: {len(vault)} saved passwords.\n")

    while True:
        try:
            show_menu()
            choice = input("\n  Choose (0-9): ").strip()

            if choice == "0":
                print("\n  👋 Stay secure! Goodbye!")
                print("  ✅ Module 9 Complete! Move on to 10_capstone/")
                break

            elif choice == "1":
                print("\n  Password options:")
                try:
                    length = int(input("  Length (8-128, default 16): ").strip() or "16")
                except ValueError:
                    length = 16
                upper = input("  Include uppercase? (Y/n): ").strip().lower() != "n"
                digits = input("  Include digits? (Y/n): ").strip().lower() != "n"
                symbols = input("  Include symbols? (Y/n): ").strip().lower() != "n"
                no_ambig = input("  Exclude similar chars (il1O0)? (y/N): ").strip().lower() == "y"

                password = gen.generate(length, upper, digits, symbols, no_ambig)
                display_password(password)

            elif choice == "2":
                try:
                    count = int(input("  Number of words (3-8, default 4): ").strip() or "4")
                except ValueError:
                    count = 4
                sep = input("  Separator (default '-'): ").strip() or "-"
                passphrase = gen.generate_passphrase(count, sep)
                display_password(passphrase, "Passphrase")

            elif choice == "3":
                try:
                    length = int(input("  PIN length (4-12, default 6): ").strip() or "6")
                except ValueError:
                    length = 6
                pin = gen.generate_pin(length)
                display_password(pin, "PIN")

            elif choice == "4":
                pwd = input("  Enter password to check: ")
                strength = PasswordGenerator.check_strength(pwd)
                print(f"\n  💪 Strength: {strength}")
                print(f"  📏 Length: {len(pwd)} characters")

            elif choice == "5":
                pwd = input("  Enter password to hash: ")
                hashed = PasswordGenerator.hash_password(pwd)
                print(f"\n  🔒 SHA-256 Hash:")
                print(f"  {hashed}")
                # Use our custom module's TextHelper!
                print(f"  Truncated: {TextHelper.truncate(hashed, 30)}")

            elif choice == "6":
                history = gen.history
                if not history:
                    print("\n  📭 No passwords generated yet!")
                else:
                    print(f"\n  📋 History ({len(history)} entries):")
                    for i, entry in enumerate(history, 1):
                        print(f"    {i}. [{entry['created']}] "
                              f"{entry['strength']} — "
                              f"{entry['password'][:20]}{'...' if len(entry['password']) > 20 else ''}")

            elif choice == "7":
                history = gen.history
                if not history:
                    print("\n  📭 Generate a password first!")
                else:
                    print(f"\n  Last generated: {history[-1]['password'][:30]}...")
                    label = input("  Label (e.g., 'Gmail'): ").strip()
                    if label:
                        add_to_vault(vault, label, history[-1]["password"])
                        print(f"  💾 Saved '{label}' to vault!")
                    else:
                        print("  ❌ Label required!")

            elif choice == "8":
                if not vault:
                    print("\n  📭 Vault is empty!")
                else:
                    print(f"\n  🔒 Password Vault ({len(vault)} entries):\n")
                    for i, entry in enumerate(vault, 1):
                        print(f"    {i}. {entry['label']}")
                        print(f"       🔑 {entry['password']}")
                        print(f"       📅 {entry['created']}\n")

            elif choice == "9":
                gen.clear_history()
                print("  🗑️  History cleared!")

            else:
                print("  ❌ Invalid choice! Pick 0-9.")

        except ValueError as e:
            print(f"  ❌ {e}")

        except KeyboardInterrupt:
            print("\n\n  ⚠️ Use option 0 to exit properly.")

        except Exception as e:
            print(f"  🔴 Error: {type(e).__name__}: {e}")

    # Cleanup
    if os.path.exists(VAULT_FILE):
        os.remove(VAULT_FILE)
        print("🧹 Cleaned up vault file!")
