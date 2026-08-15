# PROGRAM - 7.1 : Write a program that opens two files using command line arguments. Copy the contents of the first file into the second file while transforming all uppercase characters into lowercase characters.

import sys
with open(sys.argv[1]) as file_1, open(sys.argv[2], "w") as file_2:
    for line in file_1:
        file_2.write(line.lower())
print(f"{sys.argv[1]} copied into {sys.argv[2]} with all letters converted to lowercase......")