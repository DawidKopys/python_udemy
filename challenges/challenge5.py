a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

for el in a:
    if el in b:
        if not el in common:
            common.append(el)

print(common)

# rozw2
common2 = []
for el in a:
    if el in b:
        common2.append(el)

common2 = list(set(common2))
print(common2)

# rozw3
common3 = set()
for el in a:
    if el in b:
        common3.add(el)

common3 = list(common3)
print(common3)

# rozw4
common4 = list(set(a) & set(b))
print(common4)
