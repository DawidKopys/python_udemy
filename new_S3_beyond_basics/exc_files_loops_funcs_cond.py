temperatures = [10, -20, -289, 100]

# ROZW1
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 + 32
        return f

myfile = open("exc_files_loops_funcs_cond.txt", "w")
for t in temperatures:
    myfile.write("%s\n" % str(c_to_f(t)))
myfile.close()

# ROZW2
def writer(temp, filepath):
    with open(filepath, "w") as file:
        for t in temp:
            if t < -273.15:
                file.write("That temperature doesn't make sense!\n")
            else:
                f = t * 9/5 + 32
                file.write(str(f) + "\n")

writer(temperatures, "exc_files_loops_funcs_cond2.txt")
