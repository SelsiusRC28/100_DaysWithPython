import tkinter as tk

root = tk.Tk()
root.title("Counter App")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

counter = 0


def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")


def decement():
    global counter

    counter -= 1
    counter_label.config(text=f"Clicks: {counter}")


def reset():
    global counter
    counter = 0
    counter_label.config(text=f"Clicks: 0")


counter_title = tk.Label(text="Counter App", font=("Arial", 20))
counter_title.pack(pady=20)


counter_label = tk.Label(text="Click= 0")
counter_label.pack(pady=10)

button = tk.Button(text="Click Me", command=increment, font=("Arial", 14))
button.pack(pady=10)

button_decrement = tk.Button(
    text="Decrement Me", command=decement, font=("Arial", 14))
button_decrement.pack(pady=10)


button_reset = tk.Button(text="Reset", command=reset, font=("Arial", 14))
button_reset.pack(pady=10)

root.mainloop()
