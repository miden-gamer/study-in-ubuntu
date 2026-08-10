# EXAMPLE 7.11 : Program to split the line into a series of words and use spacae to perform the split operation

with open("./example-files/file-2.txt", "r") as file:
    line = file.readline()
    words = line.split()
    print(words)
