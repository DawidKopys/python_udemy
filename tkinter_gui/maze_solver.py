from tkinter import *
from tkinter import ttk

root = Tk()
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

mazeframe = ttk.Frame(root, padding="3 3 3 3")
mazeframe.grid(column=0, row=0, sticky=N+S+E+W)
mazeframe.configure(borderwidth=2, relief='sunken')
# mazeframe.columnconfigure(0, weight=1)
# mazeframe.rowconfigure(0, weight=1)
# mazeframe.columnconfigure(1, weight=1)
# mazeframe.rowconfigure(1, weight=1)

menuframe = ttk.Frame(root, padding="3 3 3 3")
menuframe.grid(column=1, row=0, sticky=N+S+E+W)
menuframe.configure(borderwidth=2, relief='sunken')
menuframe.columnconfigure(0, weight=2)
menuframe.rowconfigure(0, weight=2)

label2 = ttk.Label(menuframe, width='20')
label2.configure(background='blue')

# label1.grid(row=0, column=0, sticky=N+S+E+W)
label2.grid(row=0, column=0, sticky=N+S+E+W)

l = []
dim_x = range(16)
dim_y = range(16)

for y in dim_y:
    l.append([])
    for x in dim_x:
        if (x+y)%2==0:
            color = '#202020'
        else:
            color = '#E8E8E8'
        l[y].append(ttk.Label(mazeframe, width='3', background=color))

for y in dim_y:
    for x in dim_x:
        l[y][x].grid(row=y, column=x, sticky=N+S+E+W)

root.mainloop()
