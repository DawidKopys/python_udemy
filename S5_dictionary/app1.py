import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate_mine(word):
    word = word.lower()
    try:
        return data[word]
    except KeyError:
        return "This is not even a word."

def translate_udemy(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) != 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist."

in_word = input("Enter word: ")

output = translate_udemy(in_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
