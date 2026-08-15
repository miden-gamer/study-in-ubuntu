# EXAMPLE 7.15 : Program to delete a file named "new-name.txt"

from pathlib import Path
import os

directory = Path(__file__).parent / "example-files"

os.remove(directory / "new-name.txt")
print("File Deleted......")