# EXAMPLE 7.7 : Read contents of file using readline() method.

# Path is Python's cross-platform way of working with file and directory paths.
# __file__ gives the path of this Python program, and .parent gives its directory.
# The / operator joins the directory with "example-files/file-6.txt".
# This is used instead of a relative path like "./example-files/file-6.txt"
# so the file is found relative to the program's location, regardless of
# the current working directory or whether the program runs on Windows/Linux.
from pathlib import Path
file_path = Path(__file__).parent / "example-files" / "file-2.txt"

# Actual Program
file = open(file_path, "r")  # Uses "file-2.txt"
i = 1
while True:
    line = file.readline()
    if line == "":
        break
    print(f"Line {i} : {line}", end = "")
    i += 1
file.close()