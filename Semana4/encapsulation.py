class Account:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password
        self.set_password()

    def get_email(self):
        return self._email

    def get_username(self):
        return self.username

    def get_oassword(self):
        return self.__password

    def set_password(self):
        self.__password = '******'

    def set_email(self, new_email):
        if "@" in new_email and '.' in new_email:
            self._email = new_email
            print("Email change succesfully")
        else:
            print("Format invalit")

    def display_info(self):
        print("\n ---- User ------")
        print(self.username)
        print(self._email)
        print(self.__password)


accounts = []


def add_account():
    name = input("Name is: ").strip()
    email = input("Email is: ").strip()
    account = Account(name, email, None)
    accounts.append(account)
    print("Account createed succesfully")


def edit_account():
    inputt = input("Find User: ").strip()

    
    for name in accounts:
        if name.username == inputt:
            new_email = input("Enter your new email: ").strip()
            name.set_email(new_email)
            return

    print("Account no find")


def view_accounts():
    if accounts:
        for acc in accounts:
            acc.display_info()
    else:
        print("Not found :( ")

# Main


while True:
    print("\n -------- Play -------")
    print("1. Add Account")
    print("2. Edit Account")
    print("3. Show Accounts")
    print("4. Exit")

    choise = int(input("Enter you choise: ").strip())

    if choise == 1:
        add_account()
    elif choise == 2:
        edit_account()
    elif choise == 3:
        view_accounts()
    elif choise == 4:
        break
    else:
        print("Enter the valit option")
