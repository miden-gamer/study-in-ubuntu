# EXAMPLE 7.26 : Program to demonstrate use of os.path.getsize(path) and os.listdir(path) method

import os

directory = os.path.join(os.path.dirname(__file__), "example-files")

print(f"Size of file \"{os.path.basename(__file__)}\" = {os.path.getsize(__file__)} bytes")
print(f"List of files and directories within \"{directory}\":")
print(os.listdir(directory))