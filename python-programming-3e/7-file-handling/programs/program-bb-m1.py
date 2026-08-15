# MY SIDE PROGRAM - 7.1 : To show the use of fileno() method

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
    print(f"File Descriptor Number of {file_path.name} is {file.fileno()}")
# file.name may contain the complete path used to open the file.
# Since file_path is a Path object, .name gives only the file's name, without the directory path.