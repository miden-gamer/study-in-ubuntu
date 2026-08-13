# MY SIDE PROGRAM - 7.3(I) : To show the use of isatty() method, example returning False.

with open("./example-files/file-4.txt", "r")  as file:
    print("File object is connected to a terminal?", file.isatty())
