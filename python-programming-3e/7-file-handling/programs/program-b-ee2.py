# program-b-ee2.py (Program from Book, Extra Example NO.2)
# PG.286

# Closing an already closed file

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

with open(file_path, "r") as file:
    for line in file:
        print(line, end = "")
# file-1.txt closes, after this "with" block of code is executed
print("\nLet's check if the file is closed:", file.closed)
file.close() # attempt to close a file that is already closed