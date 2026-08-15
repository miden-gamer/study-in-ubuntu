# EXAMPLE 7.3 : Program that writes a message in the file, file-1.txt

# Path is Python's cross-platform way of working with file and directory paths.
# __file__ gives the path of this Python program, and .parent gives its directory.
# The / operator joins the directory with "example-files/file-6.txt".
# This is used instead of a relative path like "./example-files/file-6.txt"
# so the file is found relative to the program's location, regardless of
# the current working directory or whether the program runs on Windows/Linux.
from pathlib import Path
file_path = Path(__file__).parent / "example-files" / "file-1.txt"

# Actual Program
file = open(file_path, "w")  # Uses "file-1.txt"
file.write("Hello, This is the \"file-1.txt\".")
file.close()
print("Data written into the file......")