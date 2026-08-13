# MY SIDE PROGRAM - 7.1 : To show the use of fileno() method

with open("./example-files/file-1.txt", "r") as file:
    print(f"File Descriptor Number of {file.name} is {file.fileno()}")
