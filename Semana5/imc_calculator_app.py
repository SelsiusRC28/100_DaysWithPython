import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("IMC Calculator")
root.geometry("400x400")
root.configure(bg="#fcffa6")

#Title
title = tk.Label(root, text="IMC Calculator", font=("Arial", 20), bg="#fcffa6")
title.pack(pady=20)

#Weight
weight_label = tk.Label(root, text="Weight: ", font=("Arial", 14), bg="#fcffa6")
weight_label.pack()
weight_input = tk.Entry(root, font=("Arial", 10), bg="white", width=20)
weight_input.pack(pady=10)

#Height
height_label = tk.Label(root, text="Height: ", font=("Arial", 14), bg="#fcffa6")
height_label.pack()
height_input = tk.Entry(root, font=("Arial", 10), bg="white", width=20)
height_input.pack(pady=10)

#IMC Result
result_label = tk.Label(root, text="", font=("Arial", 10), bg="#fcffa6")
result_label.pack(pady=10)


#Calculate IMC
def calculator_imc():
    try: 
        weight = float(weight_input.get())
        height = float(height_input.get())
        
        if weight <= 0 and height <= 0:
            raise ValueError("Weight and Height must be positive numbers")
        else:
            imc = weight / (height * height)
            status = ''
            if imc < 18.5:
                status = "Underweight"
            elif 18.5 <= imc <= 24.9:
                status = "Normal"
            elif 24.9 <= imc <= 29.9:
                status = "Overweight"
            else:
                status = "Obesity"
        result_label.config(text=f"IMC: {imc:.2f}\n Status: {status}", fg="green")
        print(float(height_input.get()))
    except ValueError:
        messagebox.showerror("Error","Value Error")

#Buttons
calculator_button = tk.Button(root, text="Calculator", font=("Arial", 10), bg="black", fg="white", command=calculator_imc)
calculator_button.pack(pady=10)
clear_button = tk.Button(root, text="Clear", font=("Arial", 10), bg="black", fg="white", command=lambda:[weight_input.delete(0, tk.END), height_input.delete(0, tk.END), result_label.config(text="")])
clear_button.pack(pady=10)

#MainLoopp
root.mainloop()