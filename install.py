#! /usr/bin/python3

from os import makedirs, path, chdir
from os.path import dirname, expanduser
from shutil import rmtree

from Utils.request_sudo import request_sudo
from Utils.print_log import print_log, print_header
from Utils.get_args import get_args

from InstallationScripts import yay, alacritty, awesome, zsh

_root_path = dirname(path.realpath(__file__))
_home = expanduser("~")
_zsh = f"{_home}/.oh-my-zsh"
CONSTANTS = {
  "ROOT_PATH": _root_path,
  "TEMP_PATH": f"{_root_path}/temp",
  "HOME": _home,
  "DOTFILES": f"{_home}/.dotfiles",
  "ZSH_PATH": _zsh,
  "ZSH_CUSTOM": f"{_zsh}/custom",
}

request_sudo()
chdir(CONSTANTS['ROOT_PATH'])
"""
Fix: sometimes, when canceling this script, and rerunning it, a permission error will be 
  triggered here, when removing the temp folder.
"""
if path.isdir(f"{CONSTANTS['TEMP_PATH']}"):
  rmtree(CONSTANTS["TEMP_PATH"])
makedirs(CONSTANTS["TEMP_PATH"])

print_header()

args = get_args() 

yay.installAndUpdate(CONSTANTS, args)

alacritty.installAndConfigure(CONSTANTS, args)
zsh.installAndConfigure(CONSTANTS, args)
awesome.installAndConfigure(CONSTANTS, args)

print_log("\nBye\n")
rmtree(CONSTANTS["TEMP_PATH"])
