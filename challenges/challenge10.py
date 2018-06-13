import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

# rozw z list comprehension ale bez set - with duplicates
common = [number for number in a if number in b]
print(common, '- list compr. w/o sets -> with duplicates')

# rozw bez list comprehension
common2 = list(set(a) & set(b))
print(common2, '- sets, without duplicates')

# rozw z list comprehension i z set - without duplicates
common3 = [number for number in set(a) if number in b]
print(common3, '- list compr. w/ sets -> without duplicates')
