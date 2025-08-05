contact = {}

def show_menu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contact:
        print("No contacts available.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        print(f"{name} - Phome {contact[name]["phone"]} Email {contact[name]["email"]}")
    else:
        print("Not found")

def del_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        contact.pop(name)
        print("successfully removed")
    else:
        print("Not found name")
        
        
while True:
    show_menu()
    
    select = input("Opciton: ")
    
    if(select == "1"):
        add_contact()
    elif(select == "2"):
        view_contacts()
    elif(select == "3"):
        search_contact()
    elif(select == "4"):
        del_contact()
    else:
        break