def cel_to_fahr(c):
    if c <= -273.15:
        return "Too low temperature, this is not possible."
    else :
        f = c * 9/5 + 32
        return f

print((cel_to_fahr(20)))
print((cel_to_fahr(0)))
print((cel_to_fahr(-20)))
print((cel_to_fahr(-400)))
print((cel_to_fahr(-20)))
