# MY SIDE PROGRAM - 7.6(II) : To show the use of rstrip() method, (Remove newline and !)

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-6.txt"

with open(file_path, "r") as file:
    for line in file:
        print(line.rstrip("\n!"))