import tkinter as tk
from tkinter import messagebox

#config
root = tk.Tk()
root.title("app")
root.geometry("400x600")
root.config(bg="#aadafa")

#functions
def add_task():
    select = input_task.get()
    if select:
        listbox.insert(tk.END ,select)
        select.delete(0, tk.END)
    else:
        messagebox.showerror("Eror", "This input is emply")

def del_task():
    select = listbox.curselection()
    if select:
        listbox.delete(select[0])
        input_task.delete(0, tk.END)
    else:
        messagebox.showerror("Eror", "Select one task")

def clear():
    listbox.delete(0, tk.END)

title = tk.Label(root, text="To Do List App", font=('Arial', 20), bg="#aadafa")
title.pack(pady=5)

input_task = tk.Entry(root, font=("Arial", 12), width=30)
input_task.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

#Buttons
button_add = tk.Button(frame_buttons, text="Add Task", command=add_task, bg="#aafadf", fg="black")
button_add.grid(row=0, column=0)

#Buttons
button_del = tk.Button(frame_buttons, text="Delet Task", command=del_task, bg="#aafadf", fg="black")
button_del.grid(row=0, column=1)

#Buttons
button_clear = tk.Button(frame_buttons, text="Clear", command=clear, bg="#aafadf", fg="black")
button_clear.grid(row=0, column=2)


#To do frame
frame_todo = tk.Frame(root , width=200, height=300)
frame_todo.pack()

scrollbar = tk.Scrollbar(frame_todo)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox = tk.Listbox(frame_todo, width=50, height=15, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)

scrollbar.config(command=listbox.yview)

button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.pack(pady=10)


#mainloop
root.mainloop()