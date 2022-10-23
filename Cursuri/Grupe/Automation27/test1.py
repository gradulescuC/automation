import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
				firstname = first_name_entry.get()
				lastname = last_name_entry.get()


window = tkinter.Tk()
window.title("Formular masă Grădinița Paradisul copiilor")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="Nume Copil")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Prenume copil")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Grupa")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

for widget in user_info_frame.winfo_children():
		widget.grid_configure(padx=10, pady=5)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()