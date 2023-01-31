from tkinter import *
import random

root = Tk()
root.title("Aceita namorar comigo?")
root.geometry("400x200")
root.config(bg="#ffffff")

def move_button(event):
    x = random.randint(0, 300)
    y = random.randint(0, 100)
    button.place(x=x, y=y)

def on_click():
    label = Label(root, text="Claro que sim! <3", font=("Helvetica", 16), bg="#ffffff")
    label.pack()

label = Label(root, text="Aceita namorar comigo?", font=("Helvetica", 20), bg="#ffffff")
label.pack(pady=50)

button = Button(root, text="Claro que sim!", command=on_click, font=("Helvetica", 16), bg="#ff69b4")
button.pack()
button.bind("<Enter>", move_button)

root.mainloop()
