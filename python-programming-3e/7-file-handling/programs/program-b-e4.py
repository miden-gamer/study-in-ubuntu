# EXAMPLE 7.4 : Program to write to a file using the writelines() method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "w")
lines = ["This is the line 1.\n", "This is line 2.", " In continuation to line 2."]
file.writelines(lines)
file.close()
print("Data written to file......")