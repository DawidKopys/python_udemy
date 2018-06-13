u_in = input('Give me a sentence: ')

def write_reversed(sentence):
    words = sentence.split(' ')
    return ' '.join(reversed(words))

def write_reversed2(sentence):
    words = sentence.split(' ')
    return ' '.join(words[::-1])

def reverseWord(w):
    return ' '.join(w.split()[::-1])

print(write_reversed(u_in))
print(write_reversed2(u_in))
print(reverseWord(u_in))
