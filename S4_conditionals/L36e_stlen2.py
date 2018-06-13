def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers dont have length"
    elif type(mystring) == float:
        return "Sorry, floats dont have length"
    else:
        return len(mystring)

# in_str = input("Podaj stringa: ")
# print("Dlugosc stringa: " + str(string_length(in_str)))

print(string_length('kakao'))
print(string_length(10))
print(string_length(10.0))
