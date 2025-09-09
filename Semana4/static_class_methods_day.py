class Inventory:
    total_items = 0
    
    def __init__(self, product_name, price, quantity ):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity
        
    def show_product(self):
        print(f"\n ---- {self.product_name}")
        print(f"{self.price}")
        print(f"{self.quantity}")
        
    def sell_product(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"{self.quantity } sold {self.product_name}")
        else:
            print("Insufficient quantity.")
        
    @staticmethod
    def calculate_discount(price, discount):
        print( price * (discount / 100))
    
    @classmethod
    def total_price(cls):
        print(f"Total: {cls.total_items}")
        
products = []

def add_product():
    name = input("Name of product: ")
    quantity = int(input("Quantity: "))
    price = int(input("Price: "))
    
    product = Inventory(name, price, quantity)
    products.append(product)
    print(f"{quantity} {name}(s) added to inventory.")
    
def view_products():
    if products:
        for product in products:
            product.show_product()
    else:
        print("No have products")
        
def sell_product():
   name = input("Name of product: ")
   for product in products:
       if product.product_name== name:
           amount = int(input("Amount: "))
           product.sell_product(amount)
           break
       else:
           print("Product not found")

def discount_price():
    discount = float(input("Discount: "))
    price = float(input("Price: "))
    Inventory.calculate_discount(discount, price)
    
# Main Menu
while True:
  print("\n--- Inventory Management System ---")
  print("1. Add Product")
  print("2. View Products")
  print("3. Sell Product")
  print("4. Calculate Discount")
  print("5. Total Items Report")
  print("6. Exit")

  choice = input("Enter your choice(1-6): ")

  if choice == "1":
    add_product()
  elif choice == "2":
    view_products()
  elif choice == "3":
    sell_product()
  elif choice == "4":
    discount_price()
  elif choice == "5":
    Inventory.total_price()
  elif choice == "6":
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please try again.")