# EXAMPLE 7.6 : Program to print the first 10 characters of the file file-1.txt

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

file = open(file_path, "r")
print(file.read(10))
file.close()