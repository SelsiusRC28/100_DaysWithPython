import json
import os

FILE_NAME = 'Semana3/file.json'

def menu():
    print("------- Menu --------")
    print("1 Add Task")
    print("2 View Tasks")
    print("3 Update Task")
    print("4 Delete Task")
    print("5 Exit")

def save_task(tasks):
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=2)
        

def load_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
    with open(FILE_NAME) as file:
        reader = json.load(file)
        return reader
    
def view_task():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
    with open(FILE_NAME) as file:
        tasks = json.load(file)
        
        for task in enumerate(tasks, start=1):
            print("\n")
            print(task[0], task[1]['task'], f"   ({task[1]['status']})")
            
def add_task():
    input_task = input("Add a new task: ").strip()
    tasks = load_file()
    try:
        tasks.append({
            "task" : input_task,
            "status" : "Incomplete"
        })
    except KeyError:
        print("Error de key")
    
    save_task(tasks)
        

def edit_task():
    view_task()
    
    try: 
        input_task = int(input("Edit task at number: ").strip()) -1
        tasks = load_file()
        if 0 <= input_task < len(tasks):
            tasks[input_task]["status"] = "Complete"
            # print(tasks[input_task]["status"])
            save_task(tasks)
            view_task()
        else:
            print("Select one nomber correct")
    except KeyError:
        print("Error de key")
    except ValueError:
        print("Coloca un numero valido")
        
def delete_task():
    view_task()
    
    try: 
        input_task = int(input("Delete task at number: ").strip()) -1
        tasks = load_file()
        if 0 <= input_task < len(tasks):
            tasks.pop(input_task)
            save_task(tasks)
            view_task()
        else:
            print("Select one nomber correct")
    except KeyError:
        print("Error de key")
    except ValueError:
        print("Coloca un numero valido")

while True:
    menu()
    select = int(input("Select the options: ").strip())
    if(select == 1):
        add_task()
    elif(select == 2):
        view_task()
    elif(select == 3):
        edit_task()
    elif(select == 4):
        delete_task()
    elif(select == 5):
        break
    else:
        print("Select valid option")