# EXAMPLE 7.10 : Program to display the contents of a file using loop

file = open("./example-files/file-2.txt", "r")
for line in file:
    print(line, end = "")
