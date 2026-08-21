# Improved Version
# for program "program-b-ee9.py"

# Works on both Windows + Linux based OS
# Pre-requisite:
# To run on windows, you need "pywin32" library, to install it run:
# > pip install pywin32
# in windows terminal.

from pathlib import Path
import os


file_path = Path(__file__).parent / "example-files" / "file-1.txt"


# ============================================================
# LINUX / UNIX
# ============================================================

def get_linux_ownership(path):
    import pwd
    import grp

    stat = os.stat(path)

    user = pwd.getpwuid(stat.st_uid).pw_name
    group = grp.getgrgid(stat.st_gid).gr_name

    return user, group


def change_linux_ownership(path, requested_user=None, requested_group=None):
    import pwd
    import grp
    from shutil import chown

    valid_user = None
    valid_group = None

    # Check user
    if requested_user is not None:
        try:
            pwd.getpwnam(requested_user)
            valid_user = requested_user
        except KeyError:
            print(f'ERROR: User "{requested_user}" does not exist.')

    # Check group
    if requested_group is not None:
        try:
            grp.getgrnam(requested_group)
            valid_group = requested_group
        except KeyError:
            print(f'ERROR: Group "{requested_group}" does not exist.')

    # Nothing valid to change
    if valid_user is None and valid_group is None:
        print("No ownership changes were made.")
        return

    try:
        chown(
            path,
            user=valid_user,
            group=valid_group
        )

        print("Ownership change completed.")

    except PermissionError as e:
        print(f"ERROR: Permission denied: {e}")

    except OSError as e:
        print(f"ERROR: Could not change ownership: {e}")


# ============================================================
# WINDOWS
# ============================================================

def get_windows_ownership(path):
    import win32security

    security_descriptor = win32security.GetFileSecurity(
        str(path),
        win32security.OWNER_SECURITY_INFORMATION |
        win32security.GROUP_SECURITY_INFORMATION
    )

    owner_sid = security_descriptor.GetSecurityDescriptorOwner()
    group_sid = security_descriptor.GetSecurityDescriptorGroup()

    owner_name, owner_domain, _ = win32security.LookupAccountSid(
        None,
        owner_sid
    )

    group_name, group_domain, _ = win32security.LookupAccountSid(
        None,
        group_sid
    )

    return owner_name, group_name


def change_windows_ownership(path, requested_user=None, requested_group=None):
    import win32security

    valid_user_sid = None
    valid_group_sid = None

    # --------------------------------------------------------
    # Check user
    # --------------------------------------------------------

    if requested_user is not None:
        try:
            user_sid, _, _ = win32security.LookupAccountName(
                None,
                requested_user
            )

            valid_user_sid = user_sid

        except Exception as e:
            print(
                f'ERROR: User "{requested_user}" does not exist '
                f'or could not be resolved: {e}'
            )

    # --------------------------------------------------------
    # Check group
    # --------------------------------------------------------

    if requested_group is not None:
        try:
            group_sid, _, _ = win32security.LookupAccountName(
                None,
                requested_group
            )

            valid_group_sid = group_sid

        except Exception as e:
            print(
                f'ERROR: Group "{requested_group}" does not exist '
                f'or could not be resolved: {e}'
            )

    # --------------------------------------------------------
    # Nothing valid to change
    # --------------------------------------------------------

    if valid_user_sid is None and valid_group_sid is None:
        print("No ownership changes were made.")
        return

    # --------------------------------------------------------
    # Change ownership
    # --------------------------------------------------------

    security_information = 0

    if valid_user_sid is not None:
        security_information |= (
            win32security.OWNER_SECURITY_INFORMATION
        )

    if valid_group_sid is not None:
        security_information |= (
            win32security.GROUP_SECURITY_INFORMATION
        )

    try:
        win32security.SetNamedSecurityInfo(
            str(path),
            win32security.SE_FILE_OBJECT,
            security_information,
            valid_user_sid,
            valid_group_sid,
            None,
            None
        )

        print("Ownership change completed.")

    except PermissionError as e:
        print(f"ERROR: Permission denied: {e}")

    except Exception as e:
        print(f"ERROR: Could not change ownership: {e}")


# ============================================================
# PLATFORM-INDEPENDENT FUNCTIONS
# ============================================================

def get_ownership(path):
    if os.name == "nt":
        return get_windows_ownership(path)

    return get_linux_ownership(path)


def change_ownership(path, requested_user=None, requested_group=None):
    if os.name == "nt":
        change_windows_ownership(
            path,
            requested_user,
            requested_group
        )
    else:
        change_linux_ownership(
            path,
            requested_user,
            requested_group
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

print(f"Operating system: {os.name}")

# ------------------------------------------------------------
# Show current ownership
# ------------------------------------------------------------

try:
    user, group = get_ownership(file_path)

    print(f'\nCurrent owners of "{file_path.name}":')
    print(f"User  = {user}")
    print(f"Group = {group}")

except FileNotFoundError:
    print(f'ERROR: File "{file_path}" does not exist.')

except PermissionError as e:
    print(f"ERROR: Permission denied while reading ownership: {e}")

except Exception as e:
    print(f"ERROR: Could not read ownership: {e}")


# ------------------------------------------------------------
# Try to change ownership
# ------------------------------------------------------------

change_ownership(
    file_path,
    requested_user="miden",
    requested_group="mes"
)


# ------------------------------------------------------------
# Show ownership after the operation
# ------------------------------------------------------------

try:
    user, group = get_ownership(file_path)

    print(f'\nOwners of "{file_path.name}" after operation:')
    print(f"User  = {user}")
    print(f"Group = {group}")

except FileNotFoundError:
    print(f'ERROR: File "{file_path}" does not exist.')

except PermissionError as e:
    print(f"ERROR: Permission denied while reading ownership: {e}")

except Exception as e:
    print(f"ERROR: Could not read ownership: {e}")
