# PROGRAM 7.3 : Improved Version
# Program that copies one Python script into another in such a way that all 
# comment anywhere in program are removed and not copied in destination file, 
# also remove blank lines that were left after removing comments.

from pathlib import Path
import tokenize

# Create the paths of the two files
source_file = Path(__file__).parent / "example-files" / "python-file-1.py"
destination_file = Path(__file__).parent / "example-files" / "python-file-2.py"

# Open the source Python file
with tokenize.open(source_file) as file:
    source_code = file.read()

# Convert the program into Python tokens
tokens = tokenize.generate_tokens(iter(source_code.splitlines(keepends = True)).__next__)

# Remove tokens whose type is COMMENT
tokens_without_comments = (
    token for token in tokens
    if token.type != tokenize.COMMENT
)

# Convert the tokens back into Python code
result = tokenize.untokenize(tokens_without_comments)

# Write the result into another file
with open(destination_file, "w", encoding = "utf-8") as file:
    file.write(result)

print("Comments removed successfully.")
# Learn and improve more.