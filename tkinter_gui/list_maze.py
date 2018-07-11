
l = []

dim_x = range(10)
dim_y = range(10)

for y in dim_y:
    l.append([])
    for x in dim_x:
        l[y].append(x)

for row in l:
    for col in row:
        print(col)
    print(type(row))
    print(row)
