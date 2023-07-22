import tkinter
from tkinter import Label, Entry, Button, Text, END
from Translator.uzbek_and_cyrilic_dictionary import to_cyrillic, to_latin


def trans():
    resul = ""
    a = text_entry.get()
    if a.isascii():
        resul = to_cyrillic(a)
        resulat.configure(text="Krilcha-Ko'rinishi")
    else:
        resul = to_latin(a)
        resulat.configure(text="Lotin-Ko'rinishi")
    text_vidget.delete(1.0, END)
    text_vidget.insert(END, resul)


windows = tkinter.Tk()
windows.title("Lotin-Kril-Perevochik")
windows.geometry('500x600')
text_label = Label(windows, text="So'z kiriting", bg="red", font=20)
text_label.place(x=0, y=10)
text_entry = Entry(windows, width=20, font=20)
text_entry.place(x=0, y=50)

resulat = Label(windows, text="", bg="red", font=20)
resulat.place(x=0, y=90)

buttton = Button(windows, text="Enter", padx=20, pady=10, bg="green", command=trans)
buttton.place(x=210, y=40)

text_vidget = Text(windows)
text_vidget.place(x=0, y=120)
if __name__ == "__main__":
    windows.mainloop()
