import tkinter as tk

# 1. Crear la ventana principal
root = tk.Tk()
root.title("Mi Primera GUI") # Título de la ventana
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# 2. Crear un widget (una etiqueta)
label = tk.Label(root, text="Hola, Usuario", font=("Arial", 18))
label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

#3 Acctions
def greet():
    name = entry.get()
    if name:
         label.config(text=f"Hola, {name}", fg="green")
    else:
        label.config(text="Please enter your name!", fg="red")

def clear():
    entry.delete(0, 'end')
    label.config(text="")



button = tk.Button(root, text="Enviar", command=greet)
butto2 = tk.Button(root, text="Limpiar", command=clear)

button.pack(pady=10)
butto2.pack()


# 4. Iniciar el bucle principal
root.mainloop()