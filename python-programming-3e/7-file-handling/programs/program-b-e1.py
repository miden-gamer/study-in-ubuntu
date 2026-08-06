file = open("./example-files/file-1.txt", "wb")
print("Name of the file:", file.name)
print("File is closed.", file.closed)
print("File has been opened in", file.mode, "mode.")
