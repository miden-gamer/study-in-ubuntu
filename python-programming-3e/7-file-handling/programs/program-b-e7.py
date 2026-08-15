# EXAMPLE 7.7 : Read contents of file using readline() method.

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "r")
i = 1
while True:
    line = file.readline()
    if line == "":
        break
    print(f"Line {i} : {line}", end = "")
    i += 1
file.close()