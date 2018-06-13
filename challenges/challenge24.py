def v_line(length):
    line = ' '
    line += '--- ' * length
    return line

def h_line(length):
    line = '|   ' * length + '|'
    return line

def draw_game_board(length, height):
    height_range = range(height)
    for _ in height_range:
        print(v_line(length))
        print(h_line(length))
    print(v_line(length))

def list_game_board(length, height):
    height_range = range(height)
    game_board = []
    for _ in height_range:
        game_board.append(v_line(length))
        game_board.append(h_line(length))
    game_board.append(v_line(length))
    return game_board

def str_game_board(length, height):
    height_range = range(height)
    game_board = ''
    for _ in height_range:
        game_board += v_line(length) + '\n'
        game_board += h_line(length) + '\n'
    game_board += v_line(length)
    return game_board

def str_join_game_board(length, height):
    game_board = '\n'.join((v_line(length), h_line(length)+'\n')) * height
    game_board += v_line(length)
    return game_board

def lst_to_str(lst):
    game_board = ''
    for line in lst:
        game_board += line + '\n'
    return game_board[:-2]

x = int(input('Gimme the length of the game board: '))
y = int(input('Gimme the height of the game board: '))

print('draw_game_board')
draw_game_board(x, y)

print('list_game_board')
[print(x) for x in list_game_board(x,y)]

print('str_game_board')
print(str_game_board(x,y))

print('list_game_board (with lst_to_str)')
print(lst_to_str(list_game_board(x,y)))

print('str_join_game_board')
print(str_join_game_board(x,y))
