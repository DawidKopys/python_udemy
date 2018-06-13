a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

roof = int(input('Choose a number: '))

# extras1
new_list = []
for element in a:
    if element < roof:
        new_list.append(element)

print(new_list)
