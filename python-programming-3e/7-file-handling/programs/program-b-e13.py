# EXAMPLE 7.13 : Program that tells and sets the position of the file pointer

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

with open(file_path, "rb") as file:
    print("Position of file pointer before reading is:", file.tell())
    print(file.read(10))
    print("Position of file pointer after reading is:", file.tell())
    print("Setting 3 bytes from the current position of file pointer.")
    file.seek(3, 1)
    print(file.read(10))
    file.close()