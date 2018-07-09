"""
A program that storees this book information;
Title, Author
Year, ISBN

User can:
View all records
Seach an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from tkinter import ttk
import backend

root = Tk()

l1 = Label(root, text='Title')
l1.grid(row=0, column=0)

l2 = Label(root, text='Year')
l2.grid(row=1, column=0)

l3 = Label(root, text='Author')
l3.grid(row=0, column=2)

l4 = Label(root, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = ttk.Entry(root, textvariable=title_text)
e1.grid(row=0, column=1)

year_text = StringVar()
e2 = ttk.Entry(root, textvariable=year_text)
e2.grid(row=1, column=1)

author_text = StringVar()
e3 = ttk.Entry(root, textvariable=author_text)
e3.grid(row=0, column=3)

isbn_text = StringVar()
e4 = ttk.Entry(root, textvariable=isbn_text)
e4.grid(row=1, column=3)

list_box = Listbox(root, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = ttk.Scrollbar(root)
scroll_bar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

b1 = ttk.Button(root, text='View all', width=12)
b1.grid(row=2, column=3)

b2 = ttk.Button(root, text='Search entry', width=12)
b2.grid(row=3, column=3)

b3 = ttk.Button(root, text='Add entry', width=12)
b3.grid(row=4, column=3)

b4 = ttk.Button(root, text='Update', width=12)
b4.grid(row=5, column=3)

b5 = ttk.Button(root, text='Delete', width=12)
b5.grid(row=6, column=3)

b6 = ttk.Button(root, text='Close', width=12)
b6.grid(row=7, column=3)

root.mainloop()
