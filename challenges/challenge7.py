a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [number for number in a if number%2==0]
print('Full list:', a)
print('Even numbers (list comprehension):\n', even)

even2 = []
for number in a:
    if number%2==0:
        even2.append(number)

print('Even numbers (for loop with if cond):\n', even2)

# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = []
# for year in years_of_birth:
#     ages.append(2018 - year)
#
# print(ages)
#
# ages = [2018 - year for year in years_of_birth]
# print(ages)
#
# # new_list = [expression for_clause 0_or_more_for_or_if_clauses]
# # result - new list resulting from evaluating the expression in the
# # context of the for and if clauses which follow it
#
# # For example, this listcomp combines the elements of two
# # lists if they are not equal:
# new_list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(new_list)
