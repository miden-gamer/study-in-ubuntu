# MY SIDE PROGRAM - 7.3(I) : To show the use of isatty() method, example returning False.

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-4.txt"

with open(file_path, "r")  as file:
    print("File object is connected to a terminal?", file.isatty())