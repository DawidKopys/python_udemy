# Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen. I have a .txt file for you,
# if you want to use it!

dict_names = {}

with open('ch22_names.txt', 'r') as o_file:
    name = o_file.readline().strip()
    while name:
        if name in dict_names.keys():
            dict_names[name] = dict_names[name] + 1
        else:
            dict_names[name] = 1
        name = o_file.readline().strip()

for pair in dict_names.items():
    print(pair)
