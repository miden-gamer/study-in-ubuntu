# MY SIDE PROGRAM - 7.1 : To show the use of fileno() method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

with open(file_path, "r") as file:
    print(f"File Descriptor Number of {file_path.name} is {file.fileno()}")