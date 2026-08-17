# EXAMPLE 7.22 : Program to demonstrate use of os.path.isabs(path) method

import os

relative_path = os.path.join(".", "example-files", "file-1.txt")
absolute_path = __file__

print(f"os.path.isabs({relative_path}) = {os.path.isabs(relative_path)}")
print(f"os.path.isabs({absolute_path}) = {os.path.isabs(absolute_path)}")