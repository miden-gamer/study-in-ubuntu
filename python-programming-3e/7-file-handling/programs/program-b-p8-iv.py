# PROGRAM 7.8 : Improved Version
# Program to detect if a USB drive is attached to computer, on different OS, and 
# even if drive is connected but not mounted.

import platform
import subprocess
import json

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output = True,
            text = True,
            check = True
        )
        return result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def check_linux():
    output = run_command([
        "lsblk",
        "-J",
        "-o",
        "NAME,TRAN,TYPE,MOUNTPOINTS"
    ])

    if not output:
        return []

    data = json.loads(output)
    usb_drives = []

    for device in data["blockdevices"]:
        if device.get("tran") == "usb" and device.get("type") == "disk":
            usb_drives.append({
                "device": "/dev/" + device["name"],
                "mounted": any_mount(device)
            })

    return usb_drives

def any_mount(device):
    if device.get("mountpoints"):
        if any(point for point in device["mountpoints"]):
            return True

    for child in device.get("children", []):
        if child.get("mountpoints"):
            if any(point for point in child["mountpoints"]):
                return True

        if any_mount(child):
            return True

    return False

def check_windows():
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "Get-Disk | Where-Object {$_.BusType -eq 'USB'} | "
        "Select-Object Number, FriendlyName, IsOffline, IsBoot, OperationalStatus | "
        "ConvertTo-Json"
    ]

    output = run_command(command)

    if not output:
        return[]

    data = json.loads(output)

    if not data:
        return[]

    if isinstance(data, dict):
        data = [data]

    usb_drives = []

    for disk in data:
        usb_drives.append({
            "device": "Disk" + str(disk["Number"]),
            "name": disk.get("FriendlyName"),
            "mounted": not disk.get("IsOffline", False)
        })

    return usb_drives

def check_macos():
    output = run_command([
        "diskutil",
        "list",
        "external",
        "physical"
    ])

    if not output:
        return[]

    usb_drives = []

    for line in output.splitlines():
        line = line.strip()

        if line.startswith("/dev/disk"):
            device = line.split()[0]

            info = run_command([
                "diskutil",
                "info",
                device
            ])

            if not info:
                continue

            protocol = None
            mounted = False

            for info_line in info.splitlines():
                if ":" not in info_line:
                    continue

                key, value = info_line.split(":", 1)

                key = key.strip()
                value = value.strip()

                if key == "Protocol":
                    protocol = value
                elif key == "Mounted":
                    mounted = value == "Yes"

            if protocol == "USB":
                usb_drives.append({
                    "device": device,
                    "mounted": mounted
                })

    return usb_drives

def check_usb():
    system = platform.system()

    if system == "Linux":
        return check_linux()
    elif system == "Windows":
        return check_windows()
    elif system == "Darwin":
        return check_macos()
    else:
        print("Unsupported operating system.")
        return []

drives = check_usb()

if drives:
    print("USB storage drive detected.")

    for drive in drives:
        print("Device:", drive["device"])

        if drive["mounted"]:
            print("Status: Connected and mounted")
        else:
            print("Status: Connected but NOT mounted")
else:
    print("No USB storage drive detected.")

# Can be modified further.