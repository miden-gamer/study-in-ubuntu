# PG.301

# Know the file permissions of a particular file

from pathlib import Path
import os
import stat  # Imported for using "stat.filemode()"

file = Path(__file__).parent / "example-files" / "file-1.txt"
stats = os.stat(file)
print("Decimal Representation:", stats.st_mode)  # Decimal Representation (Default)
print("Octal Representation:", oct(stats.st_mode))  # Octal Representation

print("rwx Representation:", stat.filemode(stats.st_mode))  # rwx Representation

# Refer "../../Unorganized/"