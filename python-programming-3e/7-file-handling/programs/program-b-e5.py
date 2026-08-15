# EXAMPLE 7.5 : Program to append data to an already existing file

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

file = open(file_path, "a")
lines = ["\nThis is line 3.", "\nThis is line 4."]
file.writelines(lines)
file.close()
print("Data appended into file......")