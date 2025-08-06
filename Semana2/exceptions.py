def add(x, y ):
    print("La suma es", x + y)
    
def sub(x, y ):
    print("La resta es", x - y)

def mult(x, y ):
    print("La multiplicacion es", x * y)

def div(x, y ):
   print("La divicion es", x / y)

def menu():
    print("\n ------- Menu Calculator Safe -------")
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicacion")
    print("4 Divicion")
    print("5 Exit")
    
while True:
    menu()
    choise = int(input("Select the opcion: "))
   
    
    try:
        if(choise == 5):
            break
        num1 = int(input("Number: "))
        num2 = int(input("Number2: "))
        
        if(choise == 1):
            add(num1, num2)
        elif(choise == 2):
            sub(num1, num2)
        elif(choise == 3):
            mult(num1, num2)
        elif(choise == 4):
            div(num1, num2)
        else:
            print("Invalid option")
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print("Error:", e)
    else:
        print("Operation completed successfully")
    finally:
        print("Thank you for using the calculator")
    