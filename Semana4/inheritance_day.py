

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def display_info(self):
        print(f"\n------ {self.name} -------")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        
    def calculate_bonus(self):
        return self.salary * 0.1
        
class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
    
    def calculate_bonus(self):
        return self.salary * 0.2
    
class Developer(Employee):
    def __init__(self, name, id, salary, lenguaje_programming):
        super().__init__(name, id, salary)
        self. lenguaje_programming =  lenguaje_programming
        
    def display_info(self):
        super().display_info()
        print(f"Lenguaje: {self.lenguaje_programming}")
    
    def calculate_bonus(self):
        return self.salary * 0.5
    
employees = []

def add_employee():
    print("1. Employee")
    print("2. Manager")
    print("3. Developer")
    print("4. Return")
    
    choise = int(input("Select the option: ").strip())
    id = input("ID: ").strip()
    name = input("Name: ").strip()
    salary = int(input("Salary: ").strip())
    
    if choise == 1:
        
        employees.append(Employee(id=id, name=name,salary=salary))
        print("Created Succesfully")
    elif choise == 2:
        department = input("Department: ").strip()
        employees.append(Manager(id=id, name=name,salary=salary, department=department))
        print("Created Succesfully")
    elif choise == 3:
        lenguaje = input("Lenguaje: ").strip()
        employees.append(Developer(id=id, name=name,salary=salary, lenguaje_programming=lenguaje))
        print("Created Succesfully")
    else :
        return

def show_info():
    if employees:
        for employee in employees:
            employee.display_info()
            print(f"Bonus: {employee.calculate_bonus()}")
    else:
        print("\n No employees")
            

#Main
while True:
    print("\n -------- Company ---------")
    print("1. Add new Employee/Manager/Developer")
    print("2. Show Info")
    print("3. Exit")
    
    choise = int(input("Select the option: ").strip())
    
    if choise == 1 :
        add_employee()
    elif choise == 2:
        show_info()
    elif choise == 3:
        break
    else:
        print("Invalit option")