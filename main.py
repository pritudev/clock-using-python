from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("Retroica", 80),
              background="#1f1f1f", foreground="white")
label.pack(anchor="center")

time()
mainloop()
