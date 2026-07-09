# ============================================================
# 🎯 MINI PROJECT: Personal Diary App 📔
# ============================================================
# Uses everything from Module 6:
# ✅ Reading files  — load and display diary entries
# ✅ Writing files  — save new entries with timestamps
# ✅ Appending      — add entries without losing old ones
# ✅ JSON           — structured storage of entries
# ✅ CSV export     — export diary to spreadsheet format
# ============================================================

import json
import csv
import os
from datetime import datetime

# ============================================================
# 📗 Configuration
# ============================================================

DIARY_FILE = "my_diary.json"

# ============================================================
# 📗 Data Functions
# ============================================================

def load_diary():
    """Load diary entries from JSON file."""
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_diary(entries):
    """Save diary entries to JSON file."""
    with open(DIARY_FILE, "w") as f:
        json.dump(entries, f, indent=4)

# ============================================================
# 📗 Feature Functions
# ============================================================

def add_entry(entries):
    """Write a new diary entry."""
    print("\n  📝 Write your diary entry:")
    print("  (Type your entry, then press Enter twice to save)\n")

    lines = []
    while True:
        line = input("  ")
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("  ❌ Empty entry — not saved.")
        return

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "mood": get_mood(),
        "content": "\n".join(lines),
    }

    entries.append(entry)
    save_diary(entries)
    print(f"\n  ✅ Entry saved! ({len(entries)} total entries)")

def get_mood():
    """Ask user for their mood."""
    moods = {
        "1": "😊 Happy",
        "2": "😢 Sad",
        "3": "😡 Angry",
        "4": "😴 Tired",
        "5": "🤩 Excited",
        "6": "😌 Calm",
        "7": "🤔 Thoughtful",
    }
    print("\n  How are you feeling?")
    for key, mood in moods.items():
        print(f"    {key}. {mood}")

    choice = input("\n  Pick (1-7): ").strip()
    return moods.get(choice, "😐 Neutral")

def view_entries(entries):
    """Display all diary entries."""
    if not entries:
        print("\n  📭 No entries yet! Start writing!")
        return

    print(f"\n  📖 Your Diary — {len(entries)} entries\n")
    for i, entry in enumerate(entries, 1):
        print(f"  ╔══ Entry #{i} ══════════════════════╗")
        print(f"  ║ 📅 {entry['date']}  ⏰ {entry['time']}")
        print(f"  ║ {entry['mood']}")
        print(f"  ╠═══════════════════════════════════╣")
        for line in entry["content"].split("\n"):
            print(f"  ║  {line}")
        print(f"  ╚═══════════════════════════════════╝\n")

def search_entries(entries):
    """Search diary entries by keyword."""
    if not entries:
        print("\n  📭 No entries to search!")
        return

    keyword = input("\n  🔍 Search for: ").strip().lower()
    if not keyword:
        return

    found = []
    for i, entry in enumerate(entries, 1):
        if keyword in entry["content"].lower():
            found.append((i, entry))

    if found:
        print(f"\n  Found {len(found)} entries with '{keyword}':\n")
        for num, entry in found:
            preview = entry["content"][:60] + "..."
            print(f"  #{num} [{entry['date']}] {entry['mood']}")
            print(f"       {preview}\n")
    else:
        print(f"\n  ❌ No entries contain '{keyword}'")

def view_by_mood(entries):
    """Filter entries by mood."""
    if not entries:
        print("\n  📭 No entries yet!")
        return

    # Collect unique moods
    moods = list(set(e["mood"] for e in entries))
    print("\n  Filter by mood:")
    for i, mood in enumerate(moods, 1):
        count = sum(1 for e in entries if e["mood"] == mood)
        print(f"    {i}. {mood} ({count} entries)")

    choice = input("\n  Pick: ").strip()
    try:
        selected_mood = moods[int(choice) - 1]
    except (ValueError, IndexError):
        print("  ❌ Invalid choice!")
        return

    filtered = [e for e in entries if e["mood"] == selected_mood]
    print(f"\n  Entries with mood {selected_mood}:\n")
    for entry in filtered:
        preview = entry["content"][:50]
        print(f"  [{entry['date']}] {preview}")

def export_csv(entries):
    """Export diary entries to CSV file."""
    if not entries:
        print("\n  📭 Nothing to export!")
        return

    csv_file = "diary_export.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "time", "mood", "content"])
        writer.writeheader()
        writer.writerows(entries)

    print(f"\n  ✅ Exported {len(entries)} entries to '{csv_file}'")

def delete_entry(entries):
    """Delete an entry by number."""
    if not entries:
        print("\n  📭 No entries to delete!")
        return

    print(f"\n  You have {len(entries)} entries.")
    for i, entry in enumerate(entries, 1):
        preview = entry["content"][:40]
        print(f"    {i}. [{entry['date']}] {preview}...")

    choice = input("\n  Delete entry #: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(entries):
            removed = entries.pop(idx)
            save_diary(entries)
            print(f"  🗑️  Deleted entry from {removed['date']}")
        else:
            print("  ❌ Invalid number!")
    except ValueError:
        print("  ❌ Enter a number!")

def show_stats(entries):
    """Show diary statistics."""
    if not entries:
        print("\n  📭 No entries for stats!")
        return

    total = len(entries)
    total_words = sum(len(e["content"].split()) for e in entries)
    moods = {}
    for e in entries:
        moods[e["mood"]] = moods.get(e["mood"], 0) + 1
    top_mood = max(moods, key=moods.get)
    dates = [e["date"] for e in entries]

    print(f"\n  📊 Diary Statistics")
    print(f"  ─────────────────────────")
    print(f"  📝 Total entries:  {total}")
    print(f"  📝 Total words:    {total_words}")
    print(f"  📝 Avg words:      {total_words // total}")
    print(f"  😊 Top mood:       {top_mood} ({moods[top_mood]}x)")
    print(f"  📅 First entry:    {dates[0]}")
    print(f"  📅 Latest entry:   {dates[-1]}")

# ============================================================
# 📗 Menu & Main Loop
# ============================================================

def show_menu():
    """Display the main menu."""
    print("\n╔══════════════════════════════════╗")
    print("║        📔 MY DIARY APP           ║")
    print("╠══════════════════════════════════╣")
    print("║  1.  ✏️  Write New Entry          ║")
    print("║  2.  📖 View All Entries          ║")
    print("║  3.  🔍 Search Entries            ║")
    print("║  4.  😊 View by Mood              ║")
    print("║  5.  📊 Statistics                ║")
    print("║  6.  📤 Export to CSV             ║")
    print("║  7.  🗑️  Delete Entry              ║")
    print("║  0.  👋 Exit                      ║")
    print("╚══════════════════════════════════╝")

# --- Main Program ---
print("Welcome to your Personal Diary! 📔")
entries = load_diary()
print(f"  Loaded {len(entries)} existing entries.\n")

while True:
    show_menu()
    choice = input("\n  Choose (0-7): ").strip()

    if choice == "0":
        save_diary(entries)
        print("\n  👋 Goodbye! Your diary is saved.")
        print("  ✅ Module 6 Complete! Move on to 07_error_handling/")
        break
    elif choice == "1":
        add_entry(entries)
    elif choice == "2":
        view_entries(entries)
    elif choice == "3":
        search_entries(entries)
    elif choice == "4":
        view_by_mood(entries)
    elif choice == "5":
        show_stats(entries)
    elif choice == "6":
        export_csv(entries)
    elif choice == "7":
        delete_entry(entries)
    else:
        print("  ❌ Invalid choice! Pick 0-7.")
