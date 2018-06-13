import random

def generate_password():
    letters_range = [0, 1, 2]
    numbers_range = [3, 4]
    symbols_range = [5]

    symbols_sample = list(range(33,45)) + list(range(91,96))

    # generate number of characters for the password
    number_of_characters = random.randint(10,15)
    print(number_of_characters)

    i = 0
    password = ''
    while i < number_of_characters:
        # generate a character
        # step1. letter-[0,1,2]/number-[3,4]/symbol-2
        character_type = random.randint(0, 5)
        if character_type in letters_range: # letter
            character = chr(random.randint(97, 122))
            # big-0/small-1
            size = random.randint(0, 1)
            if size == 0:
                character = character.capitalize()
        elif character_type in numbers_range: # number
            character = str(random.randint(0, 9))
        elif character_type in symbols_range:
            character = chr(random.sample(symbols_sample, 1)[0])

        password = password + character
        i = i + 1

    return password

print(generate_password())
