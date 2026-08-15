# EXAMPLE 7.15 : Program to delete a file named "new-name.txt"

from pathlib import Path
import os

directory = Path(__file__).parent / "example-files"
file_path = Path(__file__).parent / "example-files" / "new-name.txt"

# Create file if not exist
file = open(file_path, "w")
file.close()

os.remove(file_path)
print("File Deleted......")