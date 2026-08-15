# EXAMPLE 7.3 : Program that writes a message in the file, file-1.txt

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

file = open(file_path, "w")
file.write("Hello, This is the \"file-1.txt\".")
file.close()
print("Data written into the file......")