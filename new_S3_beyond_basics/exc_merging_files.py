
# ROZW1
def merge_files1(new_file_filename, nr_of_files_to_merge):
    i = 0
    with open(new_file_filename, "w") as new_file:
        while i < nr_of_files_to_merge:
            i = i + 1
            filename = "file%s.txt" % str(i)
            with open(filename, "r") as file:
                new_file.write("%s\n" % file.read())

# ROZW2
def merge_files2(new_file_filename, filenames_list):
    with open(new_file_filename, "w") as new_file:
        for filename in filenames_list:
            with open(filename, "r") as file:
                new_file.write("%s\n" % file.read())

# prepare new file filename
from datetime import datetime
new_filename = "%s.txt" % datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# AD. ROZW1
merge_files1(new_filename, 3)

# AD. ROZW2
files = ["file1.txt", "file2.txt", "file3.txt"]
merge_files2(new_filename.rstrip(".txt") + "_2.txt", files)

# AD. ROZW2 + GLOB2
import glob2
files = glob2.glob("file*.txt")
merge_files2(new_filename.rstrip(".txt") + "_3.txt", files)
