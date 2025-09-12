class BankAccount:
    def __init__(self, account_number, pin):
      self.account_number = account_number
      self.__pin = pin
      self.__balance = 0
      
    def validate_pin(self, old_pin):
        return self.__pin == old_pin
    
    def check_balance(self):
        print(f"Current balance: {self.__balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Ammount: {amount}, new balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
             print("Invalid withdrawal amount")
    
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Failed to change Pin. Ensure the old Pin si correct and the new PIN is 4 digits")
            
class ATM:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self):
        account_number = input("Number: ")
        pin = input("Pin: ")
        
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully.")
        else:
            print("Invalid PIN. PIN must be 4 digits.")
    
    def autenticate_account(self):
        account_number = input("Number: ")
        pin = input("Pin: ")
        account = self.accounts.get(account_number)
        
        if account and account.validate_pin(pin):
            print("Authentication Successful.")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN.")
            
    def main_menu(self):
        while True:
            print("-------- ATM BANK --------")
            print("1. Add Account")
            print("2. Autenticate Account")
            print("3. Exit")
            
            choise = input("Select the option(1-3): ")
            
            if choise == '1':
                self.create_account()
            elif choise == '2':
                self.autenticate_account()
            elif choise == '3':
                print("Thank you for using Mini ATM Machine. Goodbye!")
                break
            else:
                print("Option invalit")
                
    def account_menu(self, account):
         while True:
            print("-------- ATM BANK --------")
            print("1. Check Balance ")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change pin")
            print("5. Logout")
            
            choise = input("Select the option(1-5): ")
            
            if choise == '1':
                account.check_balance()
            elif choise == '2':
                amount = float(input("Amount: "))
                account.deposit(amount)
            elif choise == '3':
                amount = float(input("Amount: "))
                account.withdraw(amount)
            elif choise == '4':
                old_pin = input("Your old pin:")
                new_pin = input("New pin: ")
                account.change_pin(old_pin, new_pin)
            elif choise == '5':
                print("Logout...")
                break
            else:
                   print("Invalid choice. Please select a valid option.")
                   
                   
if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
