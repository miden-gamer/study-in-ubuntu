# PG.295

# Program to demonstrate use of rmtree() method

from pathlib import Path
import shutil

directory = Path(__file__).parent / "example-directories" / "new-dir"

# Fill the empty directory if empty
file = open(directory / "file-1.txt", "w")
file.close()
file = open(directory / "file-2.txt", "w")
file.close()

shutil.rmtree(directory)
print("Non-Empty Directory Deleted......")