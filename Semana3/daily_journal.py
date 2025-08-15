JOURNAL_FILE = "Semana3/daily_journal.txt"

def add_entry(entry):
    with open(JOURNAL_FILE, "a") as file:
        file.write(entry + "\n")
    print("Entry added.")

def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.read()
            if entries:
                print("\n--- Journal Entries ---")
                print(entries)
            else:
                print("No entries found.")
                
    except FileNotFoundError:
        print("No entries found.")
        
def search_entries(keyword):
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()
            found_entries = [entry.strip() for entry in entries if keyword.lower() in entry.lower()]
            if found_entries:
                print("\n--- Search Results ---")
                for entry in found_entries:
                    print(entry)
            else:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No entries found.")

def show_menu():
    print("\n--- Daily Journal Menu ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Exit")
    
while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()
    
    if choice == "1":
        entry = input("Write your journal entry: ")
        add_entry(entry)
    elif choice == "2":
        view_entries()
    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        search_entries(keyword)
    elif choice == "4":
        print("Exiting the journal. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")