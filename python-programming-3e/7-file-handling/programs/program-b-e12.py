# EXAMPLE 7.12 : Program to perform split operation whenever a string 'list' is encountered

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

with open(file_path, "r") as file:
    for line in file:
        words = line.split('line')
        print(words)