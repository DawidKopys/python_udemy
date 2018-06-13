import random

a = random.randint(1, 9)
counter, choice = 0, 0
print('Welcome in the game! To exit, type exit.')

while choice != a:
    counter = counter + 1
    choice = input('Guess a number between 1 and 9: ').lower()
    if choice == 'exit':
        break
    else:
        choice = int(choice)
    if choice > a:
        print('Go lower!')
    elif choice < a:
        print('Go higher!')
    else:
        print('You guessed it! The number was', choice)
        print('You needed', counter, 'tries!')
