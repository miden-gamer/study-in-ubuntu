# PG.295

# Program to demonstrate use of makedirs() method (Makes directory with sub-directories)

from pathlib import Path
import os

directory = Path(__file__).parent / "example-directories"

os.makedirs(directory / "dir-2" / "sub-dir-2-1" / "sub-dir-2-1-1")
print("Directories Created......")