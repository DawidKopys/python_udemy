
# param:
#   @filename - a file containing maze layotu description in
#               the following format (1-wall, 0-no wall, 3-cell):
# 1 1 1 1 1 1 1 1 1 1 1
# 1 3 0 3 0 3 0 3 0 3 1
# 1 0 0 0 0 0 0 0 0 0 1
# 1 3 0 3 0 3 0 3 0 3 1
# 1 0 0 0 0 0 0 0 0 0 1
# 1 3 0 3 0 3 0 3 0 3 1
# 1 0 0 0 0 0 0 0 0 0 1
# 1 3 0 3 0 3 0 3 0 3 1
# 1 1 1 1 1 1 1 1 1 1 1


# return:
#   @maze_list - list representing a maze in the following format:
# ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1']
# ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']


def read_maze(filename):
    f = open(filename, 'r')
    contents = f.readlines()
    cont_raw = [line.strip() for line in contents]
    maze_list = [line.split(' ') for line in cont_raw]
    return maze_list

if __name__=='__main__':
    l = read_maze('maze.txt')
    for line in l:
        print(line)
