# PROGRAM 7.6 : Write a program that counts the number of tabs, spaces and 
# newline characters in a file.

import os

directory = os.path.join(os.path.dirname(__file__), "example-files")

print("Available files:")
for file in os.listdir(directory):
    path = os.path.join(directory, file)

    if os.path.isfile(path):
        print(file)

filename = input("Enter the filename of file to be opened: ")
source_file = os.path.join(directory, filename)

with open(source_file) as file:
    text = file.read()

count_tab = 0
count_space = 0
count_newline = 0

for char in text:
    if char == '\t':
        count_tab += 1
    elif char == ' ':
        count_space += 1
    elif char == '\n':
        count_newline += 1
    else:
        continue

print("Tabs =", count_tab)
print("Spaces =", count_space)
print("Newlines =", count_newline)