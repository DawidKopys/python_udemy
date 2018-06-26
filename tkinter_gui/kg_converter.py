from tkinter import *

def km_to_grams():
    grams = float(kg_val.get())*1000
    t_grams.delete("1.0", END)
    t_grams.insert(END, grams)

def km_to_pounds():
    pounds = float(kg_val.get())*2.20462
    t_pounds.delete("1.0", END)
    t_pounds.insert(END, pounds)

def km_to_ounces():
    ounces = float(kg_val.get())*35.274
    t_ounces.delete("1.0", END)
    t_ounces.insert(END, ounces)

def convert():
    km_to_grams()
    km_to_pounds()
    km_to_ounces()

window = Tk()

b1 = Button(window, text='Convert', command=convert)
b1.grid(row=0, column=2)

kg_label = Label(window, text='Kg')
kg_label.grid(row=0, column=0)

kg_val = StringVar()
kg_entry = Entry(window, textvariable=kg_val)
kg_entry.grid(row=0, column=1)

t_grams = Text(window, height=1, width=20)
t_grams.grid(row=1, column=0)

t_pounds = Text(window, height=1, width=20)
t_pounds.grid(row=1, column=1)

t_ounces = Text(window, height=1, width=20)
t_ounces.grid(row=1, column=2)

window.mainloop()
