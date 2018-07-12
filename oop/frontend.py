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
from backend import Database

database = Database()

class Bookstore:

    def __init__(self, parent_root):
        parent_root.wm_title('BookStore')

        l1 = Label(root, text='Title')
        l1.grid(row=0, column=0)

        l2 = Label(root, text='Year')
        l2.grid(row=1, column=0)

        l3 = Label(root, text='Author')
        l3.grid(row=0, column=2)

        l4 = Label(root, text='ISBN')
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = ttk.Entry(root, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.year_text = StringVar()
        self.e2 = ttk.Entry(root, textvariable=self.year_text)
        self.e2.grid(row=1, column=1)

        self.author_text = StringVar()
        self.e3 = ttk.Entry(root, textvariable=self.author_text)
        self.e3.grid(row=0, column=3)

        self.isbn_text = StringVar()
        self.e4 = ttk.Entry(root, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list_box = Listbox(root, height=6, width=45)
        self.list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

        scroll_bar = ttk.Scrollbar(root)
        scroll_bar.grid(row=2, column=2, rowspan=6)

        self.list_box.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=self.list_box.yview)

        # list_box.bind(event_type, function_to_be_bound_to_the_event)
        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = ttk.Button(root, text='View all', width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = ttk.Button(root, text='Search entry', width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = ttk.Button(root, text='Add entry', width=12, command=self.insert_command)
        b3.grid(row=4, column=3)

        b4 = ttk.Button(root, text='Update', width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        # bind - used to bind a function to a widget event
        b5 = ttk.Button(root, text='Delete', width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = ttk.Button(root, text='Close', width=12, command=parent_root.destroy)
        b6.grid(row=7, column=3)

    # this function is bound to an event so it get a special 'event' parameter
    # the 'event' parameter holds information about the type of the event
    def get_selected_row(self, event):
        global selected_row
        try:
            index = self.list_box.curselection()[0]
            selected_row = self.list_box.get(index)
            # fill entreis with selected row values
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e1.insert(END, selected_row[1])
            self.e2.insert(END, selected_row[3])
            self.e3.insert(END, selected_row[2])
            self.e4.insert(END, selected_row[4])
        except IndexError:
            pass

    def view_command(self):
        self.list_box.delete(0, END)
        cont = database.view()
        for row in cont:
            self.list_box.insert(END, row)

    def search_command(self):
        self.list_box.delete(0, END)
        cont = database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        for row in cont:
            self.list_box.insert(END, row)
            # list_box.select_set(cont)

    def insert_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list_box.delete(0, END)
        self.view_command()
        # list_box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))#wg mnie zamiast tej linii powinna być ta zakomentowana na górze

    def update_command(self):
        database.update(selected_row[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()

    def delete_command(self):
        database.delete(selected_row[0])
        self.view_command()
        # nie da się tutaj, bez tego bind i get_selected_row?

    # def __del__(self):
    #     parent_root.destroy()

root = Tk()

bookstore = Bookstore(root)

root.mainloop()
