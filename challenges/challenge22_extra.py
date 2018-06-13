# count how many of each “category” of each image there are

categories = {}

def get_category(text):
    category = text[3:text.rindex('/')]
    return category

with open('ch22_extra.txt', 'r') as o_file:
    path = o_file.readline()
    while path:
        category = get_category(path)
        if category in categories.keys():
            categories[category] = categories[category] + 1
        else:
            categories[category] = 1
        path = o_file.readline()


for pair in categories.items():
    print(pair)
