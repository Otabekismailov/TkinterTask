import csv
import tkinter
from tkinter import *
from tkcalendar import *
from regis import Hotel
from tkinter import messagebox
import os

hospitels = []


def add():
    hotell = Hotel(
        name_entry.get(),
        faml_entr.get(),
        age_entr.get(),
        from_entr.get(),
        day_entr.get(),
        result_entr.get()
    )
    hospitels.append(hotell.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    with open("hotel.csv", "a", newline="\n") as file:
        header = ["First_name", "Last_name", "Age", "Countr", "Day", "Payment"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("hotel.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(hospitels)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    name_entry.delete(0, END)
    faml_entr.delete(0, END)
    from_entr.delete(0, END)
    day_entr.delete(0, END)
    result_entr.delete(0, END)


hotel = Tk()
hotel.title("P10-Mexmonxonamizga Xush kelibsiz")
name = Frame(hotel, height=600, width=600, bg='white', )
name.grid(row=0, column=1)
hotel.resizable(width=False, height=False)
label_hotel = Label(hotel, text="Iltimos Ro'yxatdan O'ting", bg="red", font=(None, 20))
label_hotel.place(x=130, y=0)

name_label = Label(hotel, text='Ismingizni Kiriting', font=20)
name_label.place(x=80, y=80)
name_entry = Entry(hotel, width=20)
name_entry.place(x=80, y=120)

faml_label = Label(hotel, text="Familangizni Kiriting", font=20)
faml_label.place(x=80, y=160)
faml_entr = Entry(hotel, width=20)
faml_entr.place(x=80, y=200)

age_label = Label(hotel, text="Yoshingiz, Kiriting", font=20)
age_label.place(x=80, y=240)
age_entr = DateEntry(hotel)
age_entr.place(x=80, y=280)

countr_label = Label(hotel, text="Qaysi Mamlakatdansiz  Kiriting", font=20)
countr_label.place(x=80, y=320)
from_entr = Entry(hotel, width=30)
from_entr.place(x=80, y=360)
day_label = Label(hotel, text='Necha Kun Qolmoqchisiz  Kiriting', font=20)
day_label.place(x=80, y=400)

text = tkinter.StringVar()


def day_result():
    try:
        day_entr.get()
        current = 200
        summa = current * int(day_entr.get())
        summa = str(summa)
        text.set(summa + '$')
    except:
        messagebox.showerror(("Erorr"),
                             "Erorr Fayl")


day_entr = Entry(hotel, width=5)
day_entr.place(x=80, y=440)

result_label = Label(hotel, text="Shuncha To'lov Qilishingiz Kerak |", font=20, bg="red")
result_label.place(x=80, y=480)
result_entr = Entry(hotel, textvariable=text, font=20)
result_entr.place(x=80, y=520)

button = Button(hotel, text="Enter", padx=10, pady=10, bg="green", command=day_result)
button.place(x=130, y=427)
save_btn = Button(hotel, text="Save", padx=20, pady=10, bg="red", command=save)
save_btn.place(x=155, y=550)

# Add button
add_btn = Button(hotel, text="Add", padx=20, pady=10, bg="red", command=add)
add_btn.place(x=80, y=550)

# Clear button
clear_btn = Button(hotel, text="Clear", padx=18, pady=10, bg="red", command=clear)
clear_btn.place(x=235, y=550)

# Exit button
exit_btn = Button(hotel, text="Exit", padx=20, pady=10, bg="red", command=hotel.quit)
exit_btn.place(x=315, y=550)

hotel.mainloop()
