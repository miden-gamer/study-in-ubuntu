# PG.304

# Program to work on symlinks and hardlinks in files (Part-2)

import os
from pathlib import Path

source_file = Path(__file__).parent / "example-files" / "file-10.txt"
sl_file = Path(__file__).parent / "example-files" / "slf-to-file-10.txt"
hl_file = Path(__file__).parent / "example-files" / "hlf-to-file-10.txt"

# create symlink
#os.symlink(source_file, sl_file)

# create hardlink
#os.link(source_file, hl_file)

# check if a file is symlink
print(f'Is "{sl_file.name}" a symlink? {os.path.islink(sl_file)}')
print(f'Is "{source_file.name}" a symlink? {os.path.islink(source_file)}')

# see number of hardlinks associated with a file
stats = os.stat(source_file)
print(f'No. of hardlinks for "{source_file.name}" = {stats.st_nlink}')
