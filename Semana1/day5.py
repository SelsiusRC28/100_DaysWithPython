import time

number = int(input("Coloca el numero "))

for n in range(number, 0, -1):
    print(n)
    if(n == number /2 ):
        print("Esta por el medio, ya falta poco")
    time.sleep(0.05)
    
print("feliz anio nuevo")