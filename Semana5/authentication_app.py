from tkinter import messagebox
import tkinter as tk

#Main windows
root = tk.Tk()
root.title("Authentication App")
root.geometry("400x400")
root.config(bg="#f0f4c3")

#title
title_app = tk.Label(root, text="Authentication App", font=("Arial", 20), bg="#f0f4c3")
title_app.pack(pady=10)

#CREDENTIALS
USER_CREDENTIALS = {
    'admin' : '1234',
    'user1' : 'pass'
}


#user input
user_label = tk.Label(root, text="Username: ", bg="#f0f4c3")
user_label.pack()
user_input = tk.Entry(root)
user_input.pack(pady=10)

#password input
password_label = tk.Label(root, text="Password: ", bg="#f0f4c3")
password_label.pack()
password_input = tk.Entry(root)
password_input.pack(pady=10)

#functions
def login():
    username = user_input.get()
    password = password_input.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Succesfully", f'Welcome {username}')
    else:
        messagebox.showerror("Error", 'Error login')

def clear():
    user_input.delete(0, tk.END)
    password_input.delete(0, tk.END)

#buttons
button_login = tk.Button(root, text="Login", command=login, bg='blue', fg='white').pack(pady=10)
button_clear = tk.Button(root, text="Clear", command=clear, bg='cyan', fg='black').pack(pady=10)
button_destroy = tk.Button(root, text="Exit", command=root.destroy, bg='red', fg='white').pack(pady=10)

#Loop main
root.mainloop()