# MY SIDE PROGRAM - 7.2 : To show the use of flush() method

with open("./example-files/file-4.txt", "w") as file:
    file.write("First line.\n")
    file.flush()
    file.write("Second updated line.\n")
    file.flush()
    file.write("Third updated line.\n")
print(f"{file.name} updated three times......")
