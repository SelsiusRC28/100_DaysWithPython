class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name 
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
        print(f"New balance added successfully. ${self.balance}")
    
    def withdraw_balance(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
        print(f"New balance withdraw successfully. ${self.balance}")
        
    def show_info(self):
        print("Name Acoount:", self.name)
        print("Your balance is: $", self.balance)
        
        
accounts = {}

def create_account():
    name = input("Write your name: ").strip()
    balance = float(input("Write your balance: ").strip())
    account = BankAccount(name, balance)
    accounts[name] = account
    print("Account created successfully")
    
def access_account():
    name = input("Write to account: ").strip()
    
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n--------Bank-------")
            print("1. Add Balance")
            print("2. Without Balance")
            print("3. Show Details")
            print("4. Exit")
            option = int(input("Select the option: ").strip())
            
            if option == 1:
                amount = float(input("Select amount: "))
                account.deposit(amount)
            elif option == 2:
                amount = float(input("Select amount: "))
                account.withdraw_balance(amount)
            elif option == 3:
                account.show_info()
            elif option == 4:
                break
            else:
                print("Invalit option")
               
    else:
        print("Account not found")
        
        
#Main
while True:
    print("\n---- THEBANK -----")
    print("1. Create Account")
    print("2. Acces Account")
    print("3. Exit")
    
    choise = int(input("Select the option: ").strip())
    if choise == 1:
        create_account()
    elif choise == 2:
        access_account()
    elif choise == 3:
        break
    else :
        print("Invalit option")
        
    