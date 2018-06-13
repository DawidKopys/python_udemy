
password = ''

# ask for password as long as the user provides wrong password
while password != 'python123':
    password = input("Enter password:")
    if password == 'python123':
        print("You are logged in!")
    else:
        print('Sorry, try again!')
