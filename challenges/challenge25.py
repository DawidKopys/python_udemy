import math

top = 101
bot = 1
guess_range = range(bot, top)
y_n = ''

while y_n != 'Y':
    if top - bot == 2:
        print('yolo')
        mid = top - 1
    else:
        mid = math.ceil(bot-1+(top-bot)/2)

    print('My guess: ' + str(mid))
    y_n = input('L - go lower  \nH - go higher\nY - got it\n')
    if y_n == 'L':
        top = mid
    elif y_n == 'H':
        bot = mid


print('I guessed it! :D')
