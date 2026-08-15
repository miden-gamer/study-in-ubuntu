# EXAMPLE 7.8 : Program to demonstrate readlines() function

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "r")
print(file.readlines())
file.close()