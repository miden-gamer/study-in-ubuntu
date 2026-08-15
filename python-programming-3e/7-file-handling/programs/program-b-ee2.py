# program-b-ee2.py (Program from Book, Extra Example NO.2)
# PG.286

# Closing an already closed file

# Path is Python's cross-platform way of working with file and directory paths.
# __file__ gives the path of this Python program, and .parent gives its directory.
# The / operator joins the directory with "example-files/file-6.txt".
# This is used instead of a relative path like "./example-files/file-6.txt"
# so the file is found relative to the program's location, regardless of
# the current working directory or whether the program runs on Windows/Linux.
from pathlib import Path
file_path = Path(__file__).parent / "example-files" / "file-1.txt"

# Actual Program
with open(file_path, "r") as file:  # Uses "file-1.txt"
    for line in file:
        print(line, end = "")
# file-1.txt closes, after this "with" block of code is executed
print("\nLet's check if the file is closed:", file.closed)
file.close() # attempt to close a file that is already closed