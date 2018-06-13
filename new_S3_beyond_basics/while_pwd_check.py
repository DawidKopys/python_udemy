correct_pwd = "123"
name = input("Enter name: ")
pwd = input("Enter password: ")

while pwd != correct_pwd:
    pwd = input("Enter password: ")

print("Hi", name, "you are logged in!")
print("Hi %s you are logged in!" % name)
message = "Hi %s you are logged in!" % name
print(message)

surname = "Kopys"
message = "Hi %s %s you are logged in!" % (name, surname)
print(message)
