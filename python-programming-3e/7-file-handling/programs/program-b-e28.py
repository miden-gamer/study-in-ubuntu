# EXAMPLE 7.28 : Write a program to create copy of a file using shutil module.

import os
import shutil

source_file = os.path.join(os.path.dirname(__file__), "example-files", "file-2.txt")
copy_of_file = os.path.join(os.path.dirname(__file__), "example-files", "file-2-copy-1.txt")

shutil.copy(source_file, copy_of_file)
print(f"Copy of {os.path.basename(source_file)} created, name of copy = {os.path.basename(copy_of_file)}")