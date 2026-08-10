# EXAMPLE 7.12 : Program to perform split operation whenever a string 'list' is encountered

with open("./example-files/file-2.txt", "r") as file:
    for line in file:
        words = line.split('line')
        print(words)
