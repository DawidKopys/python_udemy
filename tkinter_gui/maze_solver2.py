from tkinter import *
from tkinter import ttk
from maze_read import read_maze
from maze_gen import generate_maze

maze_list = read_maze('maze.txt')

def place_maze(maze):
    dim_y = range(len(maze))
    dim_x = range(len(maze[0]))
    for y in dim_y:
        for x in dim_x:
            l[y][x].grid(row=y, column=x, sticky=N+S+E+W)

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

label2.grid(row=0, column=0, sticky=N+S+E+W)

l = generate_maze(read_maze('maze.txt'), mazeframe)
place_maze(l)

root.mainloop()
