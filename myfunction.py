def to_hours(minutes, seconds=0):
    hours = minutes / 60 + seconds / 3600
    return hours

l_minutes = input("Ile minut?:")
l_seconds = input("Ile sekund?:")
print(to_hours(int(l_minutes), int(l_seconds)))
