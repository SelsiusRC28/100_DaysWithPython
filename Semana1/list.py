shop_car = []

def show_menu():
    print("\n ------Shop Cart------")
    print("1 Show Cart")
    print("2 Add Item")
    print("3 Remove Item")
    print("4 Clear Cart")
    print("5 Exit")
    print("----------------------")
    
while True:
    show_menu()
  
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Showing cart items...")
        for index, item in enumerate(shop_car, start=1):
            print(f"{index}. {item}")
    elif choice == '2':
        item = input("Enter item to add: ")
        if not item:
            print("No item entered, please try again.")
        else:
            shop_car.append(item)
            print(f"Adding {item} to cart...")
        # Logic to add item to cart
    elif choice == '3':
        item = input("Enter item to remove: ")
        if not item:
            print("No item entered, please try again.")
        else:
            shop_car.pop(int(item) - 1)
            print(f"Removing {item} from cart...")
        # Logic to remove item from cart
    elif choice == '4':
        shop_car.clear()
        print("Clearing the cart...")
        # Logic to clear the cart
    elif choice == '5':
        print("Exiting the shop cart.")
        break
    else:
        print("Invalid choice, please try again.")
    