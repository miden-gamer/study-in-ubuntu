# EXAMPLE 7.10 : Program to display the contents of a file using loop

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "r")
for line in file:
    print(line, end = "")