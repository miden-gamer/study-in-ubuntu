# PG.303

# Show use of st_atime, st_mtime and st_ctime

import os
from pathlib import Path
import datetime

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

stats = os.stat(file_path)
print(f'Filestamps of "{file_path.name}":')
print(f'Access Time: {stats.st_atime}')
print(f'Modification Time: {stats.st_mtime}')
print(f'Creation Time: {stats.st_ctime}')

print(f'\nFilestamps of "{file_path.name}" in readable form:')

readable_at = datetime.datetime.fromtimestamp(stats.st_atime)
readable_mt = datetime.datetime.fromtimestamp(stats.st_mtime)
readable_ct = datetime.datetime.fromtimestamp(stats.st_ctime)

print(f'Access Time: {readable_at}')
print(f'Modification Time: {readable_mt}')
print(f'Creation Time: {readable_ct}')
