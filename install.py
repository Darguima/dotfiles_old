#! /usr/bin/python3

from os import path, chdir
from os.path import dirname, expanduser
from shutil import rmtree

from Utils.logger import logger_init
from Utils.run_command import run_command_init

from Utils.request_sudo import request_sudo
from Utils.print_log import print_log, print_header, print_log_box, print_log_status
from Utils.get_args import get_args
from Utils.mkdir import mkdir
from Utils.colors import colors

from InstallationScripts import arch, yay, zsh, xorg, qt, lightdm, awesome, rofi, alacritty, syncthing, gimp, obs, ufw, others

_root_path = dirname(path.realpath(__file__))
_home = expanduser("~")
_zsh = f"{_home}/.oh-my-zsh"
CONSTANTS = {
  "ROOT_PATH": _root_path,
  "TEMP_PATH": f"{_root_path}/temp",
  "LOG_FILE": f"{_root_path}/log.txt",
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
mkdir(CONSTANTS["TEMP_PATH"])

print_header()

args = get_args() 

logger_init(CONSTANTS["LOG_FILE"])
run_command_init(args["show_commands"])

print_log_box("Some Info")

print_log_status(0, f"For a detailed log of everything (like commands output) check the log file (with cat) at {colors.UNDERLINE}{CONSTANTS['LOG_FILE']}{colors.ENDC}", 0)

print_log_box()

arch.configure(CONSTANTS, args)
yay.installAndUpdate(CONSTANTS, args)

zsh.installAndConfigure(CONSTANTS, args)
xorg.installAndConfigure(CONSTANTS, args)
qt.installAndConfigure(CONSTANTS, args)
lightdm.installAndConfigure(CONSTANTS, args)
awesome.installAndConfigure(CONSTANTS, args)
rofi.installAndConfigure(CONSTANTS, args)
alacritty.installAndConfigure(CONSTANTS, args)
syncthing.installAndConfigure(CONSTANTS, args)
gimp.installAndConfigure(CONSTANTS, args)
obs.installAndConfigure(CONSTANTS, args)
ufw.installAndConfigure(CONSTANTS, args)
others.installAndConfigure(CONSTANTS, args)

print_log("\nBye\n")
rmtree(CONSTANTS["TEMP_PATH"])
