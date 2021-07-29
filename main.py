from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock Using Python")
p1 = PhotoImage(file='G:\IMAGES\Others\pngaaa.com-3626848.png')
root.iconphoto(False, p1)


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("Roboto Black", 100),
              background="#1f1f1f", foreground="white")

label.pack(anchor="center")
time()
mainloop()
