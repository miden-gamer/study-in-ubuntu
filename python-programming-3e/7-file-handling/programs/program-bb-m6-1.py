# MY SIDE PROGRAM - 7.6 (I) : To show the use of rstrip() method, (By default removes spaces, newlines and tabs from right of lines.)

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-6.txt"

with open(file_path, "r") as file:
    for line in file:
        print(line.rstrip())