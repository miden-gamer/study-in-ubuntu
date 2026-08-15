# program-b-e2.py (Program from Book, which is EXAMPLE 7.2)
# EXAMPLE 7.2 : Program to access a file after it is closed.

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

file = open(file_path, "wb")
print("Name of the file:", file_path.name)
print("File is closed.", file.closed)
print("File is now being closed.. You cannot use the File Object.")
file.close()
print("File is closed.", file.closed)
print(file.read())