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
up = offset
left = offset
down = size+offset
right = size+offset

def print_border(parent_canvas):
    #canvas.create_line(x0, y0, x1, y1)
    parent_canvas.create_line(left, up, right, up, width=2) #gora pozioma
    parent_canvas.create_line(left, up, left, down, width=2) #lewa pion
    parent_canvas.create_line(right, up, right, down, width=2) #prawa pion
    parent_canvas.create_line(left, down, right, down, width=2) #dol poziom

def print_grid(parent_canvas):
    step = size/nr_of_cells
    if step%1!=0:   #sprawdzamy czy liczba jest calkowita (czy size jest podzielne przez nr_of_cells)
        print('error')
    else:
        pass
        x_pion = left
        y_poziom = up
        for line in range(nr_of_cells):
            x_pion = x_pion + step
            parent_canvas.create_line(x_pion, up, x_pion, down, width=2)
            y_poziom = y_poziom + step
            parent_canvas.create_line(left, y_poziom, right, y_poziom, width=2)

def print_outline(parent_canvas):
    print_border(parent_canvas)
    print_grid(parent_canvas)

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
print_outline(canvas)

# stworzenie listy koordynat punktów (środki cell)
step = size/nr_of_cells
crds = []
for x in range(nr_of_cells):
    crds.append([])
    for y in range(nr_of_cells):
        crds[x].append([int(x*step+offset+step/2), int(y*step+offset+step/2)])

for row in crds:
    print(row)

print('crds[0][1] =', crds[0][1])
print('crds[0][1][0] =', crds[0][1][0])
print('crds[0][1][1] =', crds[0][1][1])

i = 0
for row in range(nr_of_cells):
    for col in range(nr_of_cells):
        canvas.create_text(crds[row][col][0], crds[row][col][1], text=str(i))
        i = i + 1

# crds to lista zawierająca środki cel, lista jest o formacie:
# [[[x0, y0], [x1, y0], [x2, y0], ...]
#  [[x0, y1], [x1, y1], [x2, y1], ...]
#   [[],[],[]]...]



root.mainloop()
