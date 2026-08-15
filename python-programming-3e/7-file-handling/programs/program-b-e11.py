# EXAMPLE 7.11 : Program to split the line into a series of words and use spacae to perform the split operation

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

with open(file_path, "r") as file:
    line = file.readline()
    words = line.split()
    print(words)