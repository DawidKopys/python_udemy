from datetime import datetime as dt

name = input('What is your name: ')
print('Your name is: ', name)
age = int(input('How old are you: '))
year = str(dt.now().year + (100 - age))
number = int(input('How many times: '))
print(number*(name + ', you will be 100 years old in year ' + year + '\n'))
