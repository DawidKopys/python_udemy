number = int(input('Give me number: '))
if  number % 2 == 0:
    if number % 4 == 0:
        print(str(number) + ' is divisable by 4.')
    else:
        print(str(number) + ' is an even number.')
else:
    print(str(number) + ' is an odd number.')

# extras2
num = int(input('Give me a number: '))
check = int(input('Give me a number to divide by: '))
if num % check == 0:
    print(str(num) + ' is divisable by ' + str(check) + '.')
else:
    print(str(num) + ' is NOT divisable by ' + str(check) + '.')
