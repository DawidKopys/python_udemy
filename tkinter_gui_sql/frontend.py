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

# this function is bound to an event so it get a special 'event' parameter
# the 'event' parameter holds information about the type of the event
def get_selected_row(event):
    global selected_row
    index = list_box.curselection()[0]
    selected_row = list_box.get(index)
    # we also want to fill entreis with selected row values
    # todo...
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.insert(END, selected_row[2])
    e3.insert(END, selected_row[3])
    e4.insert(END, selected_row[4])
    # title_text.set(selected_row[1])
    # year_text.set(selected_row[2])
    # author_text.set(selected_row[3])
    # isbn_text.set(selected_row[4])


def insert_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    # view_command()
    list_box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))#wg mnie zamiast tej linii powinna być ta zakomentowana na górze

def update_command():
    backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # view_command()

def delete_command():
    backend.delete(selected_row[0])
    # view_command()
    # nie da się tutaj, bez tego bind i get_selected_row?


root = Tk()

window.wm_title('BookStore')

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

# list_box.bind(event_type, function_to_be_bound_to_the_event)
list_box.bind('<<ListboxSelect>>', get_selected_row)

b1 = ttk.Button(root, text='View all', width=12)
b1.grid(row=2, column=3)

b2 = ttk.Button(root, text='Search entry', width=12)
b2.grid(row=3, column=3)

b3 = ttk.Button(root, text='Add entry', width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = ttk.Button(root, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

# bind - used to bind a function to a widget event
b5 = ttk.Button(root, text='Delete', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = ttk.Button(root, text='Close', width=12, command=root.destroy())
b6.grid(row=7, column=3)

root.mainloop()
