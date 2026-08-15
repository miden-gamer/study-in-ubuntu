# EXAMPLE 7.18 : Program to demonstrate use of rmdir() function

from pathlib import Path
import os

directory = Path(__file__).parent / "example-directories" / "new-dir"

os.rmdir(directory)
print("Directory Deleted......")
# Refer "program-b-ee5.py" for deleting non-empty directories.