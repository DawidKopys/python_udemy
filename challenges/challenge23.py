numbers_file1, numbers_file2 = [], []

def read2list(filename, a_list):
    with open(filename, 'r') as o_file:
        number = o_file.readline()
        while number:
            a_list.append(int(number))
            number = o_file.readline()

read2list('ch23_second.txt', numbers_file2)
read2list('ch23_first.txt', numbers_file1)

ov2 = [x for x in numbers_file1 if x in numbers_file2]

print(ov2)
