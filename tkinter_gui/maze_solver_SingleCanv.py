from tkinter import *
from tkinter import ttk

#   N
# W   E
#   S

# Labirynt ma wymiar 16x16, mapa labiryntu przechowywana będzie więc
# w liście, w której będzie 16 list, każda o długości 16 elementów.
# Każdy element przedstawia pojedyńczą komórkę labiryntu, zakodowane są
# tam informacje o obecności/braku ścian: 1 - ściana obecna, 0 - brak ściany:
# Potrzebujemy po 8 bitów na każdą komórę, układ bitów w pojedyńczej komórce:
# x x x x N E S W                         x x x x N E S W
# przykład, komórka |_| będzie oznaczona: x x x x 0 1 1 1
# wymiar labiryntu - 800x800px (co daje 50x50px na komórkę)
size = 800
nr_of_cells = 16
offset = 20
down = size+offset
right = size+offset
up = offset
left = offset

def print_border(parent_canvas):
    #canvas.create_line(x0, y0, x1, y1)
    parent_canvas.create_line(offset, offset, size+offset, offset)
    parent_canvas.create_line(offset, offset, offset, size+offset)
    parent_canvas.create_line(size+offset, offset, size+offset, size+offset)
    parent_canvas.create_line(offset, size+offset, size+offset, size+offset)

root = Tk()
# root childs can stretch
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

mazeframe = ttk.Frame(root, padding="3 3 3 3")
mazeframe.grid(column=0, row=0, sticky=N+S+E+W)
mazeframe.configure(borderwidth=2, relief='sunken')
mazeframe.columnconfigure(0, weight=2)
mazeframe.rowconfigure(0, weight=2)

menuframe = ttk.Frame(root, padding="3 3 3 3")
menuframe.grid(column=1, row=0, sticky=N+S+E+W)
menuframe.configure(borderwidth=2, relief='sunken')
menuframe.columnconfigure(0, weight=2)
menuframe.rowconfigure(0, weight=2)

label2 = ttk.Label(menuframe)
label2.configure(background='blue', width='20')
label2.grid(row=0, column=0, sticky=N+S+E+W)

# create Canvas

canvas = Canvas(mazeframe, width=size+2*offset, height=size+2*offset)
canvas.configure(background='white')
canvas.grid(row=0, column=0, sticky=N+S+E+W)
#canvas.create_line(x0, y0, x1, y1)
print_border(canvas)

step = size/nr_of_cells
if step%1!=0:   #sprawdzamy czy liczba jest calkowita (czy size jest podzielne przez nr_of_cells)
    print('error')
else:
    pass
    # x = offset
    # for line in range(nr_of_cells):
    #     x = x + step
    #     canvas.create_line(x, )


root.mainloop()
