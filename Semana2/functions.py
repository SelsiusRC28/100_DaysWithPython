# Step 1: Define conversion functions
def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  return (kelvin - 273.15) * 9/5 + 32

def menu():
    print("\n ------- Temperature Conversion Menu -------")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Kelvin to Celsius & Farenheit")
    print("3. Fahrenheit to Celsius & Kelvin")
    print("4. Exit")

while True:
    menu()
    choise = int(input("Select the option: "))
    
    if(choise == 1):
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.5f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius):.5f}")
    elif(choise == 2):
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin)}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin)}")
    elif(choise == 3):
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(fahrenheit)}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit)}")
    elif(choise == 4):
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")
    