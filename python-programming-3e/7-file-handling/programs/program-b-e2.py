# program-b-e2.py (Program from Book, which is EXAMPLE 7.2)
# EXAMPLE 7.2 : Program to access a file after it is closed.

file = open("./example-files/file-1.txt", "wb")
print("Name of the file:", file.name)
print("File is closed.", file.closed)
print("File is now being closed.. You cannot use the File Object.")
file.close()
print("File is closed.", file.closed)
print(file.read())
