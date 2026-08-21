# PG.303

# Program to show use of shutil.chown()
# ! Limitation: Works only on Linux based OS (as pwd and grp are supported on Linux only)

from shutil import chown
from pathlib import Path
import os
import pwd
import grp

file_path = Path(__file__).parent / "example-files" / "file-1.txt"

def get_ownership(path):
    stat = os.stat(path)

    user = pwd.getpwuid(stat.st_uid).pw_name
    group = grp.getgrgid(stat.st_gid).gr_name

    return user, group

def change_ownership(path, requested_user=None, requested_group=None):
    valid_user = None
    valid_group = None

    # check whether user exists
    if requested_user is not None:
        try:
            pwd.getpwnam(requested_user)
            valid_user = requested_user
        except KeyError:
            print(f'ERROR: User "{requested_user}" does not exist.')

    # check wheter group exists
    if requested_group is not None:
        try:
            grp.getgrnam(requested_group)
            valid_group = requested_group
        except KeyError:
            print(f'ERROR: Group "{requested_group}" does not exist.')

    # nothing valid to change
    if valid_user is None and valid_group is None:
        print("No ownership changes were made.")
        return

    # change whatever is valid
    # None means "leave this one unchanged"
    try:
        chown(path, user=valid_user, group=valid_group)
        print("Ownership changes completed.")
    except PermissionError as e:
        print(f'ERROR: Permission denied: {e}')
    except OSError as e:
        print(f'ERROR: Could not change ownership: {e}')
# -----------------------------------------------------------------------------
# Show current ownership
# -----------------------------------------------------------------------------

user, group = get_ownership(file_path)

print(f'Current owners of "{file_path.name}":')
print(f'User = {user}')
print(f'Group = {group}')

# -----------------------------------------------------------------------------
# Try to change ownership
# -----------------------------------------------------------------------------

print("\nPerforming ownership change operation......")
change_ownership(file_path, requested_user='miden', requested_group='mes')

# -----------------------------------------------------------------------------
# Show ownership after operation
# -----------------------------------------------------------------------------

user, group = get_ownership(file_path)

print(f'\nOwners of "{file_path.name}" after operation:')
print(f'User = {user}')
print(f'Group = {group}')

# setting root as user and group
#chown(file_path, user = 'root', group = 'root')
# using uid and gid for same purpose
#chown(file_path, user = 0, group = 0)  # root uid = 0 & root gid = 0

# not changing user only changing group
#chown(file_path, user = None, group = 'mes')
# not changing group only changing user
#chown(file_path, user = 'miden', group = None)
