# EXAMPLE 7.7 : Read contents of file using readline() method.

file = open("./example-files/file-2.txt", "r")
i = 1
while True:
    line = file.readline()
    if line == "":
        break
    print(f"Line {i} : {line}", end = "")
    i += 1
file.close()
