# EXAMPLE 7.3 : Program that writes a message in the file, file-1.txt

file = open("./example-files/file-1.txt", "w")
file.write("Hello, This is the \"file-1.txt\".")
file.close()
print("Data written into the file......")
