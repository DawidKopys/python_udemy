# List:
emails = ['me@gmail.com', 'you@hotmail.com', 'they@gmail.com']

# wyświetl wszystkie pozycje z listy
for item in emails:
    print(item)

print('\nEmails containing \'gmail\'')
# wyświetl tylko te pozycje, w których jest string 'gmail'
for item in emails:
    if 'gmail' in item:
        print(item)
