import timeit
# word = input('Give me a word: ')
word = 'abcdefghijklmnopqrstuvwxyz' * 10

# rozw1
def pal_mine():
    n_of_letters = len(word)
    i = 0
    palindrome = True

    while i < n_of_letters/2:
        if word[i] != word[n_of_letters-i-1]:
            palindrome = False
            break
        i = i + 1

    # if palindrome == True:
    #     print('no_reverse: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('no_reverse: The word \"' + word + '\" is NOT a palindrome!')

# rozw2
def pal_slicing():
    def reverse_slicing(string):
        return string[::-1]

    reverse_word = reverse_slicing(word)
    # if reverse_word == word:
    #     print('reverse_slicing: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('reverse_slicing: The word \"' + word + '\" is NOT a palindrome!')

# rozw3
def pal_for_range():
    def reverse_for_range(word):
        x = ''
        for i in range(len(word)):
            x += word[len(word)-1-i]
        return x

    reverse_word = reverse_for_range(word)
    # if reverse_word == word:
    #     print('reverse_for_range: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('reverse_for_range: The word \"' + word + '\" is NOT a palindrome!')

# rozw4
def pal_for_reversed():
    def reverse_for_reversed(word):
        x = ''
        for letter in reversed(word):
            x += letter
        return x

    reverse_word = reverse_for_reversed(word)
    # if reverse_word == word:
    #     print('reverse_for_reversed: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('reverse_for_reversed: The word \"' + word + '\" is NOT a palindrome!')

# rozw5
def pal_string_join():
    def reverse_string_join(string):
        return ''.join(reversed(string))

    reverse_word = reverse_string_join(word)
    # if reverse_word == word:
    #     print('reverse_string_join: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('reverse_string_join: The word \"' + word + '\" is NOT a palindrome!')

# rozw6
def pal_string_slowly():
    def reverse_string_slowly(string):
        new_string = ''
        index = len(string)
        while index:
            index -= 1
            new_string += string[index]
        return new_string

    reverse_word = reverse_string_slowly(word)
    # if reverse_word == word:
    #     print('reverse_string_slowly: The word \"' + word + '\" is a palindrome!')
    # else:
    #     print('reverse_string_slowly: The word \"' + word + '\" is NOT a palindrome!')

print('Reverse comparision:')
t_reverse_mine = timeit.repeat(lambda: pal_mine())
print('pal_mine:', max(t_reverse_mine))
t_reverse_slicing = timeit.repeat(lambda: pal_slicing())
print('pal_slicing:', max(t_reverse_slicing))
t_reverse_for_range = timeit.repeat(lambda: pal_for_range())
print('pal_for_range:', max(t_reverse_for_range))
t_reverse_for_reversed = timeit.repeat(lambda: pal_for_reversed())
print('pal_for_reversed:', max(t_reverse_for_reversed))
t_reverse_string_join = timeit.repeat(lambda: pal_string_join())
print('pal_string_join:', max(t_reverse_string_join))
t_reverse_string_slowly = timeit.repeat(lambda: pal_string_slowly())
print('pal_string_slowly:', max(t_reverse_string_slowly))
