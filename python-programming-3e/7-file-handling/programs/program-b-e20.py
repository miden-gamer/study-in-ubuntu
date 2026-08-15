# EXAMPLE 7.20 : Program to print the absolute path of a file using os.path.join

from pathlib import Path
import os

directory = Path(__file__).parent

print(os.path.join(directory, "example-files", "file-1.txt"))