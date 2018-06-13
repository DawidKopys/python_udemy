def print_list(list):
    i = 0;
    for el in list:
        print(str(i)+ ": " + str(el))
        i = i + 1;

def print_list2(list, list2=[]):
    i = 0;
    if len(list2) != 0: # jesli podalismy drugą listę
        for el, el2 in zip(list, list2):
            print(str(i)+ ": " + str(el) + ", " + str(el2))
            i = i + 1;
    else:
        for el in list:
            print(str(i)+ ": " + str(el))
            i = i + 1;

def print_list3(list, list2=[], list3=[]):
    i = 0;
    for el, el2, el3 in zip(list, list2, list3):
            print(str(i)+ ": " + str(el) + ", " + str(el2) + ", " + str(el3))
            print(type(el3))
            i = i + 1;

import pandas
data = pandas.read_csv("http://www.pythonhow.com/data/Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
names = list(data["NAME"])

cords = []
for lt, ln in zip(lat, lon):
    position = len(cords)
    cords.insert(position, [lt, ln])


# cords = zip(lat, lon)
print("Typ cords: " + str(type(cords)))
print("Typ lat: " + str(type(lat)))
print("Typ lon: " + str(type(lon)))
print("Ilosc elementow w cords: " + str(len(cords)))
print("Ilosc elementow w LAT: " + str(len(lat)))
print("Ilosc elementow w LON: " + str(len(lon)))

print("cords :")
print_list(cords)
# print("lat :")
# print_list(lat)
# print("lon :")
# print_list(lon)
print("lat, lon :")
print_list2(lat, lon)
print("names: ")
print(type(names[0]))
print_list(names)

print("lat, lon, names: ")
print_list3(lat, lon, names)

# i = 0;
# for el in cords:
#     print(str(i)+ ": " + str(el))
#     i = i + 1;
