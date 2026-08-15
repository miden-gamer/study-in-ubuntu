# PROGRAM 7.3 : Write a program that copies one Python script into another in 
# such a way that all comment lines are skipped and not copied in the 
# destination file.

from pathlib import Path

file_path_1 = Path(__file__).parent / "example-files" / "python-file-1.py"
file_path_2 = Path(__file__).parent / "example-files" / "python-file-2.py"

with open(file_path_1, "rb") as file_1:
    with open(file_path_2, "wb") as file_2:
        while True:
            buf = file_1.readline()
            if len(buf) != 0:
                if buf.startswith(b'#'):
                    continue
                else:
                    file_2.write(buf)
            else:
                break
print("File copied......")