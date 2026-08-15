# PROGRAM 7.2 : Write a program that copies first 10 bytes of a binary file into another.

from pathlib import Path

file_path_1 = Path(__file__).parent / "example-files" / "file-2.txt"
file_path_2 = Path(__file__).parent / "example-files" / "file-7.txt"

with open(file_path_1, "rb") as file_1:
    with open(file_path_2, "wb") as file_2:
        buf = file_1.read(10)
        file_2.write(buf)
print("File copied......")