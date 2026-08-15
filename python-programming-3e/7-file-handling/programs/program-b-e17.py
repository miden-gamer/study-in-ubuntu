# EXAMPLE 7.17 : Program that changes the current directory to our newly created 
# directory - "new-dir"

from pathlib import Path
import os

directory = Path(__file__).parent / "example-directories" / "new-dir"

print("Current Working Directory is:", os.getcwd())
os.chdir(directory)
print("After chdir, the current directory is now......", os.getcwd())