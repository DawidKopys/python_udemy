import timeit

def find_divisors(number):
    num_list = range(2, number)
    div_list = []

    for num in num_list:
        if number % num == 0:
            div_list.append(num)

    # print(number, 'divisors:', div_list)
    return div_list

def find_divisors_list_comprehension(number):
    return [x for x in range(2,number) if number % x == 0]

def find_divisors_no_list(number):
    num_list = range(2, number)
    divisors = 0

    for num in num_list:
        if number % num == 0:
            divisors = divisors + 1

    return divisors

def find_divisors_no_list_faster(number):
    divisors = 0
    i = 2

    while i < number:
        if number % i == 0:
            divisors = divisors + 1
        i = i + 1

    return divisors

def find_divisors_no_list_fastest(number):
    num_list = range(2, number)
    divisors = 0

    for num in num_list:
        if number % num == 0:
            divisors = divisors + 1
            if divisors >= 2:
                break

    return divisors

def is_prime(number, find_divisors_func):
    div = find_divisors_func(number)
    if type(div) == list:
        div = len(div)
    if  div >= 1:
        return False
    else:
        return True

n = input('Choose number: ')

def f_find_divisors():
    if is_prime(int(n), find_divisors):
        pass
    #     print('The number ' + n + ' is a prime number. find_divisors')
    # else:
    #     print('The number ' + n + ' is NOT a prime number. find_divisors')

def f_find_divisors_list_comprehension():
    if is_prime(int(n), find_divisors_list_comprehension):
        pass
    #     print('The number ' + n + ' is a prime number. find_divisors_list_comprehension')
    # else:
    #     print('The number ' + n + ' is NOT a prime number. find_divisors_list_comprehension')

def f_find_divisors_no_list():
    if is_prime(int(n), find_divisors_no_list):
        pass
    #     print('The number ' + n + ' is a prime number. find_divisors_no_list')
    # else:
    #     print('The number ' + n + ' is NOT a prime number. find_divisors_no_list')

def f_find_divisors_no_list_faster():
    if is_prime(int(n), find_divisors_no_list_faster):
        pass
    #     print('The number ' + n + ' is a prime number. find_divisors_no_list_faster')
    # else:
    #     print('The number ' + n + ' is NOT a prime number. find_divisors_no_list_faster')
def f_find_divisors_no_list_fastest():
    if is_prime(int(n), find_divisors_no_list_fastest):
        pass

print('Prime comparision:')
t_find_divisors = timeit.repeat(lambda: f_find_divisors())
print('t_find_divisors:', max(t_find_divisors))
t_find_divisors_list_comprehension = timeit.repeat(lambda: f_find_divisors_list_comprehension())
print('t_find_divisors_list_comprehension:', max(t_find_divisors_list_comprehension))
t_find_divisors_no_list = timeit.repeat(lambda: f_find_divisors_no_list())
print('t_find_divisors_no_list:', max(t_find_divisors_no_list))
t_find_divisors_no_list_faster = timeit.repeat(lambda: f_find_divisors_no_list_faster())
print('t_find_divisors_no_list_faster:', max(t_find_divisors_no_list_faster))
t_find_divisors_no_list_fastest = timeit.repeat(lambda: f_find_divisors_no_list_fastest())
print('t_find_divisors_no_list_fastest:', max(t_find_divisors_no_list_fastest))
