#! /usr/bin/python3

from os import makedirs, path, chdir
from os.path import dirname
from shutil import rmtree

from Utils.request_sudo import request_sudo
from Utils.print_log import print_log
from Utils.colors import colors

from InstallationScripts import yay, alacritty

_root_path = dirname(path.realpath(__file__))
CONSTANTS = {
  "ROOT_PATH": _root_path,
  "TEMP_PATH": f"{_root_path}/temp",
}

request_sudo()
chdir(CONSTANTS['ROOT_PATH'])
"""
Fix: sometimes, when canceling this script, and rerunning it, a permission error wil be 
  triggered here, when removing the temp folder.
"""
if path.isdir(f"{CONSTANTS['TEMP_PATH']}"):
  rmtree(CONSTANTS["TEMP_PATH"])
makedirs(CONSTANTS["TEMP_PATH"])

print_log(f"""
Welcome to my {colors.BOLD}.dotfiles{colors.ENDC}.
  by {colors.BOLD}Darguima{colors.ENDC}
""")

yay.install(CONSTANTS)
yay.update(CONSTANTS)

alacritty.installAndConfigure(CONSTANTS)

print_log("\nBye\n")
rmtree(CONSTANTS["TEMP_PATH"])
