FILE_NAME = "Semana2/myNotes.txt"

def menu():
    print("\n ----- Menu ---------")
    print("1 Add note")
    print("2 View notes")
    print("3 Delet notes")
    print("4 Exit")


def add_note():
    with open(FILE_NAME, 'a') as file:
        note_input = input("Write your note: ")
        file.write(note_input + '\n')
        print("\n Note added")
        
def view_notes():
       try:
           with open(FILE_NAME, "r") as file:
            notes = file.read()
            if notes :
                print(notes)
            else:
                print("Notes not found")
       except FileNotFoundError:
           print("Nottt found")
            
def delet_notes():
    input_notes = input("You have sure? (Yes/no): ")
    if(input_notes.lower() == 'yes'):
        with open(FILE_NAME, 'w'):
            pass
    else:
        print("Delection cancelled")
        
        
while True:
    menu()
    input_user = int(input("Select you option: "))
    if(input_user == 1):
        add_note()
    elif(input_user == 2):
        view_notes()
    elif(input_user ==3):
        delet_notes()
    elif(input_user == 4):
        break
    else:
        print("Invalid option")