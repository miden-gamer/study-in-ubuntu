# PROGRAM 7.7 : Write a program that computes the total size of all the files 
# in "example-files" directory.

import os

directory = os.path.join(os.path.dirname(__file__), "example-files")

total_size = 0
for file in os.listdir(directory):
    path = os.path.join(directory, file)

    if os.path.isfile(path):
        total_size += os.path.getsize(path)

print("Total size of all files in", directory, "=", total_size, "bytes")