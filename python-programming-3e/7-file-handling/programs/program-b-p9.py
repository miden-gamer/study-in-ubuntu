# PROGRAM 7.9 : Write a program that reads a file line by line. Each line read 
# from the file is copied to another file with line numbers specified at 
# beginning of the line

from pathlib import Path

source_file = Path(__file__).parent / "example-files" / "file-2.txt"
dest_file = Path(__file__).parent / "example-files" / "file-8.txt"

with open(source_file) as sf:
    with open(dest_file, "w") as df:
        num = 1
        for line in sf:
            df.write(str(num) + " : " + line)
            num += 1
print(f"Lines from {source_file.name} pasted in {dest_file.name} with line numbers......")