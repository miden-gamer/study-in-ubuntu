# PG.290

# Seek a position in file

# os.SEEK_SET = from beginning = 0
# os.SEEK_CUR = from current = 1
# os.SEEK_END = from end = 2

from pathlib import Path
import os

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

with open(file_path, "rb") as file:
    # Jump to beginning of file
    file.seek(0)  # Equivalent to writing file.seek(0, os.SEEK_SET)

    # Read 10 bytes, moving cursor forward
    print(file.read(10))
    # Move 5 bytes backwards from current position (towards beginning)
    file.seek(-5, os.SEEK_CUR)
    # Re-read the three bytes
    print(file.read(3))
    # Go to end of file
    file.seek(0, os.SEEK_END)
    # Read last two bytes of file
    file.seek(-2, os.SEEK_CUR)
    print(file.read(2))