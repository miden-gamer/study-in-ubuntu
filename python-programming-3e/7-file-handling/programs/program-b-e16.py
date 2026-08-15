# EXAMPLE 7.16 : Program to create a new directory "new-dir" in the "example-directories" directory.

from pathlib import Path
import os

directory = Path(__file__).parent / "example-directories" / "new-dir"

os.mkdir(directory)
print("Directory Created......")