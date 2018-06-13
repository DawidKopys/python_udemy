import timeit

def remove_duplicates(a_list):
    return list(set(a_list))

def remove_duplicates2(a_list):
    new_list = []
    for x in a_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def remove_duplicates_trick(a_list):
    new_list = []
    [new_list.append(x) for x in a_list if x not in new_list]
    return new_list

a = [1, 1, 2, 12, 32, 2, 1, 9, 5, 5]*50
print(a)
print(remove_duplicates(a))
print(remove_duplicates2(a))
print(remove_duplicates_trick(a))


t1 = timeit.repeat(lambda: remove_duplicates(a))
t2 = timeit.repeat(lambda: remove_duplicates2(a))
t3 = timeit.repeat(lambda: remove_duplicates_trick(a))
print('t1 =', max(t1))
print('t2 =', max(t2))
print('t3 =', max(t3))
