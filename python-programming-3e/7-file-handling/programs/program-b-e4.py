# EXAMPLE 7.4 : Program to write to a file using the writelines() method

file = open("./example-files/file-2.txt", "w")
lines = ["This is the line 1.\n", "This is line 2.", " In continuation to line 2."]
file.writelines(lines)
file.close()
print("Data written to file......")
