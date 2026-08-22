# PG.303

# Program to show use of os.utime() function

import os
import datetime
from pathlib import Path
# if want to use time.time()
#import time

file_path = Path(__file__).parent / "example-files" / "file-9.txt"

# get current time as UNIX timestamp
#time_in_seconds = datetime.datetime.now().timestamp()
# easy way to get current time as UNIX timestamp
#now = time.time()

# set custom timestamps instead of current time
# (format: datetime(year, month, day, hour, minute, second)
# e.g. datetime(2026, 8, 21, 7, 49, 0)
# (format with microseconds: datetime(year, month, day, hour, minute, second, microsecond)
# e.g. datetime(2026, 8, 21, 7, 49, 10, 12345)
# 1 second = 10,00,000 microsecond (possible value range = 0 to 1000000)


stats = os.stat(file_path)

print(f'\nFilestamps of "{file_path.name}" before changing:')

readable_at = datetime.datetime.fromtimestamp(stats.st_atime)
readable_mt = datetime.datetime.fromtimestamp(stats.st_mtime)
readable_ct = datetime.datetime.fromtimestamp(stats.st_ctime)

print(f'Access Time: {readable_at}')
print(f'Modification Time: {readable_mt}')
print(f'Creation Time: {readable_ct}')

print("\nChanging file timestamps......")
at = datetime.datetime(2026, 8, 22, 7, 45, 0)
mt = datetime.datetime(2026, 8, 22, 8, 10, 11, 12345)

at_ts = at.timestamp()
mt_ts = mt.timestamp()

# set timestamps simply to current time
#os.utime(file_path)
# set custom timestamps
os.utime(file_path, times=(at_ts, mt_ts))
print("File timestamps changed......")

stats = os.stat(file_path)

print(f'\nFilestamps of "{file_path.name}" after changing:')

readable_at = datetime.datetime.fromtimestamp(stats.st_atime)
readable_mt = datetime.datetime.fromtimestamp(stats.st_mtime)
readable_ct = datetime.datetime.fromtimestamp(stats.st_ctime)

print(f'Access Time: {readable_at}')
print(f'Modification Time: {readable_mt}')
print(f'Creation Time: {readable_ct}')
