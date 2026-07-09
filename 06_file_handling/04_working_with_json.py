# ============================================================
# 📘 Lesson 4: Working with JSON in Python
# ============================================================
# JSON (JavaScript Object Notation) is a universal text format
# for storing and exchanging structured data. It's used
# everywhere — APIs, config files, databases, data sharing.
#
# Python has a built-in module:
#   import json
#
# You only need 4 functions:
#   json.dump()   — Python → JSON FILE
#   json.load()   — JSON FILE → Python
#   json.dumps()  — Python → JSON STRING   (s = string)
#   json.loads()  — JSON STRING → Python    (s = string)
#
# Memory trick: functions with 's' work with STRINGS,
#               functions without 's' work with FILES.
# ============================================================

import json
import os

# ============================================================
# 📗 PART 1: json.dumps() — Python → JSON String
# ============================================================
# Converts a Python object into a JSON-formatted string.
# This does NOT write to a file — it gives you a string.

print("=" * 55)
print("📗 PART 1: json.dumps() — Python → JSON String")
print("=" * 55)

user = {
    "name": "Amitesh",
    "age": 25,
    "active": True,          # Python True
    "bio": None,             # Python None
    "skills": ["Python", "JavaScript", "SQL"]
}

# Basic conversion
json_string = json.dumps(user)
print(f"\n  Raw JSON string:")
print(f"  {json_string}")
#   Notice: True → true, None → null (automatic conversion!)

# Pretty-print with indent
print(f"\n  Pretty-printed (indent=4):")
pretty = json.dumps(user, indent=4)
print(pretty)

# Sort keys alphabetically
print(f"\n  Sorted keys:")
sorted_json = json.dumps(user, indent=4, sort_keys=True)
print(sorted_json)

# Handle non-ASCII characters
print(f"\n  Non-ASCII handling:")
city_data = {"city": "München", "country": "Österreich"}
print(f"  Default:       {json.dumps(city_data)}")
print(f"  ensure_ascii:  {json.dumps(city_data, ensure_ascii=False)}")

# ============================================================
# 📗 PART 2: json.loads() — JSON String → Python
# ============================================================
# Parses a JSON string and converts it into a Python object.
# This is the REVERSE of json.dumps().

print("\n" + "=" * 55)
print("📗 PART 2: json.loads() — JSON String → Python")
print("=" * 55)

json_text = '{"name": "Priya", "scores": [90, 85, 92], "passed": true, "notes": null}'

data = json.loads(json_text)

print(f"\n  Parsed data:")
print(f"  Name:    {data['name']}")
print(f"  Scores:  {data['scores']}")
print(f"  Passed:  {data['passed']}  (type: {type(data['passed']).__name__})")
print(f"  Notes:   {data['notes']}   (type: {type(data['notes']).__name__})")
print(f"  Average: {sum(data['scores']) / len(data['scores']):.1f}")

# ============================================================
# 📗 PART 3: json.dump() — Python → JSON File
# ============================================================
# Writes a Python object directly to a .json file.
# Always use indent for readable files!

print("\n" + "=" * 55)
print("📗 PART 3: json.dump() — Write to JSON File")
print("=" * 55)

user_profile = {
    "name": "Amitesh",
    "age": 25,
    "city": "Pune",
    "is_student": False,
    "skills": ["Python", "JavaScript", "SQL"],
    "projects": [
        {"name": "Calculator", "language": "Python", "completed": True},
        {"name": "Portfolio", "language": "HTML/CSS", "completed": False},
    ]
}

with open("profile.json", "w") as file:
    json.dump(user_profile, file, indent=4)
    # indent=4 → human-readable formatting

print("\n  ✅ Created profile.json")
print("\n  File contents:")
with open("profile.json", "r") as file:
    print(file.read())

# ============================================================
# 📗 PART 4: json.load() — JSON File → Python
# ============================================================
# Reads a JSON file and parses it into a Python object.
# This is the REVERSE of json.dump().

print("=" * 55)
print("📗 PART 4: json.load() — Read from JSON File")
print("=" * 55)

with open("profile.json", "r") as file:
    loaded = json.load(file)    # Parse JSON file → Python dict

print(f"\n  Name:     {loaded['name']}")
print(f"  City:     {loaded['city']}")
print(f"  Skills:   {', '.join(loaded['skills'])}")
print(f"  Projects: {len(loaded['projects'])}")
for project in loaded["projects"]:
    status = "✅" if project["completed"] else "🔧"
    print(f"    {status} {project['name']} ({project['language']})")

# ============================================================
# 📗 PART 5: JSON ↔ Python Type Mapping
# ============================================================
# When converting, types are automatically mapped:

print("\n" + "=" * 55)
print("📗 PART 5: JSON ↔ Python Type Mapping")
print("=" * 55)

print("\n  JSON                  Python")
print("  " + "─" * 20 + "  " + "─" * 15)

type_examples = {
    '{"key": "val"}':   "dict",
    '[1, 2, 3]':        "list",
    '"hello"':          "str",
    '42':               "int",
    '3.14':             "float",
    'true / false':     "True / False",
    'null':             "None",
}
for json_type, py_type in type_examples.items():
    print(f"  {json_type:<22}  {py_type}")

# Live demonstration
print("\n  Live demo:")
demo = '{"count": 42, "pi": 3.14, "active": true, "data": null, "tags": ["a", "b"]}'
parsed = json.loads(demo)
for key, value in parsed.items():
    print(f"    {key:<8} = {str(value):<12} type: {type(value).__name__}")

# ============================================================
# 📗 PART 6: Modifying JSON Data
# ============================================================
# JSON files are just dicts/lists in Python — modify them
# with normal Python operations, then save back!

print("\n" + "=" * 55)
print("📗 PART 6: Modifying JSON Data")
print("=" * 55)

# Load existing data
with open("profile.json", "r") as file:
    profile = json.load(file)

print(f"\n  Before:")
print(f"    Skills: {profile['skills']}")
print(f"    Age:    {profile['age']}")

# Modify the data (it's just a dict!)
profile["skills"].append("Docker")           # Add a skill
profile["age"] = 26                          # Update age
profile["email"] = "amitesh@example.com"     # Add new field

# Save it back
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

# Verify the changes
with open("profile.json", "r") as file:
    updated = json.load(file)

print(f"\n  After:")
print(f"    Skills: {updated['skills']}")
print(f"    Age:    {updated['age']}")
print(f"    Email:  {updated['email']}")
print(f"\n  ✅ profile.json updated successfully!")

# ============================================================
# 📗 PART 7: Working with Nested JSON
# ============================================================
# Real-world JSON is usually deeply nested. Here's how
# to navigate and extract data from it.

print("\n" + "=" * 55)
print("📗 PART 7: Working with Nested JSON")
print("=" * 55)

# Simulating an API response
api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 101,
            "name": "Amitesh",
            "address": {
                "city": "Pune",
                "state": "Maharashtra",
                "pin": "411001"
            }
        },
        "orders": [
            {"id": 1, "item": "Laptop", "amount": 85000},
            {"id": 2, "item": "Mouse", "amount": 500},
            {"id": 3, "item": "Keyboard", "amount": 1500},
        ]
    },
    "total_orders": 3
}

# Accessing nested values — chain the keys/indices
print(f"\n  Status:    {api_response['status']}")
print(f"  User:      {api_response['data']['user']['name']}")
print(f"  City:      {api_response['data']['user']['address']['city']}")
print(f"  1st Order: {api_response['data']['orders'][0]['item']}")

# Using .get() for safe access (no KeyError if key missing!)
print(f"\n  Safe access with .get():")
phone = api_response["data"]["user"].get("phone", "Not provided")
print(f"    Phone: {phone}")

# Loop through nested lists
print(f"\n  All orders:")
total = 0
for order in api_response["data"]["orders"]:
    print(f"    #{order['id']} - {order['item']}: ₹{order['amount']:,}")
    total += order["amount"]
print(f"    {'─' * 30}")
print(f"    Total: ₹{total:,}")

# ============================================================
# 📗 PART 8: Common Pitfalls & Error Handling
# ============================================================
# JSON is strict! Here are common mistakes and how to
# handle them gracefully.

print("\n" + "=" * 55)
print("📗 PART 8: Common Pitfalls & Error Handling")
print("=" * 55)

# Pitfall 1: Single quotes are NOT valid JSON
print("\n  ❌ Pitfall 1: Single quotes")
bad_json = "{'name': 'Amitesh'}"
try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"    Error: {e}")
    print("    Fix: JSON requires double quotes!")

good_json = '{"name": "Amitesh"}'
print(f"    ✅ Correct: {json.loads(good_json)}")

# Pitfall 2: Trailing commas
print("\n  ❌ Pitfall 2: Trailing commas")
bad_json = '{"a": 1, "b": 2,}'
try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"    Error: {e}")
    print('    Fix: Remove the trailing comma!')

# Pitfall 3: Non-serializable types
print("\n  ❌ Pitfall 3: Non-serializable types")
from datetime import datetime

try:
    json.dumps({"created": datetime.now()})
except TypeError as e:
    print(f"    Error: {e}")
    print("    Fix: Convert to string first!")

# The fix:
data_fixed = {"created": datetime.now().isoformat()}
print(f"    ✅ Fixed: {json.dumps(data_fixed)}")

# Pitfall 4: Sets are not JSON serializable
print("\n  ❌ Pitfall 4: Sets")
try:
    json.dumps({"tags": {1, 2, 3}})
except TypeError as e:
    print(f"    Error: {e}")
    print("    Fix: Convert set to list first!")

print(f"    ✅ Fixed: {json.dumps({'tags': list({1, 2, 3})})}")

# Safe JSON parsing function
print("\n  ✅ Safe JSON parsing:")

def safe_parse(json_string):
    """Safely parse JSON — returns None on failure."""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"    ⚠️ Invalid JSON: {e}")
        return None

result1 = safe_parse('{"valid": true}')
result2 = safe_parse('not json at all')
print(f"    Valid:   {result1}")
print(f"    Invalid: {result2}")

# ============================================================
# 📗 PART 9: Practical — Settings Manager
# ============================================================
# Build a reusable settings manager that loads defaults,
# lets you update values, and saves them to a JSON file.

print("\n" + "=" * 55)
print("📗 PART 9: Practical — Settings Manager")
print("=" * 55)

SETTINGS_FILE = "app_settings.json"

DEFAULT_SETTINGS = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "auto_save": True,
    "notifications": True
}

def load_settings():
    """Load settings from JSON file, or return defaults."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            saved = json.load(f)
            # Merge with defaults (so new defaults are added)
            merged = DEFAULT_SETTINGS.copy()
            merged.update(saved)
            return merged
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    """Save settings to JSON file."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def update_setting(key, value):
    """Update a single setting and save."""
    settings = load_settings()
    old_value = settings.get(key, "N/A")
    settings[key] = value
    save_settings(settings)
    print(f"    {key}: {old_value} → {value}")

# Demo: Load → Modify → Save → Verify
settings = load_settings()
print(f"\n  Defaults: {json.dumps(settings, indent=4)}")

print("\n  Updating settings:")
update_setting("theme", "dark")
update_setting("font_size", 18)
update_setting("language", "de")

print(f"\n  Updated file:")
final = load_settings()
print(f"  {json.dumps(final, indent=4)}")

# ============================================================
# 📗 PART 10: Practical — Contact Book (JSON)
# ============================================================
# A mini contact book using JSON as storage.

print("\n" + "=" * 55)
print("📗 PART 10: Practical — Contact Book")
print("=" * 55)

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email):
    """Add a new contact."""
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    print(f"    ✅ Added: {name}")

def find_contact(search_name):
    """Find a contact by name (case-insensitive)."""
    contacts = load_contacts()
    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            return contact
    return None

def show_all_contacts():
    """Display all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("    📭 No contacts yet!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"    {i}. {c['name']:<12} 📞 {c['phone']:<15} 📧 {c['email']}")

# Demo
print("\n  Adding contacts:")
add_contact("Amitesh", "+91-9876543210", "amitesh@example.com")
add_contact("Priya", "+91-9876543211", "priya@example.com")
add_contact("Rahul", "+91-9876543212", "rahul@example.com")
add_contact("Sneha", "+91-9876543213", "sneha@example.com")

print("\n  All contacts:")
show_all_contacts()

print("\n  Search for 'Priya':")
found = find_contact("Priya")
if found:
    print(f"    Found: {found['name']} — {found['phone']} — {found['email']}")
else:
    print("    ❌ Not found!")

# Show the raw JSON file
print("\n  Raw JSON file:")
with open(CONTACTS_FILE, "r") as f:
    print(f.read())

# ============================================================
# 🧹 Cleanup — Remove all demo files
# ============================================================
for f in ["profile.json", "app_settings.json", "contacts.json"]:
    if os.path.exists(f):
        os.remove(f)

print("🧹 Cleaned up all demo files!")

# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a JSON "bookshelf" with 5 books (title, author,
#    year, rating). Save it, load it, print books rated > 4.
# 2. Build a TODO list manager — add tasks, mark complete,
#    list all tasks, save/load from JSON.
# 3. Write a function that takes a Python dict and validates
#    if it can be converted to JSON (handle all edge cases).
# 4. Create a "student grades" JSON. Calculate average grade,
#    find the highest/lowest scorer.
# 5. Build a JSON-based quiz game — questions and answers
#    stored in JSON, load them, and run an interactive quiz.
# ============================================================
