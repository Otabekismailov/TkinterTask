from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
from shablon import Task
from datetime import datetime
import csv
import os

trans = Tk()
trans.title("Google -> Perevochik")

trans.resizable(width=False, height=False)
name = Frame(trans, height=400, width=800, bg='#313145', )
name.grid(row=0, column=1)

original_text = Text(trans, height=15, width=30)
original_text.place(x=0, y=50)

trans_text = Text(trans, height=15, width=30)
trans_text.place(x=550, y=50)

trans_label = Label(trans, text="Tilni Tanlang", bg="red", font=20)
trans_label.place(x=0, y=320)

file_path = "Translator.csv"


def perevochik_text():
    trans_text.delete(1.0, END)

    try:
        for key, valu in language.items():
            if valu == original_combo.get():
                tarjima_key_1 = key
        for key, valu in language.items():
            if valu == trans_combo.get():
                tarjima_key_2 = key
        words = textblob.TextBlob(original_text.get(1.0, END))
        wordst = words.translate(from_lang=tarjima_key_1, to=tarjima_key_2)
        trans_text.insert(1.0, wordst, END)
        task = Task(orginal_language=words, tarns_language=wordst, created_at=datetime.now())
        with open(file_path, "a+", newline="\n") as f:
            data = task.get_attrs_as_dict()
            header = ["orginal_language", "created_at", "tarns_language"]
            dict_writer = csv.DictWriter(f, header)
            if os.path.getsize(file_path) == 0:
                dict_writer.writeheader()
            dict_writer.writerow(data)


    except:
        messagebox.showerror("Erorr", "\nSo'z topilmadi"
                                      "\nQaytatan O'rinib Ko'ring"),


def clear():
    original_text.delete(1.0, END)
    trans_text.delete(1.0, END)


language = googletrans.LANGUAGES
language_list = list(language.values())

button_trans = Button(trans, text="Perevochik!", width=20, bg="red", font=30, command=perevochik_text, )
button_trans.place(x=280, y=150)

original_combo = ttk.Combobox(trans, width=20, values=language_list)
original_combo.place(x=0, y=350)

trans_label1 = Label(trans, text="Qaysi Tilga Tanlang", bg="red", font=20, )
trans_label1.place(x=620, y=320)

trans_combo = ttk.Combobox(trans, width=20, values=language_list)
trans_combo.place(x=620, y=350)

orta_label = Label(trans, text="------>", bg="yellow", font=100)
orta_label.place(x=280, y=350)

cler_button = Button(trans, text="Clear", bg="red", font=60, command=clear)
cler_button.place(x=350, y=350)

if __name__ == ("__main__"):
    trans.mainloop()
