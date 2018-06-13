commands = ['rock', 'paper', 'scissors', 'quit']
cmd_p1, cmd_p2 = '', ''

print('Rock Paper Scissors DK\n   Type \"rock\" to choose Rock\n'
'   Type \"paper\" to choose Paper\n   Type \"scissors\" to choose Scissors\n'
'   To leave, type \"quit\"\n')

while (1):
    cmd_p1 = input('Player1: ').lower()
    while cmd_p1 not in commands:
        print('\nWrong command entered.\n   You can only use '
        '\"rock\", \"paper\", \"scissors\" and \"quit\"')
        cmd_p1 = input('Player1: ')
    if cmd_p1 == 'quit':
        break

    cmd_p2 = input('Player2: ').lower()
    while cmd_p2 not in commands:
        print('\nWrong command entered.\n   You can only use '
        '\"rock\", \"paper\", \"scissors\" and \"quit\"')
        cmd_p2 = input('Player2: ')
    if cmd_p2 == 'quit':
        break

    # todo: choose the winner
    outcome = ' p1: ' + cmd_p1 + ', p2: ' + cmd_p2

    if cmd_p1 == 'rock':
        if cmd_p2 == 'rock':
            print('Its a tie!' + outcome)
        elif cmd_p2 == 'paper':
            print('Paper beats rock! Player2 won!' + outcome)
        elif cmd_p2 == 'scissors':
            print('Rock beats scissors! Player1 won!' + outcome)
    elif cmd_p1 == 'paper':
        if cmd_p2 == 'paper':
            print('Its a tie!' + outcome)
        elif cmd_p2 == 'rock':
            print('Paper beats rock! Player1 won!' + outcome)
        elif cmd_p2 == 'scissors':
            print('Scissors beat paper! Player2 won!' + outcome)
    elif cmd_p1 == 'scissors':
        if cmd_p2 == 'scissors':
            print('Its a tie!' + outcome)
        elif cmd_p2 == 'rock':
            print('Rock beats scissors! Player2 won!' + outcome)
        elif cmd_p2 == 'paper':
            print('Scissors beat paper! Player1 won!' + outcome)



print('\nThanks for playing!')
