from tkinter import *

# generates list of Canvases based on list describing the maze layout
def generate_maze(maze_layout, root):
    l = []
    y_ind = 0
    for y in maze_layout:
        l.append([])
        for x in y:
            if x == '1':
                color = '#202020'
            elif x == '3':
                color = 'green'
            else:
                color = '#E8E8E8'
            l[y_ind].append(Canvas(root, width='15', height='15', background=color))
        y_ind = y_ind + 1
    return l
