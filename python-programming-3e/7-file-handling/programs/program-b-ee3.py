# program-b-ee3.py (Program from Book, Extra Example NO. 3)
# PG.287

# Opening a single file using command line argument

import sys
with open(sys.argv[1]) as file:
    for line in file:
        print(line, end = "")
print()

# Run the below command in terminal to execute:
# $ python3 program-b-ee3.py "<file-path>"
#
# sys.argv[0] is the name of program (Python script name) and sys.argv[1] and so on are file-paths/file-names.