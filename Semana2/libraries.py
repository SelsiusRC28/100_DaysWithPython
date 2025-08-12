import random, string

letra1 = string.ascii_lowercase
letra2 = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

def generar_contrasena(longitud = 12):
    if longitud < 4:
        raise ValueError("La longitud de la contraseña debe ser al menos 4 caracteres")
    password = [
       random.choice(letra1),
       random.choice(letra2),
       
       random.choice(numeros),
       random.choice(simbolos)
       ]
    todos_los_caracteres = letra1 + letra2 + numeros + simbolos
    print(password)
    password += random.choices(todos_los_caracteres, k=longitud - 4)
    print(password)
    random.shuffle(password)
    return ''.join(password)
try:
    input_usuario = int(input("Ingrese la longitud de la contraseña mayora 4 : "))
    print(generar_contrasena(input_usuario))
    
except ValueError as e:
    print("Error:", e)
