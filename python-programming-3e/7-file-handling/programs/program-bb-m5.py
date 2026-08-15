# MY SIDE EXAMPLE - 7.5 : To show the use of truncate(n) method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-5.txt"

with open(file_path, "r+") as file:
    file.truncate(5)
    print(file.readlines())