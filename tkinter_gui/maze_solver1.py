from tkinter import *
from tkinter import ttk
from maze_read import read_maze

maze_list = read_maze('maze.txt')

# generates list of Canvases based on list describing the maze layout
def generate_maze(maze_layout):
    l = []
    y_ind = 0
    for y in maze_layout:
        l.append([])
        for x in y:
            print('y_ind', y_ind)
            if x == '1':
                color = '#202020'
                print('czarny')
            else:
                color = '#E8E8E8'
                print('bialy')
            l[y_ind].append(Canvas(mazeframe, width='15', height='15', background=color))
        y_ind = y_ind + 1
    return l


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

# l = []
dim_x = range(10)
dim_y = range(10)

l = generate_maze(read_maze('maze.txt'))

for y in dim_y:
    for x in dim_x:
        l[y][x].grid(row=y, column=x, sticky=N+S+E+W)

root.mainloop()
