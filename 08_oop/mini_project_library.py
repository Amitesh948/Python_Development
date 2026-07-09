# ============================================================
# 🎯 MINI PROJECT: Library Management System 📚
# ============================================================
# Uses everything from Module 8:
# ✅ Classes & Objects — Book, Member, Library
# ✅ Inheritance      — Book → EBook, AudioBook
# ✅ Encapsulation    — private data, @property, validation
# ✅ Dunder methods   — __str__, __repr__, __len__, __eq__
# ✅ Class attributes — ID counters, shared config
# ============================================================

import json
import os
from datetime import datetime, timedelta

# ============================================================
# 📗 Custom Exceptions
# ============================================================

class LibraryError(Exception):
    """Base exception for library operations."""
    pass

class BookNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BorrowLimitError(LibraryError):
    pass

# ============================================================
# 📗 Book Classes (Inheritance Demo)
# ============================================================

class Book:
    """A physical book in the library."""

    _id_counter = 0

    def __init__(self, title, author, genre, year):
        Book._id_counter += 1
        self._id = Book._id_counter
        self._title = title
        self._author = author
        self._genre = genre
        self._year = year
        self._available = True
        self._borrower = None

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    @property
    def available(self):
        return self._available

    @property
    def book_type(self):
        return "📖 Physical"

    def checkout(self, member_name):
        if not self._available:
            raise BookUnavailableError(f"'{self._title}' is already borrowed!")
        self._available = False
        self._borrower = member_name

    def return_book(self):
        self._available = True
        self._borrower = None

    def __str__(self):
        status = "✅ Available" if self._available else f"📤 Borrowed by {self._borrower}"
        return f"  [{self._id:03d}] {self.book_type} {self._title} by {self._author} ({self._year}) — {status}"

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author

    def to_dict(self):
        return {
            "id": self._id, "title": self._title,
            "author": self._author, "genre": self._genre,
            "year": self._year, "type": self.book_type,
            "available": self._available, "borrower": self._borrower,
        }


class EBook(Book):
    """An electronic book — inherits from Book."""

    def __init__(self, title, author, genre, year, file_size_mb):
        super().__init__(title, author, genre, year)
        self._file_size = file_size_mb

    @property
    def book_type(self):
        return "💻 EBook"

    @property
    def file_size(self):
        return self._file_size

    def __str__(self):
        base = super().__str__()
        return f"{base} [{self._file_size}MB]"


class AudioBook(Book):
    """An audio book — inherits from Book."""

    def __init__(self, title, author, genre, year, duration_hours):
        super().__init__(title, author, genre, year)
        self._duration = duration_hours

    @property
    def book_type(self):
        return "🎧 Audio"

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        base = super().__str__()
        return f"{base} [{self._duration}hrs]"


# ============================================================
# 📗 Member Class (Encapsulation Demo)
# ============================================================

class Member:
    """A library member with borrowing privileges."""

    _id_counter = 0
    MAX_BOOKS = 5

    def __init__(self, name, email):
        Member._id_counter += 1
        self._id = Member._id_counter
        self.name = name         # Uses setter
        self.email = email       # Uses setter
        self._borrowed_books = []
        self._join_date = datetime.now().strftime("%Y-%m-%d")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty!")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value.strip().lower()

    @property
    def borrowed_count(self):
        return len(self._borrowed_books)

    @property
    def can_borrow(self):
        return self.borrowed_count < self.MAX_BOOKS

    def borrow(self, book):
        if not self.can_borrow:
            raise BorrowLimitError(
                f"{self._name} has reached the limit of {self.MAX_BOOKS} books!"
            )
        self._borrowed_books.append(book.title)

    def return_book(self, book_title):
        if book_title in self._borrowed_books:
            self._borrowed_books.remove(book_title)

    def __str__(self):
        return (f"  [M{self._id:03d}] {self._name} | {self._email} | "
                f"Books: {self.borrowed_count}/{self.MAX_BOOKS}")

    def to_dict(self):
        return {
            "id": self._id, "name": self._name,
            "email": self._email, "borrowed": list(self._borrowed_books),
            "joined": self._join_date,
        }


# ============================================================
# 📗 Library Class (Ties Everything Together)
# ============================================================

class Library:
    """The library system — manages books and members."""

    def __init__(self, name):
        self._name = name
        self._books = []
        self._members = []

    @property
    def name(self):
        return self._name

    def __len__(self):
        return len(self._books)

    # --- Book Management ---

    def add_book(self, book):
        self._books.append(book)
        print(f"  ✅ Added: '{book.title}' by {book.author}")

    def find_book(self, book_id):
        for book in self._books:
            if book.id == book_id:
                return book
        raise BookNotFoundError(f"No book with ID {book_id}")

    def search_books(self, query):
        query = query.lower()
        return [b for b in self._books
                if query in b.title.lower() or query in b.author.lower()]

    def list_books(self, available_only=False):
        books = self._books
        if available_only:
            books = [b for b in books if b.available]
        if not books:
            print("\n  📭 No books found!")
            return
        print(f"\n  📚 {self._name} — {len(books)} book(s):\n")
        for book in books:
            print(book)

    # --- Member Management ---

    def add_member(self, member):
        self._members.append(member)
        print(f"  ✅ Registered: {member.name} ({member.email})")

    def find_member(self, member_id):
        for member in self._members:
            if member.id == member_id:
                return member
        raise MemberNotFoundError(f"No member with ID {member_id}")

    def list_members(self):
        if not self._members:
            print("\n  📭 No members registered!")
            return
        print(f"\n  👥 Members ({len(self._members)}):\n")
        for member in self._members:
            print(member)

    # --- Borrowing ---

    def checkout_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        book.checkout(member.name)
        member.borrow(book)
        print(f"  📤 '{book.title}' → {member.name}")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        book.return_book()
        member.return_book(book.title)
        print(f"  📥 '{book.title}' returned by {member.name}")

    # --- Statistics ---

    def stats(self):
        total = len(self._books)
        available = sum(1 for b in self._books if b.available)
        borrowed = total - available
        genres = {}
        for b in self._books:
            genres[b.genre] = genres.get(b.genre, 0) + 1
        top_genre = max(genres, key=genres.get) if genres else "N/A"

        print(f"\n  📊 {self._name} Statistics:")
        print(f"  {'─' * 30}")
        print(f"  📚 Total books:     {total}")
        print(f"  ✅ Available:       {available}")
        print(f"  📤 Borrowed:        {borrowed}")
        print(f"  👥 Members:         {len(self._members)}")
        print(f"  🏷️  Top genre:       {top_genre} ({genres.get(top_genre, 0)})")

    # --- Persistence ---

    def save(self, filename="library_data.json"):
        data = {
            "name": self._name,
            "books": [b.to_dict() for b in self._books],
            "members": [m.to_dict() for m in self._members],
        }
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            print(f"  💾 Library saved to {filename}")
        except IOError as e:
            print(f"  ❌ Could not save: {e}")


# ============================================================
# 📗 Menu & Main Loop
# ============================================================

def show_menu():
    print("\n╔══════════════════════════════════════╗")
    print("║      📚 LIBRARY MANAGEMENT SYSTEM    ║")
    print("╠══════════════════════════════════════╣")
    print("║  1.  📖 List All Books               ║")
    print("║  2.  ✅ List Available Books          ║")
    print("║  3.  🔍 Search Books                 ║")
    print("║  4.  ➕ Add Book                      ║")
    print("║  5.  👥 List Members                  ║")
    print("║  6.  ➕ Register Member               ║")
    print("║  7.  📤 Checkout Book                 ║")
    print("║  8.  📥 Return Book                   ║")
    print("║  9.  📊 Statistics                    ║")
    print("║  10. 💾 Save Data                     ║")
    print("║  0.  👋 Exit                          ║")
    print("╚══════════════════════════════════════╝")

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("  ❌ This field is required!")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  ❌ Please enter a valid number!")

# --- Setup Library with Sample Data ---
library = Library("Python Academy Library")

# Add sample books (various types!)
sample_books = [
    Book("Python Crash Course", "Eric Matthes", "Programming", 2019),
    Book("Clean Code", "Robert Martin", "Programming", 2008),
    Book("The Pragmatic Programmer", "David Thomas", "Programming", 2019),
    EBook("Automate the Boring Stuff", "Al Sweigart", "Programming", 2019, 15),
    AudioBook("Atomic Habits", "James Clear", "Self-Help", 2018, 5.5),
    Book("Sapiens", "Yuval Harari", "History", 2011),
    EBook("Deep Work", "Cal Newport", "Productivity", 2016, 8),
    AudioBook("The Alchemist", "Paulo Coelho", "Fiction", 1988, 4.0),
]

for book in sample_books:
    library.add_book(book)

# Add sample members
sample_members = [
    Member("Amitesh", "amitesh@example.com"),
    Member("Priya", "priya@example.com"),
    Member("Rahul", "rahul@example.com"),
]

print()
for member in sample_members:
    library.add_member(member)

# --- Main Loop ---
print(f"\nWelcome to {library.name}! 📚")
print(f"  {len(library)} books | {len(sample_members)} members loaded.\n")

while True:
    try:
        show_menu()
        choice = input("\n  Choose (0-10): ").strip()

        if choice == "0":
            library.save()
            print("\n  👋 Goodbye! Library data saved.")
            print("  ✅ Module 8 Complete! Move on to 09_modules_packages/")
            break

        elif choice == "1":
            library.list_books()

        elif choice == "2":
            library.list_books(available_only=True)

        elif choice == "3":
            query = get_input("  🔍 Search: ")
            results = library.search_books(query)
            if results:
                print(f"\n  Found {len(results)} result(s):")
                for book in results:
                    print(book)
            else:
                print("  ❌ No books found!")

        elif choice == "4":
            print("\n  Add a new book:")
            btype = get_input("  Type (1=Physical, 2=EBook, 3=Audio): ")
            title = get_input("  Title: ")
            author = get_input("  Author: ")
            genre = get_input("  Genre: ")
            year = get_int("  Year: ")

            if btype == "2":
                size = get_int("  File size (MB): ")
                library.add_book(EBook(title, author, genre, year, size))
            elif btype == "3":
                hrs = float(get_input("  Duration (hours): "))
                library.add_book(AudioBook(title, author, genre, year, hrs))
            else:
                library.add_book(Book(title, author, genre, year))

        elif choice == "5":
            library.list_members()

        elif choice == "6":
            name = get_input("  Name: ")
            email = get_input("  Email: ")
            try:
                library.add_member(Member(name, email))
            except ValueError as e:
                print(f"  ❌ {e}")

        elif choice == "7":
            library.list_books(available_only=True)
            book_id = get_int("  Book ID to checkout: ")
            library.list_members()
            member_id = get_int("  Member ID: ")
            library.checkout_book(book_id, member_id)

        elif choice == "8":
            book_id = get_int("  Book ID to return: ")
            member_id = get_int("  Member ID: ")
            library.return_book(book_id, member_id)

        elif choice == "9":
            library.stats()

        elif choice == "10":
            library.save()

        else:
            print("  ❌ Invalid choice! Pick 0-10.")

    except (BookNotFoundError, BookUnavailableError,
            MemberNotFoundError, BorrowLimitError) as e:
        print(f"  ❌ {type(e).__name__}: {e}")

    except KeyboardInterrupt:
        print("\n\n  ⚠️ Use option 0 to exit properly.")

    except Exception as e:
        print(f"  🔴 Unexpected error: {type(e).__name__}: {e}")

# ============================================================
# 🧹 Cleanup
# ============================================================
if os.path.exists("library_data.json"):
    os.remove("library_data.json")
    print("🧹 Cleaned up data file!")
