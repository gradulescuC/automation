import tkinter
from tkinter import ttk, END
from tkinter import messagebox


def enter_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    file = open('user.txt', 'w')
    file.write(firstname)
    file.write(lastname)
    file.close()

    # clear the form
    firstname.delete(0, END)
    lastname.delete(0, END)

window = tkinter.Tk()
window.title("Data Entry Form")
window.geometry('500x500')


first_name_label = tkinter.Label(text="First Name")
first_name_label.place(x=15, y=60)
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(text="Last Name")
last_name_label.place(x=15, y=60)
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(textvariable=first_name_label, width=25)
last_name_entry = tkinter.Entry()
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

# Button
button = tkinter.Button(text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()