from tkinter import *
import tkinter.messagebox

root = tkinter.Tk()
root.title("Choose a number and I'll pop up it!")
root.geometry("250x250")


def number():
    for i in range(1,10):
        if num.get() == i:
            break
    tkinter.messagebox.showinfo(f"Hello,You chose number{i}")

num = IntVar()

checkbox1 = Checkbutton(root, text="1", command=number)

checkbox1.pack()

root.mainloop()