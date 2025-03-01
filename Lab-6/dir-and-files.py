import os
import string

path = os.path.abspath("Lab-6") # делаем абсолютный путь к нашей папке (не пишем вручную)
path_2 = os.path.abspath("Lab-6/Test")
path_3 = os.path.abspath("Lab-6/Test/test.txt")
path_4 = os.path.abspath("Lab-6/Test/test2.txt")
path_5 = os.path.abspath("Lab-6/Test/A.txt")

# TASK 1

print("All directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("All files:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("*" * 30)

# TASK 2

print("Existence : ", os.path.exists(path))
print("Readability : ", os.access(path, os.R_OK))
print("Writability : ", os.access(path, os.W_OK))
print("Executability : ", os.access(path, os.X_OK))

print("*" * 30)

# TASK 3

if os.path.exists(path_2):
    print(f"{path_2} exist")
    print("Directory : ", os.path.dirname(path_2))
    print("File name : ", os.path.basename(path_2))
else:
    print(f"{path_2} doesn't exist")

print("*" * 30)

# TASK 4

with open(path_3, "r") as file:
    lines = file.readlines()
    print(f"Ammount strings in {path_3}: {len(lines)}")

print("*" * 30)

# TASK 5

listik = ["Oyasumi", "Jeka", "Peka", "Bobr"]

with open(path_3, "w") as file:
        for item in listik:
            file.write(f"{item}\n")

# TASK 6

for letter in string.ascii_uppercase:
    filename = os.path.join(path_2, f"{letter}.txt")
    with open(filename, "w") as file:
            file.write(f"It is {letter}.txt")

# TASK 7

with open(path_3, "r") as src, open(path_4, "w") as dest:
            dest.write(src.read())

# TASK 8

if os.path.exists(path_5):
    if os.access(path_5, os.W_OK):
        os.remove(path_5)
    else:
        print(f"Do not have a permission {path_5}")
else:
    print(f"{path_5} does not exist")