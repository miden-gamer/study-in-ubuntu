# EXAMPLE 7.9 : Program to display the contents of the file using list() method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "r")
print(list(file))
file.close()