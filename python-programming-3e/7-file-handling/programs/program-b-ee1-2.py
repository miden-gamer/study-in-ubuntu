# program-b-ee1-2.py (Program from Book, Extra Example NO.1 Part 2)
# PG.286

# Compare normal way to open file from with keyword method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

file = open(file_path, "r")
for line in file:
    print(line, end = "")
print("\nLet's check if the file is closed:", file.closed)