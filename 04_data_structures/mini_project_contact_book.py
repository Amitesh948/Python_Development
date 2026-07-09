# ============================================================
# 🎯 MINI PROJECT: Contact Book 📱
# ============================================================
# Uses everything from Module 4:
# ✅ Lists — storing contacts
# ✅ Dictionaries — each contact's data
# ✅ Tuples — returning search results
# ✅ Sets — unique categories
# ✅ Loops & Conditions from previous modules
# ============================================================

contacts = []  # List of dictionaries

def show_menu():
    """Display the main menu."""
    print("\n╔════════════════════════════════╗")
    print("║     📱 CONTACT BOOK           ║")
    print("╠════════════════════════════════╣")
    print("║  1. Add Contact               ║")
    print("║  2. View All Contacts          ║")
    print("║  3. Search Contact             ║")
    print("║  4. Delete Contact             ║")
    print("║  5. Contact Stats              ║")
    print("║  6. Exit                       ║")
    print("╚════════════════════════════════╝")

def add_contact():
    """Add a new contact to the list."""
    print("\n--- Add New Contact ---")
    name = input("  Name: ").strip()
    if not name:
        print("  ❌ Name cannot be empty!")
        return

    phone = input("  Phone: ").strip()
    email = input("  Email: ").strip()
    category = input("  Category (friend/family/work): ").strip().lower()

    # Create a dictionary for this contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category or "other"
    }

    contacts.append(contact)  # Add to the list
    print(f"  ✅ {name} added successfully!")

def view_contacts():
    """Display all contacts in a formatted table."""
    if not contacts:
        print("\n  📭 No contacts yet! Add some first.")
        return

    print(f"\n  {'#':<4} {'Name':<15} {'Phone':<15} {'Email':<25} {'Category':<10}")
    print("  " + "─" * 69)

    for i, c in enumerate(contacts, start=1):
        print(f"  {i:<4} {c['name']:<15} {c['phone']:<15} {c['email']:<25} {c['category']:<10}")

    print(f"\n  Total contacts: {len(contacts)}")

def search_contact():
    """Search for a contact by name."""
    if not contacts:
        print("\n  📭 No contacts to search!")
        return

    query = input("\n  Search name: ").strip().lower()
    # Use list comprehension to find matches
    results = [c for c in contacts if query in c["name"].lower()]

    if results:
        print(f"\n  Found {len(results)} result(s):")
        for c in results:
            print(f"    👤 {c['name']} | 📞 {c['phone']} | 📧 {c['email']}")
    else:
        print(f"  ❌ No contacts found for '{query}'")

def delete_contact():
    """Delete a contact by number."""
    view_contacts()
    if not contacts:
        return

    try:
        num = int(input("\n  Enter contact # to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            print(f"  🗑️  Deleted: {removed['name']}")
        else:
            print("  ❌ Invalid number!")
    except ValueError:
        print("  ❌ Please enter a valid number!")

def show_stats():
    """Show contact statistics using sets and dicts."""
    if not contacts:
        print("\n  📭 No contacts for stats!")
        return

    # Use a set for unique categories
    categories = set(c["category"] for c in contacts)

    print(f"\n  📊 Contact Statistics:")
    print(f"  Total contacts: {len(contacts)}")
    print(f"  Categories: {categories}")

    # Count per category using a dictionary
    count = {}
    for c in contacts:
        cat = c["category"]
        count[cat] = count.get(cat, 0) + 1

    print("\n  Contacts per category:")
    for cat, num in count.items():
        bar = "█" * (num * 3)
        print(f"    {cat:<10} {bar} ({num})")

# ============================================================
# 🎮 MAIN LOOP
# ============================================================
print("Welcome to Contact Book! 📱")

while True:
    show_menu()
    choice = input("\n  Choose (1-6): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_stats()
    elif choice == "6":
        print("\n  👋 Goodbye! Your contacts are saved in memory.")
        print("  ✅ Module 4 Complete! Move on to 05_functions/")
        break
    else:
        print("  ❌ Invalid choice! Pick 1-6.")
