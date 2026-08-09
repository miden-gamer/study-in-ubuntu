# EXAMPLE 7.5 : Program to append data to an already existing file

file = open("./example-files/file-2.txt", "a")
lines = ["\nThis is line 3.", "\nThis is line 4."]
file.writelines(lines)
file.close()
print("Data appended into file......")
