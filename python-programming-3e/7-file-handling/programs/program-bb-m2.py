# MY SIDE PROGRAM - 7.2 : To show the use of flush() method

from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "file-4.txt"

with open(file_path, "w") as file:
    file.write("First line.\n")
    file.flush()
    file.write("Second updated line.\n")
    file.flush()
    file.write("Third updated line.\n")
print(f"{file_path.name} updated three times......")