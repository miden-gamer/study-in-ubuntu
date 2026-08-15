# EXAMPLE 7.21 : Program to demonstrate the use of os.path.abspath() method

from pathlib import Path
import os

cwd = os.getcwd()
current_file_dir = os.path.dirname(__file__)
relative_path = os.path.relpath(current_file_dir, cwd)

print("CWD:", cwd)
print("Relative Path (relative to CWD):", relative_path)

file_path = os.path.join(relative_path, Path(__file__).name)
print("File Path:", file_path)
print("Absolute Path:", os.path.abspath(file_path))