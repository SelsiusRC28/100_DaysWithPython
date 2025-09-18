import tkinter as tk
from tkinter import colorchooser

#Config tkinter
root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("600x600")
root.config(bg="#C4F1DD")

#Default senttings
curret_color = "black"
current_thickness = 2

#canvas
canvas = tk.Canvas(root, width=500, height=400, bg="white", relief="ridge", bd=2)
canvas.pack(pady=20)
 
#Func
def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - current_thickness, y - current_thickness, x + current_thickness, y + current_thickness,
                       fill=curret_color, outline=curret_color)
    
def clear():
    canvas.delete("all")

def change_color():
    global curret_color
    color = colorchooser.askcolor()[1]
    if color:
        curret_color = color
    
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

#Bind Drawing
canvas.bind("<B1-Motion>", draw)


# Control Panel
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

select_button = tk.Button(control_frame, text="Choose color" , command=change_color, bg="#4CAF50", fg="black", font=("Arial", 10))
select_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(control_frame, text="Clear" , command=clear, bg="red", fg="black", font=("Arial", 10))
clear_button.grid(row=0, column=1, padx=10)


thickness_label = tk.Label(control_frame, text="Select thickness",  font=("Arial", 10), bg="yellow")
thickness_label.grid(row=0, column=2, pady=10)

thickness_slider = tk.Scale(control_frame, from_=0, to=10, orient="horizontal", command=change_thickness,  bg="#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row=0, column=3, padx=10)

#mainloop
root.mainloop()