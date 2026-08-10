# EXAMPLE 7.9 : Program to display the contents of the file using list() method

file = open("./example-files/file-2.txt", "r")
print(list(file))
file.close()
