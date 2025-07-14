import os
import subprocess
import sys


def run_command():
    try:
        subprocess.run(["dracut", "--force"], check=True)
        print("Dracut was executed successfully")
    except subprocess.SubprocessError as sbpe:
        print(f"Dracut failed, error: {sbpe}")
        sys.exit(1)


def ask_for_reboot():
    print("Want to restart your computer? [y/n]")
    answer = input()
    if answer == "y":
        subprocess.run(["reboot"])
    else:
        sys.exit(1)


data = [
    "blacklist nouveau\n",
    "blacklist nvidia\n",
    "blacklist nvidia_drm\n",
    "blacklist nvidia_modeset\n",
    "blacklist nvidia_uvm\n",
]
fullpath = "/etc/modprobe.d/blacklist-nvidia.conf"
if os.geteuid() != 0:
    print("For executing root is required, please run this script in sudo")
    sys.exit(1)
if os.path.exists(fullpath):
    with open(fullpath, "r") as file:
        info = file.read()
        if info.strip():
            print("File already exists, truncate the file before moving")
            sys.exit(1)

with open(fullpath, "w") as file:
    file.writelines(data)
run_command()
ask_for_reboot()
