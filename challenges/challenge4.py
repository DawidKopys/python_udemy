number = int(input('Give me a number: '))
num_list = range(1, number+1)
div_list = []

print('List containing number lessser than', number, end='.\n')

for num in num_list:
    if number % num == 0:
        div_list.append(num)

print(number, 'divisors:', div_list)
