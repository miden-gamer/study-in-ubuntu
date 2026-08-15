# PROGRAM 7.5 : Write a program that reads data from a file and calculates the 
# percentage of vowels and consonants in the file.

from pathlib import Path

directory = Path(__file__).parent / "example-files"

print("Available files:")
for file in directory.iterdir():
    if file.is_file():
        print(file.name)

filename = input("\nEnter the filename of file to be opened: ")
source_file = directory / filename

with open(source_file) as file:
    text = file.read()

count_vowels = 0
count_consonants = 0
alphabet_count = 0

for char in text:
    if char.isalpha():
        alphabet_count += 1

    if char in "AEIOUaeiou":
        count_vowels += 1
    elif char.isalpha():
        count_consonants += 1
    else:
        continue
print("\nNumber of vowels =", count_vowels)
print("Number of consonants =", count_consonants)
print("Total length of file =", len(text))
print("Total number of alphabets in file =", alphabet_count)
print(f"Percentage of vowels in the file = {(count_vowels*100)/alphabet_count:.2f} %")
print(f"Percentage of consonants in the file = {(count_consonants*100)/alphabet_count:.2f} %")