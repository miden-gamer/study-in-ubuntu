# EXAMPLE 7.4 : Program to write to a file using the writelines() method

# Path is Python's cross-platform way of working with file and directory paths.
# __file__ gives the path of this Python program, and .parent gives its directory.
# The / operator joins the directory with "example-files/file-6.txt".
# This is used instead of a relative path like "./example-files/file-6.txt"
# so the file is found relative to the program's location, regardless of
# the current working directory or whether the program runs on Windows/Linux.
from pathlib import Path
file_path = Path(__file__).parent / "example-files" / "file-2.txt"

# Actual Program
file = open(file_path, "w")  # Uses "file-2.txt"
lines = ["This is the line 1.\n", "This is line 2.", " In continuation to line 2."]
file.writelines(lines)
file.close()
print("Data written to file......")