# EXAMPLE 7.14 : Program to rename file "old-name.txt" to "new-name.txt"

from pathlib import Path
import os

directory = Path(__file__).parent / "example-files"

# Create file if not exist
file = open(directory / "old-name.txt", "w")
file.close()

os.rename(directory / "old-name.txt", directory / "new-name.txt")
# there are methods in pathlib also to rename files
print("File Renamed......")