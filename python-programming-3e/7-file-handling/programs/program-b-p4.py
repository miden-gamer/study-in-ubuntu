# PROGRAM 7.4 : Write a program that accepts filename as an input from the user. 
# Open the file and count the number of times a character appears in file.

# Additions made to the original program: 
# The following lines specify the folder containing the files, display the 
# filenames available in that folder, and create the complete path of the 
# file selected by the user. This makes it easier for the user to see which 
# files are available before entering a filename. 
# 
# folder.iterdir() gets all items present in the folder. 
# file.is_file() ensures that only files, not folders, are displayed. 
# file.name displays only the filename instead of its complete path. 
# folder / filename combines the folder path and the selected filename 
# to create the complete path of the file to be opened.

from pathlib import Path

folder = Path(__file__).parent / "example-files"

print("Available files:")
for file in folder.iterdir():
    if file.is_file():
        print(file.name)

filename = input("\nEnter the file name of file to be opened: ")
source_file = folder / filename

with open(source_file) as file:
    text = file.read()

letter = input("Enter character to be searched: ")
count = 0
for char in text:
    if char == letter:
        count += 1
print(letter, "appears", count, "times in file.")