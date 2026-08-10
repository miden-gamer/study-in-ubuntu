# program-b-ee1-1.py (Program from Book, Extra Example NO.1 Part 1)
# PG.286

# Opening file using with keyword

with open("./example-files/file-1.txt", "r") as file:
    for line in file:
        print(line, end = "")
print("\nLet's check if the file is closed:", file.closed)
