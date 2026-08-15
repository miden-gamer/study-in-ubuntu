# MY SIDE EXAMPLE - 7.4 : To show the use of readline(n) method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-2.txt"

with open(file_path, "r") as file:
    print(file.readline(10))