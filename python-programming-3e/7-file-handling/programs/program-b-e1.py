# Path is Python's cross-platform way of working with file and directory paths.
# __file__ gives the path of this Python program, and .parent gives its directory.
# The / operator joins the directory with "example-files/file-6.txt".
# This is used instead of a relative path like "./example-files/file-6.txt"
# so the file is found relative to the program's location, regardless of
# the current working directory or whether the program runs on Windows/Linux.
from pathlib import Path
file_path = Path(__file__).parent / "example-files" / "file-1.txt"

# Actual Program
file = open(file_path, "wb")  # Uses "file-1.txt"
print("Name of the file:", file.name)
print("Name of the file (using file_path object):", file_path.name)
# file.name may contain the complete path used to open the file.
# Since file_path is a Path object, .name gives only the file's name, without the directory path.
print("File is closed.", file.closed)
print("File has been opened in", file.mode, "mode.")