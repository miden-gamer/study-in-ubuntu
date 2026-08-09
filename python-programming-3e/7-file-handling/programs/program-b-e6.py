# EXAMPLE 7.6 : Program to print the first 10 characters of the file file-1.txt

file = open("./example-files/file-1.txt", "r")
print(file.read(10))
file.close()
