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

def print_walls_border(parent_canvas):
    #canvas.create_line(x0, y0, x1, y1)
    parent_canvas.create_line(left, up, right, up, fill='blue', width=5) #gora pozioma
    parent_canvas.create_line(left, up, left, down, fill='blue', width=5) #lewa pion
    parent_canvas.create_line(right, up, right, down, fill='blue', width=5) #prawa pion
    parent_canvas.create_line(left, down, right, down, fill='blue', width=5) #dol poziom

def print_grid(parent_canvas):
    step = size/nr_of_cells
    if step%1!=0:   #sprawdzamy czy liczba jest calkowita (czy size jest podzielne przez nr_of_cells)
        print('error, step nie jest liczba calkowita (size jest niepodzielne przez nr_of_cells)')
    else:
        pass
        x_pion = left
        y_poziom = up
        for line in range(nr_of_cells):
            x_pion = x_pion + step
            parent_canvas.create_line(x_pion, up, x_pion, down, width=2)
            y_poziom = y_poziom + step
            parent_canvas.create_line(left, y_poziom, right, y_poziom, width=2)

# funkcja rysująca siatkę labiryntu
# param:
#   @parent_canvas - canvas na której rysujemy
#   @nr_of_cells - ilość komórek w labiryncie
#   @size - rozmiar labiryntu (dlugosc boku w pixelach)
#   @offset - odleglosc ramki od krawędzi okna
# return: none
def print_outline(parent_canvas):
    print_border(parent_canvas)
    print_grid(parent_canvas)

# funkcja tworząca listę koordynat
# param:
#   @nr_of_cells - ilość komórek w labiryncie
#   @size - rozmiar labiryntu (dlugosc boku w pixelach)
#   @offset - odleglosc ramki od krawędzi okna
# return:
#   #crds - lista zawierająca koordynaty punktów
#       crds to lista zawierająca środki cel, lista jest o formacie:
#       [[[x0, y0], [x1, y0], [x2, y0], ...]
#        [[x0, y1], [x1, y1], [x2, y1], ...]
#        [[],[],[], ...                    ]...]
def create_cell_points():
    step = size/nr_of_cells
    crds = []
    for x in range(nr_of_cells):
        crds.append([])
        for y in range(nr_of_cells):
            crds[x].append([int(x*step+offset+step/2), int(y*step+offset+step/2)])
    return crds

# funkcja rysująca numery komórek
# param:
#   @parent_canvas - canvas na której rysujemy
#   @list_cell_coordinates - lista zawierające koordynaty środków wszystkich komórek
#                           (return funkcji create_cell_points)
# return: none
def print_cells_numbers(parent_canvas, list_cell_coordinates):
    i = 0
    for row in range(nr_of_cells):
        for col in range(nr_of_cells):
            parent_canvas.create_text(list_cell_coordinates[row][col][0], list_cell_coordinates[row][col][1], text=str(i))
            i = i + 1

# funkcja rysuje numer komórki o podanym numerze
# param:
#   @parent_canvas - canvas na której rysujemy
#   @list_cell_coordinates - lista zawierające koordynaty środków wszystkich komórek
#                           (return funkcji create_cell_points)
#   @number - numer komórki, której numer chcemy narysować
# return: none
def print_cell_number(parent_canvas, list_cell_coordinates, number):
    points_list_flat = [col for row in points_list for col in row]
    parent_canvas.create_text(points_list_flat[number][0], points_list_flat[number][1], text=str(number))

# funkcja rysuje górną ścianę w komórce o podanym numerze
# param:
#   @parent_canvas - canvas na której rysujemy
#   @cell_coord_x - koordynata x komórki
#   @cell_coord_y - koordynata y komórki
#   @dist_centre_to_wall - odległość środka komórki od jej ścian
# return: none
def print_wall_N(parent_canvas, cell_coord_x, cell_coord_y, dist_centre_to_wall):
    parent_canvas.create_line(cell_coord_x - dist_centre_to_wall, cell_coord_y - dist_centre_to_wall,
                              cell_coord_x + dist_centre_to_wall, cell_coord_y - dist_centre_to_wall,
                               fill='blue', width=5)

# funkcja rysuje dolną ścianę w komórce o podanym numerze
# desc: patrz print_wall_N
def print_wall_S(parent_canvas, cell_coord_x, cell_coord_y, dist_centre_to_wall):
    parent_canvas.create_line(cell_coord_x - dist_centre_to_wall, cell_coord_y + dist_centre_to_wall,
                              cell_coord_x + dist_centre_to_wall, cell_coord_y + dist_centre_to_wall,
                              fill='blue', width=5)

# funkcja rysuje prawą ścianę w komórce o podanym numerze
# desc: patrz print_wall_N
def print_wall_E(parent_canvas, cell_coord_x, cell_coord_y, dist_centre_to_wall):
    parent_canvas.create_line(cell_coord_x + dist_centre_to_wall, cell_coord_y - dist_centre_to_wall,
                              cell_coord_x + dist_centre_to_wall, cell_coord_y + dist_centre_to_wall,
                              fill='blue', width=5)

# funkcja rysuje lewą ścianę w komórce o podanym numerze
# desc: patrz print_wall_N
def print_wall_W(parent_canvas, cell_coord_x, cell_coord_y, dist_centre_to_wall):
    parent_canvas.create_line(cell_coord_x - dist_centre_to_wall, cell_coord_y - dist_centre_to_wall,
                              cell_coord_x - dist_centre_to_wall, cell_coord_y + dist_centre_to_wall,
                              fill='blue', width=5)

def print_wall(parent_canvas, cell_list, list_cell_coordinates, **option):
    points_list_flat = [col for row in points_list for col in row]
    if type(cell_list) == int:
        cell_list = [cell_list] #jeśli argument jest pojedyńczą liczbą - utwórz listę, której jedynym elementem jest ta liczba
    for single_cell in cell_list:
        cell_x = points_list_flat[single_cell][0]
        cell_y = points_list_flat[single_cell][1]
        print('cell_x =',cell_x)
        print('cell_y =',cell_y)
        # parent_canvas.create_text(cell_x, cell_y, text='A') #sprawdz czy w dobrym miejscu
        step = (size/nr_of_cells)/2
        if N in option.get('side'):
            print_wall_N(parent_canvas, cell_x, cell_y, step)
        if S in option.get('side'):
            print_wall_S(parent_canvas, cell_x, cell_y, step)
        if E in option.get('side'):
            print_wall_E(parent_canvas, cell_x, cell_y, step)
        if W in option.get('side'):
            print_wall_W(parent_canvas, cell_x, cell_y, step)


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
points_list = create_cell_points()

# points_list_flat = [col for row in points_list for col in row]
#
# for row in points_list_flat:
#     print(row)

# draw cells' numbers
print_cells_numbers(canvas, points_list)
# print_cell_number(canvas, points_list, 50)

#canvas.create_line(x0, y0, x1, y1)
print_walls_border(canvas)

print_wall(canvas, 34, points_list, side=S)

walls_in = [34, 50, 66, 82, 98, 114]
for wall in walls_in:
    print_wall(canvas, wall, points_list, side=N)

walls_in2 = [wall+3 for wall in walls_in]
print_wall(canvas, walls_in2, points_list, side=W)

root.mainloop()
